---
capec_id: CAPEC-634
name: Probe Audio and Video Peripherals
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: [CWE-267]
related_attack: [T1123, T1125]
url: https://capec.mitre.org/data/definitions/634.html
tags: [mitre-capec, attack-pattern, CAPEC-634]
---

# CAPEC-634 - Probe Audio and Video Peripherals

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-634](https://capec.mitre.org/data/definitions/634.html)

## Description
The adversary exploits the target system's audio and video functionalities through malware or scheduled tasks. The goal is to capture sensitive information about the target for financial, personal, political, or other gains which is accomplished by collecting communication data between two parties via the use of peripheral devices (e.g. microphones and webcams) or applications with audio and video capabilities (e.g. Skype) on a system.

## Prerequisites
- Knowledge of the target device's or application’s vulnerabilities that can be capitalized on with malicious code. The adversary must be able to place the malicious code on the target device.

## Skills required
- **High**: To deploy a hidden process or malware on the system to automatically collect audio and video data.

## Consequences
- **Confidentiality**: Read Data

## Mitigations
- Prevent unknown code from executing on a system through the use of an allowlist policy.
- Patch installed applications as soon as new updates become available.

## Related weaknesses (CWE)
- [CWE-267](https://cwe.mitre.org/data/definitions/267.html)

## Related ATT&CK techniques
- T1123
- T1125

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/634.html
