---
capec_id: CAPEC-590
name: IP Address Blocking
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: [CWE-300]
related_attack: []
url: https://capec.mitre.org/data/definitions/590.html
tags: [mitre-capec, attack-pattern, CAPEC-590]
---

# CAPEC-590 - IP Address Blocking

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-590](https://capec.mitre.org/data/definitions/590.html)

## Description
An adversary performing this type of attack drops packets destined for a target IP address. The aim is to prevent access to the service hosted at the target IP address.

## Prerequisites
- This attack requires the ability to conduct deep packet inspection with an In-Path device that can drop the targeted traffic and/or connection.

## Consequences
- **Availability**: Other (Blocking packets intended for a target IP address denies its availability to the user.)

## Mitigations
- Have a large pool of backup IPs built into the application and support proxy capability in the application.

## Related weaknesses (CWE)
- [CWE-300](https://cwe.mitre.org/data/definitions/300.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/590.html
