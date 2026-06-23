---
capec_id: CAPEC-292
name: Host Discovery
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Low
related_cwe: [CWE-200]
related_attack: [T1018]
url: https://capec.mitre.org/data/definitions/292.html
tags: [mitre-capec, attack-pattern, CAPEC-292]
---

# CAPEC-292 - Host Discovery

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-292](https://capec.mitre.org/data/definitions/292.html)

## Description
An adversary sends a probe to an IP address to determine if the host is alive. Host discovery is one of the earliest phases of network reconnaissance. The adversary usually starts with a range of IP addresses belonging to a target network and uses various methods to determine if a host is present at that IP address. Host discovery is usually referred to as 'Ping' scanning using a sonar analogy. The goal is to send a packet through to the IP address and solicit a response from the host. As such, a 'ping' can be virtually any crafted packet whatsoever, provided the adversary can identify a functional host based on its response. An attack of this nature is usually carried out with a 'ping sweep,' where a particular kind of ping is sent to a range of IP addresses.

## Prerequisites
- The adversary requires logical access to the target network in order to carry out host discovery.

## Resources required
- The resources required will differ based upon the type of host discovery being performed. Usually a network scanning tool or scanning script is required due to the volume of requests that must be generated.

## Consequences
- **Access_Control**: Bypass Protection Mechanism, Hide Activities
- **Authorization**: Bypass Protection Mechanism, Hide Activities
- **Confidentiality**: Other, Bypass Protection Mechanism, Hide Activities

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

## Related ATT&CK techniques
- T1018

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/292.html
