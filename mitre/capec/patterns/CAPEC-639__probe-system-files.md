---
capec_id: CAPEC-639
name: Probe System Files
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-552]
related_attack: [T1039, T1552.001, T1552.003, T1552.004, T1552.006]
url: https://capec.mitre.org/data/definitions/639.html
tags: [mitre-capec, attack-pattern, CAPEC-639]
---

# CAPEC-639 - Probe System Files

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-639](https://capec.mitre.org/data/definitions/639.html)

## Description
An adversary obtains unauthorized information due to improperly protected files. If an application stores sensitive information in a file that is not protected by proper access control, then an adversary can access the file and search for sensitive information.

## Prerequisites
- An adversary has access to the file system of a system.

## Consequences
- **Confidentiality**: Read Data

## Mitigations
- Verify that files have proper access controls set, and reduce the storage of sensitive information to only what is necessary.

## Related weaknesses (CWE)
- [CWE-552](https://cwe.mitre.org/data/definitions/552.html)

## Related ATT&CK techniques
- T1039
- T1552.001
- T1552.003
- T1552.004
- T1552.006

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/639.html
