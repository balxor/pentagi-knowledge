---
capec_id: CAPEC-331
name: ICMP IP Total Length Field Probe
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Low
related_cwe: [CWE-204]
related_attack: []
url: https://capec.mitre.org/data/definitions/331.html
tags: [mitre-capec, attack-pattern, CAPEC-331]
---

# CAPEC-331 - ICMP IP Total Length Field Probe

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Low  -  **CAPEC:** [CAPEC-331](https://capec.mitre.org/data/definitions/331.html)

## Description
An adversary sends a UDP packet to a closed port on the target machine to solicit an IP Header's total length field value within the echoed 'Port Unreachable" error message. This type of behavior is useful for building a signature-base of operating system responses, particularly when error messages contain other types of information that is useful identifying specific operating system responses.

## Extended description
RFC1122 specifies that the Header of the request must be echoed back when an error is sent in response, but some operating systems and firmware alter the integrity of the original header. Non-standard ICMP/IP implementations result in response that are useful for individuating remote operating system or router firmware versions. There are four general response types that can be used to distinguish operating systems apart: 1) the IP total length field may be calculated correctly, 2) an operating system may add 20 or more additional bytes to the length calculation, 3) the operating system may subtract 20 or more bytes from the correct length of the field or 4) the IP total length field is calculated with any other incorrect value.

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

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/331.html
