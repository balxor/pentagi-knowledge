---
capec_id: CAPEC-596
name: TCP RST Injection
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: [CWE-940]
related_attack: []
url: https://capec.mitre.org/data/definitions/596.html
tags: [mitre-capec, attack-pattern, CAPEC-596]
---

# CAPEC-596 - TCP RST Injection

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-596](https://capec.mitre.org/data/definitions/596.html)

## Description
An adversary injects one or more TCP RST packets to a target after the target has made a HTTP GET request. The goal of this attack is to have the target and/or destination web server terminate the TCP connection.

## Prerequisites
- An On/In Path Device

## Related weaknesses (CWE)
- [CWE-940](https://cwe.mitre.org/data/definitions/940.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/596.html
