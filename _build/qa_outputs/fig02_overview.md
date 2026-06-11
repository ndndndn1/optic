### 예상 질문과 답변

#### Q. (a)의 검은 곡선과 빨간 곡선은 왜 오른쪽으로 이동해 있나요?
A. (a)는 RI sensing, 즉 굴절률 변화 감지입니다. 작은 센서 표면 주변 굴절률이 `n`에서 `n + Δn`으로 변하면 플라즈몬 공명 조건이 바뀌고, 그래프의 공명 피크가 파장축 `λ`에서 오른쪽으로 이동합니다. 그림의 `Δλ` 화살표가 바로 이 공명 파장 이동량입니다.  
근거: Figure 2(a) 캡션과 본문 2.1. 논문은 표적 결합이 국소 RI를 바꾸고 그 결과 공명 파장, 진폭, 위상이 변한다고 설명합니다. RI sensitivity는 `Δλ/Δn` 문맥으로 제시됩니다 [22-29]. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. (a)의 y축이 Intensity인데, RI 센서는 세기 변화를 보는 건가요, 파장 이동을 보는 건가요?
A. 이 그림에서는 주된 메시지가 피크의 “세기 크기”보다 “피크 위치 이동”입니다. y축은 광 응답의 세기이고 x축은 파장 `λ`인데, 검은 피크와 빨간 피크의 최대점이 달라지며 `Δλ`가 생깁니다. 실제 RI 센서는 파장 이동뿐 아니라 진폭이나 위상 변화도 추적할 수 있지만, 이 패널은 파장 이동을 대표적으로 그렸습니다.  
근거: Figure 2(a), 본문 2.1. 공명 파장, 진폭, 위상 변화가 모두 신호가 될 수 있다고 설명하지만, 식에서는 `Δλ`와 `Δn`의 관계를 강조합니다 [27-29]. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. (a)의 노란 막대와 회색 받침은 무엇을 뜻하나요?
A. 회색 받침은 플라즈몬 센서 기판 또는 나노구조 표면, 노란 막대는 표면에 놓인 감지층이나 결합된 물질을 단순화한 모식도로 볼 수 있습니다. 왼쪽은 주변 굴절률 `n`, 오른쪽은 분석물 결합 등으로 `n + Δn`이 된 상태입니다. 다만 이 그림만으로는 실제 재료가 금인지, 항체인지, 박막인지 확정할 수 없습니다.  
근거: Figure 2(a), 본문 2.1. 표면 기능화, 항체·압타머·분자각인체 같은 생체인식층, 표적 결합에 따른 국소 RI 변화가 설명됩니다 [27]. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. (b) SEIRA 그래프에서 빨간 곡선에 두 개의 dip이 생기는 이유는 무엇인가요?
A. 빨간 곡선은 안테나가 있을 때의 강화된 적외선 흡수 응답을 나타내며, `Amide I`, `Amide II` 위치에서 단백질 진동 흡수 지문이 나타납니다. 그래서 넓은 플라즈몬 배경 위에 특정 분자 진동 모드가 dip처럼 보입니다.  
근거: Figure 2(b), 본문 2.2. SEIRA는 분자의 진동 fingerprint를 플라즈몬 나노안테나 hot spot에서 강화한다고 설명하며, 성능 지표 EF도 제시됩니다 [7,30-35]. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. (b)의 “protein fingerprint”는 단백질 전체 모양을 보는 건가요?
A. 아닙니다. 여기서 fingerprint는 현미경 이미지 같은 형태가 아니라, 단백질 분자의 진동 모드가 만드는 스펙트럼 패턴입니다. 그림의 `Amide I`, `Amide II`는 단백질에서 자주 쓰이는 적외선 진동 밴드 예시입니다.  
근거: Figure 2(b), 본문 2.2. 적외선 분광은 생화학 분자의 고유 진동 fingerprint를 포착한다고 설명됩니다 [30-32]. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. (b)의 빨간 선 “with antennas”와 작은 검은/회색 신호는 무엇이 다른가요?
A. 안테나가 없으면 단백질 흡수 신호가 작아 잘 보이지 않지만, 플라즈몬 나노안테나가 입사광을 hot spot에 집중시키면 같은 분자 진동 신호가 크게 강화됩니다. 그래서 빨간 곡선은 배경 공명과 강화된 흡수 특징을 함께 보여줍니다.  
근거: Figure 2(b), 본문 2.2. 논문은 IR 분자의 흡수 단면적이 작아 민감도가 낮고, 플라즈몬 나노안테나가 전자기장을 집중시켜 SEIRA를 가능하게 한다고 설명합니다 [33-35,7]. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. (c) SERS에서 x축이 파장 `λ`가 아니라 Raman Shift `cm⁻¹`인 이유는 무엇인가요?
A. SERS는 공명 파장 이동을 보는 RI 센서가 아니라, 레이저가 분자와 비탄성 산란한 뒤 에너지가 얼마나 바뀌었는지를 봅니다. 그래서 x축은 검출된 빛의 절대 파장이 아니라 입사 레이저 대비 주파수 차이, 즉 Raman shift입니다.  
근거: Figure 2(c), 본문 2.3. Raman은 분자 진동·회전 모드를 비탄성 산란의 frequency shift와 intensity로 읽는다고 설명됩니다 [36-38]. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. (c)의 가장 큰 뾰족한 피크는 무엇을 의미하나요?
A. 특정 Raman shift에서 분자의 진동 모드가 강하게 산란된다는 뜻입니다. 그림 속 금속 구/기판 근처의 분자가 플라즈몬 hot spot에 놓이면 산란 세기가 크게 증폭되어 날카로운 피크가 잘 보입니다. 단, 이 그림만으로는 그 피크가 어떤 결합 진동인지, 어떤 분자인지 확정할 수 없습니다.  
근거: Figure 2(c), 본문 2.3. SERS는 금·은 나노구조 hot spot의 전자기장 강화와 화학적 강화로 Raman 신호를 크게 증폭한다고 설명됩니다 [39-41]. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. (c)의 위쪽 모식도에서 초록색 파와 주황색 파는 각각 무엇인가요?
A. 초록색은 incident laser, 즉 입사 레이저이고, 주황색은 Raman scattering, 즉 분자에서 산란되어 나오는 라만광입니다. 가운데 질소가 표시된 고리형 분자는 분석 대상 분자 예시이고, 아래의 metal sphere는 플라즈몬 강화 표면을 나타냅니다.  
근거: Figure 2(c), 본문 2.3. 논문은 단색광 조사 후 분자가 shifted frequency의 산란광을 내며, 금속 나노구조가 이를 강화한다고 설명합니다 [36-41]. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. SEIRA와 SERS는 둘 다 분자 fingerprint를 본다는데, 그림상 차이는 무엇인가요?
A. SEIRA 패널 (b)는 적외선 흡수 스펙트럼에서 amide band 같은 흡수 dip을 강조하고, SERS 패널 (c)는 레이저 산란 후 Raman shift 축에서 여러 날카로운 피크를 보여줍니다. 즉 SEIRA는 “흡수”, SERS는 “비탄성 산란” 기반입니다.  
근거: Figure 2(b,c), 본문 2.2-2.3. 논문은 IR은 molecular vibrational fingerprint의 흡수, Raman은 shifted scattered light의 세기를 측정한다고 구분합니다 [30-41]. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. (d)의 LCP와 RCP는 무엇이고, 왜 키랄 센싱에 필요하나요?
A. LCP는 left circularly polarized light, RCP는 right circularly polarized light입니다. 키랄 분자는 왼손/오른손 원편광과 다르게 상호작용하므로, 두 편광에 대한 흡수 또는 산란 차이를 이용해 chirality를 읽습니다. 그림의 y축 `CD`는 circular dichroism 신호를 뜻합니다.  
근거: Figure 2(d), 본문 2.4. 전통적 ORD/CD spectroscopy가 분자 chirality를 탐지하는 기술로 소개되고, 나노포토닉스가 약한 CD 신호를 증폭한다고 설명됩니다 [42-44]. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. (d)의 파란 곡선과 빨간 곡선이 위아래로 반대인 이유는 무엇인가요?
A. 파란 곡선은 right-handed molecules, 빨간 곡선은 left-handed molecules로 표시되어 있습니다. 서로 거울상인 enantiomer는 원편광에 대한 응답 부호가 반대로 나타날 수 있어 CD 스펙트럼도 양/음 방향으로 대칭적인 형태를 보입니다.  
근거: Figure 2(d), 본문 2.4. 논문은 chiral compound가 두 enantiomer로 존재하며, 이를 구분하는 능력이 중요하다고 설명합니다 [42-44]. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. (d)의 검은 점선 “Chiral sample alone”은 왜 거의 평평한가요?
A. 분자만 있을 때의 키랄 광학 신호가 약하다는 점을 보여줍니다. 금속 나노입자 또는 키랄/플라즈몬 구조가 주변 광장을 강화하면 파란색·빨간색처럼 CD 신호가 더 크게 나타납니다.  
근거: Figure 2(d), 본문 2.4. 많은 키랄 분자의 helical pitch가 가시광 파장보다 작아 기존 CD/ORD가 작은 시료 부피에서 약하다고 설명합니다. 나노포토닉 구조는 optical chirality와 CD 응답을 증폭할 수 있습니다. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. (d)의 분자 그림에 Br, H, D 같은 원자가 보이는데, 이 그림은 특정 분자를 말하나요?
A. 키랄 중심을 설명하기 위한 예시 모식도로 보는 것이 안전합니다. Br, H, D처럼 서로 다른 치환기가 붙은 구조는 왼손성과 오른손성을 직관적으로 보여주지만, 이 Figure 2 caption만으로 특정 실험 분자나 농도를 확정할 수는 없습니다.  
근거: Figure 2(d), 본문 2.4. 본문은 특정 분자 실험값보다 chiral molecule과 enantiomer의 일반 원리를 설명합니다 [42-44]. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. (e) SEF 그래프에서 검은 선이 빨간 선보다 높은 이유는 무엇인가요?
A. 검은 선은 `with Plasmons`, 빨간 선은 `without Plasmons`입니다. 금속 나노입자의 국소 표면 플라즈몬이 근처 형광체의 여기율과 방출 확률을 높이면 fluorescence intensity가 커집니다. 그래서 같은 파장 범위에서 검은 피크가 더 큽니다.  
근거: Figure 2(e), 본문 2.5. 논문은 금속 나노구조가 국소 전자기장을 강화해 excitation rate를 높이고, optical states 밀도 증가로 emission probability와 quantum yield를 높일 수 있다고 설명합니다 [45-47]. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. (e)의 초록색 물결 화살표와 파란색 물결 화살표는 각각 무엇인가요?
A. 파란색 물결은 incident laser, 즉 형광체를 여기시키는 빛이고, 초록색 물결은 fluorescence, 즉 여기된 분자가 방출하는 형광입니다. 노란 빛을 띠는 nanoparticle 주변 영역은 플라즈몬에 의해 강화된 국소장으로 해석할 수 있습니다.  
근거: Figure 2(e), 본문 2.5. SEF는 금속 나노입자의 localized surface plasmon resonance가 주변 전자기장을 강화해 형광 신호를 키우는 방식으로 설명됩니다. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. SEF에서는 금속 나노입자에 가까우면 무조건 형광이 세지나요?
A. 이 그림은 “플라즈몬이 있으면 형광이 강화될 수 있다”는 개념도이지, 거리 의존성까지 보여주지는 않습니다. 실제로는 형광체와 금속이 너무 가까우면 비복사 에너지 전달이나 quenching이 생길 수 있으므로 최적 거리가 중요합니다. 이 Figure 2만으로 그 거리는 알 수 없습니다.  
근거: Figure 2(e), 본문 2.5는 close proximity에서 SEF를 활용한다고 설명하지만, 이 개요 그림과 캡션은 거리 최적화나 quenching 조건을 정량화하지 않습니다 [45-47]. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. 다섯 패널의 y축이 모두 같은 물리량인가요?
A. 아닙니다. (a), (b), (c)는 모두 `Intensity`라고 되어 있지만 의미가 다릅니다. (a)는 공명 산란/투과/반사 같은 광 응답 세기, (b)는 적외선 흡수 강화 응답, (c)는 Raman 산란 세기입니다. (d)는 `CD`, (e)는 `FL Intensity`로 별도 물리량입니다.  
근거: Figure 2 전체 캡션과 본문 2.1-2.5. 논문은 RI, SEIRA, SERS, chiral, SEF를 서로 다른 sensing mechanism으로 나누어 설명합니다. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. 이 그림에서 공통으로 반복되는 핵심 용어는 무엇인가요?
A. 핵심은 `plasmon`, `hot spot`, `fingerprint`, `resonance`, `enhancement`입니다. RI는 공명 이동, SEIRA와 SERS는 분자 진동 fingerprint 강화, chiral sensing은 CD 강화, SEF는 형광 강화로 연결됩니다. 초보자가 헷갈리기 쉬운 점은 “모든 패널이 같은 스펙트럼을 보는 것”이 아니라, 같은 플라즈몬 기반 증폭을 서로 다른 신호 방식에 적용한다는 점입니다.  
근거: Figure 2 caption, 본문 2.1-2.5. 논문은 conventional optical sensing techniques로 RI, SEIRA, SERS, chiral, SEF를 차례로 소개하고, 각 원리를 Figure 2에 연결합니다. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))

#### Q. 이 Figure 2 하나만 보고 확정할 수 없는 정보는 무엇인가요?
A. 정확한 금속 종류, 나노입자 크기, 안테나 형상, 실제 파장값, Raman peak assignment, SEIRA enhancement factor, SEF 거리 조건, 시료 농도, 검출한 실제 바이오마커는 알 수 없습니다. 이 그림은 정량 데이터가 아니라 다섯 감지 기전의 개념도입니다.  
근거: Figure 2 caption은 “Mechanisms of photonic sensing”으로만 제시되며, 본문 2.1-2.5도 원리와 대표 성능 개념을 설명합니다. 구체 응용과 실험 사례는 이후 Figure 3-5 등에서 별도로 다룹니다. ([mdpi.com](https://www.mdpi.com/3042-5999/1/1/5))