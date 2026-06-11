# Repository Guidelines

## Project Structure & Module Organization

This repository publishes study material for an optical sensor review paper. The site entry point is `optic_review1_figures.html`, a self-contained interactive figure walkthrough served by Netlify. Core written materials live at the repository root: `terminology_optical_sensor.md`, `optic_sensor_pedagogy_6week.md`, `optic_sensor_pedagogy_6week_ko.md`, and `optic_sensor_worksheets.md`.

Build helpers and source fragments are under `_build/`: `assets/` contains the HTML shell, CSS, and JavaScript; `content/` contains per-figure HTML partials; `panels/`, `pages/`, and `crops/` contain generated image assets. Published extracted assets are under `build/`. Keep attribution files (`LICENSE`, `NOTICE`) current when changing derived paper content.

## Build, Test, and Development Commands

- `python _build/build_html.py`: rebuilds `optic_review1_figures.html` from `_build/assets`, `_build/content`, `_build/panels`, and terminology JSON. It also checks unresolved `data-k` terminology references.
- `python -m http.server 8000`: serves the repository locally; open `http://localhost:8000/optic_review1_figures.html`.
- `netlify deploy --prod --dir=. --site 173aadae-19ae-47de-ab22-fe19c34bea10`: deploys the static site as documented in `README.md`.

`_build/build_terminology.py` parses the Markdown glossary to JSON, but currently has a machine-specific `ROOT` path. Update that path or refactor it before relying on the script.

## Coding Style & Naming Conventions

Python scripts use UTF-8, standard-library modules, and simple top-level build steps. Prefer `pathlib` for paths and keep generated outputs deterministic. HTML figure tokens follow `figNN` and `figNNa` naming, matching files in `_build/panels/`. Terminology references should use `data-k="term_key"` values that resolve through `terminology_optical_sensor.json` aliases.

## Testing Guidelines

There is no formal test suite. Treat `python _build/build_html.py` as the primary validation step, then open the rebuilt HTML locally and check tooltips, image zoom/lightbox behavior, and figure navigation. When editing glossary content, verify the generated JSON contains the expected term count and no empty descriptions.

## Commit & Pull Request Guidelines

Recent commits use short imperative summaries such as `add author info` and `Add README with live Netlify link and license/attribution`. Keep commit subjects concise and describe the user-visible change. Pull requests should include a summary, affected files or generated artifacts, validation commands run, and screenshots or a Netlify preview link for visual changes.

## Security & Configuration Tips

Do not commit local Netlify state (`.netlify/` is ignored). Preserve CC BY 4.0 attribution for paper-derived figures and text, and avoid replacing source images without updating `NOTICE`.
