---
capec_id: CAPEC-635
name: Alternative Execution Due to Deceptive Filenames
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: High
related_cwe: [CWE-162]
related_attack: [T1036.007]
url: https://capec.mitre.org/data/definitions/635.html
tags: [mitre-capec, attack-pattern, CAPEC-635]
---

# CAPEC-635 - Alternative Execution Due to Deceptive Filenames

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** High  -  **CAPEC:** [CAPEC-635](https://capec.mitre.org/data/definitions/635.html)

## Description
The extension of a file name is often used in various contexts to determine the application that is used to open and use it. If an attacker can cause an alternative application to be used, it may be able to execute malicious code, cause a denial of service or expose sensitive information.

## Prerequisites
- The use of the file must be controlled by the file extension.

## Mitigations
- Applications should insure that the content of the file is consistent with format it is expecting, and not depend solely on the file extension.

## Related weaknesses (CWE)
- [CWE-162](https://cwe.mitre.org/data/definitions/162.html)

## Related ATT&CK techniques
- T1036.007

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/635.html
