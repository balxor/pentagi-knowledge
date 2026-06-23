---
capec_id: CAPEC-285
name: ICMP Echo Request Ping
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/285.html
tags: [mitre-capec, attack-pattern, CAPEC-285]
---

# CAPEC-285 - ICMP Echo Request Ping

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Low  -  **CAPEC:** [CAPEC-285](https://capec.mitre.org/data/definitions/285.html)

## Description
An adversary sends out an ICMP Type 8 Echo Request, commonly known as a 'Ping', in order to determine if a target system is responsive. If the request is not blocked by a firewall or ACL, the target host will respond with an ICMP Type 0 Echo Reply datagram. This type of exchange is usually referred to as a 'Ping' due to the Ping utility present in almost all operating systems. Ping, as commonly implemented, allows a user to test for alive hosts, measure round-trip time, and measure the percentage of packet loss.

## Extended description
Performing this operation for a range of hosts on the network is known as a 'Ping Sweep'. While the Ping utility is useful for small-scale host discovery, it was not designed for rapid or efficient host discovery over large network blocks. Other scanning utilities have been created that make ICMP ping sweeps easier to perform. Most networks filter ingress ICMP Type 8 messages for security reasons. Various other methods of performing ping sweeps have developed as a result. It is important to recognize the key security goal of the adversary is to discover if an IP address is alive, or has a responsive host. To this end, virtually any type of ICMP message, as defined by RFC 792 is useful. An adversary can cycle through various types of ICMP messages to determine if holes exist in the firewall configuration. When ICMP ping sweeps fail to discover hosts, other protocols can be used for the same purpose, such as TCP SYN or ACK segments, UDP datagrams sent to closed ports, etc.

## Prerequisites
- The ability to send an ICMP type 8 query (Echo Request) to a remote target and receive an ICMP type 0 message (ICMP Echo Reply) in response. Any firewalls or access control lists between the sender and receiver must allow ICMP Type 8 and ICMP Type 0 messages in order for a ping operation to succeed.

## Skills required
- **Low**: The adversary needs to know certain linux commands for this type of attack.

## Resources required
- Scanners or utilities that provide the ability to send custom ICMP queries.

## Consequences
- **Confidentiality**: Other (A successful attack of this kind can identify open ports and available services on a system.)

## Mitigations
- Consider configuring firewall rules to block ICMP Echo requests and prevent replies. If not practical, monitor and consider action when a system has fast and a repeated pattern of requests that move incrementally through port numbers.

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/285.html
