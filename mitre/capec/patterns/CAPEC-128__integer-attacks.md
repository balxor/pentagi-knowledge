---
capec_id: CAPEC-128
name: Integer Attacks
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Medium
related_cwe: [CWE-682]
related_attack: []
url: https://capec.mitre.org/data/definitions/128.html
tags: [mitre-capec, attack-pattern, CAPEC-128]
---

# CAPEC-128 - Integer Attacks

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-128](https://capec.mitre.org/data/definitions/128.html)

## Description
An attacker takes advantage of the structure of integer variables to cause these variables to assume values that are not expected by an application. For example, adding one to the largest positive integer in a signed integer variable results in a negative number. Negative numbers may be illegal in an application and the application may prevent an attacker from providing them directly, but the application may not consider that adding two positive numbers can create a negative number do to the structure of integer storage formats.

## Prerequisites
- The target application must have an integer variable for which only some of the possible integer values are expected by the application and where there are no checks on the value of the variable before use.
- The attacker must be able to manipulate the targeted integer variable such that normal operations result in non-standard values due to the storage structure of integers.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Related weaknesses (CWE)
- [CWE-682](https://cwe.mitre.org/data/definitions/682.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/128.html
