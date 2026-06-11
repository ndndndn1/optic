# 6-Week Graduate Seminar: Optical Sensors and In-Sensor Photonic Intelligence

Source paper: Zhou, H.; Li, D.; Lee, C. "Technology Landscape Review of In-Sensor Photonic Intelligence: From Optical Sensors to Smart Devices", `optic_review1.pdf`.

Supporting glossary: `terminology_optical_sensor.md`.

## 1. Course Aim

This seminar is designed for a graduate student who wants to understand `optic_review1.pdf` at the level required to explain, critique, and extend the review. The central thread is:

`light-matter interaction -> optical transduction -> performance metric -> integrated photonic platform -> AI/in-sensor computing`.

By the end of the seminar, the student should be able to:

- Explain RI, SEIRA, SERS, chiral sensing, and SEF from the underlying optical mechanism, not only by their names.
- Derive or interpret the main performance metrics: `S_RI`, `FoM`, `FWHM`, enhancement factor, limit of detection, Q-factor, and inference accuracy.
- Read Figures 1-11 as scientific arguments: what claim each figure supports, what evidence it gives, and what limitation remains.
- Describe why PICs change the engineering boundary conditions of optical sensors: size, power, alignment, multiplexing, packaging, and real-time operation.
- Translate the paper's challenges into a concrete research proposal.

## 2. Operating Format

Duration: 6 weeks.

Meeting length: 2 hours per week.

Language: Korean discussion, English technical terms retained.

Weekly structure:

- 10 min: terminology check from `terminology_optical_sensor.md`.
- 25 min: instructor mini-lecture on the week's physical principles.
- 35 min: equation and metric workshop.
- 35 min: figure-based paper reading.
- 15 min: synthesis, critique, and next assignment.

Required weekly output:

- One-page concept sheet.
- One solved metric or mechanism problem.
- One figure-reading note using the template in `optic_sensor_worksheets.md`.

## 3. Week 1: Map the Review Paper

Reading:

- Abstract
- Section 1
- Figure 1
- Glossary terms: `PIC`, `AI`, `RI`, `SEIRA`, `SERS`, `SEF`, `edge-intelligence`, `in-sensor-computing`

Core teaching goal:

The student must first understand the paper as a staged technological transition: conventional optical sensors are not abandoned; they become the physical basis that PIC and AI systems integrate.

Key concepts:

- Discrete optical microsystem: laser, lens, sample, detector, processor are separate.
- PIC sensor: waveguide, modulator, detector, resonator, and sometimes source/readout are chip-level components.
- AI-enhanced sensor: the sensor signal is interpreted by feature extraction, classification, regression, or control.
- In-sensor computing: part of the computation is moved into the sensor hardware or immediately adjacent photonic frontend.

Mini-lecture outline:

1. Start from the old architecture: high sensitivity but large, aligned, power-hungry, nonportable.
2. Show what integration changes: optical path becomes a fabricated object rather than a manually aligned setup.
3. Explain why AI enters the review: optical spectra and sensor arrays produce high-dimensional signals.
4. Define the three-layer map:
   - Physical layer: light-matter interaction.
   - Device layer: resonator, waveguide, metasurface, nanoantenna.
   - Intelligence layer: spectral pattern recognition, regression, edge decision.

In-session activity:

- Build a three-column map of the whole paper.
- Column 1: sensing principle.
- Column 2: representative platform.
- Column 3: computation or application.

Success criteria:

- The student can explain why Section 2 comes before Section 4.
- The student can state the review's thesis in one sentence: PIC and AI do not replace optical sensing physics; they compress, parallelize, and interpret it.

Assignment:

- Draw a one-page concept map connecting Figures 1, 2, 8, 9, 10, and 11.
- Write 5 definitions from the glossary in the student's own words.

## 4. Week 2: Basic Sensing Mechanisms and Metrics

Reading:

- Section 2.1-2.5
- Figure 2
- Glossary terms: `LSPR`, `SPP`, `FWHM`, `FoM`, `EF`, `hot-spot`, `nanoantenna`, `metasurface`, `fluorophore`, `chirality`

Core teaching goal:

The student must distinguish the five sensing modes by what optical observable changes and why the signal is enhanced.

Mechanism table:

| Method | Physical event | Measured optical change | Main strength | Main limitation |
| --- | --- | --- | --- | --- |
| RI sensing | Local refractive index changes near a plasmonic surface | Resonance wavelength, amplitude, or phase shift | Label-free, real-time binding kinetics | Limited chemical specificity without surface functionalization |
| SEIRA | Molecular vibration couples to enhanced MIR near field | Enhanced infrared absorption | Molecular fingerprinting | Weak native IR absorption, hotspot access |
| SERS | Inelastic Raman scattering is amplified by local field and chemical effects | Raman peak intensity | Trace-level molecular selectivity | Reproducibility of hotspots and substrates |
| Chiral sensing | Enantiomers interact differently with LCP/RCP or superchiral fields | CD, ORD, VCD, ROA, or TCD contrast | Enantiomer discrimination | Natural chiral signals are weak |
| SEF | Fluorophore excitation/emission rate changes near metal nanostructures | Fluorescence intensity/lifetime | Very low detection limit | Quenching and distance dependence |

Required formulas and interpretations:

- `S_RI = Delta lambda / Delta n`
  - Meaning: resonance shift per refractive-index unit.
  - Pedagogical emphasis: sensitivity is not the same as selectivity.
- `FoM = S_RI / FWHM`
  - Meaning: large shift and narrow linewidth are both needed.
  - Pedagogical emphasis: a broad resonance can hide a large shift.
- `EF_SEIRA = (I_SEIRA / I_ref) * (N_ref / N_SEIRA)`
  - Meaning: enhancement must account for both signal intensity and the number of molecules sampled.
- `I_SERS proportional to I_0 * |E_ext E_det / (E0_ext E0_det)|^2`
  - Meaning: field enhancement at both excitation and detection frequencies matters.

Mini-lecture outline:

1. Resonance shift logic for RI sensing.
2. Vibrational fingerprint logic for SEIRA and SERS.
3. Polarization and handedness logic for chiral sensing.
4. Excitation rate, radiative decay, and quenching logic for SEF.
5. Why all five methods reappear later in PIC-compatible forms.

In-session activity:

- For each panel of Figure 2, identify:
  - input light,
  - interacting structure,
  - target analyte,
  - changed observable,
  - relevant metric.

Success criteria:

- The student can explain why a "hot spot" increases signal but may also create sampling bias.
- The student can compare SEIRA and SERS without reducing both to "surface enhancement".

Assignment:

- Complete the five-method comparison table.
- Solve the Week 2 metric problems in `optic_sensor_worksheets.md`.

## 5. Week 3: Applications as Evidence, Not Examples

Reading:

- Section 3.1-3.5
- Figures 3-7
- Glossary terms: `LOD`, `PSA`, `aptamer`, `bioreceptor`, `nPLEX`, `APEX`, `MOF`, `SAM`, `VOC`, `enantiomer`

Core teaching goal:

The student must read applications as evidence for the capability and limitation of each mechanism.

Teaching stance:

Do not ask only "what was detected?" Ask:

- What molecule or physical quantity changed the optical response?
- Which nanostructure increased interaction strength?
- Which metric proved performance?
- What part of the setup prevents field deployment?
- What part of the method could be integrated into a PIC?

Figure-reading focus:

- Figure 3: RI sensing applications. Emphasize binding-induced resonance shifts, label-free assays, and biological specificity through surface chemistry.
- Figure 4: SEIRA applications. Emphasize MIR molecular fingerprints, multi-resonant antennas, MOF enrichment, and deep-learning-assisted spectral interpretation.
- Figure 5: SERS applications. Emphasize trace detection, multiplex molecular profiles, wearable formats, and high-dimensional fingerprints.
- Figure 6: Chiral sensing applications. Emphasize weak natural chiral signals and enhancement through metamaterials or superchiral near fields.
- Figure 7: SEF applications. Emphasize single-molecule or femtomolar detection and the distance-dependent balance between enhancement and quenching.

Mini-lecture outline:

1. Biological diagnostics: why selectivity requires bioreceptors, not only optics.
2. Chemical sensing: why molecular fingerprints are powerful but data-heavy.
3. Environmental and wearable sensing: why portability and stability matter.
4. Application bottlenecks: sample delivery, surface fouling, calibration, substrate reproducibility, and packaging.

In-session activity:

- Each student chooses one panel from Figures 3-7 and gives a 3-minute "claim-evidence-limit" explanation.

Success criteria:

- The student can distinguish sensitivity, selectivity, dynamic range, response time, and limit of detection.
- The student can identify which reported application is closest to PIC integration and why.

Assignment:

- Make five application cards, one for each sensing method.
- Each card must include: analyte, transduction mechanism, nanostructure, performance metric, bottleneck, PIC compatibility.

## 6. Week 4: Photonic Integrated Circuits and Plasmonic Components

Reading:

- Section 4.1
- Figure 8
- Glossary terms: `PIC`, `waveguide`, `SOI`, `MRR`, `MZI`, `PPM`, `MIM`, `MSM`, `Pockels-effect`, `BM`, `plasmonic-switcher`

Core teaching goal:

The student must understand PICs as a system architecture, not as a synonym for miniaturization.

Key components:

| Component | Role in PIC sensor | Conceptual point |
| --- | --- | --- |
| Light source | Provides excitation | On-chip source integration is difficult, especially for silicon |
| Waveguide | Routes and confines optical mode | Evanescent field enables analyte interaction |
| Resonator | Enhances interaction and spectral selectivity | Q-factor and linewidth matter |
| Modulator | Encodes or controls optical phase/intensity | Electro-optic or thermo-optic tuning creates controllability |
| Detector | Converts optical signal to electrical signal | Bandwidth, noise, and mode matching matter |
| Switch/logic element | Routes or processes optical signals | Moves toward optical information processing |

Mini-lecture outline:

1. Diffraction limit and why dielectric confinement alone is insufficient for nanoscale components.
2. Plasmonic confinement and the tradeoff with ohmic loss.
3. Figure 8 as a component library:
   - logic gate,
   - nanolight source,
   - phase modulator,
   - detector,
   - switcher.
4. Why sensing benefits from integration:
   - stable alignment,
   - small footprint,
   - multiplexing,
   - lower sample volume,
   - faster readout.
5. Why integration remains hard:
   - source integration,
   - material incompatibility,
   - packaging,
   - thermal and optical loss.

In-session activity:

- Redesign a free-space RI or SEIRA setup as a chip-level block diagram.
- Require blocks for excitation, guiding, interaction, readout, and optional computation.

Success criteria:

- The student can explain why plasmonics gives strong confinement but creates loss.
- The student can explain why SOI is useful yet spectrally limited.

Assignment:

- Produce a "bulk-to-PIC conversion" diagram for one sensing method.
- List three integration risks and one mitigation for each.

## 7. Week 5: In-Sensor Computing and Photonic AI

Reading:

- Section 4.2
- Figures 9-10
- Glossary terms: `in-sensor-computing`, `NSEC`, `PNN`, `CNN`, `MLP`, `photonic-nose`, `photonic-tongue`, `TENG`, `CMOS`, `Q-factor`

Core teaching goal:

The student must understand that in-sensor computing is a data-movement and latency solution, not simply "putting AI near a sensor".

System comparison:

| Architecture | Signal path | Main bottleneck | Advantage |
| --- | --- | --- | --- |
| Conventional sensing | Sensor -> ADC -> CPU/GPU/cloud | Data transfer and latency | Flexible computation |
| Near-sensor edge computing | Sensor -> nearby processor | Hardware integration and power | Lower latency, less cloud dependence |
| Photonic in-sensor computing | Optical signal -> photonic preprocessing or weighting -> decision | reconfigurability, analog noise, nonlinear activation | parallelism, bandwidth, low latency |

Case 1: MIR photonic nose

- Input: VOC absorption spectra in MIR range.
- Physical transduction: analyte absorption changes transmitted intensity in a waveguide.
- Computation: CNN classification and MLP concentration regression.
- Teaching point: molecular fingerprinting plus ML solves mixture interpretation.

Case 2: Waveguide-integrated graphene photodetector

- Input: optical channels or sensory signals.
- Device function: bias-tunable responsivity acts as a weight.
- Computation: weighted summation at the optical frontend.
- Teaching point: detection and multiplication can be coupled.

Case 3: AlN/Si NSEC platform

- Input: TENG mechanical signals from glove or sock.
- Feature extraction: AlN MRRs integrate temporal features.
- Weighting: Si MZIs implement matrix-vector multiplication.
- Backend: electronic activation and training.
- Teaching point: practical photonic AI is often hybrid, not purely optical.

Mini-lecture outline:

1. Why spectra and sensor arrays produce too much raw data.
2. What operation can be done optically: filtering, integration, convolution, weighting, matrix-vector multiplication.
3. What remains difficult: nonlinear activation, training, memory, reconfiguration, calibration.
4. Why analog noise and quantization matter.
5. How to evaluate an AI sensor: optical metric plus ML metric plus system metric.

In-session activity:

- For Figure 9 or Figure 10, trace the full path:
  - physical input,
  - optical interaction,
  - photonic transformation,
  - electrical conversion,
  - ML decision,
  - performance claim.

Success criteria:

- The student can explain why `accuracy` alone is insufficient for an optical AI sensor.
- The student can separate feature extraction, weighting, activation, and training in a photonic neural system.

Assignment:

- Choose one in-sensor computing case and redraw it as a signal-flow diagram.
- Include where noise, loss, and calibration error enter.

## 8. Week 6: Challenges, Outlook, and Research Proposal

Reading:

- Section 5
- Figure 11
- Glossary terms: revisit all terms connected to the student's proposal.

Core teaching goal:

The student must transform the review's outlook into a defensible research direction.

Challenge clusters:

- Integration and packaging:
  - fiber alignment,
  - light source integration,
  - microfluidic sample delivery,
  - chip-to-world interface,
  - packaging-induced loss and variability.
- Materials and spectral coverage:
  - silicon works well near 1.3-1.55 um but is not universal,
  - visible sensing may need silicon nitride or other platforms,
  - MIR sensing may need germanium, chalcogenide, graphene, or other materials,
  - active materials introduce fabrication and thermal complexity.
- Data and AI:
  - high-dimensional spectra,
  - labeled dataset scarcity,
  - overfitting under limited data,
  - analog noise,
  - hardware-constrained inference.
- System deployment:
  - calibration drift,
  - surface fouling,
  - energy budget,
  - security and trust,
  - field robustness.

Final presentation format:

- 10 min presentation.
- 5 min technical Q&A.
- 1 page written abstract.

Required proposal structure:

1. Target problem and analyte.
2. Sensing mechanism.
3. Optical/PIC platform.
4. Expected signal and metric.
5. AI or in-sensor computing role.
6. Main bottleneck.
7. Proposed validation experiment.

Success criteria:

- The proposal is grounded in one of the review's mechanisms.
- The proposal includes at least one optical performance metric and one system or ML metric.
- The student can defend why PIC integration or in-sensor computing is necessary for the chosen problem.

## 9. Instructor Checklist

Before each meeting:

- Assign exact pages and figures.
- Select 8-12 glossary terms from `terminology_optical_sensor.md`.
- Prepare one metric problem and one figure-reading question.
- Ask the student to bring a one-page handwritten or typed concept sheet.

During each meeting:

- Keep returning to the same chain: mechanism -> observable -> metric -> device -> bottleneck.
- Do not let the discussion stay at the application-label level.
- Force every claim about "better sensing" to name the metric that improves.

After each meeting:

- Mark misconceptions in three categories:
  - physics misconception,
  - device architecture misconception,
  - AI/system misconception.
- Revise the next quiz to target those misconceptions.

## 10. Minimal Mastery Rubric

| Level | Description |
| --- | --- |
| Insufficient | Can list techniques but cannot explain the changed optical observable or metric. |
| Basic | Can explain each technique and reproduce the main formulas but struggles to connect to device design. |
| Graduate-ready | Can connect mechanism, nanostructure, metric, application, and PIC bottleneck. |
| Research-ready | Can critique the review and propose a technically plausible next experiment or device architecture. |

