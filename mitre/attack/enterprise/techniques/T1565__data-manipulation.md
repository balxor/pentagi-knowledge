---
attack_id: T1565
name: Data Manipulation
type: technique
parent: null
tactics: [Impact]
platforms: [Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1565
tags: [mitre-attack, technique, T1565]
---

# T1565 - Data Manipulation

**Tactic(s):** Impact  -  **Platforms:** Linux, macOS, Windows  -  **ATT&CK:** [T1565](https://attack.mitre.org/techniques/T1565)

## Summary
Adversaries may insert, delete, or manipulate data in order to influence external outcomes or hide activity, thus threatening the integrity of the data.(Citation: Sygnia Elephant Beetle Jan 2022) By manipulating data, adversaries may attempt to affect a business process, organizational understanding, or decision making.

The type of modification and the impact it will have depends on the target application and process as well as the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise and possibly access to specialized software related to the system that would typically be gained through a prolonged information gathering campaign in order to have the desired impact.

## Role in the attack flow
Used to achieve the **Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows.

## Mitigations
- **M1041 Encrypt Sensitive Information** - Protect sensitive information at rest, in transit, and during processing by using strong encryption algorithms. Encryption ensures the confidentiality and integrity of data, preventing unauthorized access or tampering. This mitigation can be implemented through the following measures:
- **M1029 Remote Data Storage** - Remote Data Storage focuses on moving critical data, such as security logs and sensitive files, to secure, off-host locations to minimize unauthorized access, tampering, or destruction by adversaries. By leveraging remote storage solutions, organizations enhance the protection of forensic evidence, sensitive information, and monitoring data. This mitigation can be implemented through the following measures:
- **M1030 Network Segmentation** - Network segmentation involves dividing a network into smaller, isolated segments to control and limit the flow of traffic between devices, systems, and applications. By segmenting networks, organizations can reduce the attack surface, restrict lateral movement by adversaries, and protect critical assets from compromise.
- **M1022 Restrict File and Directory Permissions** - Restricting file and directory permissions involves setting access controls at the file system level to limit which users, groups, or processes can read, write, or execute files. By configuring permissions appropriately, organizations can reduce the attack surface for adversaries seeking to access sensitive data, plant malicious code, or tamper with system files.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1565
