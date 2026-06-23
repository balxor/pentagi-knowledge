---
capec_id: CAPEC-494
name: TCP Fragmentation
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: n/a
related_cwe: [CWE-770, CWE-404]
related_attack: []
url: https://capec.mitre.org/data/definitions/494.html
tags: [mitre-capec, attack-pattern, CAPEC-494]
---

# CAPEC-494 - TCP Fragmentation

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-494](https://capec.mitre.org/data/definitions/494.html)

## Description
An adversary may execute a TCP Fragmentation attack against a target with the intention of avoiding filtering rules of network controls, by attempting to fragment the TCP packet such that the headers flag field is pushed into the second fragment which typically is not filtered.

## Extended description
In comparison, IP fragmentation occurs when an IP datagram is larger than the MTU of the route the datagram has to traverse. This behavior of fragmentation defeats some IPS and firewall filters who typically check the FLAGS in the header of the first packet since dropping this packet prevents the following fragments from being processed and assembled. Another variation is overlapping fragments thus that an innocuous first segment passes the filter and the second segment overwrites the TCP header data with the true payload which is malicious in nature. The malicious payload manipulated properly may lead to a DoS due to resource consumption or kernel crash. Additionally the fragmentation could be used in conjunction with sending fragments at a rate slightly slower than the timeout to cause a DoS condition by forcing resources that assemble the packet to wait an inordinate amount of time to complete the task. The fragmentation identification numbers could also be duplicated very easily as there are only 16 bits in IPv4 so only 65536 packets are needed.

## Prerequisites
- This type of an attack requires the target system to be running a vulnerable implementation of IP, and the adversary needs to ability to send TCP packets of arbitrary size with crafted data.

## Mitigations
- This attack may be mitigated by enforcing rules at the router following the guidance of RFC1858. The essential part of the guidance is creating the following rule "IF FO=1 and PROTOCOL=TCP then DROP PACKET" as this mitigated both tiny fragment and overlapping fragment attacks in IPv4. In IPv6 overlapping(RFC5722) additional steps may be required such as deep packet inspection. The delayed fragments may be mitigated by enforcing a timeout on the transmission to receive all packets by a certain time since the first packet is received. According to RFC2460 IPv6 implementations should enforce a rule to discard all fragments if the fragments are not ALL received within 60 seconds of the FIRST arriving fragment.

## Related weaknesses (CWE)
- [CWE-770](https://cwe.mitre.org/data/definitions/770.html)
- [CWE-404](https://cwe.mitre.org/data/definitions/404.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/494.html
