---
capec_id: CAPEC-299
name: TCP SYN Ping
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/299.html
tags: [mitre-capec, attack-pattern, CAPEC-299]
---

# CAPEC-299 - TCP SYN Ping

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-299](https://capec.mitre.org/data/definitions/299.html)

## Description
An adversary uses TCP SYN packets as a means towards host discovery. Typical RFC 793 behavior specifies that when a TCP port is open, a host must respond to an incoming SYN "synchronize" packet by completing stage two of the 'three-way handshake' - by sending an SYN/ACK in response. When a port is closed, RFC 793 behavior is to respond with a RST "reset" packet. This behavior can be used to 'ping' a target to see if it is alive by sending a TCP SYN packet to a port and then looking for a RST or an ACK packet in response.

## Extended description
Due to the different responses from open and closed ports, SYN packets can be used to determine the remote state of the port. A TCP SYN ping is also useful for discovering alive hosts protected by a stateful firewall. In cases where a specific firewall rule does not block access to a port, a SYN packet can pass through the firewall to the host and solicit a response from either an open or closed port. When a stateful firewall is present, SYN pings are preferable to ACK pings because a stateful firewall will typically drop all unsolicited ACK packets as they are not part of an existing or new connection. TCP SYN pings often fail when a stateless ACL or firewall is configured to blanket-filter incoming packets to a port. The firewall device will discard any SYN packets to a blocked port. Often, an adversary will alternate between SYN and ACK pings to discover if a host is alive.

## Prerequisites
- The ability to send a TCP SYN packet to a remote target. Depending upon the operating system, the ability to craft SYN packets may require elevated privileges.

## Skills required
- **Low**: The adversary needs to know how to craft and send protocol commands from the command line or within a tool.

## Resources required
- SYN pings can be performed via the use of a port scanner or by raw socket manipulation using a scripting or programming language. Packet injection tools are also useful for this purpose. Depending upon the technique used it may also be necessary to sniff the network in order to see the response.

## Consequences
- **Access_Control**: Bypass Protection Mechanism, Hide Activities
- **Authorization**: Bypass Protection Mechanism, Hide Activities
- **Confidentiality**: Other, Bypass Protection Mechanism, Hide Activities

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/299.html
