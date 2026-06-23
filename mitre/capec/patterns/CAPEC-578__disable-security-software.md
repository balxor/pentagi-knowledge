---
capec_id: CAPEC-578
name: Disable Security Software
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: Medium
related_cwe: [CWE-284]
related_attack: [T1556.006, T1562.001, T1562.002, T1562.004, T1562.007, T1562.008, T1562.009]
url: https://capec.mitre.org/data/definitions/578.html
tags: [mitre-capec, attack-pattern, CAPEC-578]
---

# CAPEC-578 - Disable Security Software

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-578](https://capec.mitre.org/data/definitions/578.html)

## Description
An adversary exploits a weakness in access control to disable security tools so that detection does not occur. This can take the form of killing processes, deleting registry keys so that tools do not start at run time, deleting log files, or other methods.

## Prerequisites
- The adversary must have the capability to interact with the configuration of the targeted system.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Availability**: Hide Activities (By disabling certain security tools, the adversary can hide malicious activity and avoid detection.)

## Mitigations
- Ensure proper permissions are in place to prevent adversaries from altering the execution status of security tools.

## Related weaknesses (CWE)
- [CWE-284](https://cwe.mitre.org/data/definitions/284.html)

## Related ATT&CK techniques
- T1556.006
- T1562.001
- T1562.002
- T1562.004
- T1562.007
- T1562.008
- T1562.009

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/578.html
