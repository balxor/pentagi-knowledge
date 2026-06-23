---
capec_id: CAPEC-291
name: DNS Zone Transfers
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/291.html
tags: [mitre-capec, attack-pattern, CAPEC-291]
---

# CAPEC-291 - DNS Zone Transfers

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-291](https://capec.mitre.org/data/definitions/291.html)

## Description
An attacker exploits a DNS misconfiguration that permits a ZONE transfer. Some external DNS servers will return a list of IP address and valid hostnames. Under certain conditions, it may even be possible to obtain Zone data about the organization's internal network. When successful the attacker learns valuable information about the topology of the target organization, including information about particular servers, their role within the IT structure, and possibly information about the operating systems running upon the network. This is configuration dependent behavior so it may also be required to search out multiple DNS servers while attempting to find one with ZONE transfers allowed.

## Prerequisites
- Access to a DNS server that allows Zone transfers.

## Resources required
- A client application capable of interacting with the DNS server or a command-line utility or web application that automates DNS interactions.

## Consequences
- **Confidentiality**: Read Data

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/291.html
