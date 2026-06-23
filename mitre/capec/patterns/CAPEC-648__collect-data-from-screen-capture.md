---
capec_id: CAPEC-648
name: Collect Data from Screen Capture
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Medium
related_cwe: [CWE-267]
related_attack: [T1113, T1513]
url: https://capec.mitre.org/data/definitions/648.html
tags: [mitre-capec, attack-pattern, CAPEC-648]
---

# CAPEC-648 - Collect Data from Screen Capture

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-648](https://capec.mitre.org/data/definitions/648.html)

## Description
An adversary gathers sensitive information by exploiting the system's screen capture functionality. Through screenshots, the adversary aims to see what happens on the screen over the course of an operation. The adversary can leverage information gathered in order to carry out further attacks.

## Prerequisites
- The adversary must have obtained logical access to the system by some means (e.g., via obtained credentials or planting malware on the system).

## Skills required
- **Low**: Once the adversary has logical access (which can potentially require high knowledge and skill level), the adversary needs only to leverage the relevant command for screen capture.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Confidentiality**: Read Data (The adversary is able to capture potentially sensitive information and processes as they appear on the screen.)

## Mitigations
- Identify potentially malicious software that may have functionality to acquire screen captures, and audit and/or block it by using allowlist tools.
- While screen capture is a legitimate and practical function, certain situations and context may require the disabling of this feature.

## Related weaknesses (CWE)
- [CWE-267](https://cwe.mitre.org/data/definitions/267.html)

## Related ATT&CK techniques
- T1113
- T1513

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/648.html
