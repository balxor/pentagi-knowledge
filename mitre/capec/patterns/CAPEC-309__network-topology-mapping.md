---
capec_id: CAPEC-309
name: Network Topology Mapping
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Low
related_cwe: [CWE-200]
related_attack: [T1016, T1049, T1590]
url: https://capec.mitre.org/data/definitions/309.html
tags: [mitre-capec, attack-pattern, CAPEC-309]
---

# CAPEC-309 - Network Topology Mapping

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-309](https://capec.mitre.org/data/definitions/309.html)

## Description
An adversary engages in scanning activities to map network nodes, hosts, devices, and routes. Adversaries usually perform this type of network reconnaissance during the early stages of attack against an external network. Many types of scanning utilities are typically employed, including ICMP tools, network mappers, port scanners, and route testing utilities such as traceroute.

## Prerequisites
- None

## Resources required
- Probing requires the ability to interactively send and receive data from a target, whereas passive listening requires a sufficient understanding of the protocol to analyze a preexisting channel of communication.

## Consequences
- **Confidentiality**: Other

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

## Related ATT&CK techniques
- T1016
- T1049
- T1590

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/309.html
