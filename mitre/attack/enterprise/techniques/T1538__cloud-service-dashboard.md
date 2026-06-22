---
attack_id: T1538
name: Cloud Service Dashboard
type: technique
parent: null
tactics: [Discovery]
platforms: [IaaS, SaaS, Office Suite, Identity Provider]
url: https://attack.mitre.org/techniques/T1538
tags: [mitre-attack, technique, T1538]
---

# T1538 - Cloud Service Dashboard

**Tactic(s):** Discovery  -  **Platforms:** IaaS, SaaS, Office Suite, Identity Provider  -  **ATT&CK:** [T1538](https://attack.mitre.org/techniques/T1538)

## Summary
An adversary may use a cloud service dashboard GUI with stolen credentials to gain useful information from an operational cloud environment, such as specific services, resources, and features. For example, the GCP Command Center can be used to view all assets, review findings of potential security risks, and run additional queries, such as finding public IP addresses and open ports.(Citation: Google Command Center Dashboard)

Depending on the configuration of the environment, an adversary may be able to enumerate more information via the graphical dashboard than an API. This also allows the adversary to gain information without manually making any API requests.

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: IaaS, SaaS, Office Suite, Identity Provider.

## Mitigations
- **M1018 User Account Management** - User Account Management involves implementing and enforcing policies for the lifecycle of user accounts, including creation, modification, and deactivation. Proper account management reduces the attack surface by limiting unauthorized access, managing account privileges, and ensuring accounts are used according to organizational policies. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1538
