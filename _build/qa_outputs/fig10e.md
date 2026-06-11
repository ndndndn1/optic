### 예상 질문과 답변

#### Q. 이 그림은 그래프인가요, 아니면 회로/네트워크 모식도인가요?
A. x축·y축·범례가 있는 데이터 그래프가 아니라, 센서 근처 칩에서 특징 신호가 광자 신경망으로 들어가 분류되는 흐름을 그린 모식도입니다. 빨간선과 회색선은 시간 변화나 피크가 아니라 뉴런/채널 간 연결을 뜻합니다. 근거: Figure 10e 캡션의 “photonic neural-network unit”, DOI 문맥의 Figure 10 설명. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. 왼쪽의 Ch1, Ch2, Ch3, Ch4 색상 블록은 무엇을 의미하나요?
A. 네 개의 입력 특징 채널입니다. 앞 단계인 광자 특징추출 유닛에서 나온 신호가 이 네 채널로 들어오며, 그림에서는 초록·노랑·파랑·빨강으로 구분되어 있습니다. 색 자체가 물리량의 크기나 파장을 나타낸다고는 이 패널만으로 확정할 수 없습니다. 근거: Figure 10e 캡션은 “feature-extracted signals feed into Si MZIs”라고 설명하며, 본문은 Phase 2에서 네 병렬 경로가 MZI 배열로 들어간다고 설명합니다. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. “Photonic MVM”은 정확히 무엇인가요?
A. Photonic matrix-vector multiplication, 즉 광 영역에서 행렬-벡터 곱셈을 수행한다는 뜻입니다. 그림 아래의 식처럼 입력 벡터 `[x1 x2 x3 x4]`에 가중치 행렬 `[w]`를 곱해 출력 `[y1 y2 y3 y4]`를 만드는 선형층입니다. 근거: Figure 10e 캡션의 “photonic matrix-vector multiplication (linear layer)”, DOI 본문 Phase 2 설명.

#### Q. 그림 아래의 행렬식 `[W][x]=[y]`는 왜 4×4처럼 보이나요?
A. 입력이 `x1`부터 `x4`까지 네 개이고, 출력도 `y1`부터 `y4`까지 네 개라서 4입력-4출력 선형 변환을 나타냅니다. 그림의 “Fully-connected 4×1” 표기는 시각적으로 각 출력 노드가 네 입력 채널과 완전연결된다는 뜻으로 읽을 수 있습니다. 다만 실제 전체 네트워크의 모든 층 구조는 이 패널만으로 완전히 알 수 없습니다. 근거: Figure 10e의 행렬 표기와 DOI 본문에서 “4 × 4 photonic neural network”라고 설명된 문맥. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. 빨간 연결선은 무엇을 보여주나요?
A. Ch1–Ch4 입력이 오른쪽의 중간 노드들로 모두 연결되는 완전연결 선형층을 보여줍니다. 이 선들이 실제 도파관 배치의 정확한 물리적 경로라기보다는, 광자 MVM에서 입력과 가중치가 결합되는 계산 구조를 도식화한 것으로 보는 것이 안전합니다. 근거: Figure 10e 캡션의 “linear layer” 및 “weights tuned by electrode voltages”.

#### Q. 회색 연결선이 훨씬 많아 보이는 이유는 무엇인가요?
A. 중간 출력이 여러 클래스 후보로 분류되는 분류기 부분을 강조하기 위해서입니다. 오른쪽에는 Class 1부터 Class 13까지 13개 출력 후보가 있고, 회색선은 이 후보들로 향하는 분류 연결을 나타냅니다. 근거: Figure 10e 이미지의 Class 1–13 레이블과 Figure 10e 캡션/본문의 제스처·보행 분류 문맥.

#### Q. 오른쪽의 “Class 1”부터 “Class 13”은 무엇을 뜻하나요?
A. 분류 결과의 후보 클래스입니다. 그림 아래에 “Results: 13 Gestures or 7 Gaits”라고 되어 있으므로, 한 응용에서는 13개 제스처, 다른 응용에서는 7개 보행 상태를 분류하는 시스템으로 이해할 수 있습니다. 다만 각 Class 번호가 어떤 구체적 손동작이나 보행 상태인지는 이 패널만으로 알 수 없습니다. 근거: Figure 10e 하단 결과 문구, DOI 본문에서 glove gesture 및 sock gait inference를 언급한 문맥. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. “+ReLU”가 두 군데 보이는데, 광소자가 ReLU를 직접 한다는 뜻인가요?
A. 아닙니다. 캡션 문맥상 광자 MZI 배열은 주로 선형 행렬-벡터 곱셈을 담당하고, ReLU 같은 비선형 활성화는 전자 백엔드에서 수행됩니다. 그림에 “+ReLU”가 붙어 있어도, 이것을 순수 광학 비선형 소자가 구현한다고 단정하면 안 됩니다. 근거: Figure 10e 캡션의 “nonlinear activation and backpropagation occur in the electronic backend”.

#### Q. “backpropagation” 화살표는 무엇을 의미하나요?
A. 학습 과정에서 오차를 거꾸로 전파해 가중치를 조정한다는 뜻입니다. 그림에서는 위쪽에서 Photonic MVM 쪽으로 내려오는 화살표로 표시되어, 전자 백엔드가 계산한 학습 신호가 MZI 가중치 조정에 반영되는 흐름을 나타냅니다. 근거: Figure 10e 캡션의 “backpropagation” 및 “in-situ training” 문맥.

#### Q. “In-situ training”은 센서가 있는 상태에서 바로 학습한다는 뜻인가요?
A. 큰 방향은 그렇습니다. 별도 오프라인 계산만 하는 것이 아니라, 칩 위 또는 칩과 결합된 전자 백엔드에서 가중치 조정을 수행해 실제 하드웨어 상태를 반영하는 학습을 뜻합니다. 다만 이 그림만으로 학습 데이터 수, 에폭 수, 손실함수, 최적화 알고리즘은 알 수 없습니다. 근거: Figure 10e의 “In-situ training” 표기와 캡션의 전자 백엔드 역전파 설명.

#### Q. 여기서 MZI는 어떤 역할인가요?
A. MZI, 즉 Mach–Zehnder interferometer는 광의 위상/간섭을 이용해 가중치가 걸린 합산을 구현하는 광자 회로 요소입니다. 이 패널에서는 Si MZI 배열이 선형층의 가중치 연산, 즉 MVM을 맡습니다. 근거: Figure 10e 캡션의 “Si MZIs for photonic matrix–vector multiplication”; 본문은 MZI가 전극/히터 전압으로 조정된다고 설명합니다. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. 가중치 `w11` 같은 값은 어디에 저장되거나 조정되나요?
A. 캡션 문맥에서는 전극 전압으로 조정된다고 되어 있습니다. 본문에서는 Si MZI의 thermo-optic heater 전압을 정밀하게 걸어 광학적 행렬-벡터 곱셈을 구현한다고 설명합니다. 따라서 `w11` 등은 추상적인 신경망 가중치이면서, 하드웨어에서는 MZI의 위상/전달 특성으로 대응됩니다. 근거: Figure 10e 캡션 및 DOI 본문 Phase 2 설명. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. 광 신호의 흐름은 왼쪽에서 오른쪽인가요?
A. 도식적으로는 그렇습니다. Ch1–Ch4 특징 입력이 왼쪽의 Photonic MVM 블록으로 들어가고, 중간 노드와 활성화를 거쳐 오른쪽 Class 출력으로 진행합니다. 위쪽의 backpropagation 화살표는 학습 신호의 반대 방향 흐름을 나타냅니다. 근거: Figure 10e의 화살표·연결선 배치와 Figure 10e 캡션.

#### Q. 이 그림에서 센서 자체는 어디에 있나요?
A. 이 패널에는 TENG 센서나 MRR 특징추출기는 직접 그려져 있지 않고, 그 결과인 Ch1–Ch4 특징 신호부터 보입니다. 센서와 특징추출 단계는 Figure 10d 쪽 문맥에 해당하며, Figure 10e는 Phase 2인 광자 신경망 유닛을 확대해 보여줍니다. 근거: Figure 10 전체 캡션에서 (d)는 feature extraction, (e)는 photonic neural-network unit으로 구분됨. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. “13 Gestures or 7 Gaits”는 같은 네트워크가 동시에 20개를 분류한다는 뜻인가요?
A. 그렇게 보기는 어렵습니다. 문구는 두 응용 사례, 즉 13개 손 제스처 또는 7개 보행 상태를 분류할 수 있음을 나타냅니다. 오른쪽 그림에는 Class 1–13이 그려져 있어 제스처 분류 예시에 더 맞춰진 도식처럼 보입니다. 근거: Figure 10e 하단 문구와 DOI 본문에서 glove gesture inference, sock gait analysis를 따로 설명한 문맥.

#### Q. 이 패널에서 “Photonic Neural Networks”가 기존 전자 신경망과 다른 핵심은 무엇인가요?
A. 선형 행렬 연산을 전자 디지털 연산 대신 광자 회로, 특히 Si MZI 배열에서 수행한다는 점입니다. 반면 ReLU와 역전파는 전자 백엔드가 맡으므로, 완전한 all-optical neural network라기보다는 하이브리드 광-전자 신경망으로 보는 것이 정확합니다. 근거: Figure 10e 캡션 및 DOI 본문에서 “hybrid photonic–electronic near-sensor edge computing”으로 설명됨. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. 초보자가 헷갈리기 쉬운 핵심 용어는 무엇인가요?
A. `Photonic MVM`은 “광으로 행렬곱을 한다”는 뜻이고, `MZI`는 그 연산을 가능하게 하는 간섭계 소자입니다. `ReLU`는 음수 출력을 0으로 자르는 비선형 활성화 함수이고, `backpropagation`은 학습 알고리즘입니다. `in-situ training`은 실제 하드웨어 상태를 반영해 현장에서 학습/보정한다는 의미에 가깝습니다. 근거: Figure 10e 내부 레이블과 Figure 10e 캡션의 선형층·비선형·역전파 설명.

#### Q. 이 그림만 보고 정확도나 에너지 소모를 알 수 있나요?
A. 이미지 자체에는 정확도, 지연시간, 에너지 수치가 직접 표시되어 있지 않습니다. 그런 수치는 본문 문맥에서 확인해야 합니다. DOI 본문은 on-chip PNN의 제스처·보행 정확도와 저지연·저에너지 가능성을 따로 설명하지만, Figure 10e 그림만으로는 측정 조건이나 비교 기준까지 확정할 수 없습니다. 근거: DOI 본문 Phase 2 및 성능 설명. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. 이 그림에서 피크, dip, resonance shift 같은 광센서 특성을 읽을 수 있나요?
A. 이 패널 자체에서는 읽을 수 없습니다. 그런 정보는 Figure 10d의 MRR 특징추출이나 TENG-구동 변조 문맥에 더 가깝습니다. Figure 10e는 이미 추출된 Ch1–Ch4 특징을 신경망이 어떻게 분류하는지를 보여주는 단계입니다. 근거: Figure 10 캡션에서 (d)는 feature extraction, (e)는 neural-network unit으로 역할이 분리됨.

#### Q. 이 이미지 하나만으로 확정할 수 없는 점은 무엇인가요?
A. 각 Class의 실제 라벨, 광 파장, MZI 개수의 실제 레이아웃, 손실·잡음 모델, 학습 데이터셋 크기, 전극 전압 범위, ReLU 회로 구현 방식은 이 패널만으로 확정할 수 없습니다. 이 패널은 구조와 정보 흐름을 보여주는 개념도이며, 세부 수치는 본문과 원 논문 Ref. [223]을 함께 봐야 합니다. 근거: Figure 10e는 모식도이고, Ref. [223]는 Ren et al.의 NSEC 원 논문으로 인용되어 있음. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))