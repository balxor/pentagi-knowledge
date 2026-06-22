---
attack_id: T1619
name: Cloud Storage Object Discovery
type: technique
parent: null
tactics: [Discovery]
platforms: [IaaS]
url: https://attack.mitre.org/techniques/T1619
tags: [mitre-attack, technique, T1619]
---

# T1619 - Cloud Storage Object Discovery

**Tactic(s):** Discovery  ·  **Platforms:** IaaS  ·  **ATT&CK:** [T1619](https://attack.mitre.org/techniques/T1619)

## Summary
Adversaries may enumerate objects in cloud storage infrastructure. Adversaries may use this information during automated discovery to shape follow-on behaviors, including requesting all or specific objects from cloud storage.  Similar to [File and Directory Discovery](https://attack.mitre.org/techniques/T1083) on a local host, after identifying available storage services (i.e. [Cloud Infrastructure Discovery](https://attack.mitre.org/techniques/T1580)) adversaries may access the contents/objects stored in cloud infrastructure.

Cloud service providers offer APIs allowing users to enumerate objects stored within cloud storage. Examples include ListObjectsV2 in AWS (Citation: ListObjectsV2) and List Blobs in Azure(Citation: List Blobs) .

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: IaaS.

## Mitigations
- **M1018 User Account Management** - User Account Management involves implementing and enforcing policies for the lifecycle of user accounts, including creation, modification, and deactivation. Proper account management reduces the attack surface by limiting unauthorized access, managing account privileges, and ensuring accounts are used according to organizational policies. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1619
