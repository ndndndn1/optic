# -*- coding: utf-8 -*-
"""Generate per-image Codex prompts and inject saved Codex Q&A.

This script intentionally does not create image questions by heuristic rules.
Each Q&A block must come from a `codex exec` result saved in
`_build/qa_outputs/<image_id>.md`.
"""
from __future__ import annotations

from dataclasses import dataclass
from html import escape, unescape
from pathlib import Path
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import re
import shutil
import subprocess
import sys

BUILD = Path(__file__).parent
ROOT = BUILD.parent
CONTENT = BUILD / "content"
PANELS = BUILD / "panels"
PROMPTS = BUILD / "qa_prompts"
OUTPUTS = BUILD / "qa_outputs"
LOGS = BUILD / "qa_logs"
DOI = "https://doi.org/10.3390/aisens1010005"


@dataclass(frozen=True)
class ImageJob:
    image_id: str
    image_token: str
    figure: str
    kind: str
    title: str
    caption: str
    context: str
    image_path: Path
    partial_path: Path
    panel_index: int | None = None


def strip_tags(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def find_matching_div(text: str, start: int) -> int | None:
    """Return the end offset of the div that starts at `start`."""
    depth = 0
    for m in re.finditer(r"</?div\b[^>]*>", text[start:], re.I):
        tag = m.group(0)
        if tag.startswith("</"):
            depth -= 1
            if depth == 0:
                return start + m.end()
        else:
            depth += 1
    return None


def remove_notes(text: str) -> str:
    """Remove previously injected evidence-note blocks, including nested divs."""
    marker = '<div class="evidence-note'
    out: list[str] = []
    pos = 0
    while True:
        start = text.find(marker, pos)
        if start == -1:
            out.append(text[pos:])
            break
        out.append(text[pos:start])
        end = find_matching_div(text, start)
        if end is None:
            pos = start + len(marker)
        else:
            pos = end
    return "".join(out)


def first(pattern: str, text: str) -> str:
    m = re.search(pattern, text, re.S)
    return strip_tags(m.group(1)) if m else ""


def panel_blocks(text: str):
    panel_re = re.compile(r'<div class="panel(?: rev)?">')
    matches = list(panel_re.finditer(text))
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else text.find("\n</section>", m.end())
        if end != -1:
            yield i, text[start:end]


def unique_id(base: str, used: set[str]) -> str:
    if base not in used:
        used.add(base)
        return base
    i = 2
    while f"{base}_{i}" in used:
        i += 1
    value = f"{base}_{i}"
    used.add(value)
    return value


def enumerate_jobs() -> list[ImageJob]:
    jobs: list[ImageJob] = []
    used_ids: set[str] = set()
    for path in sorted(CONTENT.glob("fig*.html")):
        text = remove_notes(path.read_text(encoding="utf-8"))
        fig = re.search(r"fig(\d\d)", path.name).group(1)
        fig_title = first(r'<h2 class="fig-title">(.*?)</h2>', text)
        fig_caption = first(r'<div class="caption">(.*?)</div>', text)
        lead = first(r'<p class="lead">(.*?)</p>', text)

        full = re.search(
            r'<div class="figfull">.*?<img[^>]+src="@([^"]+)".*?<div class="imgcap">(.*?)</div>\s*</div>',
            text,
            re.S,
        )
        if full:
            image_token = full.group(1)
            image_id = unique_id(f"{image_token}_overview", used_ids)
            jobs.append(
                ImageJob(
                    image_id=image_id,
                    image_token=image_token,
                    figure=str(int(fig)),
                    kind="overview",
                    title=f"Figure {int(fig)} 전체: {fig_title}",
                    caption=strip_tags(full.group(2)),
                    context=f"{fig_caption}\n\n{lead}",
                    image_path=PANELS / f"{image_token}.jpg",
                    partial_path=path,
                )
            )

        for panel_index, panel in panel_blocks(text):
            img = re.search(r'<div class="pimg">.*?<img[^>]+src="@([^"]+)".*?<div class="imgcap">(.*?)</div>', panel, re.S)
            if not img:
                continue
            image_token = img.group(1)
            image_id = unique_id(image_token, used_ids)
            panel_title = first(r"<h4>(.*?)</h4>", panel)
            panel_text = strip_tags(panel)
            jobs.append(
                ImageJob(
                    image_id=image_id,
                    image_token=image_token,
                    figure=str(int(fig)),
                    kind="panel",
                    title=panel_title,
                    caption=strip_tags(img.group(2)),
                    context=f"{fig_caption}\n\n{lead}\n\n{panel_text}",
                    image_path=PANELS / f"{image_token}.jpg",
                    partial_path=path,
                    panel_index=panel_index,
                )
            )
    return jobs


def build_prompt(job: ImageJob) -> str:
    return f"""너는 광센서/포토닉스 리뷰 논문 Figure 해설 튜터다.

작업 질문: "이미지에 대해 어떤 예상 질문이 가능할까요?"

첨부 이미지 하나만 대상으로, 한국어 Q&A를 풍부하게 작성하라. 질문은 이미지의 실제 시각 요소에서 자연스럽게 나와야 하며, 하드코딩된 공통 질문처럼 보이면 안 된다.

반드시 다룰 것:
- 그래프가 있으면 x축, y축, 선/색/범례, 피크·dip·shift·시간 변화·컨투어·혼동행렬 등 이미지 고유 특성
- 모식도/장치 그림이면 레이블, 구성요소, 센서 역할, 광/전기/분자 흐름, 감지 기전
- 이미지 안의 핵심 용어가 무엇인지와 초보자가 헷갈릴 수 있는 점
- 이 이미지 하나만으로 확정할 수 없는 점
- 각 답변의 근거가 되는 기반 PDF의 Figure caption/body/reference 번호 또는 DOI 문맥

금지:
- "이미지 읽는 법" 같은 일반론 반복 금지
- 기존 해설 문장을 단순 재배열하거나 요약하는 답변 금지
- 근거 없이 단정 금지
- 파일 편집 금지

출력 형식:
### 예상 질문과 답변

#### Q. ...
A. ...

#### Q. ...
A. ...

대상 이미지:
- image_id: {job.image_id}
- image_file_token: {job.image_token}
- figure: Figure {job.figure}
- type: {job.kind}
- title: {job.title}
- image caption: {job.caption}
- source DOI: {DOI}

기반 PDF/본문/캡션 문맥:
{job.context}
"""


def write_prompts(jobs: list[ImageJob]) -> None:
    PROMPTS.mkdir(exist_ok=True)
    for old in PROMPTS.glob("*.md"):
        old.unlink()
    for job in jobs:
        (PROMPTS / f"{job.image_id}.md").write_text(build_prompt(job), encoding="utf-8")


def run_one_codex(job: ImageJob, model: str, force: bool) -> tuple[str, bool, str]:
    OUTPUTS.mkdir(exist_ok=True)
    LOGS.mkdir(exist_ok=True)
    out = OUTPUTS / f"{job.image_id}.md"
    if out.exists() and out.stat().st_size > 0 and not force:
        return job.image_id, True, "skip existing"

    tmp = OUTPUTS / f"{job.image_id}.tmp.md"
    log = LOGS / f"{job.image_id}.log"
    if tmp.exists():
        tmp.unlink()

    cmd = [
        "codex",
        "exec",
        "--dangerously-bypass-approvals-and-sandbox",
        "-C",
        str(ROOT),
        "--image",
        str(job.image_path),
        "--output-last-message",
        str(tmp),
        "-c",
        'model_reasoning_effort="high"',
    ]
    if model:
        cmd.extend(["-m", model])
    cmd.append(build_prompt(job))

    with log.open("w", encoding="utf-8", errors="replace") as f:
        proc = subprocess.run(cmd, cwd=ROOT, stdout=f, stderr=subprocess.STDOUT)

    if proc.returncode == 0 and tmp.exists() and tmp.stat().st_size > 0:
        shutil.move(str(tmp), str(out))
        return job.image_id, True, f"wrote {out.name}"
    if tmp.exists():
        tmp.unlink()
    return job.image_id, False, f"failed rc={proc.returncode}; see {log}"


def run_codex(jobs: list[ImageJob], model: str, limit: int | None, force: bool, workers: int) -> None:
    selected = jobs[:limit] if limit else jobs
    workers = max(1, workers)
    if workers == 1:
        for job in selected:
            image_id, ok, message = run_one_codex(job, model, force)
            print(("OK" if ok else "FAIL"), image_id, "-", message)
        return

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(run_one_codex, job, model, force) for job in selected]
        for future in as_completed(futures):
            image_id, ok, message = future.result()
            print(("OK" if ok else "FAIL"), image_id, "-", message)


def markdown_qa_to_html(md: str) -> str:
    md = md.strip()
    pairs = re.findall(r"####\s*Q\.\s*(.*?)\nA\.\s*(.*?)(?=\n####\s*Q\.|\Z)", md, re.S)
    if not pairs:
        return '<pre class="qa-markdown">' + escape(md) + "</pre>"
    parts = ['<dl class="qa-list">']
    for q, a in pairs:
        answer = re.sub(r"\n{2,}", "\n", a.strip())
        answer = "<br>".join(escape(line.strip()) for line in answer.splitlines() if line.strip())
        parts.append(f"<dt>{escape(q.strip())}</dt><dd>{answer}</dd>")
    parts.append("</dl>")
    return "\n          ".join(parts)


def note_html(job: ImageJob, md: str) -> str:
    title = "Figure 전체 예상 질문과 답변" if job.kind == "overview" else "예상 질문과 답변"
    return f'''
  <div class="evidence-note qa-note" data-qa-source="{escape(job.image_id)}">
    <h5>{title}</h5>
          {markdown_qa_to_html(md)}
  </div>'''


def output_for(job: ImageJob) -> Path | None:
    out = OUTPUTS / f"{job.image_id}.md"
    if out.exists() and out.stat().st_size > 0:
        return out
    return None


def normalize_model(model: str) -> str:
    model = model.strip()
    if model.lower() == "gpt5.5":
        return "gpt-5.5"
    return model


def inject_into_panel(panel: str, note: str) -> str:
    kv = re.search(r'<div class="kv">', panel)
    if kv:
        close = find_matching_div(panel, kv.start())
        if close is not None:
            return panel[:close] + note + panel[close:]
    return panel + note


def inject_outputs(jobs: list[ImageJob]) -> None:
    by_file: dict[Path, list[ImageJob]] = {}
    for job in jobs:
        by_file.setdefault(job.partial_path, []).append(job)

    for path, file_jobs in by_file.items():
        text = remove_notes(path.read_text(encoding="utf-8"))

        for job in [j for j in file_jobs if j.kind == "overview"]:
            out = output_for(job)
            if out is None:
                continue
            note = note_html(job, out.read_text(encoding="utf-8"))
            token = re.escape(job.image_token)
            pattern = re.compile(rf'(<div class="figfull">.*?<img[^>]+src="@{token}".*?</div>\s*</div>)', re.S)
            text = pattern.sub(lambda m: m.group(1) + note, text, count=1)

        panel_jobs = {
            j.panel_index: j
            for j in file_jobs
            if j.kind == "panel" and j.panel_index is not None and output_for(j) is not None
        }
        if panel_jobs:
            rebuilt: list[str] = []
            pos = 0
            panel_re = re.compile(r'<div class="panel(?: rev)?">')
            matches = list(panel_re.finditer(text))
            for panel_index, m in enumerate(matches):
                start = m.start()
                end = matches[panel_index + 1].start() if panel_index + 1 < len(matches) else text.find("\n</section>", m.end())
                if end == -1:
                    continue
                panel = text[start:end]
                rebuilt.append(text[pos:start])
                job = panel_jobs.get(panel_index)
                if job and f'src="@{job.image_token}"' in panel:
                    out = output_for(job)
                    if out is not None:
                        note = note_html(job, out.read_text(encoding="utf-8"))
                        panel = inject_into_panel(panel, note)
                rebuilt.append(panel)
                pos = end
            rebuilt.append(text[pos:])
            text = "".join(rebuilt)

        path.write_text(text, encoding="utf-8")


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["list", "prompts", "run", "inject"])
    parser.add_argument("--model", default="", help="Use empty string to omit -m and use the Codex default model.")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    jobs = enumerate_jobs()
    if args.action == "list":
        for job in jobs:
            print(job.image_id, job.image_token, job.kind, job.panel_index, job.image_path)
    elif args.action == "prompts":
        write_prompts(jobs)
        print("wrote prompts:", len(jobs))
    elif args.action == "run":
        write_prompts(jobs)
        run_codex(jobs, normalize_model(args.model), args.limit, args.force, args.workers)
    elif args.action == "inject":
        inject_outputs(jobs)
        print("injected available outputs")


if __name__ == "__main__":
    main()
