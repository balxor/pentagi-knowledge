---
capec_id: CAPEC-227
name: Sustained Client Engagement
type: attack-pattern
abstraction: Meta
likelihood: n/a
severity: n/a
related_cwe: [CWE-400]
related_attack: [T1499]
url: https://capec.mitre.org/data/definitions/227.html
tags: [mitre-capec, attack-pattern, CAPEC-227]
---

# CAPEC-227 - Sustained Client Engagement

**Abstraction:** Meta  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-227](https://capec.mitre.org/data/definitions/227.html)

## Description
An adversary attempts to deny legitimate users access to a resource by continually engaging a specific resource in an attempt to keep the resource tied up as long as possible. The adversary's primary goal is not to crash or flood the target, which would alert defenders; rather it is to repeatedly perform actions or abuse algorithmic flaws such that a given resource is tied up and not available to a legitimate user. By carefully crafting a requests that keep the resource engaged through what is seemingly benign requests, legitimate users are limited or completely denied access to the resource.

## Extended description
The degree to which the attack is successful depends upon the adversary's ability to sustain resource requests over time with a volume that exceeds the normal usage by legitimate users, as well as other mitigating circumstances such as the target's ability to shift load or acquire additional resources to deal with the depletion. This attack differs from a flooding attack as it is not entirely dependent upon large volumes of requests, and it differs from resource leak exposures which tend to exploit the surrounding environment needed for the resource to function. The key factor in a sustainment attack are the repeated requests that take longer to process than usual.

## Prerequisites
- This pattern of attack requires a temporal aspect to the servicing of a given request. Success can be achieved if the adversary can make requests that collectively take more time to complete than legitimate user requests within the same time frame.

## Resources required
- To successfully execute this pattern of attack, a script or program is often required that is capable of continually engaging the target and maintaining sustained usage of a specific resource. Depending on the configuration of the target, it may or may not be necessary to involve a network or cluster of objects all capable of making parallel requests.

## Mitigations
- Potential mitigations include requiring a unique login for each resource request, constraining local unprivileged access by disallowing simultaneous engagements of the resource, or limiting access to the resource to one access per IP address. In such scenarios, the adversary would have to increase engagements either by launching multiple sessions manually or programmatically to counter such defenses.

## Related weaknesses (CWE)
- [CWE-400](https://cwe.mitre.org/data/definitions/400.html)

## Related ATT&CK techniques
- T1499

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/227.html
