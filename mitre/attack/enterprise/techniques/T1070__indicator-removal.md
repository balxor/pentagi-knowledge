---
attack_id: T1070
name: Indicator Removal
type: technique
parent: null
tactics: [Stealth]
platforms: [Containers, ESXi, Linux, macOS, Network Devices, Office Suite, Windows]
url: https://attack.mitre.org/techniques/T1070
tags: [mitre-attack, technique, T1070]
---

# T1070 - Indicator Removal

**Tactic(s):** Stealth  -  **Platforms:** Containers, ESXi, Linux, macOS, Network Devices, Office Suite, Windows  -  **ATT&CK:** [T1070](https://attack.mitre.org/techniques/T1070)

## Summary
Adversaries may selectively delete or modify artifacts generated to reduce indications of their presence and blend in with legitimate activity. Rather than broadly removing evidence, adversaries may target specific artifacts that appear anomalous or are likely to draw scrutiny, while leaving sufficient data intact to maintain the appearance of normal system behavior.

Artifacts such as command histories, log entries, or file metadata may be altered in ways that align with expected user or system activity. Location, format, and type of artifact (such as command or login history) are often platform-specific, allowing adversaries to tailor modifications that minimize suspicion.

These actions may not prevent detection entirely but can delay recognition of malicious activity or reduce the fidelity of alerts by making events appear benign or consistent with routine operations. Additionally, selectively removed or modified artifacts may still be recoverable through deeper forensic analysis, though their absence or alteration can complicate timeline reconstruction and attribution.

## Role in the attack flow
Used to achieve the **Stealth** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Containers, ESXi, Linux, macOS, Network Devices, Office Suite, Windows.

## Mitigations
- **M1041 Encrypt Sensitive Information** - Protect sensitive information at rest, in transit, and during processing by using strong encryption algorithms. Encryption ensures the confidentiality and integrity of data, preventing unauthorized access or tampering. This mitigation can be implemented through the following measures:
- **M1029 Remote Data Storage** - Remote Data Storage focuses on moving critical data, such as security logs and sensitive files, to secure, off-host locations to minimize unauthorized access, tampering, or destruction by adversaries. By leveraging remote storage solutions, organizations enhance the protection of forensic evidence, sensitive information, and monitoring data. This mitigation can be implemented through the following measures:
- **M1022 Restrict File and Directory Permissions** - Restricting file and directory permissions involves setting access controls at the file system level to limit which users, groups, or processes can read, write, or execute files. By configuring permissions appropriately, organizations can reduce the attack surface for adversaries seeking to access sensitive data, plant malicious code, or tamper with system files.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1070
