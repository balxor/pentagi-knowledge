---
capec_id: CAPEC-330
name: ICMP Error Message Echoing Integrity Probe
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/330.html
tags: [mitre-capec, attack-pattern, CAPEC-330]
---

# CAPEC-330 - ICMP Error Message Echoing Integrity Probe

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Low  -  **CAPEC:** [CAPEC-330](https://capec.mitre.org/data/definitions/330.html)

## Description
An adversary uses a technique to generate an ICMP Error message (Port Unreachable, Destination Unreachable, Redirect, Source Quench, Time Exceeded, Parameter Problem) from a target and then analyze the integrity of data returned or "Quoted" from the originating request that generated the error message.

## Extended description
A tremendous amount of information about the host operating system can be deduced from its 'echoing' characteristics. Notably, inspection of key protocol header fields, including the echoed header fields of the encapsulating protocol can yield a wealth of data about the host operating system or firmware version. For this purpose "Port Unreachable" error messages are often used, as generating them requires the adversary to send a UDP datagram to a closed port on the target. When replying with an ICMP error message some IP/ICMP stack implementations change aspects of the IP header, change or reverse certain byte orders, reset certain field values to default values which differ between operating system and firmware implementations, and make other changes. Some IP/ICMP stacks are decidedly broken, indicating an idiosyncratic behavior that differs from the RFC specifications, such as the case when miscalculations affect a field value.

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources required
- A tool capable of sending/receiving UDP datagram packets from a remote system to a closed port and receive an ICMP Error Message Type 3, "Port Unreachable..

## Consequences
- **Access_Control**: Bypass Protection Mechanism, Hide Activities
- **Authorization**: Bypass Protection Mechanism, Hide Activities
- **Confidentiality**: Read Data, Bypass Protection Mechanism, Hide Activities

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/330.html
