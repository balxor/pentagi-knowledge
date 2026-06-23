---
capec_id: CAPEC-562
name: Modify Shared File
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: [CWE-284]
related_attack: [T1080]
url: https://capec.mitre.org/data/definitions/562.html
tags: [mitre-capec, attack-pattern, CAPEC-562]
---

# CAPEC-562 - Modify Shared File

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-562](https://capec.mitre.org/data/definitions/562.html)

## Description
An adversary manipulates the files in a shared location by adding malicious programs, scripts, or exploit code to valid content. Once a user opens the shared content, the tainted content is executed.

## Mitigations
- Disallow shared content. Protect shared folders by minimizing users that have write access. Use utilities that mitigate exploitation like the Microsoft Enhanced Mitigation Experience Toolkit (EMET) to prevent exploits from being run.

## Related weaknesses (CWE)
- [CWE-284](https://cwe.mitre.org/data/definitions/284.html)

## Related ATT&CK techniques
- T1080

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/562.html
