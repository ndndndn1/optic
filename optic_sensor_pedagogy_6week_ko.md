# Optical Sensor Pedagogy 6주 세미나 강의안

대상 문헌: Zhou, H.; Li, D.; Lee, C. "Technology Landscape Review of In-Sensor Photonic Intelligence: From Optical Sensors to Smart Devices", `optic_review1.pdf`

보조 자료: `terminology_optical_sensor.md`, `terminology_optical_sensor.json`

목표: 대학원생이 `optic_review1.pdf`를 단순 요약이 아니라 원리, 수식, 성능지표, 소자 구조, AI/PIC 통합 관점에서 완전히 이해하도록 훈련한다.

핵심 학습 경로:

```text
빛-물질 상호작용 -> 광학 신호 변환 -> 성능지표 -> PIC 소자화 -> AI/in-sensor computing
```

## 1. 운영 방식

- 기간: 6주
- 회차: 주 1회, 회당 2시간
- 형식: 대학원 세미나 + 문제 풀이 + 그림 독해 + 최종 연구 제안
- 언어: 설명과 토론은 한국어, 핵심 용어와 약어는 영어 병기

매주 공통 진행:

| 시간 | 활동 | 목적 |
| --- | --- | --- |
| 10분 | 용어 퀴즈 | 약어와 개념을 빠르게 고정 |
| 25분 | 미니 강의 | 해당 주차의 물리 원리 설명 |
| 35분 | 수식/성능지표 풀이 | 수식의 물리적 의미와 단위 확인 |
| 35분 | Figure 독해 | 논문의 그림을 주장-근거-한계로 해석 |
| 15분 | 종합 토론 | 다음 주차와 최종 제안으로 연결 |

매주 제출물:

- 1쪽 개념 정리
- 1개 수식 또는 성능지표 문제 풀이
- 1개 Figure 독해 노트

## 2. 공통 Figure 독해 템플릿

매주 Figure 1-11을 아래 형식으로 읽는다.

```text
Figure/panel:
이 그림이 주장하는 것:
입력 광 또는 자극:
광학 구조:
검출 대상:
변하는 광학 관측량:
성능지표:
왜 성능이 좋아지는가:
주요 한계:
PIC 또는 in-sensor computing과의 연결:
토론 질문 1개:
```

채점 기준:

- "무엇을 검출했다"에서 멈추면 부족하다.
- 반드시 "어떤 광학량이 왜 변했는가"를 설명해야 한다.
- 성능지표는 이름뿐 아니라 물리적 의미까지 설명해야 한다.

## 3. 1주차: 논문 전체 지도 만들기

읽기 범위:

- Abstract
- Section 1
- Figure 1
- 용어: PIC, AI, RI, SEIRA, SERS, SEF, edge intelligence, in-sensor computing

핵심 목표:

논문의 큰 주장이 "기존 광센싱을 버리고 AI/PIC로 대체한다"가 아니라, 기존 광센싱 원리를 PIC와 AI가 집적, 병렬화, 해석한다는 것임을 이해한다.

강의 흐름:

1. 기존 discrete optical microsystem의 구조를 설명한다.
   - laser, lens, detector, sample stage, processor가 분리됨.
   - 민감도는 높을 수 있으나 부피, 정렬, 전력, 휴대성 문제가 큼.
2. PIC sensor의 전환을 설명한다.
   - waveguide, resonator, modulator, detector가 칩 위에 통합됨.
   - 광학 경로가 수동 정렬이 아니라 fabrication으로 결정됨.
3. AI가 필요한 이유를 설명한다.
   - 광학 스펙트럼과 센서 배열은 고차원 데이터를 만든다.
   - 단일 peak shift만으로는 혼합물, 잡음, drift를 처리하기 어렵다.
4. 논문 전체를 세 층으로 재구성한다.
   - 물리층: RI, SEIRA, SERS, chiral sensing, SEF
   - 소자층: plasmonic nanostructure, metasurface, waveguide, MRR, MZI
   - 지능층: feature extraction, classification, regression, edge decision

토론 질문:

- 왜 Section 2의 기본 센싱 원리가 Section 4의 PIC/in-sensor computing보다 먼저 나오는가?
- AI-enhanced sensor와 in-sensor computing device는 무엇이 다른가?
- Figure 1은 논문의 어떤 기술 발전 방향을 압축해 보여주는가?

제출물:

- 논문 전체 개념도 1쪽
- "기존 광센서 -> PIC sensor -> AI smart device" 전환을 5문장으로 설명

## 4. 2주차: 기본 센싱 원리와 수식

읽기 범위:

- Section 2.1-2.5
- Figure 2
- 용어: LSPR, SPP, FWHM, FoM, EF, hot spot, nanoantenna, metasurface, fluorophore, chirality

핵심 목표:

RI, SEIRA, SERS, chiral sensing, SEF를 "표면증강 센서들"로 뭉뚱그리지 않고, 각각의 광학 과정과 관측량으로 구분한다.

핵심 비교표:

| 기법 | 물리 사건 | 변하는 광학량 | 강점 | 한계 |
| --- | --- | --- | --- | --- |
| RI sensing | 표면 근처 굴절률 변화 | 공명 파장, 진폭, 위상 shift | label-free, real-time | 표면 기능화 없이는 선택성 부족 |
| SEIRA | 분자 진동과 MIR 근접장 결합 | IR absorption 증가 | 분자 fingerprint | IR 흡수 단면적이 작고 hotspot 접근성 문제 |
| SERS | Raman 비탄성 산란 증강 | Raman peak intensity | trace detection, 분자 선택성 | hotspot 재현성 문제 |
| Chiral sensing | LCP/RCP 또는 superchiral field와 비대칭 상호작용 | CD, ORD, VCD, ROA, TCD contrast | enantiomer 구분 | 자연 chiral signal이 약함 |
| SEF | 금속 나노구조 근처에서 형광 여기/방출 변화 | fluorescence intensity/lifetime | 낮은 LOD | quenching과 거리 의존성 |

필수 수식:

```text
S_RI = Delta lambda / Delta n
FoM = S_RI / FWHM
EF_SEIRA = (I_SEIRA / I_ref) * (N_ref / N_SEIRA)
I_SERS proportional to I_0 * |E_ext E_det / (E0_ext E0_det)|^2
```

수식 해석:

- `S_RI`: 굴절률 단위 변화당 공명 파장이 얼마나 움직이는가.
- `FoM`: sensitivity와 linewidth를 동시에 고려한 분해능 지표.
- `EF_SEIRA`: signal 증가뿐 아니라 hotspot에 참여한 분자 수를 보정한 per-molecule 증강 지표.
- `SERS field term`: excitation과 detection 주파수 양쪽에서 field enhancement가 중요함.

문제:

1. 공명 파장이 650 nm에서 653 nm로 이동했고 굴절률 변화가 0.005 RIU라면 `S_RI`는 얼마인가?
2. 위 센서의 FWHM이 20 nm라면 `FoM`은 얼마인가?
3. `S_RI`가 큰 센서가 항상 좋은 센서가 아닌 이유를 설명하라.
4. SEIRA EF 계산에서 `N_ref/N_SEIRA`를 넣는 이유를 설명하라.
5. SERS에서 hotspot 재현성이 왜 핵심 병목인지 설명하라.

제출물:

- 5개 센싱 기법 비교표 완성
- Figure 2의 각 panel에 대해 입력, 구조, analyte, 관측량, metric을 표시

## 5. 3주차: 응용 사례를 성능 근거로 읽기

읽기 범위:

- Section 3.1-3.5
- Figures 3-7
- 용어: LOD, PSA, aptamer, bioreceptor, nPLEX, APEX, MOF, SAM, VOC, enantiomer

핵심 목표:

응용 사례를 "어떤 물질을 검출했다"로 읽지 않고, 각 sensing mechanism의 가능성과 한계를 입증하는 evidence로 읽는다.

Figure별 초점:

- Figure 3: RI sensing
  - binding-induced refractive-index shift
  - label-free immunoassay
  - biological specificity는 optical field가 아니라 surface chemistry에서 옴
- Figure 4: SEIRA
  - MIR molecular fingerprint
  - multi-resonant antenna
  - MOF enrichment와 deep learning 보조 해석
- Figure 5: SERS
  - trace analyte detection
  - multiplex molecular profile
  - wearable plasmonic metasurface와 high-dimensional fingerprint
- Figure 6: Chiral sensing
  - enantiomer detection
  - weak natural CD signal
  - superchiral near field와 metamaterial enhancement
- Figure 7: SEF
  - femtomolar 또는 single-molecule 수준 검출
  - fluorescence enhancement와 quenching 사이의 거리 의존성

응용 카드 템플릿:

```text
기법:
Figure/panel:
응용:
Analyte:
광학/표면 구조:
Signal transduction:
주요 metric:
이 기법이 analyte에 적합한 이유:
한계:
PIC화 가능성:
```

토론 질문:

- RI biosensing에서 선택성은 어디서 오는가?
- SEIRA와 SERS는 모두 fingerprint를 제공하지만 어떤 광학 과정이 다른가?
- chiral sensing에서 engineered optical field가 필요한 이유는 무엇인가?
- SEF에서 enhancement와 quenching은 어떻게 경쟁하는가?

제출물:

- RI, SEIRA, SERS, chiral sensing, SEF 각각 1개씩 총 5개 응용 카드

## 6. 4주차: PIC와 플라즈모닉 집적회로

읽기 범위:

- Section 4.1
- Figure 8
- 용어: PIC, waveguide, evanescent field, SOI, MRR, MZI, PPM, MIM, MSM, Pockels effect, Burstein-Moss effect

핵심 목표:

PIC를 단순 소형화가 아니라 optical system architecture의 변화로 이해한다.

PIC 구성요소:

| 구성요소 | 센서에서의 역할 | 핵심 tradeoff |
| --- | --- | --- |
| light source | excitation 제공 | silicon on-chip source 통합 난이도 |
| waveguide | optical mode 전달 및 analyte와 상호작용 | confinement와 propagation loss |
| resonator | interaction과 spectral selectivity 증가 | high Q와 bandwidth/tolerance |
| modulator | phase/intensity 제어 | 속도, 전압, footprint, 열 |
| detector | 광신호를 전기신호로 변환 | responsivity, bandwidth, noise, coupling |
| switch/logic | routing 또는 optical processing | 재구성성, 손실, cascading |

강의 흐름:

1. diffraction limit 때문에 dielectric waveguide만으로는 nanoscale confinement가 제한됨.
2. plasmonic mode는 subwavelength confinement를 가능하게 하지만 ohmic loss를 만든다.
3. Figure 8을 component library로 읽는다.
   - optical logic gate
   - plasmonic nanolight source
   - plasmonic phase modulator
   - MIM/MSM detector
   - plasmonic switcher
4. bulk optical setup을 PIC block diagram으로 바꾸는 법을 훈련한다.

실습:

아래 block 순서로 원하는 센싱 기법 하나를 PIC화하라.

```text
source -> coupling -> waveguide/resonator/metasurface -> analyte interface -> detector -> processor
```

표시해야 할 것:

- analyte와 빛이 만나는 위치
- propagation loss가 생기는 위치
- calibration이 필요한 위치
- 가장 어려운 integration block

제출물:

- bulk-to-PIC conversion diagram 1개
- integration risk 3개와 mitigation 1개씩

## 7. 5주차: In-Sensor Computing과 Photonic AI

읽기 범위:

- Section 4.2
- Figures 9-10
- 용어: in-sensor computing, NSEC, PNN, CNN, MLP, photonic nose, TENG, CMOS, Q-factor, quantization

핵심 목표:

in-sensor computing을 "센서 가까이에 AI를 붙이는 것"이 아니라, data movement, latency, power bottleneck을 줄이는 구조적 해법으로 이해한다.

구조 비교:

| 구조 | 신호 경로 | 병목 | 장점 |
| --- | --- | --- | --- |
| Conventional sensing | sensor -> ADC -> CPU/GPU/cloud | 데이터 전송, latency | 계산 유연성 |
| Near-sensor edge computing | sensor -> nearby processor | 전력, 통합 | 낮은 latency, cloud 의존성 감소 |
| Photonic in-sensor computing | optical signal -> photonic preprocessing/weighting -> decision | 재구성성, analog noise, nonlinear activation | 병렬성, bandwidth, 낮은 latency |

핵심 사례:

1. MIR photonic nose
   - 입력: VOC mixture absorption spectra
   - transduction: waveguide 내 MIR absorption으로 intensity 변화
   - computation: CNN classification, MLP concentration regression
   - 핵심: molecular fingerprint와 ML이 혼합물 해석을 가능하게 함
2. Graphene photodetector weighting unit
   - bias-tunable responsivity가 optical weight로 작동
   - detection과 multiplication을 결합
3. AlN/Si NSEC platform
   - TENG mechanical signal 입력
   - AlN MRR이 feature extraction/integration 수행
   - Si MZI가 matrix-vector multiplication 수행
   - nonlinear activation과 training은 electronic backend 사용

Signal-flow 템플릿:

```text
사례:
물리적 입력:
sensor frontend:
optical signal:
photonic operation:
electrical conversion:
ML model/computation:
output:
optical metric:
ML/system metric:
noise/loss source:
in-sensor computing이 필요한 이유:
```

토론 질문:

- optical AI sensor에서 accuracy만 보고 좋은 센서라고 말할 수 없는 이유는?
- MRR과 MZI는 각각 어떤 계산적 역할을 할 수 있는가?
- analog photonic AI에서 quantization과 calibration이 왜 중요한가?

제출물:

- Figure 9 또는 Figure 10의 신호 흐름도 1개
- noise, loss, calibration error가 들어가는 위치 표시

## 8. 6주차: Challenges, Outlook, 연구 제안

읽기 범위:

- Section 5
- Figure 11
- 최종 제안과 연결되는 glossary term 전체

핵심 목표:

논문의 outlook을 그대로 반복하지 않고, 실제 연구 질문으로 바꾼다.

Challenge cluster:

| Cluster | 구체 문제 |
| --- | --- |
| Integration/packaging | fiber alignment, on-chip light source, microfluidics, chip-world interface, packaging loss |
| Materials/spectral coverage | silicon spectral limit, visible/MIR platform 선택, III-V integration, graphene/LN/piezoelectric film 통합 |
| Data/AI | labeled spectra 부족, overfitting, drift, analog noise, hardware-constrained inference |
| Deployment | calibration drift, surface fouling, power budget, wireless communication, trust/security |

최종 발표 형식:

- 10분 발표
- 5분 질의응답
- 1쪽 written abstract

연구 제안 필수 구조:

```text
Title:
Target analyte/stimulus:
왜 중요한 문제인가:
선택한 sensing mechanism:
PIC 또는 nanophotonic platform:
예상 optical observable:
primary optical metric:
AI 또는 in-sensor-computing 역할:
dataset/calibration 요구:
main bottleneck:
validation experiment:
expected failure mode:
success criterion:
```

제안서 필수 조건:

- 리뷰 논문의 sensing mechanism 중 하나를 사용
- PIC 또는 nanophotonic platform 하나를 명시
- optical performance metric 하나 이상 포함
- system 또는 ML metric 하나 이상 포함
- realistic bottleneck 하나 이상 포함
- 검증 실험을 구체적으로 제시

## 9. 최종 구술시험 문항

완전 이해 여부는 아래 12개 질문으로 확인한다.

1. 이 리뷰 논문의 기술 발전 경로를 5문장으로 설명하라.
2. `S_RI`를 정의하고 `FoM`이 sensitivity 단독보다 왜 유용한지 설명하라.
3. SEIRA와 SERS를 optical process, signal type, enhancement mechanism으로 비교하라.
4. chiral sensing에서 자연 CD signal이 약한 이유와 nanophotonics가 해결하는 방식을 설명하라.
5. SEF에서 enhancement와 quenching의 거리 의존성을 설명하라.
6. Figures 3-7 중 하나를 골라 complete transduction path를 설명하라.
7. PIC sensor가 alignment 문제를 줄이면서 packaging 문제를 새로 만드는 이유를 설명하라.
8. plasmonic component가 miniaturization에 유리하지만 loss에 취약한 이유를 설명하라.
9. MRR과 MZI가 photonic computing에서 각각 어떤 역할을 하는지 설명하라.
10. in-sensor computing이 data-transfer bottleneck을 줄이는 이유를 설명하라.
11. analog photonic AI에서 calibration, noise, quantization이 왜 필요한지 설명하라.
12. 현장 배포에서 가장 먼저 실패할 수 있는 요소 3개와 mitigation을 제시하라.

통과 기준:

- 12개 중 최소 10개를 mechanism-level로 답변
- sensitivity, selectivity, LOD, accuracy를 혼동하지 않음
- 최종 연구 제안에서 optical metric과 ML/system metric을 동시에 사용

## 10. 평가 루브릭

| 수준 | 설명 |
| --- | --- |
| 부족 | 기법 이름은 외우지만 광학 관측량과 metric을 설명하지 못함 |
| 기본 | 주요 수식과 기법은 설명하지만 소자 구조와 연결이 약함 |
| 대학원 세미나 통과 | mechanism, nanostructure, metric, application, PIC bottleneck을 연결함 |
| 연구 준비 완료 | 논문을 비판적으로 읽고 실현 가능한 다음 실험 또는 소자 구조를 제안함 |

