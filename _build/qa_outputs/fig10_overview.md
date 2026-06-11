### 예상 질문과 답변

#### Q. Figure 10에서 말하는 NSEC는 무엇이고, 왜 “near-sensor”라고 부르나요?
A. NSEC는 센서에서 나온 신호를 멀리 보내기 전에 센서 가까운 칩에서 특징추출과 AI 추론을 수행하는 구조입니다. 그림 (c)에서 사람의 웨어러블/시각/분광/LiDAR/양자 센서 신호가 곧바로 `NSEC chip`으로 들어가고, 오른쪽에는 `Edge AI training and inference`, `Low-latency`, `Low-power consumption`, `Protected privacy`가 표시됩니다. 즉 데이터 전송량과 지연을 줄이려는 edge computing 구조입니다.  
근거: Figure 10 caption 및 결론부 NSEC 설명, ref. [223], DOI: https://doi.org/10.3390/aisens1010005

#### Q. (a)의 전자 인-센서 컴퓨팅과 (b)의 광자 인-센서 컴퓨팅은 무엇이 다르게 그려져 있나요?
A. (a)는 전자 소자 기반입니다. 왼쪽은 `Memristor/memtransistor array`, 오른쪽은 `Photodetector array`이고, 각각 저항/정전용량 센서 또는 이미지/분광/편광 센서 신호를 다룹니다. 반면 (b)는 `Microring/MZI array`가 중심이며, 광 신호 자체를 마이크로링 또는 MZI 배열에서 연산에 활용하는 구조로 그려져 있습니다.  
근거: Figure 10(a,b) caption, ref. [223], DOI 문맥.

#### Q. (a)에서 파란 글씨의 `Electrical sensing signal`과 `Optical sensing signal`은 왜 나뉘어 있나요?
A. 그림은 센서 출력의 물리적 도메인을 구분합니다. `Electrical sensing signal`은 촉각, 가스, 관성, 바이오센서처럼 저항·정전용량 변화 등 전기량으로 나타나는 신호입니다. `Optical sensing signal`은 이미지 센서, 분광 센서, 편광 센서처럼 빛의 세기·스펙트럼·편광 정보를 전기적 검출 배열로 읽는 신호입니다. 초보자가 헷갈릴 점은 “광학 센서”라도 최종적으로는 포토디텍터에서 전기 신호로 바뀔 수 있다는 것입니다.  
근거: Figure 10(a) 라벨 및 caption, ref. [223].

#### Q. (b)의 마이크로링/MZI 배열은 왜 AI computing 칩으로 표현되나요?
A. 마이크로링과 MZI는 빛의 위상, 간섭, 공진 조건을 조절해 가중합 연산에 해당하는 선형 변환을 구현할 수 있습니다. 그림 (b)의 격자형 광도파로와 링 구조는 광 신호가 칩 내부에서 분배·결합·변조되는 모습을 보여줍니다. 다만 이 그림만으로 링 반경, Q-factor, 삽입손실, 실제 네트워크 크기는 확정할 수 없습니다.  
근거: Figure 10(b,e) caption의 `Microring/MZI array`, `photonic matrix-vector multiplication`, ref. [223].

#### Q. (c)에서 빨간 빛줄기와 여러 색 선은 무엇을 의미하나요?
A. 빨간 빛줄기는 칩 안으로 들어오거나 통과하는 광 입력/광 경로를 시각화한 것으로 볼 수 있고, 여러 색 선은 전기-domain 및 광-domain 신호가 NSEC 칩으로 연결되는 다채널 입력을 나타냅니다. 그림 상단의 식 `y_i = ΣW_ij x_j`는 입력 `x_j`가 가중치 `W_ij`와 곱해져 출력 `y_i`를 만든다는 행렬-벡터 곱 연산을 뜻합니다.  
근거: Figure 10(c) 라벨 및 caption, ref. [223].

#### Q. (c)의 재료 범례 `AlN`, `Si`, `Al`, `SiO2`는 각각 어떤 역할인가요?
A. 범례에서 `AlN`은 분홍색, `Si`는 파란색, `Al`은 노란색, `SiO2`는 연한 청록색으로 표시됩니다. AlN은 Pockels 효과를 이용한 전기광학 변조와 관련되고, Si는 MZI 기반 광 신경망 도파로 플랫폼으로 쓰입니다. Al은 전극, SiO2는 절연/기판 또는 클래딩 역할로 해석할 수 있습니다. 단, 그림만으로 층 두께나 공정 순서는 알 수 없습니다.  
근거: Figure 10(c,d) 재료 범례 및 caption의 `AlN/Si PIC`, ref. [223].

#### Q. (d)의 TENG 센서는 무엇을 감지하나요?
A. (d-i)의 TENG 센서는 힘 또는 압력을 감지합니다. 그림에 `Force`와 `Release`가 번갈아 표시되고, 접촉/분리 과정에서 전하 분포가 달라지는 모식도가 있습니다. 아래에는 `V ∝ F`가 적혀 있어 힘이 커질수록 전압 신호가 커지는 감지 기전으로 표현됩니다.  
근거: Figure 10(d-i) 라벨 및 caption의 `TENG force/pressure sensor`, ref. [223].

#### Q. (d)의 세 그래프는 각각 무엇을 보여주나요?
A. (d-iii)는 `TENG output`으로, x축은 `Time (s)`, y축은 `Voltage (V)`이며 약 -0.2~0.2 V 범위의 빠른 펄스형 신호가 반복됩니다. (d-iv)는 `Integration` 후 `V_OC`로, y축이 약 0~20 V까지 올라가는 더 큰 누적형 파형입니다. (d-v)는 `Photonic output`으로, y축은 `V_PD (mV)`이고 약 0~30 mV 범위에서 광검출 출력이 시간에 따라 진동합니다.  
근거: Figure 10(d-iii~v) 축 라벨 및 caption, ref. [223].

#### Q. (d-iii)와 (d-iv)의 파형 차이는 어떤 의미인가요?
A. (d-iii)의 TENG 원 신호는 짧고 날카로운 양·음 피크가 반복되는 개방/접촉 동작의 직접 출력처럼 보입니다. (d-iv)는 `Open circuit` 및 `Integration`으로 표시되어, 원래의 펄스성 신호가 적분되어 더 큰 전압 진폭의 완만한 반복 파형으로 바뀐 것을 보여줍니다. 이 적분 신호가 이후 광 변조에 쓰입니다.  
근거: Figure 10(d-iii,iv) 라벨 및 caption의 `TENG output`, `open-circuit voltage`, `integration`, ref. [223].

#### Q. (d-v)의 `Photonic output`은 왜 TENG 파형과 비슷하게 시간 변화하나요?
A. TENG에서 생긴 전기장이 AlN 도파관의 굴절률을 Pockels 효과로 바꾸고, 그 결과 광 출력이 변조되기 때문입니다. 그래서 (d-v)의 `V_PD`는 힘 입력의 시간 패턴을 반영하는 광검출 신호로 나타납니다. 다만 그림만으로 변조 깊이, 잡음, 선형성, 정확한 감도는 확정할 수 없습니다.  
근거: Figure 10(d-ii~v) 및 caption의 `AlN waveguide TE mode modulation by TENG electric field`, ref. [223].

#### Q. (d-ii)의 컬러 컨투어 이미지는 무엇을 나타내나요?
A. 왼쪽의 색상 컨투어는 AlN 도파관의 TE 모드 광장 분포를 나타냅니다. 중앙의 빨강/노랑 영역이 강한 모드 영역이고, 아래 색상 막대는 `Min`에서 `Max`까지 세기를 뜻합니다. 그림에 `1.2 μm`가 표시되어 도파관 폭 또는 모드 영역의 치수 정보를 주지만, 이 이미지 하나만으로 전체 단면 치수는 알 수 없습니다.  
근거: Figure 10(d-ii) 라벨 및 caption의 `AlN waveguide TE mode`, ref. [223].

#### Q. (d)에 적힌 Pockels 효과 식은 어떤 뜻인가요?
A. 식 `n_TE = n_o - (r13/2)n_o^3 E_z`는 z방향 전기장 `E_z`가 TE 모드의 굴절률 `n_TE`를 바꾼다는 뜻입니다. 즉 TENG가 만든 전기장이 AlN 도파관의 굴절률을 변화시키고, 그 변화가 광 위상 또는 세기 변조로 이어집니다. 초보자가 헷갈릴 점은 이것이 열 효과나 흡수 변화가 아니라 전기광학 굴절률 변화라는 점입니다.  
근거: Figure 10(d-ii) 식 및 caption, ref. [223].

#### Q. (d)의 GSG 전극 그림에서 `No induced E field`와 `TENG induced E field`는 왜 비교되나요?
A. GSG는 ground-signal-ground 전극 구조입니다. 위쪽 그림은 전기장이 유도되지 않은 상태이고, 아래쪽은 TENG 출력으로 전기장이 형성된 상태입니다. 이 전기장이 AlN 도파관에 걸려 Pockels 변조를 일으키므로, 센서 신호가 광 특징추출 신호로 변환됩니다.  
근거: Figure 10(d-ii) GSG 모식도 및 caption, ref. [223].

#### Q. (e)의 `Photonic MVM`은 어떤 연산인가요?
A. `MVM`은 matrix-vector multiplication, 즉 행렬-벡터 곱입니다. 그림 아래의 행렬식은 4개 입력 `x1~x4`가 가중치 `w11~w44`와 곱해져 출력 `y1~y4`가 되는 구조를 보여줍니다. 이는 신경망의 선형층에 해당합니다.  
근거: Figure 10(e) 수식 및 caption의 `Si MZI photonic matrix-vector multiplication`, ref. [223].

#### Q. (e)의 Ch1~Ch4 색 블록은 무엇을 의미하나요?
A. `Ch1`, `Ch2`, `Ch3`, `Ch4`는 특징추출 유닛에서 나온 4개 채널 입력을 의미합니다. 각 채널은 MZI 기반 광 회로에서 서로 다른 가중치 경로로 분기되어 선형 결합됩니다. 그림의 빨간 연결선은 완전연결 `4×1` 연산을 시각화합니다.  
근거: Figure 10(e) 라벨 및 caption, ref. [223].

#### Q. (e)에서 `+ReLU`와 `backpropagation`은 광 회로 안에서 모두 수행되나요?
A. 아닙니다. 캡션 문맥에 따르면 광 회로는 주로 MZI 기반 선형 행렬-벡터 곱을 담당하고, 비선형 활성 함수와 역전파는 전자 백엔드에서 in-situ 학습으로 처리됩니다. 그림에 `+ReLU`, `backpropagation`, `In-situ training`이 함께 표시되어 있어 광-전자 하이브리드 학습 구조임을 보여줍니다.  
근거: Figure 10(e) 및 제공된 body/caption 문맥, ref. [223].

#### Q. 오른쪽의 `Class 1`부터 `Class 13`까지는 무엇을 분류하는 건가요?
A. 그림 하단에 `Results: 13 Gestures or 7 Gaits`라고 표시되어 있어, 출력 클래스는 제스처 13종 또는 보행 7종 분류 결과와 관련됩니다. 다만 이 Figure 10 하나만으로 각 클래스가 어떤 손동작이나 보행 패턴을 뜻하는지는 알 수 없습니다.  
근거: Figure 10(e) 하단 라벨 및 caption, ref. [223].

#### Q. (c)의 `Future fully-integrated PICs` 박스는 현재 구조와 무엇이 다른가요?
A. 현재 하이브리드 NSEC 시스템은 센서, 광원, 포토디텍터, 특징추출, 신경망이 완전히 하나의 PIC 안에 통합된 상태라기보다 단계별 구성으로 제시됩니다. 오른쪽 박스는 `On-chip lasers`, `On-chip PDs`, `Feature Extraction`, `Neural Networks`를 모두 칩 위에 집적하는 미래형 구조를 나타냅니다.  
근거: Figure 10(c) 오른쪽 박스 및 caption, ref. [223].

#### Q. 이 그림에서 초보자가 특히 헷갈릴 핵심 용어는 무엇인가요?
A. `In-sensor computing`은 센서 내부 또는 센서와 매우 가까운 곳에서 연산하는 개념이고, `near-sensor edge computing`은 센서 바로 옆 edge 칩에서 연산하는 구조입니다. `Photonic MVM`은 빛으로 행렬곱을 수행하는 선형층이고, `Pockels effect`는 전기장에 따른 굴절률 변화입니다. `TENG`는 힘/접촉을 전기 신호로 바꾸는 triboelectric nanogenerator입니다.  
근거: Figure 10 전체 라벨 및 caption/body 문맥, ref. [223].

#### Q. 이 이미지 하나만으로 확정할 수 없는 것은 무엇인가요?
A. 실제 칩의 정확한 치수, 마이크로링/MZI 개수, 학습 정확도, 소비전력 수치, 지연시간, 광손실, 데이터셋 구성, 각 클래스의 의미, TENG 센서의 정량 감도는 이 이미지에서 확정할 수 없습니다. 그림은 시스템 개념과 대표 파형, 연산 흐름을 보여주는 overview입니다.  
근거: Figure 10 caption은 구조와 기능을 설명하지만 정량 성능표는 포함하지 않음, ref. [223], DOI 문맥.