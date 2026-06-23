---
capec_id: CAPEC-308
name: UDP Scan
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/308.html
tags: [mitre-capec, attack-pattern, CAPEC-308]
---

# CAPEC-308 - UDP Scan

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-308](https://capec.mitre.org/data/definitions/308.html)

## Description
An adversary engages in UDP scanning to gather information about UDP port status on the target system. UDP scanning methods involve sending a UDP datagram to the target port and looking for evidence that the port is closed. Open UDP ports usually do not respond to UDP datagrams as there is no stateful mechanism within the protocol that requires building or establishing a session. Responses to UDP datagrams are therefore application specific and cannot be relied upon as a method of detecting an open port. UDP scanning relies heavily upon ICMP diagnostic messages in order to determine the status of a remote port.

## Extended description
During a UDP scan, a datagram is sent to a target port. If an 'ICMP Type 3 Port unreachable' error message is returned then the port is considered closed. Different types of ICMP messages can indicate a filtered port. UDP scanning is slower than TCP scanning. The protocol characteristics of UDP make port scanning inherently more difficult than with TCP, as well as dependent upon ICMP for accurate scanning. Due to ambiguities that can arise between open ports and filtered ports, UDP scanning results often require a high degree of interpretation and further testing to refine. In general, UDP scanning results are less reliable or accurate than TCP-based scanning.

## Prerequisites
- The ability to send UDP datagrams to a host and receive ICMP error messages from that host. In cases where particular types of ICMP messaging is disallowed, the reliability of UDP scanning drops off sharply.

## Resources required
- The ability to craft custom UDP Packets for use during network reconnaissance. This can be accomplished via the use of a port scanner, or via socket manipulation in a programming or scripting language. Packet injection tools are also useful. It is also necessary to trap ICMP diagnostic messages during this process. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- **Access_Control**: Bypass Protection Mechanism, Hide Activities
- **Authorization**: Bypass Protection Mechanism, Hide Activities
- **Confidentiality**: Other, Bypass Protection Mechanism, Hide Activities

## Execution flow
Execution Flow Experiment An adversary sends UDP packets to target ports. An adversary uses the response from the target to determine the port's state. Whether a port responds to a UDP packet is dependant on what application is listening on that port. No response does not indicate the port is not open.

## Mitigations
- Firewalls or ACLs which block egress ICMP error types effectively prevent UDP scans from returning any useful information.
- UDP scanning is complicated by rate limiting mechanisms governing ICMP error messages.

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/308.html
