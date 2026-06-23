---
capec_id: CAPEC-287
name: TCP SYN Scan
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/287.html
tags: [mitre-capec, attack-pattern, CAPEC-287]
---

# CAPEC-287 - TCP SYN Scan

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-287](https://capec.mitre.org/data/definitions/287.html)

## Description
An adversary uses a SYN scan to determine the status of ports on the remote target. SYN scanning is the most common type of port scanning that is used because of its many advantages and few drawbacks. As a result, novice attackers tend to overly rely on the SYN scan while performing system reconnaissance. As a scanning method, the primary advantages of SYN scanning are its universality and speed.

## Extended description
RFC 793 defines the required behavior of any TCP/IP device in that an incoming connection request begins with a SYN packet, which in turn must be followed by a SYN/ACK packet from the receiving service. For this reason, like TCP Connect scanning, SYN scanning works against any TCP stack. Unlike TCP Connect scanning, it is possible to scan thousands of ports per second using this method. This type of scanning is usually referred to as 'half-open' scanning because it does not complete the three-way handshake. The scanning rate is extremely fast because no time is wasted completing the handshake or tearing down the connection. This technique allows an attacker to scan through stateful firewalls due to the common configuration that TCP SYN segments for a new connection will be allowed for almost any port. TCP SYN scanning can also immediately detect 3 of the 4 important types of port status: open, closed, and filtered.

## Prerequisites
- This scan type is not possible with some operating systems (Windows XP SP 2). On Linux and Unix systems it requires root privileges to use raw sockets.

## Resources required
- The ability to send TCP SYN segments to a host during network reconnaissance via the use of a network mapper or scanner, or via raw socket programming in a scripting language. Packet injection tools are also useful for this purpose. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- **Access_Control**: Bypass Protection Mechanism, Hide Activities
- **Authorization**: Bypass Protection Mechanism, Hide Activities
- **Confidentiality**: Other (A successful attack of this kind can identify open ports and available services on a system.), Bypass Protection Mechanism, Hide Activities

## Execution flow
Execution Flow Experiment An adversary sends SYN packets to ports they want to scan and checks the response without completing the TCP handshake. An adversary uses the response from the target to determine the port's state. The adversary can determine the state of a port based on the following responses. When a SYN is sent to an open port and unfiltered port, a SYN/ACK will be generated. When a SYN packet is sent to a closed port a RST is generated, indicating the port is closed. When SYN scanning to a particular port generates no response, or when the request triggers ICMP Type 3 unreachable errors, the port is filtered.

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/287.html
