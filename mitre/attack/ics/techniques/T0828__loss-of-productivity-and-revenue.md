---
attack_id: T0828
name: Loss of Productivity and Revenue
type: technique
parent: null
tactics: [Impact]
platforms: [None]
url: https://attack.mitre.org/techniques/T0828
tags: [mitre-attack, technique, T0828]
---

# T0828 - Loss of Productivity and Revenue

**Tactic(s):** Impact  -  **Platforms:** None  -  **ATT&CK:** [T0828](https://attack.mitre.org/techniques/T0828)

## Summary
Adversaries may cause loss of productivity and revenue through disruption and even damage to the availability and integrity of control system operations, devices, and related processes. This technique may manifest as a direct effect of an ICS-targeting attack or tangentially, due to an IT-targeting attack against non-segregated environments. 

In cases where these operations or services are brought to a halt, the loss of productivity may eventually present an impact for the end-users or consumers of products and services. The disrupted supply-chain may result in supply shortages and increased prices, among other consequences. 

A ransomware attack on an Australian beverage company resulted in the shutdown of some manufacturing sites, including precautionary halts to protect key systems. (Citation: Paganini, Pierluigi June 2020) The company announced the potential for temporary shortages of their products following the attack. (Citation: Paganini, Pierluigi June 2020) (Citation: Lion Corporation June 2020) 

In the 2021 Colonial Pipeline ransomware incident, the pipeline was unable to transport approximately 2.5 million barrels of fuel per day to the East Coast.  (Citation: Colonial Pipeline Company May 2021)

## Role in the attack flow
Used to achieve the **Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0953 Data Backup** - Take and store data backups from end user systems and critical servers. Ensure backup and storage systems are hardened and kept separate from the corporate network to prevent compromise.   Maintain and exercise incident response plans  (Citation: Department of Homeland Security October 2009), including the management of  'gold-copy' back-up images and configurations for key systems to enable quick recovery and response from adversarial activities that impact control, view, or availability.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0828
