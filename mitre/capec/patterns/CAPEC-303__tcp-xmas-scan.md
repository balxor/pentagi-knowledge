---
capec_id: CAPEC-303
name: TCP Xmas Scan
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/303.html
tags: [mitre-capec, attack-pattern, CAPEC-303]
---

# CAPEC-303 - TCP Xmas Scan

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-303](https://capec.mitre.org/data/definitions/303.html)

## Description
An adversary uses a TCP XMAS scan to determine if ports are closed on the target machine. This scan type is accomplished by sending TCP segments with all possible flags set in the packet header, generating packets that are illegal based on RFC 793. The RFC 793 expected behavior is that any TCP segment with an out-of-state Flag sent to an open port is discarded, whereas segments with out-of-state flags sent to closed ports should be handled with a RST in response. This behavior should allow an attacker to scan for closed ports by sending certain types of rule-breaking packets (out of sync or disallowed by the TCB) and detect closed ports via RST packets.

## Extended description
In addition to its relative speed when compared with other types of scans, its major advantage is its ability to scan through stateless firewall or ACL filters. Such filters are configured to block access to ports usually by preventing SYN packets, thus stopping any attempt to 'build' a connection. XMAS packets, like out-of-state FIN or ACK packets, tend to pass through such devices undetected. Because open ports are inferred via no responses being generated, one cannot distinguish an open port from a filtered port without further analysis. For instance, XMAS scanning a system protected by a stateful firewall may indicate all ports being open. Because of their obvious rule-breaking nature, XMAS scans are flagged by almost all intrusion prevention or intrusion detection systems.

## Prerequisites
- The adversary needs logical access to the target network. XMAS scanning requires the use of raw sockets, and thus cannot be performed from some Windows systems (Windows XP SP 2, for example). On Unix and Linux, raw socket manipulations require root privileges.

## Resources required
- This attack can be carried out with a network mapper or scanner, or via raw socket programming in a scripting language. Packet injection tools are also useful for this purpose. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- **Access_Control**: Bypass Protection Mechanism, Hide Activities
- **Authorization**: Bypass Protection Mechanism, Hide Activities
- **Availability**: Unreliable Execution
- **Confidentiality**: Other, Bypass Protection Mechanism, Hide Activities

## Execution flow
Execution Flow Experiment An adversary sends TCP packets with all flags set but not associated with an existing connection to target ports. An adversary uses the response from the target to determine the port's state. If no response is received the port is open. If a RST packet is received then the port is closed.

## Mitigations
- Employ a robust network defensive posture that includes a managed IDS/IPS.

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/303.html
