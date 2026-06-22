---
attack_id: T1025
name: Data from Removable Media
type: technique
parent: null
tactics: [Collection]
platforms: [Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1025
tags: [mitre-attack, technique, T1025]
---

# T1025 - Data from Removable Media

**Tactic(s):** Collection  -  **Platforms:** Linux, macOS, Windows  -  **ATT&CK:** [T1025](https://attack.mitre.org/techniques/T1025)

## Summary
Adversaries may search connected removable media on computers they have compromised to find files of interest. Sensitive data can be collected from any removable media (optical disk drive, USB memory, etc.) connected to the compromised system prior to Exfiltration. Interactive command shells may be in use, and common functionality within [cmd](https://attack.mitre.org/software/S0106) may be used to gather information. 

Some adversaries may also use [Automated Collection](https://attack.mitre.org/techniques/T1119) on removable media.

## Role in the attack flow
Used to achieve the **Collection** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows.

## Mitigations
- **M1057 Data Loss Prevention** - Data Loss Prevention (DLP) involves implementing strategies and technologies to identify, categorize, monitor, and control the movement of sensitive data within an organization. This includes protecting data formats indicative of Personally Identifiable Information (PII), intellectual property, or financial data from unauthorized access, transmission, or exfiltration. DLP solutions integrate with network, endpoint, and cloud platforms to enforce security policies and prevent accidental or malicious data leaks. (Citation: PurpleSec Data Loss Prevention) This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1025
