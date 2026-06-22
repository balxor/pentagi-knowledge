---
attack_id: T1119
name: Automated Collection
type: technique
parent: null
tactics: [Collection]
platforms: [IaaS, Linux, macOS, Office Suite, SaaS, Windows]
url: https://attack.mitre.org/techniques/T1119
tags: [mitre-attack, technique, T1119]
---

# T1119 - Automated Collection

**Tactic(s):** Collection  ·  **Platforms:** IaaS, Linux, macOS, Office Suite, SaaS, Windows  ·  **ATT&CK:** [T1119](https://attack.mitre.org/techniques/T1119)

## Summary
Once established within a system or network, an adversary may use automated techniques for collecting internal data. Methods for performing this technique could include use of a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059) to search for and copy information fitting set criteria such as file type, location, or name at specific time intervals. 

In cloud-based environments, adversaries may also use cloud APIs, data pipelines, command line interfaces, or extract, transform, and load (ETL) services to automatically collect data.(Citation: Mandiant UNC3944 SMS Phishing 2023) 

This functionality could also be built into remote access tools. 

This technique may incorporate use of other techniques such as [File and Directory Discovery](https://attack.mitre.org/techniques/T1083) and [Lateral Tool Transfer](https://attack.mitre.org/techniques/T1570) to identify and move files, as well as [Cloud Service Dashboard](https://attack.mitre.org/techniques/T1538) and [Cloud Storage Object Discovery](https://attack.mitre.org/techniques/T1619) to identify resources in cloud environments.

## Role in the attack flow
Used to achieve the **Collection** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: IaaS, Linux, macOS, Office Suite, SaaS, Windows.

## Mitigations
- **M1029 Remote Data Storage** - Remote Data Storage focuses on moving critical data, such as security logs and sensitive files, to secure, off-host locations to minimize unauthorized access, tampering, or destruction by adversaries. By leveraging remote storage solutions, organizations enhance the protection of forensic evidence, sensitive information, and monitoring data. This mitigation can be implemented through the following measures:
- **M1041 Encrypt Sensitive Information** - Protect sensitive information at rest, in transit, and during processing by using strong encryption algorithms. Encryption ensures the confidentiality and integrity of data, preventing unauthorized access or tampering. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1119
