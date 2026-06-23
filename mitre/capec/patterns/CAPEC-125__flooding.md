---
capec_id: CAPEC-125
name: Flooding
type: attack-pattern
abstraction: Meta
likelihood: High
severity: Medium
related_cwe: [CWE-404, CWE-770]
related_attack: [T1498.001, T1499]
url: https://capec.mitre.org/data/definitions/125.html
tags: [mitre-capec, attack-pattern, CAPEC-125]
---

# CAPEC-125 - Flooding

**Abstraction:** Meta  -  **Likelihood:** High  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-125](https://capec.mitre.org/data/definitions/125.html)

## Description
An adversary consumes the resources of a target by rapidly engaging in a large number of interactions with the target. This type of attack generally exposes a weakness in rate limiting or flow. When successful this attack prevents legitimate users from accessing the service and can cause the target to crash. This attack differs from resource depletion through leaks or allocations in that the latter attacks do not rely on the volume of requests made to the target but instead focus on manipulation of the target's operations. The key factor in a flooding attack is the number of requests the adversary can make in a given period of time. The greater this number, the more likely an attack is to succeed against a given target.

## Prerequisites
- Any target that services requests is vulnerable to this attack on some level of scale.

## Resources required
- A script or program capable of generating more requests than the target can handle, or a network or cluster of objects all capable of making simultaneous requests.

## Consequences
- **Availability**: Unreliable Execution (A successful flooding attack compromises the availability of the target system's service by exhausting its available resources.), Resource Consumption (A successful flooding attack compromises the availability of the target system's service by exhausting its available resources.)

## Mitigations
- Ensure that protocols have specific limits of scale configured.
- Specify expectations for capabilities and dictate which behaviors are acceptable when resource allocation reaches limits.
- Uniformly throttle all requests in order to make it more difficult to consume resources more quickly than they can again be freed.

## Related weaknesses (CWE)
- [CWE-404](https://cwe.mitre.org/data/definitions/404.html)
- [CWE-770](https://cwe.mitre.org/data/definitions/770.html)

## Related ATT&CK techniques
- T1498.001
- T1499

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/125.html
