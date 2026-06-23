---
capec_id: CAPEC-297
name: TCP ACK Ping
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/297.html
tags: [mitre-capec, attack-pattern, CAPEC-297]
---

# CAPEC-297 - TCP ACK Ping

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-297](https://capec.mitre.org/data/definitions/297.html)

## Description
An adversary sends a TCP segment with the ACK flag set to a remote host for the purpose of determining if the host is alive. This is one of several TCP 'ping' types. The RFC 793 expected behavior for a service is to respond with a RST 'reset' packet to any unsolicited ACK segment that is not part of an existing connection. So by sending an ACK segment to a port, the adversary can identify that the host is alive by looking for a RST packet. Typically, a remote server will respond with a RST regardless of whether a port is open or closed. In this way, TCP ACK pings cannot discover the state of a remote port because the behavior is the same in either case. The firewall will look up the ACK packet in its state-table and discard the segment because it does not correspond to any active connection. A TCP ACK Ping can be used to discover if a host is alive via RST response packets sent from the host.

## Prerequisites
- The ability to send an ACK packet to a remote host and identify the response. Creating the ACK packet without building a full connection requires the use of raw sockets. As a result, it is not possible to send a TCP ACK ping from some systems (Windows XP SP 2) without the use of third-party packet drivers like Winpcap. On other systems (BSD, Linux) administrative privileges are required in order to write to the raw socket.
- The target must employ a stateless firewall that lacks a rule set that rejects unsolicited ACK packets.
- The adversary requires the ability to craft custom TCP ACK segments for use during network reconnaissance. Sending an ACK ping requires the ability to access "raw sockets" in order to create the packets with direct access to the packet header.

## Resources required
- ACK scanning can be performed via the use of a port scanner or by raw socket manipulation using a scripting or programming language. Packet injection tools are also useful for this purpose. Depending upon the technique used it may also be necessary to sniff the network in order to see the response.

## Consequences
- **Access_Control**: Bypass Protection Mechanism, Hide Activities
- **Authorization**: Bypass Protection Mechanism, Hide Activities
- **Confidentiality**: Other, Bypass Protection Mechanism, Hide Activities

## Mitigations
- Leverage stateful firewalls that allow for the rejection of a packet that is not part of an existing connection.

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/297.html
