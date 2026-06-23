---
capec_id: CAPEC-276
name: Inter-component Protocol Manipulation
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: n/a
related_cwe: [CWE-707]
related_attack: []
url: https://capec.mitre.org/data/definitions/276.html
tags: [mitre-capec, attack-pattern, CAPEC-276]
---

# CAPEC-276 - Inter-component Protocol Manipulation

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-276](https://capec.mitre.org/data/definitions/276.html)

## Description
Inter-component protocols are used to communicate between different software and hardware modules within a single computer. Common examples are: interrupt signals and data pipes. Subverting the protocol can allow an adversary to impersonate others, discover sensitive information, control the outcome of a session, or perform other attacks. This type of attack targets invalid assumptions that may be inherent in implementers of the protocol, incorrect implementations of the protocol, or vulnerabilities in the protocol itself.

## Related weaknesses (CWE)
- [CWE-707](https://cwe.mitre.org/data/definitions/707.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/276.html
