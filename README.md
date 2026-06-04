# In-Sensor Photonic Intelligence — 광 센서 리뷰 학습 자료

리뷰 논문 *"Technology Landscape Review of In-Sensor Photonic Intelligence: From Optical
Sensors to Smart Devices"* (Zhou, Li & Lee, *AI Sensors* 2025) 을 깊이 있게 이해하기 위한
학습 자료 모음입니다. Figure 전수 해설, 영·한 용어집, 6주 대학원 세미나 강의안을 포함합니다.

## 🔗 라이브 데모 / Live demo

### ▶ https://opticreview.netlify.app

마우스오버 용어 툴팁과 그림 확대(라이트박스)를 지원하는, **단일 파일로 완결된** 인터랙티브
Figure 해설 문서입니다. (이미지가 모두 내장되어 오프라인에서도 동작)

## 구성 / Contents

| 경로 | 설명 |
| --- | --- |
| `optic_review1_figures.html` | **Figure 1–11 인터랙티브 해설** (사이트 메인). 그림 base64 내장 + 용어 툴팁 |
| `terminology_optical_sensor.md` / `.json` | 광 센서 용어집 (영·한 병기). `.json`은 HTML 툴팁 조회용 |
| `optic_sensor_pedagogy_6week.md` / `_ko.md` | 6주 대학원 세미나 강의안 (영문 / 한국어) |
| `optic_sensor_worksheets.md` | 주차별 퀴즈·수식 문제·Figure 독해 템플릿·평가 루브릭 |
| `optic_review1.pdf`, `KR;optic_review1.pdf` | 원문 PDF 및 한국어판 |
| `_build/`, `build/` | 재현용 빌드 스크립트 및 중간 산출물 (그림 크롭, 추출 텍스트 등) |
| `prompt.md`, `yet_prompt.md` | 제작 과정 세션 로그 |

## 로컬에서 보기 / View locally

`optic_review1_figures.html` 는 자가완결형이라 브라우저로 바로 열면 됩니다.

## 재배포 / Redeploy (Netlify)

```bash
netlify deploy --prod --dir=. --site 173aadae-19ae-47de-ab22-fe19c34bea10
```

GitHub 푸시마다 자동 배포를 원하면 Netlify UI에서 이 저장소를 연결하세요
(Site → Build & deploy → Link repository). `netlify.toml` 은 이미 포함되어 있습니다.

## 출처 / Attribution

본 자료의 그림과 본문 인용은 아래 오픈액세스 논문에서 가져온 것으로, 원 라이선스
**CC BY 4.0** 을 따릅니다.

> Zhou, H.; Li, D.; Lee, C. *Technology Landscape Review of In-Sensor Photonic Intelligence:
> From Optical Sensors to Smart Devices.* AI Sensors 2025, 1, 5.
> https://doi.org/10.3390/aisens1010005
> © 2025 the authors. Licensee MDPI, Basel, Switzerland. Licensed under CC BY 4.0.

변경 사항: 한국어 번역, 그림 소패널 분할, 해설 및 용어 추가.

## 라이선스 / License

- **원저작물** (뷰어 코드·번역·용어·강의안 등): **MIT** — `LICENSE` 참조
- **논문 유래 그림·본문**: **CC BY 4.0** (출처 표기 유지) — 적용 범위는 `NOTICE` 참조
