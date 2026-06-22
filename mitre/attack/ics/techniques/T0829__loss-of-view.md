---
attack_id: T0829
name: Loss of View
type: technique
parent: null
tactics: [Impact]
platforms: [None]
url: https://attack.mitre.org/techniques/T0829
tags: [mitre-attack, technique, T0829]
---

# T0829 - Loss of View

**Tactic(s):** Impact  -  **Platforms:** None  -  **ATT&CK:** [T0829](https://attack.mitre.org/techniques/T0829)

## Summary
Adversaries may cause a sustained or permanent loss of view where the ICS equipment will require local, hands-on operator intervention; for instance, a restart or manual operation. By causing a sustained reporting or visibility loss, the adversary can effectively hide the present state of operations. This loss of view can occur without affecting the physical processes themselves. (Citation: Corero) (Citation: Michael J. Assante and Robert M. Lee) (Citation: Tyson Macaulay)

## Role in the attack flow
Used to achieve the **Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0811 Redundancy of Service** - Redundancy could be provided for both critical ICS devices and services, such as back-up devices or hot-standbys.
- **M0810 Out-of-Band Communications Channel** - Have alternative methods to support communication requirements during communication failures and data integrity attacks. (Citation: National Institute of Standards and Technology April 2013) (Citation: Defense Advanced Research Projects Agency)
- **M0953 Data Backup** - Take and store data backups from end user systems and critical servers. Ensure backup and storage systems are hardened and kept separate from the corporate network to prevent compromise.   Maintain and exercise incident response plans  (Citation: Department of Homeland Security October 2009), including the management of  'gold-copy' back-up images and configurations for key systems to enable quick recovery and response from adversarial activities that impact control, view, or availability.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0829
