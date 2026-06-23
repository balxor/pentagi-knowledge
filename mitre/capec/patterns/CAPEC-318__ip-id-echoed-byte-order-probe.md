---
capec_id: CAPEC-318
name: IP 'ID' Echoed Byte-Order Probe
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/318.html
tags: [mitre-capec, attack-pattern, CAPEC-318]
---

# CAPEC-318 - IP 'ID' Echoed Byte-Order Probe

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Low  -  **CAPEC:** [CAPEC-318](https://capec.mitre.org/data/definitions/318.html)

## Description
This OS fingerprinting probe tests to determine if the remote host echoes back the IP 'ID' value from the probe packet. An attacker sends a UDP datagram with an arbitrary IP 'ID' value to a closed port on the remote host to observe the manner in which this bit is echoed back in the ICMP error message. The identification field (ID) is typically utilized for reassembling a fragmented packet. Some operating systems or router firmware reverse the bit order of the ID field when echoing the IP Header portion of the original datagram within an ICMP error message.

## Consequences
- **Access_Control**: Bypass Protection Mechanism, Hide Activities
- **Authorization**: Bypass Protection Mechanism, Hide Activities
- **Confidentiality**: Read Data, Bypass Protection Mechanism, Hide Activities

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/318.html
