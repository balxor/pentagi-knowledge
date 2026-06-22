---
attack_id: T1041
name: Exfiltration Over C2 Channel
type: technique
parent: null
tactics: [Exfiltration]
platforms: [ESXi, Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1041
tags: [mitre-attack, technique, T1041]
---

# T1041 - Exfiltration Over C2 Channel

**Tactic(s):** Exfiltration  ·  **Platforms:** ESXi, Linux, macOS, Windows  ·  **ATT&CK:** [T1041](https://attack.mitre.org/techniques/T1041)

## Summary
Adversaries may steal data by exfiltrating it over an existing command and control channel. Stolen data is encoded into the normal communications channel using the same protocol as command and control communications.

## Role in the attack flow
Used to achieve the **Exfiltration** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: ESXi, Linux, macOS, Windows.

## Mitigations
- **M1031 Network Intrusion Prevention** - Use intrusion detection signatures to block traffic at network boundaries.
- **M1057 Data Loss Prevention** - Data Loss Prevention (DLP) involves implementing strategies and technologies to identify, categorize, monitor, and control the movement of sensitive data within an organization. This includes protecting data formats indicative of Personally Identifiable Information (PII), intellectual property, or financial data from unauthorized access, transmission, or exfiltration. DLP solutions integrate with network, endpoint, and cloud platforms to enforce security policies and prevent accidental or malicious data leaks. (Citation: PurpleSec Data Loss Prevention) This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1041
