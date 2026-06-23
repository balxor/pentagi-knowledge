---
capec_id: CAPEC-584
name: BGP Route Disabling
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/584.html
tags: [mitre-capec, attack-pattern, CAPEC-584]
---

# CAPEC-584 - BGP Route Disabling

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-584](https://capec.mitre.org/data/definitions/584.html)

## Description
An adversary suppresses the Border Gateway Protocol (BGP) advertisement for a route so as to render the underlying network inaccessible. The BGP protocol helps traffic move throughout the Internet by selecting the most efficient route between Autonomous Systems (AS), or routing domains. BGP is the basis for interdomain routing infrastructure, providing connections between these ASs. By suppressing the intended AS routing advertisements and/or forcing less effective routes for traffic to ASs, the adversary can deny availability for the target network.

## Prerequisites
- The adversary must have control of a router that can modify, drop, or introduce spoofed BGP updates.The adversary can convince

## Resources required
- BGP Router

## Consequences
- **Availability**: Other (Disabling a network route at the routing infrastructure level denies availability of that route.)

## Mitigations
- Implement Ingress filters to check the validity of received routes. However, this relies on the accuracy of Internet Routing Registries (IRRs) databases which are often not well-maintained.
- Implement Secure BGP (S-BGP protocol), which improves authorization and authentication capabilities based on public-key cryptography.

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/584.html
