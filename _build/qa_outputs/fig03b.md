### 예상 질문과 답변

#### Q. 이 패널에서 실제로 감지하려는 대상은 바이러스 전체인가요, 아니면 일부 단백질인가요?
A. 그림 상단에는 SARS-CoV-2 바이러스 전체와 숙주세포-ACE2 결합 장면이 나오지만, 센서가 직접 읽는 핵심 표적은 스파이크 단백질의 RBD입니다. 우측 위에 WT, Alpha, Beta, Gamma, Delta, Omicron RBD 구조가 따로 그려진 이유도 변이별 RBD가 항체와 얼마나 다르게 결합하는지를 보려는 의도입니다. 근거: 리뷰 Figure 3(b) 캡션의 “label-free immunoassay boosting [62]”, 본문 RI sensing 설명, ref. [62] Li et al., ACS Nano 2023, DOI: https://doi.org/10.1021/acsnano.2c08153.

#### Q. ACE2가 그림에 보이는데, 센서 표면에도 ACE2가 붙어 있는 건가요?
A. 이 패널만 보면 센서 표면에 붙은 것은 ACE2가 아니라 mAb, 즉 단클론항체로 해석하는 것이 맞습니다. ACE2는 바이러스가 숙주세포에 결합할 때 RBD가 인식하는 생물학적 수용체를 설명하기 위한 배경 요소입니다. 아래 금색 메타표면 위에는 항체처럼 생긴 분자들이 세워져 있고, 그래프에도 mAb 단계가 표시됩니다. 근거: 이미지 내 “ACE2”, “mAb”, “RBD” 레이블과 ref. [62] 제목의 “mAb-functionalized plasmonic metasurfaces”.

#### Q. 그래프의 x축과 y축은 무엇을 뜻하나요?
A. x축은 Wavelength, 즉 파장이고 범위는 약 680-740 nm입니다. y축은 Reflectance, 즉 반사도이며 단위는 a.u., arbitrary units입니다. 절대 반사율 값을 비교하기보다, 곡선의 골 또는 공명 위치가 어느 파장으로 이동하는지가 중요합니다. 근거: 이미지 우하단 그래프 축 표기와 리뷰 본문 §3.1의 RI 센서 설명, 즉 결합에 따른 공명 파장 또는 세기 변화.

#### Q. 그래프에서 색깔 선들은 변이 종류를 의미하나요?
A. 이 이미지에 보이는 그래프만 놓고 보면 색깔 선은 변이 이름이 아니라 표면 기능화 단계로 보입니다. 보라색은 Bare PM, 파란색은 MUA, 초록색은 mAb, 빨간색은 RBD로 표시되어 있습니다. 변이 구별이라는 주제는 우측 위의 WT/Alpha/Beta/Gamma/Delta/Omicron 구조와 연결되지만, 이 작은 그래프의 범례 자체는 변이별 곡선이 아닙니다. 근거: 그래프 오른쪽의 직접 레이블 “Bare PM, MUA, mAb, RBD”; Figure 3(b) 캡션과 ref. [62]의 SARS-CoV-2 RBD variants 문맥.

#### Q. 그래프의 dip은 왜 생기나요?
A. 금 플라즈모닉 메타표면에서 특정 파장의 빛이 표면 플라즈몬 공명에 강하게 결합하면 반사광이 줄어들어 골처럼 보입니다. 표면에 MUA, 항체, RBD가 차례로 붙으면 금 표면 근처의 굴절률 환경이 바뀌고, 그 결과 공명 dip의 위치나 깊이가 변합니다. 근거: 리뷰 Figure 2(a)의 공통 RI 센싱 원리와 Figure 3(b)의 PM 반사 스펙트럼.

#### Q. Bare PM, MUA, mAb, RBD 순서는 어떤 실험 과정을 보여 주나요?
A. Bare PM은 아무 생체분자가 없는 플라즈모닉 메타표면입니다. MUA는 금 표면에 항체를 고정하기 위한 화학적 linker 층으로 볼 수 있고, mAb는 단클론항체가 붙은 상태, RBD는 표적 항원이 항체에 결합한 상태입니다. 즉 그래프는 “센서 제작 → 표면 기능화 → 항체 고정 → 항원 결합”에 따라 광학 응답이 바뀌는 과정을 압축해서 보여 줍니다. 근거: 이미지의 단계별 그래프 레이블과 ref. [62]의 mAb-functionalized PM immunoassay 문맥.

#### Q. RBD 곡선이 가장 위에 있는 것은 농도가 가장 높다는 뜻인가요?
A. 이 패널만으로는 그렇게 단정할 수 없습니다. y축이 a.u.로 표시되어 있고, 곡선들이 보기 좋게 수직 offset 되었을 가능성이 큽니다. 따라서 중요한 정보는 곡선의 절대 높이보다 dip 위치 변화, 즉 표면 결합에 따른 공명 이동입니다. 근거: 그래프 y축 “Reflectance (a.u.)” 표기와 RI 센서의 공명 이동 기반 판독 원리.

#### Q. 빨간 RBD 곡선의 dip이 다른 곡선보다 오른쪽으로 이동한 것처럼 보이는데, 이것은 무엇을 의미하나요?
A. RBD가 항체에 결합하면 표면 근처 유효 굴절률이 증가해 플라즈몬 공명이 장파장 쪽으로 이동할 수 있습니다. 그림에서는 RBD 단계가 mAb, MUA, Bare PM 단계와 다른 공명 위치를 보이도록 그려져 있어 항원-항체 결합이 광학적으로 읽힌다는 점을 강조합니다. 근거: 리뷰 본문 §3.1의 “antigen-antibody binding alters local refractive index” 설명과 Figure 3(b), ref. [62].

#### Q. WT, Alpha, Beta, Gamma, Delta, Omicron 구조 그림은 왜 따로 배치되어 있나요?
A. 변이마다 RBD 아미노산 변이가 다르고, 그 차이가 항체와의 결합 친화도에 영향을 줄 수 있기 때문입니다. 센서는 이런 결합 차이를 굴절률 변화와 공명 이동량 차이로 읽어 변이 식별 또는 면역분석 성능 향상에 활용하려는 장치입니다. 근거: ref. [62] 제목과 초록 문맥의 “12 spike RBD variants” 및 “binding characteristics”.

#### Q. Omicron만 빨간 글씨로 강조된 이유는 무엇인가요?
A. 그림에서 Omicron은 다른 변이명보다 눈에 띄게 빨간색으로 표시되어 있어, 이 패널의 응용 초점이 Omicron 변이 검출 또는 항체 결합 차이 평가에 있음을 암시합니다. 다만 이 이미지 하나만으로 Omicron이 가장 강하게 결합한다거나 가장 큰 공명 이동을 만든다고 확정할 수는 없습니다. 근거: 이미지 내 Omicron 강조 표시와 ref. [62]의 Omicron variant biosensor 문맥.

#### Q. 아래의 금색 판과 구멍들은 어떤 역할을 하나요?
A. 금색 판은 플라즈모닉 메타표면입니다. 주기적 나노구조가 빛과 상호작용해 표면 플라즈몬 공명을 만들고, 그 표면에 항체가 고정됩니다. 표적 RBD가 항체에 붙으면 나노구조 주변의 국소 굴절률이 바뀌어 반사 스펙트럼이 변합니다. 근거: Figure 3(b)의 금 PM 모식도, 우하단 SEM, 리뷰 Figure 3 캡션 및 RI sensing 본문.

#### Q. 우하단 회색 SEM 이미지는 왜 필요한가요?
A. 모식도만 보면 센서가 이상화된 금 판처럼 보이지만, SEM은 실제 제작된 나노구조가 주기적인 구멍 또는 돌기 배열을 가진다는 것을 보여 줍니다. 즉 광학 공명이 단순 금막이 아니라 나노패턴 메타표면에서 나온다는 근거 이미지입니다. 근거: 이미지 우하단 SEM 패널과 ref. [62]의 plasmonic metasurface 제작 문맥.

#### Q. 이 방식이 “라벨-프리”라는 말은 무슨 뜻인가요?
A. 형광염료, 효소, 금 나노입자 같은 추가 표지를 표적에 붙여 신호를 키우는 방식이 아니라, RBD가 항체에 결합했을 때 생기는 굴절률 변화 자체를 광학 공명 변화로 읽는다는 뜻입니다. 그래서 이미지에서도 발광 신호나 염색 표지가 아니라 Reflectance vs Wavelength 그래프가 핵심 판독값으로 제시됩니다. 근거: Figure 3(b) 캡션 “label-free immunoassay boosting”과 리뷰 본문 §3.1의 label-free, real-time RI sensor 설명.

#### Q. 이 패널만 보고 실제 검출한계나 민감도를 알 수 있나요?
A. 알 수 없습니다. 이 패널에는 파장 범위와 대표 반사 스펙트럼은 있지만, 농도별 calibration curve, LOD, 반복성, 통계값이 보이지 않습니다. ref. [62] 문맥에서는 Omicron 검출과 상용 colloidal gold immunoassay 대비 성능 향상을 보고하지만, 이 이미지 하나만으로 수치 성능을 독립적으로 읽을 수는 없습니다. 근거: 이미지에 수치 LOD가 없음; ref. [62] 초록 문맥.

#### Q. 변이 구별은 그래프의 dip 위치만 보면 가능한가요?
A. 원리는 dip shift를 이용하는 것이지만, 이 이미지 하나만으로 변이별 분류 기준을 확정할 수는 없습니다. 실제 변이 구별에는 각 RBD 변이에 대한 결합 친화도, 농도, 반응 시간, 항체 종류, 통계적 분리도가 필요합니다. 이 패널은 “가능한 감지 메커니즘”을 보여 주는 요약 그림에 가깝습니다. 근거: Figure 3(b) 캡션과 ref. [62]의 Langmuir binding equilibrium 및 12 RBD variants 분석 문맥.

#### Q. 초보자가 가장 헷갈리기 쉬운 용어는 무엇인가요?
A. RBD, S protein, ACE2, mAb, MUA, PM입니다. RBD는 스파이크 단백질 중 ACE2와 직접 상호작용하는 영역이고, S protein은 바이러스 표면의 전체 스파이크 단백질입니다. ACE2는 숙주세포 수용체, mAb는 센서 표면에 고정된 단클론항체, MUA는 금 표면 기능화 linker, PM은 plasmonic metasurface입니다. 근거: 이미지 내 레이블과 ref. [62] 제목 및 Figure 3(b) 문맥.

#### Q. 이 그림은 ELISA를 완전히 대체했다는 증거인가요?
A. 그렇게까지 말하면 과합니다. 그림과 리뷰 문맥은 플라즈모닉 RI 센서가 라벨 없이 빠르게 항원-항체 결합을 읽어 기존 면역분석을 보완하거나 성능을 높일 수 있음을 보여 줍니다. 실제 임상 대체 여부는 샘플 수, 민감도, 특이도, 재현성, 표준화 자료가 필요합니다. 근거: 리뷰 본문 §3.1의 label-free, rapid biomarker quantification 설명과 ref. [62]의 immunoassay boosting 문맥.

**근거 출처:** 리뷰 논문 DOI: https://doi.org/10.3390/aisens1010005, Figure 3 caption 및 §3.1 RI sensing 본문; 원 인용 논문 ref. [62] Li et al., “Affinity Exploration of SARS-CoV-2 RBD Variants to mAb-Functionalized Plasmonic Metasurfaces for Label-Free Immunoassay Boosting,” ACS Nano 2023, DOI: https://doi.org/10.1021/acsnano.2c08153.