---
capec_id: CAPEC-646
name: Peripheral Footprinting
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: Medium
related_cwe: [CWE-200]
related_attack: [T1120]
url: https://capec.mitre.org/data/definitions/646.html
tags: [mitre-capec, attack-pattern, CAPEC-646]
---

# CAPEC-646 - Peripheral Footprinting

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-646](https://capec.mitre.org/data/definitions/646.html)

## Description
Adversaries may attempt to obtain information about attached peripheral devices and components connected to a computer system. Examples may include discovering the presence of iOS devices by searching for backups, analyzing the Windows registry to determine what USB devices have been connected, or infecting a victim system with malware to report when a USB device has been connected. This may allow the adversary to gain additional insight about the system or network environment, which may be useful in constructing further attacks.

## Prerequisites
- The adversary needs either physical or remote access to the victim system.

## Skills required
- **Medium**: If analyzing the Windows registry, the adversary must understand the registry structure to know where to look for devices.

## Mitigations
- Identify programs that may be used to acquire peripheral information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

## Related ATT&CK techniques
- T1120

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/646.html
