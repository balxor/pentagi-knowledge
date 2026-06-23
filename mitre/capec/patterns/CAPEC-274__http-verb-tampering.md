---
capec_id: CAPEC-274
name: HTTP Verb Tampering
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-302, CWE-654]
related_attack: []
url: https://capec.mitre.org/data/definitions/274.html
tags: [mitre-capec, attack-pattern, CAPEC-274]
---

# CAPEC-274 - HTTP Verb Tampering

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-274](https://capec.mitre.org/data/definitions/274.html)

## Description
An attacker modifies the HTTP Verb (e.g. GET, PUT, TRACE, etc.) in order to bypass access restrictions. Some web environments allow administrators to restrict access based on the HTTP Verb used with requests. However, attackers can often provide a different HTTP Verb, or even provide a random string as a verb in order to bypass these protections. This allows the attacker to access data that should otherwise be protected.

## Prerequisites
- The targeted system must attempt to filter access based on the HTTP verb used in requests.

## Resources required
- The attacker requires a tool that allows them to manually control the HTTP verb used to send messages to the targeted server.

## Mitigations
- Design: Ensure that only legitimate HTTP verbs are allowed.
- Design: Do not use HTTP verbs as factors in access decisions.

## Related weaknesses (CWE)
- [CWE-302](https://cwe.mitre.org/data/definitions/302.html)
- [CWE-654](https://cwe.mitre.org/data/definitions/654.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/274.html
