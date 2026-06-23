---
capec_id: CAPEC-332
name: ICMP IP 'ID' Field Error Message Probe
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Low
related_cwe: [CWE-204]
related_attack: []
url: https://capec.mitre.org/data/definitions/332.html
tags: [mitre-capec, attack-pattern, CAPEC-332]
---

# CAPEC-332 - ICMP IP 'ID' Field Error Message Probe

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Low  -  **CAPEC:** [CAPEC-332](https://capec.mitre.org/data/definitions/332.html)

## Description
An adversary sends a UDP datagram having an assigned value to its internet identification field (ID) to a closed port on a target to observe the manner in which this bit is echoed back in the ICMP error message. This allows the attacker to construct a fingerprint of specific OS behaviors.

## Extended description
The internet identification field (ID) is typically utilized for reassembling a fragmented packet. RFC791 and RFC815 discusses about IP datagrams, fragmentation and reassembly. Some operating systems or router firmware reverse the bit order of the ID field when echoing the IP Header portion of the original datagram within the ICMP error message. There are three behaviors related to the IP ID field that can be used to distinguish remote operating systems or firmware: 1) it is echoed back identically to the bit order of the ID field in the original IP header, 2) it is echoed back, but the byte order has been reversed, or it contains an incorrect or unexpected value. Different operating systems will respond by setting the IP ID field differently within error messaging.

## Prerequisites
- The ability to monitor and interact with network communications. Access to at least one host, and the privileges to interface with the network interface card.

## Resources required
- A tool capable of sending/receiving UDP datagram packets from a remote system to a closed port and receive an ICMP Error Message Type 3, "Port Unreachable."

## Consequences
- **Access_Control**: Bypass Protection Mechanism, Hide Activities
- **Authorization**: Bypass Protection Mechanism, Hide Activities
- **Confidentiality**: Read Data, Bypass Protection Mechanism, Hide Activities

## Related weaknesses (CWE)
- [CWE-204](https://cwe.mitre.org/data/definitions/204.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/332.html
