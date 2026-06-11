### 예상 질문과 답변

#### Q. Figure 9(a)에서 “Photonic Nose”는 실제 코처럼 냄새를 맡는 장치인가요?
A. 아닙니다. 그림의 “Photonic Nose”는 중적외선(MIR) 흡수 스펙트럼을 이용해 가스 혼합물을 구분하는 도파관 기반 광센서를 비유적으로 부른 이름입니다. 왼쪽 사람 그림은 인간 후각의 “감지와 인식”을 비교 대상으로 보여주고, 가운데 도파관 칩은 실제로 빛과 가스가 상호작용해 스펙트럼 정보를 얻는 부분입니다.  
근거: Figure 9 caption, ref. [221], DOI: 10.3390/aisens1010005.

#### Q. Figure 9(a)의 위쪽 그래프에서 x축과 y축은 무엇을 뜻하나요?
A. x축은 파장 `Wavelength (um)`로, 약 3.65-3.80 um의 중적외선 영역입니다. y축은 `Normalized signal`로, 특정 가스가 중적외선을 얼마나 흡수했는지를 정규화한 신호입니다. 이 파장대에서 IPA와 acetone의 흡수 패턴 차이를 이용해 혼합 가스를 구분합니다.  
근거: Figure 9(a) 내부 축 레이블 및 caption의 “Mid-IR absorption spectra”, ref. [221].

#### Q. 빨간 선, 파란 선, 검은 선은 각각 무엇인가요?
A. 범례에 따르면 빨간 선은 IPA, 파란 선은 acetone, 검은 선은 두 가스의 mixture입니다. 중요한 점은 혼합물 선이 단순히 “새로운 가스”를 의미하는 것이 아니라, IPA와 acetone의 흡수 특징이 섞여 나타난 스펙트럼이라는 점입니다.  
근거: Figure 9(a) 그래프 범례, caption의 가스 혼합물 검출 설명, ref. [221].

#### Q. 그래프에서 뚜렷한 피크나 dip이 보이는데, 이것이 가스 식별에 중요한가요?
A. 네. 이 그림에서는 특정 파장에서 신호가 올라가거나 내려가는 패턴, 즉 흡수 스펙트럼의 굴곡이 가스 종류와 혼합비 추론의 입력이 됩니다. 다만 이 이미지 하나만으로 각 dip이 어떤 분자 진동 모드에 대응하는지는 확정할 수 없습니다.  
근거: Figure 9(a)의 “Mid-IR absorption spectra” 및 caption의 성분·농도 추론 설명, ref. [221].

#### Q. Figure 9(a)에서 CNN과 MLP는 서로 같은 역할인가요?
A. 아닙니다. 그림에는 CNN이 `Spectra recognition`, MLP가 `Spectra decomposition` 쪽으로 배치되어 있습니다. 즉 CNN은 스펙트럼 패턴을 분류해 혼합물 라벨을 인식하는 역할로, MLP는 혼합 스펙트럼을 성분별 스펙트럼과 농도로 분해하는 역할로 제시됩니다.  
근거: Figure 9(a) 오른쪽 AI 블록의 레이블, caption의 cloud ML 설명, ref. [221].

#### Q. 오른쪽의 “19 mixture labels”는 무엇을 의미하나요?
A. 19개의 서로 다른 혼합 조건, 즉 가스 조성 또는 혼합비 조합을 라벨로 만든 것으로 보입니다. 그림 안에는 `20, 30, 40 Vol%` 및 `80, 70, 60 Vol%` 같은 농도 표기가 보이므로, IPA와 acetone의 비율 변화가 라벨 구성에 반영된 것으로 해석할 수 있습니다. 단, 19개 라벨의 정확한 전체 조합은 이 이미지 하나만으로는 모두 확정할 수 없습니다.  
근거: Figure 9(a)의 “19 mixture labels” 및 caption의 gas mixture ratio 설명, ref. [221].

#### Q. Figure 9(a)의 재구성 스펙트럼 두 개는 무엇을 보여주나요?
A. 오른쪽 아래의 두 그래프는 혼합 스펙트럼에서 각 단일 가스 성분의 원래 스펙트럼을 복원하는 예시입니다. 위쪽은 `25 Vol%`, 아래쪽은 `75 Vol%`로 표시되어 있어 혼합물 안의 성분 농도까지 추정한다는 메시지를 줍니다.  
근거: Figure 9(a) 오른쪽 “Reconstructed spectrum” 패널 및 “Resolved” 박스, ref. [221].

#### Q. Figure 9(a)에서 “edge-based”와 “cloud-based”가 함께 나오는 이유는 무엇인가요?
A. 그림상 엣지 장치인 도파관 “Photonic Nose”가 현장에서 중적외선 스펙트럼을 얻고, 클라우드 기반 AI가 그 스펙트럼을 분석해 라벨과 농도를 추론하는 구조입니다. 따라서 모든 연산이 칩 안에서 끝난다는 뜻은 아니며, sensing은 edge, AI 추론은 cloud 쪽으로 그려져 있습니다.  
근거: Figure 9(a)의 “Edge-based Waveguide Photonic Nose”, “Cloud-based Artificial-Intelligence” 레이블 및 caption, ref. [221].

#### Q. Figure 9(b)는 Figure 9(a)와 무엇이 다른가요?
A. Figure 9(a)는 가스 흡수 스펙트럼을 얻고 AI로 해석하는 광자코 개념이고, Figure 9(b)는 도파관 통합 중적외선 광전 처리유닛이 센싱 신호를 광학·전자적으로 처리해 분류까지 수행하는 구조입니다. 특히 (b)는 `On-device AI Processing`이라고 되어 있어, 외부 AI 분석보다 칩 내 처리 쪽에 더 초점이 있습니다.  
근거: Figure 9 caption의 (a), (b) 설명, ref. [221], [222].

#### Q. Figure 9(b-i)의 여러 색깔 원형 입력 채널은 무엇을 의미하나요?
A. 여러 도파관 채널 또는 여러 파장/신호 채널을 나타내는 것으로 보입니다. 그림에는 `Mid-IR wavelength 3.65-3.8 um`와 함께 여러 입력이 신경망 구조로 들어가는 모습이 그려져 있어, 스펙트럼 정보를 병렬 채널로 나누어 처리한다는 의미입니다.  
근거: Figure 9(b-i) 모식도 및 caption의 “중적외선을 여러 도파관 채널로 나누고” 설명, ref. [222].

#### Q. Figure 9(b)에 있는 VOA와 tunable PD는 각각 어떤 역할인가요?
A. VOA는 variable optical attenuator로, 각 광 채널의 세기를 조절하는 구성요소로 해석됩니다. Tunable PD는 조정 가능한 photodetector이며, caption 문맥상 바이어스 가변 그래핀 검출기가 광신호와 가중치를 곱하는 역할을 합니다. 초보자가 헷갈릴 점은 PD가 단순 검출기만이 아니라, 이 구조에서는 신경망 연산의 가중치 적용 요소처럼 쓰인다는 점입니다.  
근거: Figure 9(b-i)의 VOA, Tunable PD 레이블 및 caption의 바이어스 가변 그래핀 검출기 설명, ref. [222].

#### Q. Figure 9(b)의 광 흐름과 전기 흐름은 어떻게 연결되나요?
A. `Optical input`으로 들어온 중적외선 신호가 도파관 회로를 지나며 여러 채널로 분리되고, 그래핀 광검출기에서 전기 신호로 변환됩니다. 이후 그림의 `Electronic Post-processing`, `Hidden layers`, `Classification results`로 이어져 최종 분류 결과가 만들어집니다.  
근거: Figure 9(b-i) 및 오른쪽 장치 삽화, caption의 광신호 곱셈·합산·전자 후처리 설명, ref. [222].

#### Q. Figure 9(b-iii)의 3D 그래프는 무엇을 나타내나요?
A. y축은 `Transmission (a.u.)`, 한 축은 `Mixed gas no.`, 다른 축은 라벨 1-19로 보이는 가스 혼합 조건입니다. 여러 색의 스펙트럼 곡선이 층처럼 쌓여 있어, 혼합 가스 조건마다 전송 스펙트럼 패턴이 달라짐을 보여줍니다.  
근거: Figure 9(b-iii) 축 레이블 및 caption의 “가스 혼합물 측정 스펙트럼”, ref. [222].

#### Q. Figure 9(b-iv)의 초록색 대각선 패턴은 무엇을 의미하나요?
A. 혼동행렬에서 대각선에 값이 집중된다는 것은 실제 클래스와 예측 클래스가 잘 일치한다는 뜻입니다. 그림 상단에는 `With On-chip Processing: 87.14%`가 표시되어 있어, 온칩 처리를 사용한 분류 정확도가 87.14%였음을 보여줍니다.  
근거: Figure 9(b-iv) 혼동행렬 레이블 및 caption의 분류 혼동행렬 설명, ref. [222].

#### Q. 혼동행렬에 대각선 밖 숫자들이 있는 이유는 무엇인가요?
A. 대각선 밖의 숫자는 오분류 사례를 뜻합니다. 예를 들어 실제 특정 혼합 라벨이 다른 출력 클래스로 예측된 경우입니다. 이 그림만으로 각 오분류가 어떤 농도 조합 사이에서 발생했는지까지는 세부적으로 확정하기 어렵습니다.  
근거: Figure 9(b-iv)의 off-diagonal 숫자 분포 및 caption의 classification confusion matrix, ref. [222].

#### Q. 이 Figure에서 핵심 용어는 무엇인가요?
A. 핵심 용어는 `PIC`, `Mid-IR`, `Photonic Nose`, `absorption spectra`, `CNN`, `MLP`, `VOA`, `tunable PD`, `on-device AI processing`, `confusion matrix`입니다. 특히 PIC는 단순 센서 칩이 아니라 광 도파관, 검출기, 연산 요소가 집적된 회로라는 점이 중요합니다.  
근거: Figure 9 내부 레이블, caption의 “Photonic integrated circuit-based sensors”, ref. [221], [222].

#### Q. 이 이미지 하나만으로 확정할 수 없는 내용은 무엇인가요?
A. 각 가스의 정확한 분자 흡수선 배정, 19개 라벨의 전체 농도 조합, CNN/MLP의 구체적 층 수와 학습 데이터 규모, 그래핀 검출기의 바이어스 조건, 그리고 87.14% 정확도의 데이터 분할 방식은 이미지와 제공된 캡션만으로는 확정할 수 없습니다. 원 논문 [221], [222]의 실험 조건을 확인해야 합니다.  
근거: Figure 9 caption은 개념과 대표 결과를 요약하지만 상세 실험 조건은 ref. [221], [222] 문맥에 의존함; DOI: 10.3390/aisens1010005.