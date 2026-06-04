# Worksheets for the 6-Week Optical Sensor Seminar

These worksheets implement the weekly outputs for `optic_sensor_pedagogy_6week.md`. Use them with `optic_review1.pdf` and `terminology_optical_sensor.md`.

## 1. Standard Figure-Reading Template

Use this template for every assigned figure or figure panel.

```text
Figure/panel:
Claim:
Physical input:
Optical structure:
Target analyte or stimulus:
Changed optical observable:
Performance metric:
Why the metric improves:
Main limitation:
PIC/in-sensor-computing relevance:
One question for discussion:
```

Grading standard:

- Full credit requires a mechanism-level answer.
- Do not write only the application name.
- Every metric must include what physical quantity it measures.

## 2. Week 1 Worksheet: Paper Map

### Terminology Quiz

Define each term in one sentence and give one reason it matters in this review.

1. PIC
2. AI
3. edge intelligence
4. in-sensor computing
5. optical microsystem
6. smart photonic sensor

### Concept Questions

1. Why does the paper begin with conventional optical sensing methods before discussing PICs?
2. What engineering limitations of discrete optical systems motivate PIC sensors?
3. Why is AI useful for optical spectra?
4. What is the difference between an AI-enhanced sensor and an in-sensor computing device?
5. In the review's logic, what is the relationship between sensing hardware and intelligent decision-making?

### Required Output

Create a one-page map with three layers:

- Layer 1: physical sensing mechanisms.
- Layer 2: photonic/PIC device platforms.
- Layer 3: AI or edge-computing functions.

Acceptance criteria:

- Includes RI, SEIRA, SERS, chiral sensing, SEF, PIC, and in-sensor computing.
- Shows at least three arrows explaining how lower-layer physics supports upper-layer intelligence.

## 3. Week 2 Worksheet: Mechanisms and Metrics

### Terminology Quiz

Define:

1. LSPR
2. SPP
3. hot spot
4. FWHM
5. FoM
6. enhancement factor
7. fluorophore
8. chirality

### Problem 2.1: RI Sensitivity

A plasmonic RI sensor resonance shifts from 650 nm to 653 nm when the refractive index changes from 1.330 to 1.335.

Tasks:

1. Compute `S_RI`.
2. If the resonance FWHM is 20 nm, compute `FoM`.
3. Explain whether this sensor is necessarily selective to one biomolecule.

Expected reasoning:

- `Delta lambda = 3 nm`.
- `Delta n = 0.005 RIU`.
- `S_RI = 600 nm/RIU`.
- `FoM = 30 RIU^-1`.
- Selectivity requires surface chemistry such as antibody, aptamer, or molecular imprinting.

### Problem 2.2: Linewidth Tradeoff

Sensor A has `S_RI = 800 nm/RIU` and `FWHM = 80 nm`. Sensor B has `S_RI = 400 nm/RIU` and `FWHM = 10 nm`.

Tasks:

1. Compute both FoM values.
2. Which sensor gives more precise resonance-shift detection?
3. Why can lower raw sensitivity still be better?

Expected reasoning:

- Sensor A: `FoM = 10 RIU^-1`.
- Sensor B: `FoM = 40 RIU^-1`.
- Narrow linewidth improves resolvability.

### Problem 2.3: SEIRA Enhancement Factor

A pure reference sample gives `I_ref = 1.0` from `N_ref = 10^9` molecules. A SEIRA hotspot measurement gives `I_SEIRA = 0.2` from `N_SEIRA = 10^5` hotspot-coupled molecules.

Tasks:

1. Compute `EF_SEIRA`.
2. Explain why molecule count must be included.
3. Name one material or structure strategy for increasing hotspot molecule participation.

Expected reasoning:

- `EF = (0.2 / 1.0) * (10^9 / 10^5) = 2000`.
- Without molecule count, a small absolute signal could hide strong per-molecule enhancement.
- Possible strategies: MOF enrichment, SAM control, nanopedestal access, metasurface hotspot design.

### Problem 2.4: SERS Field Dependence

Assume the local field amplitude is enhanced by 10 times at excitation and 8 times at Raman detection.

Tasks:

1. Estimate the SERS intensity enhancement from the field term.
2. Explain why both frequencies matter.
3. Explain why substrate reproducibility is a major issue.

Expected reasoning:

- Enhancement factor from the given term: `|10 * 8|^2 = 6400`.
- Excitation generates Raman scattering; detection-frequency enhancement affects emitted/scattered photons.
- Hotspots vary with nanoparticle geometry, gaps, aggregation, and surface chemistry.

### Required Output

Complete the five-method comparison table from the course guide.

## 4. Week 3 Worksheet: Application Cards

### Terminology Quiz

Define:

1. LOD
2. PSA
3. aptamer
4. bioreceptor
5. nPLEX
6. APEX
7. MOF
8. VOC
9. enantiomer

### Application Card Template

```text
Method:
Figure/panel:
Application:
Analyte:
Surface or photonic structure:
Signal transduction:
Main metric:
Why this method fits the analyte:
One limitation:
Could this become a PIC sensor? Why or why not?
```

### Discussion Questions

1. In RI biosensing, what provides molecular specificity if the optical signal only sees refractive-index change?
2. Why is SEIRA especially natural for chemical fingerprinting?
3. Why is SERS attractive for multiplex profiling?
4. Why do chiral sensors need engineered optical fields?
5. Why can SEF be extremely sensitive but still hard to engineer?

### Required Output

Submit five application cards:

- one RI card,
- one SEIRA card,
- one SERS card,
- one chiral sensing card,
- one SEF card.

Evaluation criteria:

- Each card names the optical observable.
- Each card distinguishes sensitivity from selectivity.
- Each card includes one realistic implementation bottleneck.

## 5. Week 4 Worksheet: PIC Conversion

### Terminology Quiz

Define:

1. waveguide
2. evanescent field
3. SOI
4. MRR
5. MZI
6. PPM
7. MIM waveguide
8. MSM photodetector
9. Pockels effect
10. Burstein-Moss effect

### Problem 4.1: Component Function

For each component, write its role in a PIC sensor and one design tradeoff.

| Component | Role | Tradeoff |
| --- | --- | --- |
| waveguide |  |  |
| resonator |  |  |
| modulator |  |  |
| detector |  |  |
| switch |  |  |
| light source |  |  |

Expected examples:

- Waveguide: routes optical mode and exposes evanescent field; tradeoff between confinement and propagation loss.
- Resonator: enhances interaction and spectral selectivity; tradeoff between high Q and bandwidth/tolerance.
- Modulator: changes phase or intensity; tradeoff between speed, voltage, footprint, and thermal load.
- Detector: converts optical signal to electrical readout; tradeoff between bandwidth, responsivity, noise, and coupling.

### Problem 4.2: Bulk-to-PIC Redesign

Choose RI, SEIRA, SERS, chiral sensing, or SEF.

Redesign it as a chip-level sensor using this block order:

`source -> coupling -> waveguide/resonator/metasurface -> analyte interface -> detector -> processor`.

Tasks:

1. Draw the block diagram.
2. Mark where light interacts with the analyte.
3. Mark where loss enters.
4. Mark where calibration is required.
5. Mark which block is hardest to integrate.

### Discussion Questions

1. Why does plasmonic confinement help sensing?
2. Why does the same plasmonic confinement create loss?
3. Why is silicon photonics not a universal platform for all optical sensors?
4. What does packaging mean in a sensor, beyond simply covering the chip?

### Required Output

Submit one bulk-to-PIC conversion diagram and a 300-word design rationale.

## 6. Week 5 Worksheet: In-Sensor Computing

### Terminology Quiz

Define:

1. in-sensor computing
2. NSEC
3. PNN
4. CNN
5. MLP
6. photonic nose
7. TENG
8. Q-factor
9. quantization
10. matrix-vector multiplication

### Signal-Flow Template

Use this for Figure 9 or Figure 10.

```text
Case:
Physical stimulus:
Sensor frontend:
Optical signal:
Photonic operation:
Electrical conversion:
ML model or computation:
Output:
Optical metric:
ML/system metric:
Main noise/loss source:
Why in-sensor or near-sensor computing matters:
```

### Problem 5.1: Architecture Classification

Classify each system as conventional, near-sensor edge computing, or photonic in-sensor computing. Justify in one sentence.

1. A Raman spectrometer sends raw spectra to a cloud GPU for classification.
2. A chip uses MRRs to extract features and MZIs to apply weights before electronic activation.
3. A phone receives processed concentration estimates from a wearable optical sensor.
4. A waveguide-integrated photodetector changes responsivity with bias voltage to implement optical weighting.

Expected reasoning:

- 1: conventional or cloud AI sensing.
- 2: photonic near-sensor/in-sensor computing hybrid.
- 3: edge or near-sensor depending on where processing occurs; answer must specify ambiguity.
- 4: photonic in-sensor computing element.

### Problem 5.2: Metrics Beyond Accuracy

A gas-mixture classifier reports 95 percent accuracy.

Tasks:

1. Name three additional metrics needed to judge whether this is a good optical sensor.
2. Explain why high accuracy can be misleading if the optical frontend is unstable.
3. Explain why training data distribution matters.

Expected answers:

- Possible metrics: LOD, response time, concentration RMSE, drift, calibration stability, power per inference, latency, confusion matrix, robustness to humidity/temperature.
- Optical instability changes the input distribution, causing model failure.
- Limited or biased spectra can cause overfitting and poor deployment performance.

### Required Output

Submit one full signal-flow diagram for either the MIR photonic nose, the graphene photodetector weighting unit, or the AlN/Si NSEC platform.

## 7. Week 6 Worksheet: Final Proposal

### Terminology Quiz

The student selects 12 terms from the glossary that are directly relevant to the final proposal and defines them orally.

### Proposal Template

```text
Title:
Target analyte or stimulus:
Why this problem matters:
Chosen sensing mechanism:
Optical/PIC platform:
Expected optical observable:
Primary optical metric:
AI or in-sensor-computing role:
Dataset or calibration need:
Main bottleneck:
Validation experiment:
Expected failure mode:
What would count as success:
```

### Proposal Constraints

The proposal must include:

- one sensing mechanism from the review,
- one PIC or nanophotonic platform,
- one optical performance metric,
- one system or ML metric,
- one realistic bottleneck,
- one validation experiment.

### Review Questions

1. Does the chosen analyte match the chosen spectral region?
2. Does the sensing mechanism produce a measurable optical observable?
3. Is the claimed role of AI necessary, or merely decorative?
4. What data are required to train or calibrate the system?
5. What part of the proposal would fail first in field deployment?

### Final Presentation Rubric

| Criterion | Excellent | Adequate | Insufficient |
| --- | --- | --- | --- |
| Mechanism | Correctly explains light-matter interaction and optical observable | Names the mechanism but explanation is partial | Lists the method without mechanism |
| Metric | Uses optical and system/ML metrics correctly | Uses one metric correctly | Metrics are missing or confused |
| PIC/platform reasoning | Platform choice follows from spectral, integration, or size constraints | Platform choice is plausible but under-justified | Platform is arbitrary |
| AI/in-sensor role | Computation solves a concrete bottleneck | AI role is useful but generic | AI is decorative |
| Critique | Identifies realistic failure modes | Identifies broad limitations | No serious limitation |
| Communication | Clear 10-minute technical argument | Understandable but uneven | Unstructured |

## 8. Final Mastery Oral Exam

Use these questions after Week 6 if the goal is "complete understanding" of the review.

1. Explain the paper's full technology trajectory in five sentences.
2. Derive `S_RI` and explain why `FoM` is more informative than sensitivity alone.
3. Compare SEIRA and SERS in terms of optical process, signal type, and enhancement mechanism.
4. Explain why chiral sensing is difficult for nanoscale sample volumes.
5. Explain the enhancement-versus-quenching tradeoff in SEF.
6. Choose one application from Figures 3-7 and explain the complete transduction path.
7. Explain why PIC sensors reduce alignment complexity but introduce packaging problems.
8. Explain why plasmonic components are attractive for miniaturization but limited by loss.
9. Explain how MRRs and MZIs can support photonic computing.
10. Explain why in-sensor computing reduces data-transfer bottlenecks.
11. Explain why analog photonic AI systems need calibration and quantization analysis.
12. Name three barriers to field deployment and propose one mitigation for each.

Pass condition:

- The student can answer at least 10 of 12 questions with mechanism-level reasoning.
- The student must not confuse sensitivity, selectivity, LOD, and accuracy.

