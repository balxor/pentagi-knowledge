---
capec_id: CAPEC-589
name: DNS Blocking
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: [CWE-300]
related_attack: []
url: https://capec.mitre.org/data/definitions/589.html
tags: [mitre-capec, attack-pattern, CAPEC-589]
---

# CAPEC-589 - DNS Blocking

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-589](https://capec.mitre.org/data/definitions/589.html)

## Description
An adversary intercepts traffic and intentionally drops DNS requests based on content in the request. In this way, the adversary can deny the availability of specific services or content to the user even if the IP address is changed.

## Prerequisites
- This attack requires the ability to conduct deep packet inspection with an In-Path device that can drop the targeted traffic and/or connection.

## Consequences
- **Availability**: Other (Preventing DNS from resolving a request denies the availability of a target site or service for the user.)

## Mitigations
- Hard Coded Alternate DNS server in applications
- Avoid dependence on DNS
- Include "hosts file"/IP address in the application.
- Ensure best practices with respect to communications channel protections.
- Use a .onion domain with Tor support

## Related weaknesses (CWE)
- [CWE-300](https://cwe.mitre.org/data/definitions/300.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/589.html
