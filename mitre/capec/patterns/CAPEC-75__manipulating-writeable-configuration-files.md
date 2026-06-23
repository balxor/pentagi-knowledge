---
capec_id: CAPEC-75
name: Manipulating Writeable Configuration Files
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Very High
related_cwe: [CWE-349, CWE-99, CWE-77, CWE-346, CWE-353, CWE-354]
related_attack: []
url: https://capec.mitre.org/data/definitions/75.html
tags: [mitre-capec, attack-pattern, CAPEC-75]
---

# CAPEC-75 - Manipulating Writeable Configuration Files

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-75](https://capec.mitre.org/data/definitions/75.html)

## Description
Generally these are manually edited files that are not in the preview of the system administrators, any ability on the attackers' behalf to modify these files, for example in a CVS repository, gives unauthorized access directly to the application, the same as authorized users.

## Prerequisites
- Configuration files must be modifiable by the attacker

## Skills required
- **Medium**: To identify vulnerable configuration files, and understand how to manipulate servers and erase forensic evidence

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges

## Mitigations
- Design: Enforce principle of least privilege
- Design: Backup copies of all configuration files
- Implementation: Integrity monitoring for configuration files
- Implementation: Enforce audit logging on code and configuration promotion procedures.
- Implementation: Load configuration from separate process and memory space, for example a separate physical device like a CD

## Related weaknesses (CWE)
- [CWE-349](https://cwe.mitre.org/data/definitions/349.html)
- [CWE-99](https://cwe.mitre.org/data/definitions/99.html)
- [CWE-77](https://cwe.mitre.org/data/definitions/77.html)
- [CWE-346](https://cwe.mitre.org/data/definitions/346.html)
- [CWE-353](https://cwe.mitre.org/data/definitions/353.html)
- [CWE-354](https://cwe.mitre.org/data/definitions/354.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/75.html
