---
attack_id: T0852
name: Screen Capture
type: technique
parent: null
tactics: [Collection]
platforms: [None]
url: https://attack.mitre.org/techniques/T0852
tags: [mitre-attack, technique, T0852]
---

# T0852 - Screen Capture

**Tactic(s):** Collection  -  **Platforms:** None  -  **ATT&CK:** [T0852](https://attack.mitre.org/techniques/T0852)

## Summary
Adversaries may attempt to perform screen capture of devices in the control system environment. Screenshots may be taken of workstations, HMIs, or other devices that display environment-relevant process, device, reporting, alarm, or related data. These device displays may reveal information regarding the ICS process, layout, control, and related schematics. In particular, an HMI can provide a lot of important industrial process information. (Citation: ICS-CERT October 2017) Analysis of screen captures may provide the adversary with an understanding of intended operations and interactions between critical devices.

## Role in the attack flow
Used to achieve the **Collection** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0816 Mitigation Limited or Not Effective** - This type of attack technique cannot be easily mitigated with preventative controls since it is based on the abuse of system features.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0852
