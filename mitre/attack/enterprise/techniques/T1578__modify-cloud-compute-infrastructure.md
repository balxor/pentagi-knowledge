---
attack_id: T1578
name: Modify Cloud Compute Infrastructure
type: technique
parent: null
tactics: [Defense Impairment]
platforms: [IaaS]
url: https://attack.mitre.org/techniques/T1578
tags: [mitre-attack, technique, T1578]
---

# T1578 - Modify Cloud Compute Infrastructure

**Tactic(s):** Defense Impairment  -  **Platforms:** IaaS  -  **ATT&CK:** [T1578](https://attack.mitre.org/techniques/T1578)

## Summary
An adversary may attempt to modify a cloud account's compute service infrastructure to evade defenses. A modification to the compute service infrastructure can include the creation, deletion, or modification of one or more components such as compute instances, virtual machines, and snapshots.

Permissions gained from the modification of infrastructure components may bypass restrictions that prevent access to existing infrastructure. Modifying infrastructure components may also allow an adversary to evade detection and remove evidence of their presence.(Citation: Mandiant M-Trends 2020)

## Role in the attack flow
Used to achieve the **Defense Impairment** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: IaaS.

## Mitigations
- **M1018 User Account Management** - User Account Management involves implementing and enforcing policies for the lifecycle of user accounts, including creation, modification, and deactivation. Proper account management reduces the attack surface by limiting unauthorized access, managing account privileges, and ensuring accounts are used according to organizational policies. This mitigation can be implemented through the following measures:
- **M1047 Audit** - Auditing is the process of recording activity and systematically reviewing and analyzing the activity and system configurations. The primary purpose of auditing is to detect anomalies and identify potential threats or weaknesses in the environment. Proper auditing configurations can also help to meet compliance requirements. The process of auditing encompasses regular analysis of user behaviors and system logs in support of proactive security measures.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1578
