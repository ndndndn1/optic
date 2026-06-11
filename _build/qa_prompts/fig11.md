너는 광센서/포토닉스 리뷰 논문 Figure 해설 튜터다.

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
- image_id: fig11
- image_file_token: fig11
- figure: Figure 11
- type: panel
- title: 읽는 법 세 개의 발전 단계
- image caption: 3단계 발전 경로
- source DOI: https://doi.org/10.3390/aisens1010005

기반 PDF/본문/캡션 문맥:
원문 캡션. Development pathways of in-sensor photonic intelligence.

논문을 갈무리하는 발전 경로 지도입니다. 데이터 그래프가 아니라, 가로축은 기술 발전 단계, 세로축은 도전과제·목표(Challenges & Goals)를 나타내며, 상승하는 화살표가 "고전 광 센서 → 광자 집적회로 → 인-센서 광자 지능"으로의 진화를 의미합니다.

3단계 발전 경로 읽는 법 세 개의 발전 단계 개념 그림은 세 기둥(왼→오)으로 구성됩니다. ① Classical optical sensors RI·SEIRA·SERS·SEF 기반 센서 (Fig 2–7) — 감도는 높지만 부피가 큼. ② Photonic integrated circuits Lasers·Gates·Modulators·Detectors·Switches와 온칩 광원·검출기 (Fig 8) — 소형·저전력 집적. ③ In-sensor photonic intelligence In-sensor·Hybrid near-sensor·인-센서 컴퓨팅·엣지 인텔리전스 (Fig 9–10) — 칩이 곧 컴퓨터. 상승 화살표는 각 단계가 앞 단계 위에 쌓이며 감지에서 지능으로 발전함을 나타냅니다. 저자는 향후 "스마트 픽셀·스마트 도파관"처럼 센서와 컴퓨터의 경계가 사라지고, 에너지 하베스팅으로 자율 동작하는 광자 센서 네트워크를 전망합니다.
