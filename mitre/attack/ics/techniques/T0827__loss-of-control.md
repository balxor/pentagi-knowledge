---
attack_id: T0827
name: Loss of Control
type: technique
parent: null
tactics: [Impact]
platforms: [None]
url: https://attack.mitre.org/techniques/T0827
tags: [mitre-attack, technique, T0827]
---

# T0827 - Loss of Control

**Tactic(s):** Impact  -  **Platforms:** None  -  **ATT&CK:** [T0827](https://attack.mitre.org/techniques/T0827)

## Summary
Adversaries may seek to achieve a sustained loss of control or a runaway condition in which operators cannot issue any commands even if the malicious interference has subsided. (Citation: Corero) (Citation: Michael J. Assante and Robert M. Lee) (Citation: Tyson Macaulay)

The German Federal Office for Information Security (BSI) reported a targeted attack on a steel mill in its 2014 IT Security Report.(Citation: BSI State of IT Security 2014) These targeted attacks affected industrial operations and resulted in breakdowns of control system components and even entire installations. As a result of these breakdowns, massive impact resulted in damage and unsafe conditions from the uncontrolled shutdown of a blast furnace.

## Role in the attack flow
Used to achieve the **Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0953 Data Backup** - Take and store data backups from end user systems and critical servers. Ensure backup and storage systems are hardened and kept separate from the corporate network to prevent compromise.   Maintain and exercise incident response plans  (Citation: Department of Homeland Security October 2009), including the management of  'gold-copy' back-up images and configurations for key systems to enable quick recovery and response from adversarial activities that impact control, view, or availability.
- **M0811 Redundancy of Service** - Redundancy could be provided for both critical ICS devices and services, such as back-up devices or hot-standbys.
- **M0810 Out-of-Band Communications Channel** - Have alternative methods to support communication requirements during communication failures and data integrity attacks. (Citation: National Institute of Standards and Technology April 2013) (Citation: Defense Advanced Research Projects Agency)

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0827
