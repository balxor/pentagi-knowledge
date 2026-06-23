---
capec_id: CAPEC-643
name: Identify Shared Files/Directories on System
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Medium
related_cwe: [CWE-267, CWE-200]
related_attack: [T1135]
url: https://capec.mitre.org/data/definitions/643.html
tags: [mitre-capec, attack-pattern, CAPEC-643]
---

# CAPEC-643 - Identify Shared Files/Directories on System

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-643](https://capec.mitre.org/data/definitions/643.html)

## Description
An adversary discovers connections between systems by exploiting the target system's standard practice of revealing them in searchable, common areas. Through the identification of shared folders/drives between systems, the adversary may further their goals of locating and collecting sensitive information/files, or map potential routes for lateral movement within the network.

## Prerequisites
- The adversary must have obtained logical access to the system by some means (e.g., via obtained credentials or planting malware on the system).

## Skills required
- **Low**: Once the adversary has logical access (which can potentially require high knowledge and skill level), the adversary needs only the capability and facility to navigate the system through the OS graphical user interface or the command line. The adversary, or their malware, can simply employ a set of commands that search for shared drives on the system (e.g., net view \\remote system or net share).

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Confidentiality**: Read Data (The adversary is potentially able to identify the location of sensitive information or lateral pathways through the network.)

## Mitigations
- Identify unnecessary system utilities or potentially malicious software that may contain functionality to identify network share information, and audit and/or block them by using allowlist tools.

## Related weaknesses (CWE)
- [CWE-267](https://cwe.mitre.org/data/definitions/267.html)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

## Related ATT&CK techniques
- T1135

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/643.html
