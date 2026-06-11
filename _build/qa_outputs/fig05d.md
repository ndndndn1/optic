### 예상 질문과 답변

#### Q. 이 패널에서 센서가 실제로 피부의 무엇을 측정하나요?
A. 그림의 변수는 `Sweat` 안에 있는 `Analyte`, 즉 땀으로 배출된 분자입니다. 피부 안쪽에서 땀이 올라오고, 그 안의 분석물이 패치의 플라즈모닉 메타필름 쪽으로 이동해 SERS 신호로 읽히는 구도입니다. 근거는 Figure 5 캡션의 “wearable plasmonic-metasurface sensor [157]”와 본문 설명의 “epidermal sweat에서 analyte를 수확해 Raman fingerprint로 실시간 분자 프로파일링” 문맥입니다. ([doi.org](https://doi.org/10.3390/aisens1010005))

#### Q. 위쪽의 `Excitation`과 `SERS` 화살표는 무엇을 의미하나요?
A. `Excitation`은 센서 표면에 쏘는 레이저 여기광이고, `SERS`는 그 결과로 증강되어 나오는 라만 산란 신호입니다. 즉 이 장치는 전기 신호만 읽는 패치가 아니라, 땀 분자의 진동 지문을 광학적으로 읽는 SERS 웨어러블입니다. 근거: 이 패널은 Figure 5의 SERS 응용 중 하나이며, Figure 2(c)가 SERS 기반 감지 메커니즘으로 제시되어 있습니다. ([doi.org](https://doi.org/10.3390/aisens1010005))

#### Q. 오른쪽 확대도에서 `Plasmonic metafilm`이 가장 중요한 이유는 무엇인가요?
A. SERS에서는 금속 나노구조 주변의 국소 전자기장, 즉 핫스팟이 라만 신호를 크게 키웁니다. 그림에서 맨 위쪽 원형 금속 패턴이 있는 얇은 층이 `Plasmonic metafilm`로 표시되어 있어, 땀 속 분자가 이 근처에 도달했을 때 분자별 라만 지문을 증강하는 핵심 감지층으로 해석됩니다. 근거: 본문은 이 사례를 “flexible SERS-active metasurface”와 “continuous sweat sampling”의 결합으로 설명합니다. ([doi.org](https://doi.org/10.3390/aisens1010005))

#### Q. `Hydrogel film (contains sweat-inducing drug)`는 왜 들어가 있나요?
A. 이 하이드로겔막은 단순 접착층이 아니라 발한 유도 약물을 포함하는 층으로 그려져 있습니다. 즉 사용자가 격렬히 운동하지 않아도 피부 표면에서 땀을 유도하고, 그 땀을 센서 쪽으로 공급하려는 설계입니다. 다만 그림만으로는 어떤 약물인지, 방출 속도나 투여량은 확정할 수 없습니다. 근거: 패널 내부 레이블과 Figure 5(d)의 웨어러블 땀 SERS 센서 문맥, 참고문헌 [157]입니다. ([doi.org](https://doi.org/10.3390/aisens1010005))

#### Q. `Flexible electrodes`는 SERS 신호를 읽는 전극인가요?
A. 그렇게 단정하면 안 됩니다. 그림의 주된 분자 판독은 `Excitation`과 `SERS`로 표시된 광학 경로입니다. `Flexible electrodes`는 하이드로겔의 발한 유도 약물과 함께 배치되어 있으므로 발한 유도, 패치 구동, 또는 보조 전기 자극에 관여하는 구성요소로 보는 것이 자연스럽습니다. 하지만 이 패널 하나만으로 전극의 정확한 역할, 전압, 회로 방식은 알 수 없습니다. 근거: 본문은 SERS-active metasurface와 compliant microfluidic system의 통합을 강조합니다. ([doi.org](https://doi.org/10.3390/aisens1010005))

#### Q. `Breathable polymer film`은 감지 성능과 어떤 관련이 있나요?
A. 맨 아래의 통기성 고분자막은 피부에 붙는 웨어러블 패치가 장시간 착용될 수 있게 하는 기계적·착용성 층으로 보입니다. 분자 지문을 직접 만드는 층은 플라즈모닉 메타필름이지만, 피부 표면에서 안정적으로 땀을 모으려면 패치가 부드럽고 통기성이 있어야 합니다. 근거: 본문은 기존 SERS 기판의 강성이 부드럽고 움직이는 생체 표면에서 문제이며, 이를 해결하기 위해 skin-conformable 플랫폼이 필요하다고 설명합니다. ([doi.org](https://doi.org/10.3390/aisens1010005))

#### Q. 그림 왼쪽의 파란색·빨간색 점들은 각각 무엇인가요?
A. 파란색 점은 `Sweat`, 빨간색 점은 `Analyte`로 표시되어 있습니다. 중요한 점은 센서가 “땀 자체”를 측정한다기보다 땀에 섞여 나온 특정 분자들의 라만 지문을 읽는다는 것입니다. 초보자가 흔히 `sweat = analyte`로 생각하지만, 이 그림에서는 땀이 운반 매질이고 analyte가 분석 대상입니다. 근거: 패널 레이블과 본문 “sweat에서 analyte를 직접 수확한다”는 설명입니다. ([doi.org](https://doi.org/10.3390/aisens1010005))

#### Q. 오른쪽 확대도에 원형 금속 패턴이 여러 개 보이는 이유는 무엇인가요?
A. 원형 금속 패턴들은 플라즈모닉 메타표면의 반복 단위 또는 SERS 활성 영역으로 볼 수 있습니다. 이런 주기적·나노구조화된 금속 패턴은 국소 전자기장을 집중시켜 라만 신호를 증강하는 데 쓰입니다. 다만 이 이미지 해상도와 캡션만으로 정확한 지름, 주기, 금속 재료, 공진 파장은 확정할 수 없습니다. 근거: Figure 5(d)는 wearable plasmonic-metasurface sensor로 분류되고, 참고문헌 [157]의 제목도 “plasmonic-metasurface sensor”입니다. ([doi.org](https://doi.org/10.3390/aisens1010005))

#### Q. 아래쪽 사진과 SEM 이미지는 왜 같이 들어가 있나요?
A. 위쪽은 작동 원리 모식도이고, 아래쪽은 실제 패치 또는 메타표면 구조를 보여 주는 증거 이미지입니다. 특히 SEM처럼 보이는 흑백 이미지는 나노패턴 배열과 변형된 구조가 실제로 존재함을 보여 주며, 신축 상태에서도 SERS 핫스팟 구조가 유지되는지를 뒷받침하는 역할을 합니다. 다만 이 패널만으로 정량적인 신축률이나 신호 감소율은 읽을 수 없습니다. 근거: Figure 5(d)와 본문에서 stretchable plasmonic metasurface sensor라고 설명합니다. ([doi.org](https://doi.org/10.3390/aisens1010005))

#### Q. 이 장치가 “웨어러블”인 핵심 설계 포인트는 무엇인가요?
A. 단순히 작다는 것보다, 피부 표면에 맞게 휘고 움직일 수 있는 구조라는 점이 핵심입니다. 그림에는 `Flexible electrodes`, `Breathable polymer film`, 얇은 메타필름, 하이드로겔막이 함께 그려져 있어 딱딱한 실험실용 SERS 기판을 피부 부착형 패치로 바꾼 설계를 보여 줍니다. 근거: 본문은 기존 SERS 기판의 강성이 웨어러블 적용의 문제이며, 이를 유연하고 skin-conformable한 SERS 플랫폼으로 해결한다고 설명합니다. ([doi.org](https://doi.org/10.3390/aisens1010005))

#### Q. 이 센서는 혈액을 뽑는 방식인가요?
A. 아닙니다. 그림에는 피부 표면, 땀 유도 약물, 땀, 분석물이 표시되어 있고, 본문도 “noninvasive”와 “epidermal sweat” 문맥으로 설명합니다. 따라서 이 패널의 의도는 혈액 채취가 아니라 피부 표면의 땀을 이용한 비침습 분자 감지입니다. 근거: 참고문헌 [157]의 제목은 “noninvasive and universal molecular fingerprint detection on biointerfaces”이고, Figure 5(d) 캡션은 웨어러블 플라즈모닉 메타표면 센서입니다. ([doi.org](https://doi.org/10.3390/aisens1010005))

#### Q. 여기서 `metafilm`, `metasurface`, `SERS substrate`는 같은 뜻인가요?
A. 완전히 같은 말은 아닙니다. `Metasurface`는 빛과 상호작용하도록 설계된 인공 표면 구조를 뜻하고, `metafilm`은 그 구조가 얇은 필름 형태로 구현된 층을 가리키는 그림 속 표현입니다. `SERS substrate`는 라만 신호를 증강하는 기판이라는 기능적 표현입니다. 이 패널에서는 플라즈모닉 메타필름이 SERS-active metasurface 역할을 하는 것으로 연결됩니다. 근거: 본문은 “flexible SERS-active metasurface”와 “stretchable plasmonic metasurface sensor”라고 설명합니다. ([doi.org](https://doi.org/10.3390/aisens1010005))

#### Q. 이 그림에서 시간 변화나 실시간 모니터링을 직접 볼 수 있나요?
A. 직접적인 시간축 그래프는 없습니다. x축, y축, 피크 이동, 시간에 따른 농도 변화 같은 정량 데이터는 이 패널에 표시되지 않습니다. 다만 모식도와 본문 문맥상 땀을 연속 채취하고 SERS 지문을 읽어 실시간 분자 프로파일링을 목표로 하는 장치임을 알 수 있습니다. 근거: 본문은 “continuous sweat sampling”과 “real-time molecular profiling”을 언급하지만, 이 패널 자체는 장치 구조 중심입니다. ([doi.org](https://doi.org/10.3390/aisens1010005))

#### Q. 이 이미지에서 어떤 분자를 검출했는지는 알 수 있나요?
A. 이 패널만으로는 특정 분자 이름을 확정할 수 없습니다. 그림에는 `Analyte`라는 일반 표기만 있고, 스펙트럼 피크나 분자명 라벨은 없습니다. 따라서 포도당, 젖산, 요산, 약물, 대사체 중 무엇을 검출했는지는 원 논문 [157]의 세부 실험이나 스펙트럼을 봐야 합니다. 근거: Figure 5 캡션은 응용 사례 수준에서 “wearable plasmonic-metasurface sensor”라고만 제시합니다. ([doi.org](https://doi.org/10.3390/aisens1010005))

#### Q. 초보자가 이 그림에서 가장 헷갈리기 쉬운 포인트는 무엇인가요?
A. 첫째, 전극이 보인다고 해서 전기화학 센서라고 단정하면 안 됩니다. 핵심 판독은 SERS 광학 신호입니다. 둘째, 땀은 분석 대상 그 자체라기보다 분석물을 운반하는 매질입니다. 셋째, 아래 SEM 이미지는 예쁜 표면 사진이 아니라 플라즈모닉 핫스팟을 만들 나노구조가 실제로 구현됐다는 구조적 근거입니다. 근거: Figure 5는 SERS-based sensing applications이고, 본문은 flexible SERS-active metasurface와 sweat sampling의 결합으로 이 사례를 설명합니다. ([doi.org](https://doi.org/10.3390/aisens1010005))

#### Q. 이 이미지 하나만으로 확정할 수 없는 정보는 무엇인가요?
A. 검출 분자 종류, SERS 피크 위치, 검출한계, 레이저 파장, 금속 재료, 나노패턴 치수, 신축률에 따른 감도 변화, 전극 구동 조건, 실제 인체 착용 시간은 이 패널만으로 확정할 수 없습니다. 이 그림은 “피부 위에서 땀을 유도·채취하고 플라즈모닉 메타표면으로 SERS 지문을 읽는 웨어러블 구조”를 보여 주는 장치 개념 패널입니다. 근거: 원 리뷰의 Figure 5 캡션과 본문은 응용 개요를 제공하고, 세부 정량값은 참고문헌 [157]의 원 연구 문맥에 속합니다. ([doi.org](https://doi.org/10.3390/aisens1010005))