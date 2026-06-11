### 예상 질문과 답변

#### Q. Figure 3는 왜 네 가지 전혀 다른 바이오마커를 한 그림에 묶었나요?
A. 네 패널은 모두 표적이 센서 표면에 결합하면 주변 **굴절률(RI)** 이 변하고, 그 결과 플라즈몬 공명 파장이나 세기가 이동한다는 같은 원리를 공유합니다. (a)는 엑소좀-결합 Aβ, (b)는 SARS-CoV-2 관련 면역결합, (c)는 단일세포 분비물, (d)는 도파민을 예로 든 응용 범위입니다. 근거: Figure 3 caption, DOI `10.3390/aisens1010005`; 본문 RI 센싱 설명은 Fig. 2(a) 원리와 연결됩니다.

#### Q. (a)에서 “Before amplification”과 “After amplification”은 무엇이 달라진 건가요?
A. 왼쪽 아래의 금색 나노구조 표면을 보면, 증폭 전에는 엑소좀 같은 작은 입자만 표면에 붙어 있고, 증폭 후에는 붉고 어두운 **optical deposit**이 더 크게 형성되어 있습니다. 이는 표면에 결합한 표적이 더 큰 광학적 굴절률 변화를 만들도록 신호를 키운다는 의미입니다. 근거: Fig. 3(a) caption의 순환 엑소좀-결합 amyloid β 분석 문맥, ref. [50] 또는 제공 문맥상 APEX/엑소좀-Aβ 응용 [62], DOI `10.3390/aisens1010005`.

#### Q. (a)의 오른쪽 위 그래프에서 파란 피크와 빨간 피크의 이동은 무엇을 뜻하나요?
A. x축은 파장 `λ`, y축은 투과도 또는 광신호 세기입니다. “Sensor”, “Exosome before”, “Optical deposit after”로 표시된 피크가 오른쪽으로 이동하고 있으며, 점선 화살표의 `Spectral shift Δλ`가 핵심 판독값입니다. 엑소좀 결합과 광학 침착물이 표면 근처 굴절률을 바꾸어 공명 파장을 이동시킨다는 뜻입니다. 근거: Fig. 3(a) 이미지의 spectral shift 표시, Figure 3 caption, Fig. 2(a) RI sensing mechanism, DOI `10.3390/aisens1010005`.

#### Q. (a)의 아래 오른쪽 그래프에서 빨간색과 파란색 곡선은 무엇을 비교하나요?
A. x축은 `Exosome counts`, y축은 `Normalized response`입니다. 범례상 파란색은 `Before`, 빨간색은 `After`입니다. 빨간 곡선이 같은 엑소좀 수에서 더 높은 반응을 보이고 더 왼쪽에서 상승하므로, 증폭 후 더 낮은 입자 수에서도 검출 가능하다는 메시지를 줍니다. 오른쪽에 `ELISA`, `Western` 기준선이 함께 그려져 있어 기존 분석법과 민감도 범위를 비교하려는 의도가 보입니다. 근거: Fig. 3(a) 그래프와 캡션, 엑소좀-결합 Aβ 분석 문맥 [50]/[62], DOI `10.3390/aisens1010005`.

#### Q. (a)에서 “Free Aβ”와 “Exosome-bound Aβ”를 왜 구분하나요?
A. 그림은 혈중에 자유롭게 떠다니는 Aβ와 엑소좀 표면 또는 내부와 연관된 Aβ를 분리해서 보여줍니다. 센서가 단순히 총 Aβ만 보는 것이 아니라, 엑소좀에 결합된 Aβ 아형이 뇌의 amyloid plaque 침착을 반영할 수 있다는 메시지입니다. 다만 이 이미지 하나만으로 어떤 Aβ 아형, 임상군 수, 통계적 정확도까지는 확정할 수 없습니다. 근거: Figure 3 caption의 “circulating exosome-bound amyloid β reflects brain plaque deposition”, ref. [50]/제공 문맥 [62], DOI `10.3390/aisens1010005`.

#### Q. (b)에서 위쪽의 Host cell, ACE2, SARS-CoV-2, S protein, RBD는 어떤 흐름을 말하나요?
A. 위쪽 모식도는 바이러스 표면의 S protein 중 `RBD`가 숙주세포의 `ACE2`와 결합하는 생물학적 인식 단계를 보여줍니다. 센서 관점에서는 RBD, 항체, 표면 기능화층이 결합하면서 표면 굴절률이 바뀌고, 그 변화가 광학 반사 스펙트럼의 이동으로 읽힙니다. 근거: Fig. 3(b) 이미지 레이블, Figure 3 caption의 label-free immunoassay boosting 문맥 [62]/SARS-CoV-2 RBD metasurface 문맥상 ref. [68], DOI `10.3390/aisens1010005`.

#### Q. (b)의 WT, Alpha, Beta, Gamma, Delta, Omicron 표시는 무엇을 비교하려는 건가요?
A. 서로 다른 SARS-CoV-2 변이의 RBD 구조 또는 결합 특성을 비교하려는 시각 요소입니다. 오른쪽 위에 변이별 RBD가 따로 그려져 있고, 아래 그래프에는 여러 색의 반사도 곡선이 함께 표시되어 변이에 따라 결합 신호나 공명 위치가 달라질 수 있음을 암시합니다. 하지만 이 이미지 단독으로 각 변이의 친화도 순위나 중화항체 회피 정도를 정량화할 수는 없습니다. 근거: Fig. 3(b) 변이 레이블, Figure 3 caption의 면역분석 부스팅 문맥, DOI `10.3390/aisens1010005`.

#### Q. (b)의 그래프에서 x축 680-740 nm와 y축 Reflectance는 무엇을 읽는 건가요?
A. x축은 파장, y축은 반사도입니다. `Bare PM`, `MUA`, `mAb`, `RBD`처럼 표면에 순차적으로 층이 쌓이거나 분자가 결합할 때 반사 스펙트럼의 dip 또는 특징점이 이동합니다. 세로 점선과 화살표는 결합 전후의 파장 이동을 강조합니다. 이는 라벨 없이도 표면 결합을 광학적으로 추적할 수 있다는 뜻입니다. 근거: Fig. 3(b) 반사도 그래프, RI 기반 센싱 원리 Fig. 2(a), Figure 3 caption, DOI `10.3390/aisens1010005`.

#### Q. (b)의 금색 구멍 배열과 아래 SEM 이미지는 어떤 센서 구조를 뜻하나요?
A. 금색 기판의 주기적 구멍 배열은 플라즈몬 또는 메타표면 기반 센서로 보입니다. 아래 흑백 SEM 이미지는 실제 나노/마이크로 구조의 구멍 배열을 보여주는 증거 이미지입니다. 이 배열은 빛과 표면 플라즈몬 모드를 강하게 결합시켜 표면 결합에 민감한 반사 스펙트럼을 만들기 위한 구조입니다. 근거: Fig. 3(b) 장치 그림과 SEM 삽입 이미지, label-free immunoassay boosting 문맥 [62]/[68], DOI `10.3390/aisens1010005`.

#### Q. (c)는 단일세포 분비물을 어떻게 공간적으로 구분하나요?
A. 왼쪽 모식도에서 세포가 각각 `sensing well` 또는 microwell 안에 놓이고, 아래쪽에는 `CMOS camera`가 광학 신호를 기록합니다. 각 well의 위치가 곧 특정 세포의 위치이므로, 분비물이 표면에 결합해 생긴 신호 변화를 위치별로 추적할 수 있습니다. 근거: Fig. 3(c) 레이블 `sensing well`, `CMOS camera`, Figure 3 caption의 high-throughput spatiotemporal single-cell secretions [83], DOI `10.3390/aisens1010005`.

#### Q. (c)의 가운데 그래프 세 개에서 피크 위치가 달라지는 것은 무엇을 의미하나요?
A. x축은 wavelength, y축은 transmittance입니다. 표면에 receptor와 analyte가 결합하면서 공명 피크가 `λ1`, `λ2`, `λ3`처럼 이동합니다. 세 그림은 같은 센서 지점에서 결합 상태가 달라질 때 스펙트럼 피크가 달라진다는 것을 단계적으로 보여줍니다. 근거: Fig. 3(c) 스펙트럼 피크와 `λ1`, `λ2`, `λ3` 표시, RI sensing mechanism Fig. 2(a), ref. [83], DOI `10.3390/aisens1010005`.

#### Q. (c)의 오른쪽 시간 그래프에서 I1, I2, I3는 무엇인가요?
A. x축은 time, y축은 peak intensity입니다. `t1`, `t2`, `t3` 시점에 따라 피크 세기 `I1`, `I2`, `I3`가 변하며, 오른쪽 작은 삽화는 표면에 결합한 분비물 양이 달라지는 상황을 대응시킵니다. 즉 단일세포가 시간에 따라 얼마나 분비하는지를 실시간으로 추적하는 그림입니다. 근거: Fig. 3(c) time-intensity 그래프, Figure 3 caption의 spatiotemporal monitoring [83], DOI `10.3390/aisens1010005`.

#### Q. (c)에서 “label-free”라는 말이 왜 중요할까요?
A. 형광 표지나 효소 표지를 붙이지 않고도, 분비물이 센서 표면에 결합하면서 생긴 굴절률 변화만으로 신호를 읽는다는 점이 중요합니다. 단일세포 분비를 오래 관찰할 때 표지 과정이 세포 상태를 바꿀 수 있으므로, 라벨-프리 광학 판독은 장점이 있습니다. 다만 이 그림만으로는 어떤 분비 단백질을 어떤 receptor로 잡았는지까지는 확인하기 어렵습니다. 근거: Fig. 3(c), 본문 단일세포 분비 모니터링 설명 [83], RI 기반 센싱 설명, DOI `10.3390/aisens1010005`.

#### Q. (d)에서 optical microfiber가 왜 등장하나요?
A. (d)의 아래쪽에는 빛이 `Light in`으로 들어가고, 굽은 optical microfiber의 sensing region을 지나 `Light out`으로 나가는 구조가 보입니다. microfiber 표면의 evanescent field가 주변 나노입자와 결합하고, 도파민이 aptamer-나노입자 계면에 결합하면 광학 주파수 또는 파장 이동이 발생합니다. 근거: Fig. 3(d) 레이블 `Microfiber: sensing region`, Figure 3 caption의 dopamine detection [89], DOI `10.3390/aisens1010005`.

#### Q. (d)의 ①, ②, ③ 번호는 어떤 감지 순서를 나타내나요?
A. ①은 도파민 분자가 센서 쪽으로 로딩되는 단계, ②는 도파민이 나노입자 또는 aptamer 기능화 표면에 결합하는 단계, ③은 결합 때문에 주파수 또는 파장 이동이 생기는 단계입니다. 그림 오른쪽에도 `Δλ`와 `Wavelength shift`가 표시되어 있어 최종 판독값이 광학 공명 이동임을 보여줍니다. 근거: Figure 3 caption의 “(1) Loading dopamine molecules. (2) Binding... (3) Frequency shift...”, ref. [89], DOI `10.3390/aisens1010005`.

#### Q. (d)의 Au NPs, MoS2, Cu2-xS@GO, Aptamer는 각각 어떤 역할인가요?
A. `Au NPs`는 플라즈몬 결합과 국소장 증강에 기여하는 금 나노입자, `MoS2`와 `Cu2-xS@GO`는 표면 결합 및 광학 증폭 계면을 구성하는 나노재료로 해석할 수 있습니다. `Aptamer`는 도파민을 선택적으로 잡는 분자 인식 요소입니다. 초보자가 헷갈릴 점은 “금 나노입자가 도파민을 직접 진단한다”가 아니라, 인식 분자와 나노광학 구조가 함께 주파수/파장 이동을 만든다는 것입니다. 근거: Fig. 3(d) 범례와 dopamine detection [89], DOI `10.3390/aisens1010005`.

#### Q. (d)에서 말하는 단분자 검출은 이미지에서 어떻게 암시되나요?
A. microfiber sensing region의 작은 발광점과 확대 삽입 이미지, 그리고 단일 도파민 결합이 나노입자 결합 상태를 바꾸어 `Δλ`를 만든다는 단계도가 단분자 수준 검출을 암시합니다. 하지만 이미지 하나만으로 실제 검출한계, false positive, 생체시료 종류, 반복성 수치는 확정할 수 없습니다. 근거: Figure 3 caption의 “single-molecule and noninvasive dopamine detection” [89], 본문 dopamine detection 문맥, DOI `10.3390/aisens1010005`.

#### Q. 이 Figure에서 가장 중요한 용어는 무엇인가요?
A. 핵심 용어는 `RI`, `LSPR/plasmon resonance`, `spectral shift Δλ`, `reflectance/transmittance`, `label-free`, `exosome`, `amyloid β`, `RBD`, `ACE2`, `microwell array`, `aptamer`, `optical microfiber`입니다. 특히 RI 센싱은 분자의 화학적 지문을 직접 읽는 방식이 아니라, 표면 결합으로 인한 굴절률 변화와 공명 이동을 읽는 방식이라는 점을 구분해야 합니다. 근거: Fig. 3 전체 레이블, Fig. 2(a) RI sensing mechanism, Figure 3 caption, DOI `10.3390/aisens1010005`.

#### Q. 이 이미지 하나만 보고 확정하면 안 되는 것은 무엇인가요?
A. 각 패널의 정확한 검출한계, 샘플 수, 통계 유의성, 임상 민감도/특이도, 변이별 결합상수, 도파민 선택성, 장기 안정성은 이 이미지 단독으로 확정할 수 없습니다. 그림은 “어떤 센서 원리와 응용을 보여주는가”에는 강하지만, 성능 수치는 원 논문 본문과 각 reference를 확인해야 합니다. 근거: Figure 3는 overview figure이며, 세부 성능은 패널별 원 연구 ref. [50]/[62]/[83]/[89] 및 DOI `10.3390/aisens1010005` 본문 문맥에 의존합니다.