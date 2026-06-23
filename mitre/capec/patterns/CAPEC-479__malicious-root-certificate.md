---
capec_id: CAPEC-479
name: Malicious Root Certificate
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: Low
related_cwe: [CWE-284]
related_attack: [T1553.004]
url: https://capec.mitre.org/data/definitions/479.html
tags: [mitre-capec, attack-pattern, CAPEC-479]
---

# CAPEC-479 - Malicious Root Certificate

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** Low  -  **CAPEC:** [CAPEC-479](https://capec.mitre.org/data/definitions/479.html)

## Description
An adversary exploits a weakness in authorization and installs a new root certificate on a compromised system. Certificates are commonly used for establishing secure TLS/SSL communications within a web browser. When a user attempts to browse a website that presents a certificate that is not trusted an error message will be displayed to warn the user of the security risk. Depending on the security settings, the browser may not allow the user to establish a connection to the website. Adversaries have used this technique to avoid security warnings prompting users when compromised systems connect over HTTPS to adversary controlled web servers that spoof legitimate websites in order to collect login credentials.

## Prerequisites
- The adversary must have the ability to create a new root certificate.

## Related weaknesses (CWE)
- [CWE-284](https://cwe.mitre.org/data/definitions/284.html)

## Related ATT&CK techniques
- T1553.004

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/479.html
