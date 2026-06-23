---
capec_id: CAPEC-300
name: Port Scanning
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Low
related_cwe: [CWE-200]
related_attack: [T1046]
url: https://capec.mitre.org/data/definitions/300.html
tags: [mitre-capec, attack-pattern, CAPEC-300]
---

# CAPEC-300 - Port Scanning

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-300](https://capec.mitre.org/data/definitions/300.html)

## Description
An adversary uses a combination of techniques to determine the state of the ports on a remote target. Any service or application available for TCP or UDP networking will have a port open for communications over the network.

## Extended description
Although common services have assigned port numbers, services and applications can run on arbitrary ports. Additionally, port scanning is complicated by the potential for any machine to have up to 65535 possible UDP or TCP services. The goal of port scanning is often broader than identifying open ports, but also give the adversary information concerning the firewall configuration. Depending upon the method of scanning that is used, the process can be stealthy or more obtrusive, the latter being more easily detectable due to the volume of packets involved, anomalous packet traits, or system logging. Typical port scanning activity involves sending probes to a range of ports and observing the responses. There are four port statuses that this type of attack aims to identify: open, closed, filtered, and unfiltered. For strategic purposes it is useful for an adversary to distinguish between an open port that is protected by a filter vs. a closed port that is not protected by a filter. Making these fine grained distinctions is requires certain scan types. Collecting this type of information tells the adversary which ports can be attacked directly, which must be attacked with filter evasion techniques like fragmentation, source port scans, and which ports are unprotected (i.e. not firewalled) but aren't hosting a network service. An adversary often combines various techniques in order to gain a more complete picture of the firewall filtering mechanisms in place for a host.

## Prerequisites
- The adversary requires logical access to the target's network in order to carry out this type of attack.

## Resources required
- The adversary requires a network mapping/scanning tool, or must conduct socket programming on the command line. Packet injection tools are also useful for this purpose. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- **Access_Control**: Bypass Protection Mechanism, Hide Activities
- **Authorization**: Bypass Protection Mechanism, Hide Activities
- **Confidentiality**: Other, Bypass Protection Mechanism, Hide Activities

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

## Related ATT&CK techniques
- T1046

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/300.html
