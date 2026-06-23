---
capec_id: CAPEC-305
name: TCP ACK Scan
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/305.html
tags: [mitre-capec, attack-pattern, CAPEC-305]
---

# CAPEC-305 - TCP ACK Scan

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-305](https://capec.mitre.org/data/definitions/305.html)

## Description
An adversary uses TCP ACK segments to gather information about firewall or ACL configuration. The purpose of this type of scan is to discover information about filter configurations rather than port state. This type of scanning is rarely useful alone, but when combined with SYN scanning, gives a more complete picture of the type of firewall rules that are present.

## Extended description
When a TCP ACK segment is sent to a closed port, or sent out-of-sync to a listening port, the RFC 793 expected behavior is for the device to respond with a RST. Getting RSTs back in response to a ACK scan gives the attacker useful information that can be used to infer the type of firewall present. Stateful firewalls will discard out-of-sync ACK packets, leading to no response. When this occurs the port is marked as filtered. When RSTs are received in response, the ports are marked as unfiltered, as the ACK packets solicited the expected behavior from a port. When combined with SYN techniques an attacker can gain a more complete picture of which types of packets get through to a host and thereby map out its firewall rule-set. ACK scanning, when combined with SYN scanning, also allows the adversary to analyze whether a firewall is stateful or non-stateful (described in notes). TCP ACK Scans are somewhat faster and more stealthy than other types of scans but often requires rather sophisticated analysis by an experienced person. A skilled adversary may use this method to map out firewall rules, but the results of ACK scanning will be less useful to a novice.

## Prerequisites
- The adversary requires logical access to the target network. ACK scanning requires the use of raw sockets, and thus cannot be performed from some Windows systems (Windows XP SP 2, for example). On Unix and Linux, raw socket manipulations require root privileges.

## Resources required
- This attack can be achieved via the use of a network mapper or scanner, or via raw socket programming in a scripting language. Packet injection tools are also useful for this purpose. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- **Access_Control**: Bypass Protection Mechanism, Hide Activities
- **Authorization**: Bypass Protection Mechanism, Hide Activities
- **Confidentiality**: Other, Bypass Protection Mechanism, Hide Activities

## Execution flow
Execution Flow Experiment An adversary sends TCP packets with the ACK flag set and that are not associated with an existing connection to target ports. An adversary uses the response from the target to determine the port's state. If a RST packet is received the target port is either closed or the ACK was sent out-of-sync. If no response is received, the target is likely using a stateful firewall.

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/305.html
