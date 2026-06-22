---
attack_id: T0832
name: Manipulation of View
type: technique
parent: null
tactics: [Impact]
platforms: [None]
url: https://attack.mitre.org/techniques/T0832
tags: [mitre-attack, technique, T0832]
---

# T0832 - Manipulation of View

**Tactic(s):** Impact  -  **Platforms:** None  -  **ATT&CK:** [T0832](https://attack.mitre.org/techniques/T0832)

## Summary
Adversaries may attempt to manipulate the information reported back to operators or controllers. This manipulation may be short term or sustained. During this time the process itself could be in a much different state than what is reported. (Citation: Corero) (Citation: Michael J. Assante and Robert M. Lee) (Citation: Tyson Macaulay) 

Operators may be fooled into doing something that is harmful to the system in a loss of view situation. With a manipulated view into the systems, operators may issue inappropriate control sequences that introduce faults or catastrophic failures into the system. Business analysis systems can also be provided with inaccurate data leading to bad management decisions.

## Role in the attack flow
Used to achieve the **Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0802 Communication Authenticity** - When communicating over an untrusted network, utilize secure network protocols that both authenticate the message sender and can verify its integrity. This can be done either through message authentication codes (MACs) or digital signatures, to detect spoofed network messages and unauthorized connections.
- **M0810 Out-of-Band Communications Channel** - Have alternative methods to support communication requirements during communication failures and data integrity attacks. (Citation: National Institute of Standards and Technology April 2013) (Citation: Defense Advanced Research Projects Agency)
- **M0953 Data Backup** - Take and store data backups from end user systems and critical servers. Ensure backup and storage systems are hardened and kept separate from the corporate network to prevent compromise.   Maintain and exercise incident response plans  (Citation: Department of Homeland Security October 2009), including the management of  'gold-copy' back-up images and configurations for key systems to enable quick recovery and response from adversarial activities that impact control, view, or availability.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0832
