---
capec_id: CAPEC-290
name: Enumerate Mail Exchange (MX) Records
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/290.html
tags: [mitre-capec, attack-pattern, CAPEC-290]
---

# CAPEC-290 - Enumerate Mail Exchange (MX) Records

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-290](https://capec.mitre.org/data/definitions/290.html)

## Description
An adversary enumerates the MX records for a given via a DNS query. This type of information gathering returns the names of mail servers on the network. Mail servers are often not exposed to the Internet but are located within the DMZ of a network protected by a firewall. A side effect of this configuration is that enumerating the MX records for an organization my reveal the IP address of the firewall or possibly other internal systems. Attackers often resort to MX record enumeration when a DNS Zone Transfer is not possible.

## Prerequisites
- The adversary requires access to a DNS server that will return the MX records for a network.

## Resources required
- A command-line utility or other application capable of sending requests to the DNS server is necessary.

## Consequences
- **Access_Control**: Bypass Protection Mechanism, Hide Activities
- **Authorization**: Bypass Protection Mechanism, Hide Activities
- **Confidentiality**: Other, Bypass Protection Mechanism, Hide Activities

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/290.html
