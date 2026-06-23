---
capec_id: CAPEC-294
name: ICMP Address Mask Request
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/294.html
tags: [mitre-capec, attack-pattern, CAPEC-294]
---

# CAPEC-294 - ICMP Address Mask Request

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-294](https://capec.mitre.org/data/definitions/294.html)

## Description
An adversary sends an ICMP Type 17 Address Mask Request to gather information about a target's networking configuration. ICMP Address Mask Requests are defined by RFC-950, "Internet Standard Subnetting Procedure." An Address Mask Request is an ICMP type 17 message that triggers a remote system to respond with a list of its related subnets, as well as its default gateway and broadcast address via an ICMP type 18 Address Mask Reply datagram. Gathering this type of information helps the adversary plan router-based attacks as well as denial-of-service attacks against the broadcast address.

## Extended description
Many modern operating systems will not respond to ICMP type 17 messages for security reasons. Determining whether a system or router will respond to an ICMP Address Mask Request helps the adversary determine operating system or firmware version. Additionally, because these types of messages are rare, they are easily spotted by intrusion detection systems. Many ICMP scanning tools support IP spoofing to help conceal the origin of the actual request among a storm of similar ICMP messages. It is a common practice for border firewalls and gateways to be configured to block ingress ICMP type 17 and egress ICMP type 18 messages.

## Prerequisites
- The ability to send an ICMP type 17 query (Address Mask Request) to a remote target and receive an ICMP type 18 message (ICMP Address Mask Reply) in response. Generally, modern operating systems will ignore ICMP type 17 messages, however, routers will commonly respond to this request.

## Resources required
- The ability to send custom ICMP queries. This can be accomplished via the use of various scanners or utilities.

## Consequences
- **Access_Control**: Hide Activities
- **Authorization**: Hide Activities
- **Confidentiality**: Other, Hide Activities

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/294.html
