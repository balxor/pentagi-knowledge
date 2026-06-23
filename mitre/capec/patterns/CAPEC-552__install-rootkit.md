---
capec_id: CAPEC-552
name: Install Rootkit 
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-284]
related_attack: [T1014, T1542.003, T1547.006]
url: https://capec.mitre.org/data/definitions/552.html
tags: [mitre-capec, attack-pattern, CAPEC-552]
---

# CAPEC-552 - Install Rootkit 

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-552](https://capec.mitre.org/data/definitions/552.html)

## Description
An adversary exploits a weakness in authentication to install malware that alters the functionality and information provide by targeted operating system API calls. Often referred to as rootkits, it is often used to hide the presence of programs, files, network connections, services, drivers, and other system components.

## Mitigations
- Prevent adversary access to privileged accounts necessary to install rootkits.

## Related weaknesses (CWE)
- [CWE-284](https://cwe.mitre.org/data/definitions/284.html)

## Related ATT&CK techniques
- T1014
- T1542.003
- T1547.006

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/552.html
