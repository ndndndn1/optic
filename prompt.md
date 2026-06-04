# Session: optic terminology

> 작업 디렉토리: `.`
> 원본 문서: `optic_review1.pdf` (Zhou, Li, Lee. *Technology Landscape Review of In-Sensor Photonic Intelligence: From Optical Sensors to Smart Devices.* AI Sens. 2025, 1, 5. MDPI, 82 pages / 8 MB)

---

## Q1. 용어집 1차 생성 요청

**User**:
> @optic_review1.pdf 용어 및 키워드(영한 병기)에 대한 설명(한글)을 terminology_optical_sensor 로 정리. 형식은 다른 프로세스에서 특정 키워드를 검색하여 해당 내용만 추출하기 용이한 형태로

**Assistant 작업 요약**:
- PDF를 페이지 단위(1–8, 9–20, 21–32)로 분할 읽기 후 본문(1–26쪽) 내 주요 용어를 모두 추출.
- `./terminology_optical_sensor.md` 생성 (약 90개 엔트리).
- **파서 친화적 포맷 규칙**:
  - 엔트리 시작: `## <KEY> | <English Full Name> | <한글명>`
  - 엔트리 종료: `---`
  - 필드 라인: `EN:`, `KO:`, `ABBR:`, `CATEGORY:`, `DESC:`, `FORMULA:` (선택), `RELATED:`
  - 관련어 표기: `[[키]]` 위키링크 형식
  - 정규식 일괄 추출: `(?s)## [^\n]+\n.*?\n---`
- **수록 카테고리(요약)**:
  - 핵심 플랫폼: PIC, AI
  - 기본 센싱 5종: RI, SEIRA, SERS, SEF, Chiral
  - 키랄 분광: CD, VCD, ORD, ROA, TCD
  - 광 물리: LSPR, SPP, SPhP, Pockels, Burstein-Moss, Reststrahlen, 회절 한계, 핫스팟, 소산장
  - 광 부품/메타구조: metasurface, nanoantenna, nanopedestal, SRR, supercell, SWG, waveguide, bowtie
  - PIC 부품: MRR, MZI, PPM, MIM, MSM, plasmonic laser/switcher/logic gate, graphene photodetector
  - 성능 지표: FWHM, FoM, EF, LOD, Sensitivity, RIU, Q
  - AI/컴퓨팅: in-sensor computing, NSEC, edge intelligence, PNN, CNN, MLP, memristor
  - 응용/바이오마커: photonic nose, photonic tongue, exosome, nPLEX, APEX, PSA, amyloid β, dopamine, SARS-CoV-2 sensor, E. coli, breathalyzer, wearable
  - 재료/공정: SOI, silicon photonics, silicon nitride, lithium niobate, chalcogenide glass, MOF, ZIF-8, SAM, aptamer, bioreceptor, heterogeneous integration, FDTD, coupled-mode theory, CMOS

---

## Q2. 세션명 변경

**User**: `/rename optic terminology`

**Assistant 작업 요약**:
- 세션명이 `optic terminology` 로 변경됨 (포커스: 광 센서 용어 정리).

---

## Q3. 목표(goal) 설정 — JSON 자체 완결형 용어집

**User**: `/goal 용어 설명을 하다보면 그 안에서도 용어가 나옵니다. 더이상 용어가 나오지 않을 정도로 설명. @terminology_optical_sensor.json`

**의도 분석**:
- 현재 `.md` 용어집은 한 엔트리의 설명 안에 또 다른 미정의 용어(예: "에바네센트 장", "양자수율" 등)가 등장 → 독자가 외부 참조를 더 따라가야 함.
- 요구사항: 각 엔트리만 보고도 추가 검색 없이 이해 가능하도록, **설명 내부에 등장하는 모든 기술 용어를 그 엔트리 안에서 즉시 풀이**할 것.
- 출력 형식: JSON (`terminology_optical_sensor.json`).

**Assistant 설계안**:
- 각 엔트리에 `embedded_terms` (또는 `glossary_in_description`) 필드를 추가.
- `embedded_terms`는 해당 엔트리의 `description` 안에 등장하는 모든 기술 용어를 영한 병기 키로 매핑해, 그 자리에서 풀이.
- 최상위 구조 예시:
  ```json
  {
    "metadata": { "source": "...", "format": "...", "extraction_guide": "..." },
    "terms": {
      "SERS": {
        "en": "Surface-Enhanced Raman Spectroscopy",
        "ko": "표면증강 라만 분광법",
        "abbr": "SERS",
        "category": "기본 센싱 기법 / 진동 분광법",
        "description": "...",
        "embedded_terms": {
          "라만 산란 (Raman scattering)": "...",
          "비탄성 산란 (inelastic scattering)": "...",
          "핫스팟 (hot spot)": "..."
        },
        "formula": "I_SERS ≈ I_0 × |E(ω_ext)E(ω_det) / E_0(ω_ext)E_0(ω_det)|^2",
        "related": ["SEIRA", "LSPR"]
      }
    }
  }
  ```

**상태**: 작업 중. (JSON 파일은 다음 단계에서 생성)

---

## Q4. 세션 Q&A 기록

**User**: `이 세션에서 질의응답을 prompt.md 에 반영`

**Assistant 작업 요약**:
- 본 파일(`./prompt.md`)을 새로 생성하여 세션의 모든 질의/응답과 산출물 경로, 포맷 규칙, 미해결 작업을 기록.

---

## Q5. (신규 세션 "optic review html") 모든 figure 해설 인터랙티브 문서 요청

**User**:
> @optic_review1.pdf 각 figure 설명과 구성요소를 모르는 것 없이 설명
> - 그래프: 주요 변수를 변화(상호작용)시켰을 때 저자가 그림을 삽입한 의도에 맞게 변화하고 그 의미에 대해 설명
> - 3d 그림: 각 파트의 문맥에서 해당 그림의 의의. 무엇이 optic sensor가 사용된 것이고 그림 중 sensor 역할을 하는 것과 감지 기전이 무엇인지
> 파일 형식은 이들을 잘 표현할 수 있는 것으로 함. 설명 중 용어가 나올 경우 해당 용어에 마우스오버하면 terminology_optical_sensor.md를 참조하여 설명을 띄움 (*.md 파일이 이러한 작업에 적합하지 않다면 json 혹은 db 등으로 수정해서 진행)

**명확화 질의응답 (AskUserQuestion)**:

| 질문 | 선택지 | **답변** |
|------|--------|---------|
| 설명 텍스트 **언어** | 한국어 / 영어 / 한·영 병기 | **한국어** |
| 결과물 **패키징** | 단일 HTML / 폴더(HTML+images+json) | **단일 HTML 파일** (이미지 base64 + 용어 JSON inline) |
| 조밀 그림(Fig 8·9·10) **이미지 처리** | 전체+클릭확대 / 소패널 개별 분할 | **소패널까지 개별 분할** |

**Assistant 작업 요약**:
- 논문 실제 36쪽 확인(최초 "82쪽"은 과대추정). 본문 1–26쪽에 **Figure 1–11** 전수 해설.
- 해설 틀: 원문 캡션 → 전체 의의 → 패널별. 그래프=축·변수·의미·의도 / 모식도=`광 센서`·`센서 역할`·`감지 기전`(kv 박스).
- `terminology_optical_sensor.md`(111 엔트리) → `terminology_optical_sensor.json`으로 파싱(`build_terminology.py`).
  - **구조**: `{ "terms": { KEY: {en,ko,abbr,category,desc,formula,related[]} }, "alias": { 소문자키/약어 → KEY } }` — **HTML 툴팁 조회용**.
  - ⚠️ 이는 **Q3의 `embedded_terms` 자체완결형 JSON과 구조·목적이 다름**(Q3 목표는 별개로 미해결).
- 그림: `pdftoppm -r 300` 렌더 → 색채도(saturation) 투영으로 figure bbox 자동검출 → 소패널 크롭 54장(`detect.py`, `crop.py`).
- 단일 HTML 조립(`build_html.py`): 이미지 base64 + 용어 JSON inline + 사이드바 목차 + 용어 hover 툴팁 + 그림 클릭 라이트박스 + `loading="lazy"`.
- **검증**: 11 섹션 / 47 패널 / 58 이미지 참조, 임베드 JPEG 58/58 디코딩, 용어 참조 170건(고유 82) **전부 연결(깨진 툴팁 0)**, `</script>` 누수 0. 헤드리스 부분 렌더로 실제 그림·레이아웃·툴팁 확인.
- 참고: 샌드박스 헤드리스 렌더러는 메모리 제약으로 54장 동시 디코딩(전체 파일 스냅샷) 불가 → 일반 데스크톱 브라우저는 lazy 디코딩으로 정상.

---

## Q6. 세션 Q&A 기록 (본 명령)

**User**: `이 세션에서 질의응답을 prompt.md 에 반영`

**Assistant 작업 요약**:
- 기존 `prompt.md`(이전 세션 Q1–Q4)에 본 세션의 Q5·Q6 질의응답과 산출물을 추가하고 인벤토리·Pending 갱신.

---

## Q7. Hover ↔ Click 이중 툴팁 + 자체완결형 통합

**User**: `용어에 마우스 over하면 기존의 용어 툴팁 / 용어를 클릭하면 자체 완결형 용어집 툴팁`

**채택 방향**: Q3의 옵션 (b) 변형 — 사이드카 파일 분리로 두 목적 통합.
- `terminology_optical_sensor.json`(툴팁 조회용)은 **구조 그대로 유지**.
- **신규 사이드카** `terminology_embedded.json`(자체완결형 풀이)을 도입.
- `build_html.py`가 빌드 시 두 JSON을 머지해 인라인 TERMS 객체의 각 `terms[KEY]`에 `embedded_terms`/`desc_full?` 필드를 더해 단일 HTML에 임베드.

**Assistant 작업 요약**:
- **신규**: `./terminology_embedded.json` — 111/111 키 모두 작성 (110개 채움, `INDEX`만 의도적 비움). 각 키 평균 5~9개 하위 용어를 영한 병기 키 → 한 줄 풀이로 인라인.
- **`_build/build_html.py`**: 사이드카 자동 로드·머지 로직 추가. 사이드카 없어도 빌드 정상 동작.
- **`_build/assets/shell.html`**: 모달 컨테이너 `#tf`(닫기 버튼 포함) 추가, 사용법 문구를 hover/click 2단계로 갱신.
- **`_build/assets/style.css`**: `#tf` 모달 카드/닫기 버튼/`tf-emb` 하위용어 리스트/관련어 점프 스타일 추가. `.term { cursor:pointer }`로 클릭 가능 표시.
- **`_build/assets/app.js`**:
  - **hover/focus** → 기존 `buildTip`(짧은 desc) 유지. "↻ 클릭하면 자체완결형 상세 풀이" 안내 한 줄 추가.
  - **click** → 새 `buildTipFull` 모달: 설명(`desc_full` 우선, 없으면 `desc`) / 수식 / **설명 내 용어 풀이(자체완결)** / 관련 용어.
  - 관련 용어는 `data-jump` 앵커로 모달 안에서 즉시 점프(재오픈).
  - ESC 우선순위: 모달 → 라이트박스 → 툴팁.
  - 모달 열린 동안 그림 라이트박스 트리거 비활성.
- **검증**:
  - 빌드 로그: `sidecar merged: 111/111`, `data-k check: OK (all term references resolve)`, 8.98 MB.
  - 인라인 TERMS 파싱: 111개 키 중 110개에 `embedded_terms` 비어있지 않음(INDEX 1개만 비어 있음 — 메타 엔트리).
  - 모달 자산 확인: `#tf` 컨테이너 / `tf-card` CSS / `buildTipFull` / `showFull(` / `data-jump` 연계 / UI 힌트 텍스트 — 모두 존재.

---

## 산출물 인벤토리 (갱신)

| 파일 | 경로 | 상태 |
|------|------|------|
| 원본 PDF | `./optic_review1.pdf` | 읽기 전용 (실제 36쪽) |
| 1차 용어집 (Markdown) | `./terminology_optical_sensor.md` | 완료 (111 엔트리) |
| 용어집 (JSON, **툴팁 조회용**) | `./terminology_optical_sensor.json` | 완료 — `{terms, alias}` 구조 그대로 |
| **자체완결형 사이드카 (JSON)** | `./terminology_embedded.json` | **신규(Q7)** — `{KEY: {embedded_terms, desc_full?}}` 111키 |
| **Figure 해설 HTML** | `./optic_review1_figures.html` | **재빌드(Q7)** — hover 짧은 툴팁 + click 자체완결형 모달, ≈8.98 MB |
| 빌드 작업물 | `./_build/` | `build_html.py`가 사이드카 자동 머지. 스크립트·이미지·콘텐츠 일체 |
| 세션 로그 | `./prompt.md` | 본 파일 |

---

## 다음 작업 (Pending)

- [x] (Q3/Q7) `embedded_terms` 자체완결형 통합 — 완료 (사이드카 + 클릭 모달).
- [x] (Q5) Figure 1–11 해설 단일 HTML — 완료 / Q7에서 재빌드.
- [ ] (옵션) `.md` ↔ `.json` ↔ `.embedded.json` ↔ HTML 동기화 정책 문서화
  (현재 흐름: `.md` 수정 → `build_terminology.py` → `.json` 갱신 → `build_html.py`가 사이드카 자동 머지 후 HTML 재빌드).
