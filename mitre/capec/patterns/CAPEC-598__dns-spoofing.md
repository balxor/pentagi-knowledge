---
capec_id: CAPEC-598
name: DNS Spoofing
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/598.html
tags: [mitre-capec, attack-pattern, CAPEC-598]
---

# CAPEC-598 - DNS Spoofing

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-598](https://capec.mitre.org/data/definitions/598.html)

## Description
An adversary sends a malicious ("NXDOMAIN" ("No such domain") code, or DNS A record) response to a target's route request before a legitimate resolver can. This technique requires an On-path or In-path device that can monitor and respond to the target's DNS requests. This attack differs from BGP Tampering in that it directly responds to requests made by the target instead of polluting the routing the target's infrastructure uses.

## Prerequisites
- On/In Path Device

## Skills required
- **Low**: To distribute email

## Mitigations
- Design: Avoid dependence on DNS
- Design: Include "hosts file"/IP address in the application
- Implementation: Utilize a .onion domain with Tor support
- Implementation: DNSSEC
- Implementation: DNS-hold-open

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/598.html
