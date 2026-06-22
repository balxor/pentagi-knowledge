---
attack_id: T0801
name: Monitor Process State
type: technique
parent: null
tactics: [Collection]
platforms: [None]
url: https://attack.mitre.org/techniques/T0801
tags: [mitre-attack, technique, T0801]
---

# T0801 - Monitor Process State

**Tactic(s):** Collection  -  **Platforms:** None  -  **ATT&CK:** [T0801](https://attack.mitre.org/techniques/T0801)

## Summary
Adversaries may gather information about the physical process state. This information may be used to gain more information about the process itself or used as a trigger for malicious actions. The sources of process state information may vary such as, OPC tags, historian data, specific PLC block information, or network traffic.

## Role in the attack flow
Used to achieve the **Collection** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0816 Mitigation Limited or Not Effective** - This type of attack technique cannot be easily mitigated with preventative controls since it is based on the abuse of system features.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0801
