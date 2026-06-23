---
capec_id: CAPEC-278
name: Web Services Protocol Manipulation
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: n/a
related_cwe: [CWE-707]
related_attack: []
url: https://capec.mitre.org/data/definitions/278.html
tags: [mitre-capec, attack-pattern, CAPEC-278]
---

# CAPEC-278 - Web Services Protocol Manipulation

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-278](https://capec.mitre.org/data/definitions/278.html)

## Description
An adversary manipulates a web service related protocol to cause a web application or service to react differently than intended. This can either be performed through the manipulation of call parameters to include unexpected values, or by changing the called function to one that should normally be restricted or limited. By leveraging this pattern of attack, the adversary is able to gain access to data or resources normally restricted, or to cause the application or service to crash.

## Prerequisites
- The targeted application or service must rely on web service protocols in such a way that malicious manipulation of them can alter functionality.

## Resources required
- The attacker must be able to manipulate the communications to the targeted application or service.

## Mitigations
- Design: Range, size and value and consistency verification for any arguments supplied to applications and services from external sources and devise appropriate error response.
- Design: Ensure that function calls that should not be called by an unprivileged user are not accessible to them.

## Related weaknesses (CWE)
- [CWE-707](https://cwe.mitre.org/data/definitions/707.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/278.html
