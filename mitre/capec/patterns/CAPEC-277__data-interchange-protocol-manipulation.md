---
capec_id: CAPEC-277
name: Data Interchange Protocol Manipulation
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: n/a
related_cwe: [CWE-707]
related_attack: []
url: https://capec.mitre.org/data/definitions/277.html
tags: [mitre-capec, attack-pattern, CAPEC-277]
---

# CAPEC-277 - Data Interchange Protocol Manipulation

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-277](https://capec.mitre.org/data/definitions/277.html)

## Description
Data Interchange Protocols are used to transmit structured data between entities. These protocols are often specific to a particular domain (B2B: purchase orders, invoices, transport logistics and waybills, medical records). They are often, but not always, XML-based. Subverting the protocol can allow an adversary to impersonate others, discover sensitive information, control the outcome of a session, or perform other attacks. This type of attack targets invalid assumptions that may be inherent in implementers of the protocol, incorrect implementations of the protocol, or vulnerabilities in the protocol itself.

## Related weaknesses (CWE)
- [CWE-707](https://cwe.mitre.org/data/definitions/707.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/277.html
