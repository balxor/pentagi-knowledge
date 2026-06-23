---
capec_id: CAPEC-496
name: ICMP Fragmentation
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: n/a
related_cwe: [CWE-770, CWE-404]
related_attack: []
url: https://capec.mitre.org/data/definitions/496.html
tags: [mitre-capec, attack-pattern, CAPEC-496]
---

# CAPEC-496 - ICMP Fragmentation

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-496](https://capec.mitre.org/data/definitions/496.html)

## Description
An attacker may execute a ICMP Fragmentation attack against a target with the intention of consuming resources or causing a crash. The attacker crafts a large number of identical fragmented IP packets containing a portion of a fragmented ICMP message. The attacker these sends these messages to a target host which causes the host to become non-responsive. Another vector may be sending a fragmented ICMP message to a target host with incorrect sizes in the header which causes the host to hang.

## Prerequisites
- This type of an attack requires the target system to be running a vulnerable implementation of IP, and the attacker needs to ability to send arbitrary sized ICMP packets to the target.

## Mitigations
- This attack may be mitigated through egress filtering based on ICMP payload so a network is a "good neighbor" to other networks. Bad IP implementations become patched, so using the proper version of a browser or OS is recommended.

## Related weaknesses (CWE)
- [CWE-770](https://cwe.mitre.org/data/definitions/770.html)
- [CWE-404](https://cwe.mitre.org/data/definitions/404.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/496.html
