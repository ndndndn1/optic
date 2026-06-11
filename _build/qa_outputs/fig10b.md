### 예상 질문과 답변

#### Q. 이 패널은 그래프인가요, 아니면 장치 모식도인가요?
A. 그래프가 아니라 **광자 인-센서 컴퓨팅 칩의 개념 모식도**입니다. 따라서 x축, y축, 피크, dip, 시간 변화, 컨투어 같은 그래프 해석 요소는 없습니다. 대신 칩 위의 **마이크로링/MZI 어레이**, 빨간 광 신호, 파란 도파로 격자, 분자 아이콘, “Optical sensing signal” 레이블을 읽어야 합니다.  
근거: Figure 10 캡션의 “(b) In-sensor computing with photonic integrated circuits” 및 “Microring/MZI array” 문맥, DOI: https://doi.org/10.3390/aisens1010005; Ref. [223] 문맥. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. 그림 제목의 “photonic in-sensor computing chip”은 무슨 뜻인가요?
A. 센서에서 나온 광 신호를 멀리 떨어진 CPU/GPU로 보내기 전에, **광자 칩 내부에서 바로 전처리 또는 AI 연산을 수행하는 구조**를 뜻합니다. 이미지의 칩은 센서 신호를 받는 장치이면서 동시에 계산 회로 역할을 하는 것으로 그려져 있습니다.  
근거: 본문은 in-sensor computing을 “센서 하드웨어 안에서 feature extraction 또는 neural-network inference를 수행”하는 개념으로 설명합니다. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. 칩 위의 동그란 고리들은 무엇인가요?
A. 동그란 고리는 **마이크로링 resonator**를 나타내는 것으로 볼 수 있습니다. 마이크로링은 특정 파장의 빛을 공진시키거나 필터링하고, 센서 신호 변화가 있으면 공진 조건이 달라져 광 세기나 위상 변화를 만들 수 있습니다. 이 패널에서는 개별 링의 스펙트럼 피크 이동을 보여주지는 않고, “마이크로링/MZI 어레이”라는 연산 블록으로 표현합니다.  
근거: 패널 내부 레이블 “Microring/MZI array for AI computing”; Figure 10 캡션 [223]. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. MZI는 이미지에서 어디에 해당하나요?
A. MZI, 즉 **Mach-Zehnder interferometer**는 보통 빛을 두 경로로 나누고 다시 합쳐 위상 차이를 세기 변화로 바꾸는 구조입니다. 이 작은 패널만 보면 MZI의 두 팔 구조가 명확히 분해되어 보이진 않지만, 파란 도파로 격자와 교차 연결된 광 회로가 마이크로링/MZI 어레이를 상징합니다.  
근거: 패널 레이블과 Figure 10 캡션의 “Microring/MZI array”; Ref. [223]에서는 Si MZI가 photonic neural-network 연산에 쓰인다고 설명됩니다. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. 빨간색 빛줄기는 무엇을 의미하나요?
A. 빨간색 빛줄기는 칩으로 들어오거나 칩에서 나가는 **광 신호 경로**를 나타냅니다. 왼쪽/아래쪽에서 들어오는 빨간 빔은 센서에서 얻은 optical sensing signal의 입력처럼 보이고, 오른쪽으로 나가는 여러 빨간 빔은 칩 내부 연산 후의 출력 채널처럼 해석할 수 있습니다. 다만 이 패널만으로 입력·출력 포트의 정확한 개수나 방향은 확정할 수 없습니다.  
근거: 이미지의 “Optical sensing signal” 레이블 및 Figure 10(b)의 photonic in-sensor computing chip 설명. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. 검은색과 빨간색의 작은 분자 아이콘은 어떤 역할인가요?
A. 칩 앞쪽 도파로 근처에 그려진 분자 아이콘은 **액체, 기체, 생체분자 같은 분석 대상**을 상징합니다. 이들은 실제 분자 구조식을 정확히 그린 것이 아니라, 분광 센서가 다룰 수 있는 analyte를 직관적으로 표시한 그림 요소로 보는 것이 맞습니다.  
근거: 패널 하단의 “spectroscopic sensors (liquid, gas, biomolecules)” 문구와 Figure 10(b) 캡션. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. “Optical sensing signal”은 전기 신호와 어떻게 다른가요?
A. 여기서 optical sensing signal은 광의 **파장, 세기, 위상, 스펙트럼 패턴, 시간 지연** 등에 담긴 센서 정보를 뜻합니다. 전자 회로 기반 인-센서 컴퓨팅이 전압/전류 신호를 다루는 것과 달리, 이 패널의 비교군은 빛 자체를 도파로와 간섭계/공진기 어레이로 처리하는 방향을 보여줍니다.  
근거: Figure 10 캡션에서 (a)는 electronic-integrated circuits, (b)는 photonic integrated circuits로 대비됩니다. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. 왜 하단에 spectroscopic sensors, LiDAR sensors, quantum sensors가 함께 적혀 있나요?
A. 이 칩이 특정 한 종류의 센서만을 뜻하는 것이 아니라, **다양한 광센서 출력**을 광자 회로에서 처리할 수 있다는 범위를 보여주기 위해서입니다. 분광 센서는 파장별 흡수/산란 패턴, LiDAR는 거리·시간-of-flight 관련 광 신호, 양자 센서는 매우 민감한 광/양자 상태 변화를 다룰 수 있습니다. 단, 이 패널 하나만으로 실제로 어떤 센서가 제작·측정되었는지는 알 수 없습니다.  
근거: 패널 하단 레이블; 본문은 고대역 이미지·스펙트럼 데이터의 전송 병목이 in-sensor/near-sensor computing의 동기라고 설명합니다. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. 이 칩은 센서인가요, AI 가속기인가요?
A. 이 패널에서는 둘의 경계가 흐려진 구조로 제시됩니다. 광 신호를 받아들이는 점에서는 센서 시스템의 일부이고, 마이크로링/MZI 어레이로 신호를 처리한다는 점에서는 **광자 AI 연산 블록**입니다. 그래서 “in-sensor computing”이라는 표현이 붙습니다.  
근거: 본문 Section 4.2는 센서가 단순 검출기를 넘어 primitive computer처럼 동작한다고 설명합니다. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. “AI computing”은 이 그림에서 구체적으로 어떤 계산을 말하나요?
A. 가장 자연스러운 해석은 **광 행렬-벡터 곱셈, 필터링, 특징 추출, 분류 전 단계의 선형 연산**입니다. MZI 네트워크는 광 신호의 간섭을 이용해 가중합 연산을 구현할 수 있고, 마이크로링은 파장 선택/가중/변조 기능을 맡을 수 있습니다. 하지만 이 패널 자체에는 학습 알고리즘, 신경망 층 수, 정확도는 표시되어 있지 않습니다.  
근거: 본문은 interferometer network가 optical signal의 multiply-and-accumulate, 즉 analog linear algebra engine으로 작동할 수 있다고 설명합니다. Figure 10(e) 캡션은 Si MZI의 matrix-vector multiplication을 언급합니다. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. 이 패널에서 마이크로링과 MZI가 동시에 필요한 이유는 무엇인가요?
A. 마이크로링은 파장 선택성, 공진 기반 민감도, 소형화에 유리하고, MZI는 위상 조절과 간섭 기반 선형 연산에 유리합니다. 그래서 둘을 어레이로 묶으면 **센서 신호의 광학적 특징 추출과 AI 연산**을 한 칩에서 수행하는 방향을 상상할 수 있습니다. 다만 이 그림은 개념도라 실제 회로가 링과 MZI를 어떤 비율로 배치했는지는 확정할 수 없습니다.  
근거: 패널 레이블 “Microring/MZI array”; Ref. [223]는 AlN microring feature extraction과 Si MZI neural-network operation을 함께 강조합니다. ([nmlett.org](https://www.nmlett.org/index.php/nml/article/view/2049))

#### Q. 파란 격자선은 전선인가요, 광 도파로인가요?
A. 이 패널의 문맥에서는 전선이라기보다 **광 도파로 네트워크**로 보는 것이 적절합니다. 광자 집적회로에서는 빛이 금속 배선이 아니라 실리콘, AlN 같은 도파로를 따라 이동합니다. 단, 실제 칩에는 제어 전극도 필요할 수 있지만, 이 작은 패널에서는 전극과 도파로가 분리되어 명확히 표시되어 있지는 않습니다.  
근거: Figure 10(b)는 photonic integrated circuits이고, Ref. [223]는 AlN/Si waveguide platform을 기반으로 한 NSEC 시스템을 설명합니다. ([nmlett.org](https://www.nmlett.org/index.php/nml/article/view/2049))

#### Q. 이 그림에서 감지 기전은 무엇인가요?
A. 이 패널만 놓고 보면 감지 기전은 넓게 표현되어 있습니다. 분광 센서라면 analyte가 광 흡수, 굴절률 변화, 산란, Raman/IR fingerprint 등을 바꾸고, 그 변화가 칩에 들어가는 optical sensing signal이 됩니다. 이후 마이크로링/MZI 어레이가 그 광 신호를 계산에 사용합니다. 특정 분자가 어떤 공진 피크를 얼마나 이동시키는지는 이 패널에 없습니다.  
근거: 리뷰 본문은 RI sensing, SEIRA, SERS 등 다양한 광센서 원리를 앞 절에서 다루고, Figure 10(b)는 이들의 광 신호를 처리하는 photonic in-sensor computing 비교군으로 제시됩니다. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. 이 패널이 Figure 10의 나머지 패널들과 비교해서 맡는 역할은 무엇인가요?
A. (b)는 최종 제안 시스템 자체라기보다 **기존/비교군에 가까운 광자 인-센서 컴퓨팅 칩의 개념**입니다. Figure 10 전체에서는 (a)가 전자회로 기반 방식, (b)가 광자회로 기반 방식, (c) 이후가 AlN/Si PIC 기반 하이브리드 near-sensor edge computing으로 이어집니다.  
근거: 사용자가 제공한 Figure 10 문맥 및 원문 캡션: (a) electronic IC, (b) photonic IC, (c) hybrid photonic-electronic NSEC. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. 이 이미지 하나만으로 확정할 수 없는 정보는 무엇인가요?
A. 실제 파장, 도파로 재료, 링 반지름, MZI 개수, 입력/출력 포트 수, 검출 대상 물질, 측정 정확도, 에너지 소모, 지연시간, 학습 방식은 확정할 수 없습니다. 그림은 “마이크로링/MZI 어레이로 광센서 신호를 AI 연산에 쓴다”는 수준의 개념도입니다. 성능 수치나 실제 구현은 Figure 10 전체와 Ref. [223]의 본문을 봐야 합니다.  
근거: Figure 10(b) 캡션은 구조 범주만 제시하며, Ref. [223] 초록/하이라이트에서 별도로 NSEC 성능 수치와 AlN/Si 구현을 설명합니다. ([nmlett.org](https://www.nmlett.org/index.php/nml/article/view/2049))