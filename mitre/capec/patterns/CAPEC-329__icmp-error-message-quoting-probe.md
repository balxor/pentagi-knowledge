---
capec_id: CAPEC-329
name: ICMP Error Message Quoting Probe
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/329.html
tags: [mitre-capec, attack-pattern, CAPEC-329]
---

# CAPEC-329 - ICMP Error Message Quoting Probe

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Low  -  **CAPEC:** [CAPEC-329](https://capec.mitre.org/data/definitions/329.html)

## Description
An adversary uses a technique to generate an ICMP Error message (Port Unreachable, Destination Unreachable, Redirect, Source Quench, Time Exceeded, Parameter Problem) from a target and then analyze the amount of data returned or "Quoted" from the originating request that generated the ICMP error message.

## Extended description
For this purpose "Port Unreachable" error messages are often used, as generating them requires the adversary to send a UDP datagram to a closed port on the target. The goal of this analysis to make inferences about the type of operating system or firmware that sent the error message in reply. This is useful for identifying unique characteristics of operating systems because the RFC-1122 expected behavior reads: "Every ICMP error message includes the Internet header and at least the first 8 data octets of the datagram that triggered the error; more than 8 octets MAY be sent [...]." This contrasts with RFC-792 expected behavior, which limited the quoted text to 64 bits (8 octets). Given the latitude in the specification the resulting RFC-1122 stack implementations often respond with a high degree of variability in the amount of data quoted in the error message because "older" or "legacy" stacks may comply with the RFC-792 specification, while other stacks may choose a longer format in accordance with RFC-1122. As a general rule most operating systems or firmware will quote the first 8 bytes of the datagram triggering the error, but some IP stacks will quote more than the first 8 bytes of data.

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

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/329.html
