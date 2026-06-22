---
attack_id: T0815
name: Denial of View
type: technique
parent: null
tactics: [Impact]
platforms: [None]
url: https://attack.mitre.org/techniques/T0815
tags: [mitre-attack, technique, T0815]
---

# T0815 - Denial of View

**Tactic(s):** Impact  -  **Platforms:** None  -  **ATT&CK:** [T0815](https://attack.mitre.org/techniques/T0815)

## Summary
Adversaries may cause a denial of view in attempt to disrupt and prevent operator oversight on the status of an ICS environment. This may manifest itself as a temporary communication failure between a device and its control source, where the interface recovers and becomes available once the interference ceases. (Citation: Corero) (Citation: Michael J. Assante and Robert M. Lee) (Citation: Tyson Macaulay) 

An adversary may attempt to deny operator visibility by preventing them from receiving status and reporting messages. Denying this view may temporarily block and prevent operators from noticing a change in state or anomalous behavior. The environment's data and processes may still be operational, but functioning in an unintended or adversarial manner.

## Role in the attack flow
Used to achieve the **Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0810 Out-of-Band Communications Channel** - Have alternative methods to support communication requirements during communication failures and data integrity attacks. (Citation: National Institute of Standards and Technology April 2013) (Citation: Defense Advanced Research Projects Agency)
- **M0953 Data Backup** - Take and store data backups from end user systems and critical servers. Ensure backup and storage systems are hardened and kept separate from the corporate network to prevent compromise.   Maintain and exercise incident response plans  (Citation: Department of Homeland Security October 2009), including the management of  'gold-copy' back-up images and configurations for key systems to enable quick recovery and response from adversarial activities that impact control, view, or availability.
- **M0811 Redundancy of Service** - Redundancy could be provided for both critical ICS devices and services, such as back-up devices or hot-standbys.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0815
