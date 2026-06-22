---
attack_id: T0877
name: I/O Image
type: technique
parent: null
tactics: [Collection]
platforms: [None]
url: https://attack.mitre.org/techniques/T0877
tags: [mitre-attack, technique, T0877]
---

# T0877 - I/O Image

**Tactic(s):** Collection  -  **Platforms:** None  -  **ATT&CK:** [T0877](https://attack.mitre.org/techniques/T0877)

## Summary
Adversaries may seek to capture process values related to the inputs and outputs of a PLC. During the scan cycle, a PLC reads the status of all inputs and stores them in an image table. (Citation: Nanjundaiah, Vaidyanath) The image table is the PLCs internal storage location where values of inputs/outputs for one scan are stored while it executes the user program. After the PLC has solved the entire logic program, it updates the output image table. The contents of this output image table are written to the corresponding output points in I/O Modules.

The Input and Output Image tables described above make up the I/O Image on a PLC. This image is used by the user program instead of directly interacting with physical I/O. (Citation: Spenneberg, Ralf 2016) 

Adversaries may collect the I/O Image state of a PLC by utilizing a devices [Native API](https://attack.mitre.org/techniques/T0834) to access the memory regions directly. The collection of the PLCs I/O state could be used to replace values or inform future stages of an attack.

## Role in the attack flow
Used to achieve the **Collection** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0816 Mitigation Limited or Not Effective** - This type of attack technique cannot be easily mitigated with preventative controls since it is based on the abuse of system features.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0877
