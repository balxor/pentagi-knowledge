---
capec_id: CAPEC-253
name: Remote Code Inclusion
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: n/a
related_cwe: [CWE-829]
related_attack: []
url: https://capec.mitre.org/data/definitions/253.html
tags: [mitre-capec, attack-pattern, CAPEC-253]
---

# CAPEC-253 - Remote Code Inclusion

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-253](https://capec.mitre.org/data/definitions/253.html)

## Description
The attacker forces an application to load arbitrary code files from a remote location. The attacker could use this to try to load old versions of library files that have known vulnerabilities, to load malicious files that the attacker placed on the remote machine, or to otherwise change the functionality of the targeted application in unexpected ways.

## Prerequisites
- Target application server must allow remote files to be included.The malicious file must be placed on the remote machine previously.

## Mitigations
- Minimize attacks by input validation and sanitization of any user data that will be used by the target application to locate a remote file to be included.

## Related weaknesses (CWE)
- [CWE-829](https://cwe.mitre.org/data/definitions/829.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/253.html
