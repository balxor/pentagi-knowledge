---
capec_id: CAPEC-495
name: UDP Fragmentation
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: n/a
related_cwe: [CWE-770, CWE-404]
related_attack: []
url: https://capec.mitre.org/data/definitions/495.html
tags: [mitre-capec, attack-pattern, CAPEC-495]
---

# CAPEC-495 - UDP Fragmentation

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-495](https://capec.mitre.org/data/definitions/495.html)

## Description
An attacker may execute a UDP Fragmentation attack against a target server in an attempt to consume resources such as bandwidth and CPU. IP fragmentation occurs when an IP datagram is larger than the MTU of the route the datagram has to traverse. Typically the attacker will use large UDP packets over 1500 bytes of data which forces fragmentation as ethernet MTU is 1500 bytes. This attack is a variation on a typical UDP flood but it enables more network bandwidth to be consumed with fewer packets. Additionally it has the potential to consume server CPU resources and fill memory buffers associated with the processing and reassembling of fragmented packets.

## Prerequisites
- This type of an attack requires the attacker to be able to generate fragmented IP traffic containing crafted data.

## Mitigations
- This attack may be mitigated by changing default cache sizes to be larger at the OS level. Additionally rules can be enforced to prune the cache with shorter timeouts for packet reassembly as the cache nears capacity.

## Related weaknesses (CWE)
- [CWE-770](https://cwe.mitre.org/data/definitions/770.html)
- [CWE-404](https://cwe.mitre.org/data/definitions/404.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/495.html
