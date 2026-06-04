# Terminology: Optical Sensor & In-Sensor Photonic Intelligence

> 출처: Zhou, H.; Li, D.; Lee, C. *Technology Landscape Review of In-Sensor Photonic Intelligence: From Optical Sensors to Smart Devices.* AI Sens. 2025, 1, 5. (MDPI)
> 
> **추출 규칙(파서용)**:
> - 각 엔트리는 `## ` 로 시작하고 `---` 로 종료됨.
> - 헤더 형식: `## <ABBR/KEY> | <English Full Name> | <한글명>`
> - 필드: `EN:`, `KO:`, `ABBR:`, `CATEGORY:`, `DESC:`, `FORMULA:`, `RELATED:`
> - 특정 키워드 검색 시 `## ` 또는 `KEY:` 라인 grep 권장. 엔트리 추출은 `## ` 부터 다음 `---` 까지.

---

## INDEX | 약어 색인 | 인덱스

EN: Index of all abbreviations
KO: 약어 색인
ABBR: INDEX
CATEGORY: 메타
DESC:
AI, APEX, BM, CD, CMOS, CNN, ELISA, EF, FoM, FWHM, IPA, LCP, LOD, LSPR, MIM, MIR, MLP, MOF, MRR, MSM, MZI, NSEC, nPLEX, ORD, PCR, PIC, PNN, POC, PPM, PSA, RCP, RI, ROA, SAM, SEF, SEIRA, SERS, SOI, SPhP, SPP, SWG, TCD, TENG, VCD, VOC
RELATED: 본 문서 전체

---

## PIC | Photonic Integrated Circuit | 광자 집적회로

EN: Photonic Integrated Circuit
KO: 광자 집적회로 / 광집적회로
ABBR: PIC
CATEGORY: 핵심 플랫폼 / 광자 하드웨어
DESC:
밀리미터 스케일의 단일 칩 위에 광원(laser), 도파관(waveguide), 변조기(modulator), 검출기(photodetector) 등 광학 부품들을 통합한 회로. 기존 벌크 광학계 대비 소형화·저전력·저비용·고확장성을 제공하며, 휴대용 및 웨어러블 응용에 필수적인 기술. AI와 결합해 "스마트 광자 센서"의 하드웨어 기반을 이룬다.
RELATED: [[SOI]], [[MRR]], [[MZI]], [[in-sensor-computing]], [[silicon-photonics]]

---

## AI | Artificial Intelligence | 인공지능

EN: Artificial Intelligence
KO: 인공지능
ABBR: AI
CATEGORY: 핵심 플랫폼 / 데이터 처리
DESC:
센서에서 수집된 복잡한 광학 스펙트럼의 신호 처리, 패턴 인식, 실시간 의사결정에 사용되는 머신러닝 알고리즘 군. PIC 센서와 결합되어 (1) 신호처리 향상, (2) 미세 특징 추출, (3) 엣지(edge)에서의 실시간 판단, (4) 클라우드 의존성 제거를 가능케 한다.
RELATED: [[CNN]], [[MLP]], [[PNN]], [[edge-intelligence]], [[in-sensor-computing]]

---

## RI | Refractive Index Sensing | 굴절률 센싱

EN: Refractive Index Sensing
KO: 굴절률 센싱
ABBR: RI
CATEGORY: 기본 센싱 기법 (Basic Sensing)
DESC:
금속-유전체 계면에 전자기장을 가두는 표면 플라즈몬을 이용해 굴절률 변화를 측정하는 기법. 표적 분자가 센서 표면의 생체수용체(항체, 압타머 등)에 결합되면 국소 굴절률이 변하여 공명 파장(λ), 진폭, 위상이 이동한다. 라벨-프리(label-free), 실시간, 비침습 측정이 가능.
FORMULA: S_RI = Δλ / Δn  (감도)
RELATED: [[LSPR]], [[FoM]], [[FWHM]], [[plasmonic-sensor]], [[aptamer]]

---

## SEIRA | Surface-Enhanced Infrared Absorption | 표면증강 적외선 흡수

EN: Surface-Enhanced Infrared Absorption (Spectroscopy)
KO: 표면증강 적외선 흡수 분광법
ABBR: SEIRA
CATEGORY: 기본 센싱 기법 / 진동 분광법
DESC:
플라즈모닉 나노안테나 주변의 나노스케일 "핫스팟(hot spot)"에 입사 적외선을 집속·증폭하여, 본래 약한 분자의 진동 흡수 신호를 크게 강화하는 기법. 1980년 Hartstein 등이 임의 분포 금속섬 박막에서 최초 관측. 금속-유기 골격체(MOF) 코팅, 메타표면, 나노받침대(nanopedestal) 등으로 감도를 향상시킨다.
FORMULA: EF = (I_SEIRA / I_ref) × (N_ref / N_SEIRA)
RELATED: [[SERS]], [[hot-spot]], [[nanoantenna]], [[metasurface]], [[SPhP]]

---

## SERS | Surface-Enhanced Raman Spectroscopy | 표면증강 라만 분광법

EN: Surface-Enhanced Raman Spectroscopy
KO: 표면증강 라만 분광법
ABBR: SERS
CATEGORY: 기본 센싱 기법 / 진동 분광법
DESC:
은 또는 금 나노구조를 "핫스팟"으로 활용해 약한 라만(비탄성 산란) 신호를 수 자릿수 증폭하는 분광법. 전자기적 증강(electromagnetic enhancement)과 화학적 증강(chemical enhancement)이 작동. 단분자 검출 수준의 초고감도와 분자 특이성으로, 바이오의료 진단·식품안전·환경모니터링에 응용된다. Fleischmann 등이 거친 은 전극의 피리딘에서 최초 관측.
FORMULA: I_SERS ≈ I_0 × |E(ω_ext)E(ω_det) / E_0(ω_ext)E_0(ω_det)|^2
RELATED: [[SEIRA]], [[LSPR]], [[hot-spot]], [[Raman-scattering]], [[plasmonic-sensor]]

---

## SEF | Surface-Enhanced Fluorescence | 표면증강 형광

EN: Surface-Enhanced Fluorescence (Spectroscopy)
KO: 표면증강 형광 분광법
ABBR: SEF
CATEGORY: 기본 센싱 기법 / 형광 분광법
DESC:
귀금속 나노입자의 국소 표면플라즈몬 공명을 활용해 형광단(fluorophore)의 여기율과 양자수율을 증대시켜 형광 방출을 증폭하는 기법. 1960년대 Drexhage 등이 형광체-금속막 거리에 따른 수명 변화를 관찰. 단분자 수준의 검출이 가능하며, 진단·바이오마커 분석·병원체 검출에 광범위 응용.
RELATED: [[LSPR]], [[plasmonic-sensor]], [[quantum-yield]], [[fluorophore]]

---

## CD | Circular Dichroism | 원편광 이색성

EN: Circular Dichroism (Spectroscopy)
KO: 원편광 이색성 분광법
ABBR: CD
CATEGORY: 키랄 분광법 (Chiral Spectroscopy)
DESC:
좌원편광(LCP)과 우원편광(RCP)에 대한 흡광도 차이를 측정하여 분자의 키랄성(거울상 비대칭성)을 분석하는 기법. 천연 CD 신호는 매우 약하여(~10⁻⁵), 키랄 플라즈모닉 메타표면(예: 감마형, 수리검형)으로 6 자릿수까지 신호 증폭 가능.
RELATED: [[VCD]], [[ROA]], [[TCD]], [[enantiomer]], [[chirality]]

---

## VCD | Vibrational Circular Dichroism | 진동 원편광 이색성

EN: Vibrational Circular Dichroism
KO: 진동 원편광 이색성
ABBR: VCD
CATEGORY: 키랄 분광법
DESC:
CD를 중적외선 영역으로 확장하여 키랄 진동 전이를 탐지하는 기법. 전자 CD보다 10²–10³배 약한 신호가 한계였으나, 플라즈모닉 메타재료로 4 자릿수 이상 증강(Chanda 그룹) 및 13 자릿수 감도 향상까지 보고됨.
RELATED: [[CD]], [[ROA]], [[plasmonic-metasurface]]

---

## ORD | Optical Rotatory Dispersion | 광회전 분산

EN: Optical Rotatory Dispersion
KO: 광회전 분산
ABBR: ORD
CATEGORY: 키랄 분광법
DESC:
파장에 따른 광학 회전각의 분산을 측정하여 분자 키랄성을 분석하는 전통적 기법. 헬리컬 피치가 가시광 파장보다 작은 키랄 분자에서는 신호가 약하다.
RELATED: [[CD]], [[chirality]]

---

## ROA | Raman Optical Activity | 라만 광활성

EN: Raman Optical Activity
KO: 라만 광활성
ABBR: ROA
CATEGORY: 키랄 분광법
DESC:
좌/우 원편광 여기에 대한 라만 응답 차이를 이용하는 키랄 분광 기법. 수용액(중적외선이 강하게 흡수되는 환경)에서 VCD의 보완 기법으로 부상. 은 키랄 나노와이어를 플라즈모닉 도파관으로 사용해 ROA 강도를 증폭한 사례가 있다.
RELATED: [[CD]], [[VCD]], [[chirality]]

---

## TCD | Terahertz Circular Dichroism | 테라헤르츠 원편광 이색성

EN: Terahertz Circular Dichroism
KO: 테라헤르츠 원편광 이색성
ABBR: TCD
CATEGORY: 키랄 분광법
DESC:
THz 대역에서 생체고분자의 진동·회전 시그니처를 키랄성으로 탐지하는 기법. 효율적 THz 편광 변조기 부재로 정체되었으나, 키리가미(kirigami) 패턴 플라즈모닉 시트와 판차라트남-베리 위상 비선형 메타표면으로 돌파구가 마련됨.
RELATED: [[CD]], [[Pancharatnam-Berry-phase]], [[metasurface]]

---

## LSPR | Localized Surface Plasmon Resonance | 국소 표면 플라즈몬 공명

EN: Localized Surface Plasmon Resonance
KO: 국소 표면 플라즈몬 공명
ABBR: LSPR
CATEGORY: 광 물리 현상
DESC:
금속 나노구조(나노입자, 나노디스크, 나노스파이크 등)에서 전자의 집단 진동이 입사광과 공명을 일으키는 현상. 국소 굴절률 변화에 따라 공명 파장이 크게 이동하여 RI 센싱·SEIRA·SERS·SEF의 물리적 기반이 된다.
RELATED: [[SPP]], [[plasmonic-sensor]], [[RI]], [[hot-spot]]

---

## SPP | Surface Plasmon Polariton | 표면 플라즈몬 폴라리톤

EN: Surface Plasmon Polariton
KO: 표면 플라즈몬 폴라리톤
ABBR: SPP
CATEGORY: 광 물리 현상
DESC:
금속-유전체 계면을 따라 전파되는, 광자와 전자 집단 진동(플라즈몬)의 결합 모드. 회절 한계 이하로 빛을 가둘 수 있어 플라즈모닉 도파관·변조기 등의 동작 원리이며, 40 Gbit/s 위상 변조기(PPM) 등이 구현됨.
RELATED: [[LSPR]], [[PPM]], [[plasmonic-waveguide]]

---

## SPhP | Surface Phonon Polariton | 표면 포논 폴라리톤

EN: Surface Phonon Polariton
KO: 표면 포논 폴라리톤
ABBR: SPhP
CATEGORY: 광 물리 현상
DESC:
극성 결정 표면의 광학 포논과 광이 결합한 폴라리톤. Reststrahlen 대역에서 극도의 굴절률 감도를 보여, 수직 적층 적외선 나노안테나와 결합 시 겹친 진동 신호를 딥러닝으로 분리할 수 있게 한다.
RELATED: [[SPP]], [[Reststrahlen-band]], [[SEIRA]]

---

## Reststrahlen-band | Reststrahlen Band | 레스트스트랄렌 대역

EN: Reststrahlen Band
KO: 레스트스트랄렌 대역(잔류선 대역)
ABBR: —
CATEGORY: 광 물리 현상
DESC:
극성 결정에서 종방향/횡방향 광학 포논 주파수 사이의 영역으로, 굴절률 실부분이 음수가 되어 표면 포논 폴라리톤(SPhP)이 지지되는 적외선 대역.
RELATED: [[SPhP]]

---

## FWHM | Full Width at Half Maximum | 반치전폭

EN: Full Width at Half Maximum
KO: 반치전폭
ABBR: FWHM
CATEGORY: 성능 지표 (Metric)
DESC:
공명 피크의 최대값 절반 높이에서의 폭. 좁을수록 분광 분해능과 검출 정밀도가 높음. FoM 계산에 사용된다.
RELATED: [[FoM]], [[RI]]

---

## FoM | Figure of Merit | 성능 지수

EN: Figure of Merit
KO: 성능 지수
ABBR: FoM
CATEGORY: 성능 지표
DESC:
플라즈모닉 RI 센서의 감도를 공명 선폭으로 정규화한 무차원 지수. 값이 클수록 단위 RI 변화당 더 큰 파장 이동과 더 날카로운 공명을 의미.
FORMULA: FoM = S_RI / FWHM
RELATED: [[RI]], [[FWHM]]

---

## EF | Enhancement Factor | 증강 인자

EN: Enhancement Factor
KO: 증강 인자
ABBR: EF
CATEGORY: 성능 지표
DESC:
SEIRA·SERS 등에서 플라즈모닉 증강 효율을 나타내는 표준 지표. 안테나에 의한 광학적 이득과 핫스팟에 위치한 분자 비율을 모두 반영. SEIRA의 초기 EF는 10¹–10²였으나 메타표면 도입 후 크게 향상.
FORMULA: EF = (I_SEIRA/I_ref) × (N_ref/N_SEIRA)
RELATED: [[SEIRA]], [[SERS]], [[hot-spot]]

---

## LOD | Limit of Detection | 검출 한계

EN: Limit of Detection
KO: 검출 한계
ABBR: LOD
CATEGORY: 성능 지표
DESC:
센서가 신뢰성 있게 검출할 수 있는 최소 분석물 농도. 예: 도파민 검출에서 뇌척수액 1.3 attomolar, 전혈 1.5 attomolar, 인공 땀 0.5 attomolar 달성.
RELATED: [[sensitivity]], [[detection-limit]]

---

## Sensitivity | Sensitivity (S_RI) | 감도

EN: Sensitivity
KO: 감도
ABBR: S, S_RI
CATEGORY: 성능 지표
DESC:
RI 센서에서는 단위 굴절률 변화당 공명 파장 이동량(nm/RIU)으로 정의. 예시: 금 나노디스크 어레이 113 nm/RIU, 실리콘 질화물 마이크로링 750 nm/RIU.
FORMULA: S_RI = Δλ / Δn
RELATED: [[RI]], [[FoM]], [[RIU]]

---

## RIU | Refractive Index Unit | 굴절률 단위

EN: Refractive Index Unit
KO: 굴절률 단위
ABBR: RIU
CATEGORY: 성능 지표 단위
DESC:
RI 센서 감도 표기 단위(nm/RIU). 단위 굴절률 변화에 대응되는 공명 파장 이동(nm) 수치를 의미.
RELATED: [[Sensitivity]], [[RI]]

---

## hot-spot | Hot Spot | 핫스팟

EN: Hot Spot
KO: 핫스팟 / 열점
ABBR: —
CATEGORY: 광 물리 현상
DESC:
플라즈모닉 나노구조의 좁은 갭이나 첨두에서 입사 전자기장이 극단적으로 집중되는 나노스케일 영역. SEIRA·SERS·SEF 증강의 핵심 메커니즘. 14 nm 갭 금 보타이에서 형광 1340배 증강 사례.
RELATED: [[SEIRA]], [[SERS]], [[SEF]], [[nanoantenna]]

---

## nanoantenna | Plasmonic Nanoantenna | 플라즈모닉 나노안테나

EN: Plasmonic Nanoantenna
KO: 플라즈모닉 나노안테나
ABBR: —
CATEGORY: 광 부품 / 메타구조
DESC:
입사광을 나노스케일 영역으로 집속해 광-물질 상호작용을 극대화하는 금속 나노구조. 비대칭 십자, 분할 링 공진기(SRR), 프랙탈, 후크형, 슈퍼셀, 그라디언트 등 다양한 형태로 SEIRA·SERS 성능을 조정. WMHNA(파장다중 후크 나노안테나) 등.
RELATED: [[metasurface]], [[hot-spot]], [[SRR]], [[SEIRA]]

---

## metasurface | Metasurface | 메타표면

EN: Metasurface
KO: 메타표면
ABBR: —
CATEGORY: 광 부품 / 메타구조
DESC:
파장 이하 크기의 인공 단위셀(meta-atom)을 평면에 주기적으로 배열하여 광의 위상·진폭·편광을 임의 제어하는 2차원 인공구조. SEIRA, 키랄 검출, 무분광기 검출, 광역 흡수기 등에 활용. 공간 다중화 메타표면은 RI 변화를 원거리장 강도 패턴으로 인코딩.
RELATED: [[nanoantenna]], [[SRR]], [[plasmonic-metamaterial]]

---

## nanopedestal | Nanopedestal | 나노 받침대

EN: Nanopedestal
KO: 나노받침대
ABBR: —
CATEGORY: 광 부품 / 구조
DESC:
유전체 기판 일부를 식각해 플라즈모닉 소자를 자유 공간으로 들어올린 구조. 평면 나노안테나 대비 SEIRA 감도 2.5–10배 향상 및 분석물 포획 능력 강화.
RELATED: [[SEIRA]], [[nanoantenna]]

---

## SRR | Split-Ring Resonator | 분할 링 공진기

EN: Split-Ring Resonator
KO: 분할 링 공진기
ABBR: SRR
CATEGORY: 광 부품 / 메타구조
DESC:
링의 일부를 잘라낸 형태의 공진형 메타원자. SEIRA 강화 및 단일 분자 단층 적외선 검출에 사용.
RELATED: [[metasurface]], [[SEIRA]]

---

## supercell | Supercell Nanoantenna | 슈퍼셀 나노안테나

EN: Supercell (16 hook-shaped nanoantenna sub-cells)
KO: 슈퍼셀(후크형 나노안테나 16셀 배열)
ABBR: —
CATEGORY: 광 부품 / 메타구조
DESC:
16개의 후크형 서브셀로 구성된 안테나 배열로, 안테나 간 결합을 억제하면서 6–9 µm 연속 공명을 구현. 광대역 SEIRA 측정에 적합.
RELATED: [[nanoantenna]], [[SEIRA]]

---

## waveguide | Optical Waveguide | 광 도파관

EN: Optical Waveguide
KO: 광 도파관
ABBR: —
CATEGORY: 광 부품
DESC:
고굴절률 코어를 저굴절률 클래딩으로 둘러싸 전반사 또는 모드 가둠으로 빛을 안내하는 유전체 구조. 코어 밖으로 새어나가는 소산장(evanescent field)을 이용해 RI 센싱·가스 센싱 수행. 부파장 격자(SWG) 구조로 외부 가둠 인자를 85.9%까지 향상한 예가 있다.
RELATED: [[evanescent-field]], [[SWG]], [[SOI]], [[MZI]], [[MRR]]

---

## evanescent-field | Evanescent Field | 소산장

EN: Evanescent Field
KO: 소산장 / 에바네센트 장
ABBR: —
CATEGORY: 광 물리 현상
DESC:
도파관 코어 외부로 지수 감쇠하며 새어나가는 광학 장. 주변 매질의 굴절률 변화에 따라 가이드 모드의 유효 굴절률이 이동하여, 공명 파장·전송 강도·위상 변화로 검출 가능.
RELATED: [[waveguide]], [[RI]]

---

## SWG | Subwavelength Grating | 부파장 격자

EN: Subwavelength Grating
KO: 부파장 격자
ABBR: SWG
CATEGORY: 광 부품 / 구조
DESC:
파장보다 작은 주기로 패턴된 격자 구조. 도파관 지지대로 사용 시 하부 산화막을 제거해 저전파손실과 큰 외부 가둠 인자를 동시에 달성. 광자코(photonic nose) 등에 사용.
RELATED: [[waveguide]], [[photonic-nose]]

---

## SOI | Silicon-on-Insulator | 실리콘 온 인슐레이터

EN: Silicon-on-Insulator
KO: 실리콘 온 인슐레이터
ABBR: SOI
CATEGORY: 광 부품 / 재료 플랫폼
DESC:
실리콘 박막 아래 매립 산화막(BOX)을 둔 웨이퍼 플랫폼. 근적외선(1.3–1.55 µm) 영역의 실리콘 포토닉스 표준 기판으로 PIC 제작에 광범위 사용.
RELATED: [[silicon-photonics]], [[PIC]], [[waveguide]]

---

## silicon-photonics | Silicon Photonics | 실리콘 포토닉스

EN: Silicon Photonics
KO: 실리콘 포토닉스
ABBR: —
CATEGORY: 광자 하드웨어 / 재료 플랫폼
DESC:
실리콘(SOI) 기반 광집적 기술. 근적외선에서는 우수하나, 가시광 및 ~8 µm 초과 중적외선에서는 불투명. 활성 광원 부재로 III-V 화합물(InP, GaAs) 또는 그래핀·리튬 니오베이트 등의 이종 통합이 필요.
RELATED: [[SOI]], [[PIC]], [[lithium-niobate]]

---

## MRR | Microring Resonator | 마이크로링 공진기

EN: Microring Resonator
KO: 마이크로링 공진기
ABBR: MRR
CATEGORY: PIC 부품
DESC:
링 형태의 광 공진기. 공명 파장 이동으로 특징 추출 또는 RI 센싱 수행. AlN MRR는 Pockels 효과로 0.26 pm/V의 DC 튜닝 효율, Q≈65,700 달성. 듀얼 마이크로링 실리콘 질화물 PIC는 SARS-CoV-2 RNA를 10 cp/µL 수준으로 라벨-프리 검출.
RELATED: [[PIC]], [[Pockels-effect]], [[MZI]], [[Q-factor]]

---

## MZI | Mach-Zehnder Interferometer | 마하-젠더 간섭계

EN: Mach-Zehnder Interferometer
KO: 마하-젠더 간섭계
ABBR: MZI
CATEGORY: PIC 부품
DESC:
두 광 경로의 위상차를 간섭으로 검출하는 광 부품. PIC에서 신경망식 가중치 부여(matrix-vector multiplication)에 활용. Si MZI는 30 dB 변조 깊이와 V_π ≈ 5.6 V 구현, 열광학 히터로 가중치 조정.
RELATED: [[PIC]], [[PNN]], [[MRR]]

---

## PPM | Plasmonic Phase Modulator | 플라즈모닉 위상 변조기

EN: Plasmonic Phase Modulator
KO: 플라즈모닉 위상 변조기
ABBR: PPM
CATEGORY: PIC 부품
DESC:
표면 플라즈몬 폴라리톤의 위상에 40 Gbit/s 정보를 인코딩하는 변조기. 길이 29 µm. 두 금속 패드 사이 비선형 유기 슬롯에 Pockels 효과로 굴절률 변조. 1550 nm 중심 120 nm 대역, 65 GHz 변조 응답, 85 °C 열적 안정성.
RELATED: [[SPP]], [[Pockels-effect]], [[plasmonic-modulator]]

---

## MIM | Metal-Insulator-Metal Waveguide | 금속-절연체-금속 도파관

EN: Metal-Insulator-Metal Waveguide
KO: 금속-절연체-금속 도파관
ABBR: MIM
CATEGORY: 플라즈모닉 도파관
DESC:
두 금속층 사이에 얇은 절연체를 둔 도파관. 플라즈모닉 모드를 강하게 가둠. MSM 광검출기와 통합 시 빠른 광응답과 높은 SNR 달성.
RELATED: [[MSM]], [[plasmonic-detector]]

---

## MSM | Metal-Semiconductor-Metal Photodetector | 금속-반도체-금속 광검출기

EN: Metal-Semiconductor-Metal Photodetector
KO: 금속-반도체-금속 광검출기
ABBR: MSM
CATEGORY: PIC 부품
DESC:
플라즈몬 신호를 접점 겸 커플러로 동작시키는 초고속 검출기. 660 nm에서 3.5 µm, 870 nm에서 9.5 µm의 e⁻¹ 감쇠 길이.
RELATED: [[MIM]], [[photodetector]]

---

## Pockels-effect | Pockels Effect | 포켈스 효과

EN: Pockels Effect (Linear Electro-Optic Effect)
KO: 포켈스 효과 (선형 전기광학 효과)
ABBR: —
CATEGORY: 광 물리 현상
DESC:
전기장에 비례해 굴절률이 선형으로 변하는 전기광학 효과. AlN, 리튬 니오베이트, 비선형 유기 폴리머 등에서 발현되며, PPM, AlN MRR, TENG-구동 광 변조기 등의 동작 원리.
RELATED: [[PPM]], [[MRR]], [[TENG]]

---

## BM | Burstein-Moss Effect | 버스타인-모스 효과

EN: Burstein-Moss Effect
KO: 버스타인-모스 효과
ABBR: BM
CATEGORY: 광 물리 현상
DESC:
반도체의 캐리어 농도 증가로 전도대가 채워지면서 흡수단이 고에너지 쪽으로 밀려 겉보기 밴드갭이 커지는 현상. 플라즈몬으로 증강된 BM 효과로 CdS 나노와이어 레이저 파장을 504→483 nm 튜닝.
RELATED: [[plasmonic-laser]], [[CdS-nanowire]]

---

## plasmonic-laser | Plasmonic Laser | 플라즈모닉 레이저

EN: Plasmonic Laser
KO: 플라즈모닉 레이저
ABBR: —
CATEGORY: PIC 부품 / 광원
DESC:
플라즈몬 공명을 활용한 나노광원. 단일 반도체 나노와이어(CdS) + SiO₂/Au 박막 하이브리드 구조에서 BM 효과로 레이저 파장 조절 가능.
RELATED: [[BM]], [[CdS-nanowire]]

---

## plasmonic-logic-gate | Plasmonic Logic Gate | 플라즈모닉 논리 게이트

EN: Plasmonic Logic Gate
KO: 플라즈모닉 논리 게이트
ABBR: —
CATEGORY: PIC 부품 / 광 컴퓨팅
DESC:
유기/금속 나노와이어 이종접합에서 엑시톤 폴라리톤과 표면 플라즈몬을 결합해 광학적 OR/AND 연산을 수행. 입사 레이저 편광 방향으로 출력 강도를 조정, 임계값 0.4 au 기준으로 (1,1)→1 등의 논리 동작 구현.
RELATED: [[exciton-polariton]], [[SPP]]

---

## plasmonic-switcher | Plasmonic Switcher | 플라즈모닉 스위처

EN: Plasmonic Optical Switcher
KO: 플라즈모닉 광 스위처
ABBR: —
CATEGORY: PIC 부품
DESC:
서브파장·고속·저전력 광 스위치. UV로 광크롬 분자가 가역적으로 변화하면서 단일 금 나노로드의 플라즈몬 공명과의 결합을 조절. 변조 깊이 7.2 dB, 단일 나노로드 스위치 동작에 ~13 pW 전력과 ~39 pJ 에너지만 필요.
RELATED: [[plasmonic-switching]], [[photochromic]]

---

## in-sensor-computing | In-Sensor Computing | 센서 내 컴퓨팅

EN: In-Sensor Computing
KO: 센서 내(內) 컴퓨팅 / 인-센서 컴퓨팅
ABBR: —
CATEGORY: AI / 컴퓨팅 패러다임
DESC:
센서 하드웨어 내부에서 신호 처리·패턴 인식·신경망 추론을 수행하여, 데이터를 디지털화·전송하기 전에 의미를 추출하는 패러다임. 지연·에너지 비용 절감, 클라우드 의존도 제거, 의료 진단·자율주행 등 실시간 응용에 필수.
RELATED: [[edge-intelligence]], [[NSEC]], [[PNN]], [[PIC]]

---

## NSEC | Near-Sensor Edge Computing | 센서 근접 엣지 컴퓨팅

EN: Near-Sensor Edge Computing
KO: 센서 근접 엣지 컴퓨팅
ABBR: NSEC
CATEGORY: AI / 컴퓨팅 패러다임
DESC:
센서와 분리되었지만 물리적으로 인접한 위치에서 처리를 수행하는 시스템. AlN MRR(특징 추출) + Si MZI(신경망 가중)를 결합한 AlN/Si PIC 플랫폼이 대표 사례. 4×4 PNN으로 13가지 ASL 제스처 100% 정확도, 7개 보행 사이클 99% 분류.
RELATED: [[in-sensor-computing]], [[PNN]], [[TENG]], [[MRR]], [[MZI]]

---

## edge-intelligence | Edge Intelligence | 엣지 인텔리전스

EN: Edge Intelligence
KO: 엣지 인텔리전스
ABBR: —
CATEGORY: AI / 컴퓨팅 패러다임
DESC:
센서 위치에서 직접 집약적 계산을 수행해, 클라우드 의존 없이 즉각 의사결정을 가능케 하는 흐름. PIC 기반 인-센서 컴퓨팅의 상위 개념.
RELATED: [[in-sensor-computing]], [[NSEC]]

---

## PNN | Photonic Neural Network | 광자 신경망

EN: Photonic Neural Network
KO: 광자 신경망
ABBR: PNN
CATEGORY: AI / 광 컴퓨팅
DESC:
광 도파관·MZI·MRR로 구현된 행렬-벡터 곱셈 기반 신경망. 4×4 PNN은 칩 위에서 글러브 제스처 96.77%, 양말 보행 98.31% 정확도(아날로그 대비 향상). 추론당 <10 ns 지연, <0.34 pJ 에너지의 VR/AR·낙상 감지에 응용 전망.
RELATED: [[MZI]], [[MRR]], [[in-sensor-computing]]

---

## CNN | Convolutional Neural Network | 합성곱 신경망

EN: Convolutional Neural Network (1D-CNN here)
KO: 합성곱 신경망 (본문은 1D-CNN)
ABBR: CNN, 1D-CNN
CATEGORY: AI / 머신러닝
DESC:
공간(또는 1D 시계열)에서의 국소 패턴을 합성곱 필터로 추출하는 신경망. 본 논문에서는 3.65–3.80 µm MIR 흡수 스펙트럼으로부터 IPA/아세톤 19개 혼합비를 분류, 미지 데이터 93.6% 정확도.
RELATED: [[MLP]], [[photonic-nose]], [[in-sensor-computing]]

---

## MLP | Multilayer Perceptron | 다층 퍼셉트론

EN: Multilayer Perceptron
KO: 다층 퍼셉트론
ABBR: MLP
CATEGORY: AI / 머신러닝
DESC:
완전연결 다층 신경망. 본문에서는 혼합 스펙트럼을 순수 성분 스펙트럼으로 분해하는 회귀에 사용되어, 모든 혼합물에 대해 평균 RMSE 2.44 vol% 달성.
RELATED: [[CNN]], [[regression]]

---

## photonic-nose | Photonic Nose | 광자 코

EN: Photonic Nose
KO: 광자 코
ABBR: —
CATEGORY: 응용 (Application)
DESC:
인간 후각을 모방한, 가스 혼합물 검출용 광학 센서. SOI MIR 도파관 + SWG + 1D-CNN/MLP 조합으로 휘발성 유기화합물(VOC) 검출. 응답시간 4 s 이하, 평균 후 200 ppm 검출한계.
RELATED: [[VOC]], [[SWG]], [[CNN]], [[MLP]]

---

## photonic-tongue | Photonic Tongue | 광자 혀

EN: Photonic Tongue
KO: 광자 혀
ABBR: —
CATEGORY: 응용
DESC:
액체 분석물(예: 와인 향)을 다중수용체로 인식해 화학정량적으로 모델링하는 SERS 기반 시스템. 8개 SERS 기판에 자기조립 단분자막(SAM)을 다르게 기능화해 "수용체 무관" 센싱 플랫폼 구축.
RELATED: [[SERS]], [[SAM]]

---

## TENG | Triboelectric Nanogenerator | 마찰전기 나노발전기

EN: Triboelectric Nanogenerator
KO: 마찰전기 나노발전기
ABBR: TENG
CATEGORY: 센서 / 자가전원
DESC:
접촉-분리 기반 자가전원 압력/힘 센서. 출력 전압이 인가력에 비례. NSEC 칩에서 장갑·양말 부착 TENG가 AlN MRR을 구동, 광 적분기 역할로 동작.
RELATED: [[NSEC]], [[Pockels-effect]], [[wearable]]

---

## MIR | Mid-Infrared | 중적외선

EN: Mid-Infrared
KO: 중적외선
ABBR: MIR
CATEGORY: 파장 영역
DESC:
약 2.5–25 µm(파수 4000–400 cm⁻¹) 영역. 분자의 진동·회전 지문(fingerprint)이 위치해 SEIRA·MIR 도파관 가스 센싱·VCD 등에 핵심.
RELATED: [[SEIRA]], [[VOC]], [[photonic-nose]]

---

## VOC | Volatile Organic Compound | 휘발성 유기화합물

EN: Volatile Organic Compound
KO: 휘발성 유기화합물
ABBR: VOC
CATEGORY: 분석 대상
DESC:
대기 중에서 쉽게 기화되는 유기화합물(IPA, 아세톤 등). 광자 코 등에서 검출 대상.
RELATED: [[photonic-nose]], [[MIR]]

---

## IPA | Isopropyl Alcohol | 이소프로필 알코올

EN: Isopropyl Alcohol
KO: 이소프로필 알코올 / 아이소프로판올
ABBR: IPA
CATEGORY: 분석 대상 (VOC)
DESC:
대표적 VOC 분석물. MIR 광자 코에서 아세톤과 혼합비를 1D-CNN으로 분류·정량.
RELATED: [[VOC]], [[photonic-nose]]

---

## CMOS | Complementary Metal-Oxide-Semiconductor | 상보형 금속산화막 반도체

EN: Complementary Metal-Oxide-Semiconductor
KO: 상보형 금속산화막 반도체
ABBR: CMOS
CATEGORY: 전자/광자 공정 플랫폼
DESC:
표준 반도체 공정. 본문에서는 8인치 SOI 웨이퍼 위 AlN/Si 이중층 도파관을 CMOS 호환 공정(딥-UV 리소그래피, 식각, SiO₂ 평탄화 등)으로 제작.
RELATED: [[PIC]], [[NSEC]], [[SOI]]

---

## Q-factor | Quality Factor | 품질 계수

EN: Quality Factor
KO: 품질 계수 / Q-인자
ABBR: Q
CATEGORY: 성능 지표
DESC:
공진기의 에너지 저장 효율 지표. AlN MRR Q ≈ 65,700 보고. 클수록 좁은 선폭과 높은 분해능.
RELATED: [[MRR]], [[FWHM]]

---

## hot-spot enrichment | Molecular Enrichment Coating | 분자 농축 코팅

EN: Molecular Enrichment Coating
KO: 분자 농축 코팅
ABBR: —
CATEGORY: 표면 기능화
DESC:
나노안테나 표면을 ZIF-8(MOF), MOF/폴리머 하이브리드 등으로 코팅해 기체 분자를 농축. CO₂ 검출한계를 ppm 미만으로 낮춤(Li 등).
RELATED: [[MOF]], [[SEIRA]]

---

## MOF | Metal-Organic Framework | 금속-유기 골격체

EN: Metal-Organic Framework
KO: 금속-유기 골격체 / 금속-유기 구조체
ABBR: MOF
CATEGORY: 재료
DESC:
금속 이온/클러스터와 유기 링커가 결합한 다공성 결정 재료. 가스 분자 흡착/농축, 광섬유 센서 코팅, SEIRA 향상에 활용.
RELATED: [[ZIF-8]], [[hot-spot-enrichment]]

---

## ZIF-8 | Zeolitic Imidazolate Framework-8 | 제올라이트성 이미다졸레이트 골격체-8

EN: Zeolitic Imidazolate Framework-8
KO: 제올라이트성 이미다졸레이트 골격체-8
ABBR: ZIF-8
CATEGORY: 재료 (MOF의 일종)
DESC:
대표적 MOF 중 하나로, 가스 농축 코팅에 사용되어 SEIRA 감도를 크게 향상.
RELATED: [[MOF]], [[SEIRA]]

---

## SAM | Self-Assembled Monolayer | 자기조립 단분자막

EN: Self-Assembled Monolayer
KO: 자기조립 단분자막
ABBR: SAM
CATEGORY: 표면 기능화
DESC:
기판 표면에 분자가 자발적으로 정렬하여 형성하는 단분자층. SERS 기판에 다양한 SAM을 기능화해 "SERS taster" 등 다중수용체 센서 구축. 혼합-티올 SAM은 장거리 표면 플라즈몬을 지지해 E. coli를 <10 CFU/mL 검출.
RELATED: [[SERS]], [[photonic-tongue]], [[E-coli]]

---

## aptamer | Aptamer | 압타머

EN: Aptamer
KO: 압타머 / 핵산 결합체
ABBR: —
CATEGORY: 생체수용체
DESC:
표적 분자에 특이적으로 결합하는 짧은 DNA/RNA 올리고. 항체 대체로 RI 센서 표면 기능화에 사용. PSA-특이 DNA 압타머로 113 nm/RIU 감도, 검출한계 1.49 ng/mL 달성. DNA 압타머 + FITC + 은 나노입자 조합은 LOD 1.25 pM 도달.
RELATED: [[bioreceptor]], [[PSA]], [[RI]]

---

## bioreceptor | Bioreceptor / Biorecognition Element | 생체수용체

EN: Bioreceptor / Biorecognition Element
KO: 생체수용체 / 생체인식 소자
ABBR: —
CATEGORY: 표면 기능화
DESC:
센서 표면에 고정되어 표적 분석물을 특이적으로 포획하는 분자(항체, 압타머, 분자 임프린트 등). RI 센서에서 결합 후 국소 굴절률·공명 시그널 변화로 정량 분석.
RELATED: [[aptamer]], [[antibody]], [[RI]]

---

## ELISA | Enzyme-Linked Immunosorbent Assay | 효소면역측정법

EN: Enzyme-Linked Immunosorbent Assay
KO: 효소면역측정법
ABBR: ELISA
CATEGORY: 비교 진단 기법
DESC:
효소 결합 항체를 이용한 전통 면역측정법. 플라즈모닉 RI 센서가 라벨-프리·실시간으로 ELISA를 대체할 수 있음.
RELATED: [[PCR]], [[RI]], [[bioreceptor]]

---

## PCR | Polymerase Chain Reaction | 중합효소 연쇄반응

EN: Polymerase Chain Reaction
KO: 중합효소 연쇄반응
ABBR: PCR
CATEGORY: 비교 진단 기법
DESC:
DNA를 지수적으로 증폭하는 분자 진단의 표준. PIC 기반 라벨-프리 광학 진단의 비교 대상.
RELATED: [[ELISA]]

---

## PSA | Prostate-Specific Antigen | 전립선 특이 항원

EN: Prostate-Specific Antigen
KO: 전립선 특이 항원
ABBR: PSA
CATEGORY: 바이오마커
DESC:
전립선암 선별의 핵심 지표. 건강한 사람은 4.0–10 ng/mL, 10 ng/mL 초과 시 위험 상승. Khan 등은 PSA-특이 DNA 압타머 기능화 금 나노디스크 어레이로 1.49 ng/mL 검출.
RELATED: [[aptamer]], [[RI]], [[biomarker]]

---

## exosome | Exosome | 엑소좀

EN: Exosome
KO: 엑소좀
ABBR: —
CATEGORY: 바이오마커
DESC:
혈액·소변·타액 등 체액에 존재하는 50–150 nm 세포외 소포. 세포 간 분자 전달 매개. 상승된 엑소좀 수치는 악성 종양과 상관, 진단 바이오마커로 유망.
RELATED: [[nPLEX]], [[APEX]]

---

## nPLEX | Nanoplasmonic Exosome Assay | 나노플라즈모닉 엑소좀 분석

EN: Nanoplasmonic Exosome Assay
KO: 나노플라즈모닉 엑소좀 분석
ABBR: nPLEX
CATEGORY: 응용 플랫폼
DESC:
주기적 나노홀 어레이로 강한 SPR을 유도해 엑소좀 결합 시그널을 위상/강도 변화로 정량. 어레이 주기를 엑소좀 크기에 맞추면 감도 향상.
RELATED: [[exosome]], [[APEX]], [[LSPR]]

---

## APEX | Amplified Plasmonic Exosome | 증폭 플라즈모닉 엑소좀

EN: Amplified Plasmonic Exosome
KO: 증폭 플라즈모닉 엑소좀
ABBR: APEX
CATEGORY: 응용 플랫폼
DESC:
국소 광 증착과 in situ 효소 변환을 이중층 플라즈모닉 나노구조에 적용한 다중 엑소좀 프로파일링 플랫폼. 약 200개 엑소좀 수준 감도, 혈액 내 amyloid β 결합/비결합 엑소좀 직접 구별 가능 → 알츠하이머 뇌 플라크 부담 비침습 평가.
RELATED: [[exosome]], [[nPLEX]], [[amyloid-beta]]

---

## enantiomer | Enantiomer | 거울상 이성질체

EN: Enantiomer
KO: 거울상 이성질체
ABBR: —
CATEGORY: 화학 개념
DESC:
회전·평행이동으로 겹쳐지지 않는, 서로 거울상인 키랄 화합물의 두 형태. 동일한 원소조성·작용기를 갖지만 화학적 거동·약리 활성이 다를 수 있어, 의약·농약에서 구별이 필수.
RELATED: [[chirality]], [[CD]], [[VCD]]

---

## chirality | Chirality | 키랄성

EN: Chirality (Molecular Chirality)
KO: 키랄성 / 광학 이성성
ABBR: —
CATEGORY: 화학 개념
DESC:
거울상에 대한 비대칭성. 아미노산·핵산 등 생체분자에 보편적으로 존재. 분석화학·바이오의약 전반에서 핵심 분석 대상.
RELATED: [[enantiomer]], [[CD]], [[VCD]], [[ROA]]

---

## LCP-RCP | Left/Right Circularly Polarized Light | 좌/우 원편광

EN: Left/Right Circularly Polarized Light
KO: 좌원편광 / 우원편광
ABBR: LCP, RCP
CATEGORY: 광 편광
DESC:
전기장 벡터가 좌/우 회전하는 원편광. CD·VCD·ROA에서 좌·우 흡광 차이 또는 산란 차이로 키랄성을 측정. 키랄 메타표면은 입사 직선편광을 고정 헬리시티의 타원편광 모드로 변환.
RELATED: [[CD]], [[chirality]], [[Pancharatnam-Berry-phase]]

---

## Pancharatnam-Berry-phase | Pancharatnam-Berry Phase | 판차라트남-베리 위상

EN: Pancharatnam-Berry Phase
KO: 판차라트남-베리 위상 (기하 위상)
ABBR: PB-phase
CATEGORY: 광 물리 현상
DESC:
편광 상태의 기하학적 회전에 의해 발생하는 위상. McDonnell 등은 PB-위상 비선형 메타표면 기반 광대역 THz 방출기로 위상·헬리시티 동시 제어 → TCD 측정 실현.
RELATED: [[TCD]], [[metasurface]]

---

## microbottle-resonator | Microbottle Resonator | 마이크로보틀 공진기

EN: Microbottle Resonator
KO: 마이크로보틀 공진기
ABBR: —
CATEGORY: PIC 부품
DESC:
병 모양 광 공진기. PDMS/Pd-WO₃와 자기조립으로 결합 시, 25 °C에서 −3.091 nm/%H₂ 감도의 저비용 광섬유 수소 센서 구현. 습도·온도 간섭 최소.
RELATED: [[hydrogen-sensor]], [[plasmonic-microfiber]]

---

## plasmonic-microfiber | Plasmonic Optical Microfiber | 플라즈모닉 광 마이크로파이버

EN: Plasmonic Optical Microfiber Biosensor
KO: 플라즈모닉 광 마이크로파이버 바이오센서
ABBR: —
CATEGORY: 광섬유 센서
DESC:
LSPR로 에바네센트 장을 증폭한 광섬유 바이오센서. 50–500 nm 단일 분자/나노입자 검출. Huang 등의 이중증폭 인터페이스는 압타머 구조 변환과 플라즈모닉 증강을 결합해 도파민을 attomolar 수준 검출.
RELATED: [[LSPR]], [[aptamer]], [[evanescent-field]]

---

## SEI | Solid-Electrolyte Interphase | 고체-전해질 계면

EN: Solid-Electrolyte Interphase
KO: 고체-전해질 계면(상)
ABBR: SEI
CATEGORY: 응용 (배터리)
DESC:
리튬 금속 음극 표면에 형성되는 계면층. Yu 등은 depth-sensitive plasma-enhanced Raman으로 SEI 나노구조·화학조성 동적 분석, 차세대 배터리 설계 정보 제공.
RELATED: [[SERS]], [[lithium-anode]]

---

## SERS-taster | SERS Taster | SERS 미각센서

EN: SERS Taster
KO: SERS 미각센서
ABBR: —
CATEGORY: 응용 플랫폼
DESC:
복수의 비공유 수용체 화학을 SERS에 통합해 와인 등 액상 시료의 향 프로파일을 다중 분석하는 광자 혀 구현. 화학정량 모델링으로 예측 향 분석.
RELATED: [[photonic-tongue]], [[SERS]]

---

## fluorophore | Fluorophore | 형광단

EN: Fluorophore
KO: 형광단
ABBR: —
CATEGORY: 형광 분광 요소
DESC:
빛을 흡수해 형광을 방출하는 분자/구조. LSPR로 여기율 향상·수명 단축, 양자수율 상승. 알루미늄 나노입자와 수직 정렬 시 최대 3500배 증강.
RELATED: [[SEF]], [[quantum-yield]], [[LSPR]]

---

## quantum-yield | Quantum Yield | 양자 수율

EN: Quantum Yield
KO: 양자 수율
ABBR: —
CATEGORY: 형광 분광 성능 지표
DESC:
형광단이 흡수한 광자 대비 방출한 광자의 비율. 플라즈모닉 근접장에 의해 광학상태밀도(LDOS) 증가로 향상.
RELATED: [[SEF]], [[fluorophore]]

---

## bowtie-antenna | Bowtie Nanoantenna | 보타이 나노안테나

EN: Bowtie Nanoantenna
KO: 보타이 나노안테나
ABBR: —
CATEGORY: 광 부품 / 메타구조
DESC:
삼각형 두 개를 마주 본 보타이(나비넥타이) 형상의 플라즈모닉 안테나. 14 nm 갭 금 보타이로 나노갭 내 형광 1340배 증강 보고.
RELATED: [[nanoantenna]], [[hot-spot]], [[SEF]]

---

## eFMIA | Enhanced Fluorescence Microarray Immunoassay | 증강 형광 마이크로어레이 면역분석

EN: Enhanced Fluorescence Microarray Immunoassay
KO: 증강 형광 마이크로어레이 면역분석
ABBR: eFMIA
CATEGORY: 응용 플랫폼
DESC:
나노구조 금 나노섬 기판 위에 구축된 다중 증강 형광 면역분석. IRDye78의 근적외선 방출을 202.6배 증폭.
RELATED: [[SEF]], [[immunoassay]]

---

## SHIN | Shell-Isolated Nanoparticle | 쉘 격리 나노입자

EN: Shell-Isolated Nanoparticle (SHINERS-type)
KO: 쉘 격리 나노입자
ABBR: SHIN
CATEGORY: 광 부품 / 나노구조
DESC:
얇은 SiO₂ 셀로 둘러싼 Ag 입자(은 SHIN). depth-sensitive 라만 측정으로 SEI 분석 등에 활용.
RELATED: [[SERS]], [[SEI]]

---

## photonic-crystal-cavity | Photonic Crystal Cavity | 광결정 공동

EN: Photonic Crystal Cavity
KO: 광결정 공동(共洞)
ABBR: —
CATEGORY: 광 부품
DESC:
주기적 굴절률 변조로 광자 밴드갭을 형성한 결정 내의 결함 공진기. Xiong 등은 양자점 방출 증강과 깜빡임(blinking) 억제에 사용, 바이오센싱 플랫폼 개선.
RELATED: [[quantum-dot]], [[SEF]]

---

## quantum-dot | Quantum Dot | 양자점

EN: Quantum Dot
KO: 양자점
ABBR: QD
CATEGORY: 광 방출 재료
DESC:
나노미터 크기의 반도체 결정. 광결정 공동과 결합해 단일 양자점 디지털 해상도 바이오센싱에 활용.
RELATED: [[photonic-crystal-cavity]], [[SEF]]

---

## photonic-nanocavity | Plasmonic Nanocavity | 플라즈모닉 나노공동

EN: Plasmonic Nanocavity
KO: 플라즈모닉 나노공동
ABBR: —
CATEGORY: 광 부품
DESC:
형광과 라만 신호를 동시 증강해 단일 RITC 분자 반응 경로의 실시간 추적 가능(Li 등, 상관 분광).
RELATED: [[SEF]], [[SERS]]

---

## spatial-multiplexing-metasurface | Spatial-Multiplexing Metasurface | 공간 다중화 메타표면

EN: Spatial-Multiplexing Metasurface
KO: 공간 다중화 메타표면
ABBR: —
CATEGORY: 광 부품 / 무분광기 검출
DESC:
RI 변화를 원거리장 강도 패턴 변화로 인코딩하는 그라디언트/픽셀 메타표면. 협대역 광원과 단순 카메라로 분광기 없이 실시간 강도 시프트로 결합 사건 모니터링.
RELATED: [[metasurface]], [[RI]], [[spectrometer-free]]

---

## hyperspectral-imaging | Hyperspectral Imaging | 초분광 영상

EN: Hyperspectral Imaging
KO: 초분광 영상 / 하이퍼스펙트럴 이미징
ABBR: —
CATEGORY: 영상 기법
DESC:
공간 정보 각 화소에 연속 스펙트럼을 갖는 영상. 본 그룹의 SPhP 시스템은 중적외선 초분광 영상에 활용.
RELATED: [[SPhP]], [[MIR]]

---

## coupled-mode-theory | Coupled-Mode Theory | 결합모드 이론

EN: Coupled-Mode Theory
KO: 결합모드 이론
ABBR: CMT
CATEGORY: 이론
DESC:
공진기 간 에너지 결합을 기술하는 이론. Li 등이 과결합(overcoupled) 메타재료 흡수기를 설계해 6–14 µm에 걸친 균일 증강을 실현, 13개 분석물의 지문 동시 검출.
RELATED: [[metasurface]], [[SEIRA]]

---

## finite-difference-time-domain | FDTD Simulation | 시간영역 유한차분법

EN: Finite-Difference Time-Domain Simulation
KO: 시간영역 유한차분법 시뮬레이션
ABBR: FDTD
CATEGORY: 수치 해석 기법
DESC:
맥스웰 방정식을 시간·공간으로 이산화하여 푸는 전자기 시뮬레이션. SWG 주기·듀티 사이클 최적화에 사용되어 가둠 인자/손실 균형 FoM 0.77 달성.
RELATED: [[SWG]], [[waveguide]]

---

## VR-AR | Virtual / Augmented Reality | 가상현실/증강현실

EN: Virtual Reality / Augmented Reality
KO: 가상현실 / 증강현실
ABBR: VR/AR
CATEGORY: 응용 분야
DESC:
PNN 기반 초저지연(<10 ns)·초저에너지(<0.34 pJ/inference) 광 AI 인터페이스의 응용 후보. 메타버스 제어, 낙상 감지 등 칩 위에서 수행.
RELATED: [[PNN]], [[NSEC]]

---

## label-free | Label-Free Detection | 라벨-프리 검출

EN: Label-Free Detection
KO: 라벨-프리(비표지) 검출
ABBR: —
CATEGORY: 측정 방식
DESC:
형광 표지·효소 표지 없이 분석물을 직접 검출하는 방식. 플라즈모닉 RI 센서·실리콘 질화물 마이크로링 등이 라벨-프리·실시간 측정 제공.
RELATED: [[RI]], [[ELISA]]

---

## POC | Point-of-Care | 현장 진단

EN: Point-of-Care (diagnostics)
KO: 현장 진단 (POC)
ABBR: POC
CATEGORY: 응용 컨셉
DESC:
환자 가까이에서 신속히 수행하는 진단. 자원 제한 환경 등에서 라벨-프리 광 센서의 핵심 응용 컨셉.
RELATED: [[label-free]], [[SARS-CoV-2-sensor]]

---

## SARS-CoV-2-sensor | SARS-CoV-2 Optical Sensor | SARS-CoV-2 광 센서

EN: SARS-CoV-2 Plasmonic / Photonic Sensor
KO: SARS-CoV-2 플라즈모닉/광자 센서
ABBR: —
CATEGORY: 응용 (감염병 진단)
DESC:
COVID-19 신속 진단을 위한 광학 센서. Funari 등은 금-나노스파이크 옵토플루이딕 플랫폼(LSPR)으로 항-스파이크 항체 검출(183 nm/RIU, LOD 0.5 pM). Grosman 등은 SiN 듀얼 마이크로링 PIC로 바이러스 RNA를 10 cp/µL 검출(750 nm/RIU).
RELATED: [[LSPR]], [[MRR]], [[label-free]]

---

## breathalyzer-SERS | SERS-based Breathalyzer | SERS 호기 분석기

EN: SERS-based Breathalyzer
KO: SERS 기반 호기(숨) 분석기
ABBR: —
CATEGORY: 응용
DESC:
Leong 등은 비침습 COVID-19 스크리닝용 SERS 호기 분석기 개발, 민감도 96.2%·특이도 99.9% 달성.
RELATED: [[SERS]], [[POC]]

---

## wearable-SERS | Wearable Plasmonic-Metasurface Sensor | 웨어러블 플라즈모닉-메타표면 센서

EN: Wearable Plasmonic-Metasurface Sensor
KO: 웨어러블 플라즈모닉-메타표면 센서
ABBR: —
CATEGORY: 응용 (웨어러블)
DESC:
Wang 등이 개발한 신축성 SERS-활성 메타표면 + 마이크로유체 결합 센서로 땀을 지속 채취해 실시간 분자 프로파일링. Mogera 등은 플라즈모닉-페이퍼 기반 웨어러블로 땀 부피·속도·요산 농도 1 µM까지 동시 정량.
RELATED: [[SERS]], [[metasurface]], [[microfluidics]]

---

## SERS-nanoprobe-plant | SERS Nanoprobes in Plant Apoplast | 식물 아포플라스트 SERS 나노프로브

EN: SERS Nanoprobes in Plant Apoplast
KO: 식물 아포플라스트 SERS 나노프로브
ABBR: —
CATEGORY: 응용 (정밀 농업)
DESC:
Son 등이 식물 세포외 공간에 SERS 나노프로브를 도입해 살리실산·세포외 ATP·피토알렉신·글루타티온 등 내인성 스트레스 신호 분자를 비침습 실시간 추적.
RELATED: [[SERS]]

---

## amyloid-beta | Amyloid β | 아밀로이드 베타

EN: Amyloid β (Aβ)
KO: 아밀로이드 베타
ABBR: Aβ
CATEGORY: 바이오마커
DESC:
알츠하이머병 뇌 플라크 주성분 단백질. APEX 플랫폼으로 혈액 내 엑소좀-결합/비결합 Aβ 직접 구별 가능.
RELATED: [[APEX]], [[exosome]]

---

## dopamine-sensor | Dopamine Single-Molecule Sensor | 도파민 단분자 센서

EN: Dopamine Single-Molecule Sensor
KO: 도파민 단분자 센서
ABBR: —
CATEGORY: 응용 (신경전달물질)
DESC:
Huang 등의 압타머-플라즈모닉 광 마이크로파이버 이중증폭 인터페이스로 도파민을 뇌척수액 1.3 aM, 전혈 1.5 aM, 인공땀 0.5 aM 수준 검출. 압타머 서열 변경으로 타 분자에 적용 가능.
RELATED: [[plasmonic-microfiber]], [[aptamer]]

---

## E-coli-SEF | SEF-based E. coli Detection | SEF 기반 대장균 검출

EN: SEF-based E. coli Detection
KO: SEF 기반 대장균 검출
ABBR: —
CATEGORY: 응용 (병원체)
DESC:
Lakhtakia 팀은 다공성 금속 새김 표면(Ag/Al/Au/Cu)에서 ~20× 형광 증강. Knoll 등은 혼합 티올 SAM/Au 장거리 플라즈몬으로 10⁰–10⁶ CFU/mL 범위 검출.
RELATED: [[SEF]], [[SAM]]

---

## eFMIA-SARS | SEF Multiplexed Antibody Profiling | SEF 다중 항체 프로파일링

EN: SEF Multiplexed Antibody Profiling (SARS-CoV-2)
KO: SEF 다중 항체 프로파일링 (SARS-CoV-2)
ABBR: —
CATEGORY: 응용 (감염병)
DESC:
Hu 등은 나노구조 금 칩으로 SARS-CoV-2 변이 다중 항체 프로파일링, 20 fM LOD(유리 대비 >100×). Zhu 등은 in-frame Au NP 어레이 + 마이크로플레이트 리더로 N단백질 단분자 카운팅 0.84 ag/mL 도달.
RELATED: [[SEF]], [[SARS-CoV-2-sensor]]

---

## diffraction-limit | Diffraction Limit | 회절 한계

EN: Diffraction Limit of Light
KO: 빛의 회절 한계
ABBR: —
CATEGORY: 광 물리 개념
DESC:
유전체 매질 내 광 가둠의 근본 한계로, 전자기파를 파장보다 훨씬 작은 영역에 가둘 수 없게 만든다. 플라즈모닉 나노재료가 이를 우회해 IC 미세화에 기여.
RELATED: [[plasmonics]], [[PIC]]

---

## heterogeneous-integration | Heterogeneous Integration | 이종 집적

EN: Heterogeneous Integration
KO: 이종(이종소재) 집적
ABBR: —
CATEGORY: 공정 / 패키징
DESC:
실리콘 위에 III-V 반도체(InP, GaAs), 그래핀, 리튬 니오베이트, 압전 박막 등 기능성 재료를 본딩·공성장하는 공정. 광원 통합, 광학 활성 부여, 튜닝성 강화에 필요.
RELATED: [[silicon-photonics]], [[PIC]]

---

## chalcogenide-glass | Chalcogenide Glass | 칼코제나이드 유리

EN: Chalcogenide Glass
KO: 칼코제나이드 유리
ABBR: —
CATEGORY: 재료 / 중적외선 플랫폼
DESC:
중적외선 영역에 투명한 비정질 유리. 실리콘의 8 µm 한계를 넘어선 MIR PIC 재료 후보.
RELATED: [[MIR]], [[silicon-photonics]]

---

## silicon-nitride | Silicon Nitride (SiN) | 실리콘 질화물

EN: Silicon Nitride
KO: 실리콘 질화물 (SiN)
ABBR: SiN
CATEGORY: 재료 / 광자 플랫폼
DESC:
가시광부터 근적외선까지 광범위 투명. Grosman 등의 듀얼 마이크로링 PIC SARS-CoV-2 센서, Yan 등의 LN 리브 도파관 광열 가스 센서 등에서 활용.
RELATED: [[PIC]], [[MRR]]

---

## lithium-niobate | Lithium Niobate (LN) | 리튬 니오베이트

EN: Lithium Niobate
KO: 리튬 니오베이트 (LiNbO₃)
ABBR: LN
CATEGORY: 재료 / 전기광학
DESC:
강한 Pockels 효과를 가진 강유전체. 고속 변조기·온칩 광열 가스 센서에 사용.
RELATED: [[Pockels-effect]], [[PIC]]

---

## graphene-photodetector | Waveguide-Integrated Graphene Photodetector | 도파관 통합 그래핀 광검출기

EN: Waveguide-Integrated Graphene Photodetector
KO: 도파관 통합 그래핀 광검출기
ABBR: —
CATEGORY: PIC 부품
DESC:
바이어스 전압으로 광응답률을 16단계(4비트)로 조정 가능. 부유 실리콘 도파관에 결합되어 신경모방 처리(MIR 3.65–3.8 µm) 수행. 2×2 합성곱 커널, 손동작 인식, 가스 혼합물 분류에 동시 활용.
RELATED: [[in-sensor-computing]], [[CNN]], [[SWG]]

---

## memristor | Memristor / Memtransistor | 멤리스터 / 멤트랜지스터

EN: Memristor / Memtransistor
KO: 멤리스터 / 멤트랜지스터
ABBR: —
CATEGORY: 전자식 인-센서 컴퓨팅
DESC:
전기 신호 처리용 저항성/용량성 센서(촉각·가스·관성·생체)와 결합되는 전자식 인-센서 컴퓨팅 칩의 기본 요소.
RELATED: [[in-sensor-computing]], [[PNN]]

---

## photodetector-array | Photodetector Array for AI | AI용 광검출기 어레이

EN: Photodetector Array for AI Computing
KO: AI 연산용 광검출기 어레이
ABBR: —
CATEGORY: 광전 인-센서 컴퓨팅
DESC:
이미지·스펙트럼·편광 신호 처리용 광검출기 기반 광전 인-센서 컴퓨팅 칩.
RELATED: [[in-sensor-computing]], [[graphene-photodetector]]

---

## LiDAR-sensor | LiDAR Sensor | 라이다 센서

EN: LiDAR Sensor
KO: 라이다 센서 (광 측거 센서)
ABBR: LiDAR
CATEGORY: 응용
DESC:
광학 측거/거리 측정 센서. 광자 인-센서 컴퓨팅의 분광·LiDAR·양자 센서 군에 포함.
RELATED: [[photonic-sensor]]

---

## energy-harvesting | Energy Harvesting | 에너지 하베스팅

EN: Energy Harvesting (Solar, RF, Photonic)
KO: 에너지 하베스팅 (태양·RF·광 전력 전송)
ABBR: —
CATEGORY: 자율 동작
DESC:
태양광·RF·광섬유 전력 전송 등으로 자가 동작하는 센서 노드 구성. 무선 통신과 결합해 환경/의료 센서 네트워크 무한 운용을 지향.
RELATED: [[wearable]], [[autonomy]]

---

## smart-pixel | Smart Pixel / Smart Waveguide | 스마트 픽셀 / 스마트 도파관

EN: Smart Pixel / Smart Waveguide
KO: 스마트 픽셀 / 스마트 도파관
ABBR: —
CATEGORY: 미래 전망
DESC:
패턴 인식 등 연산을 본질적으로 수행하는 센싱 요소 개념. 센서와 컴퓨터의 경계를 흐릿하게 만드는 차세대 광학 소자.
RELATED: [[in-sensor-computing]], [[PNN]]
