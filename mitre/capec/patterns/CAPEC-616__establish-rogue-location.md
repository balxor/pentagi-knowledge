---
capec_id: CAPEC-616
name: Establish Rogue Location
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: Medium
related_cwe: [CWE-200]
related_attack: [T1036.005]
url: https://capec.mitre.org/data/definitions/616.html
tags: [mitre-capec, attack-pattern, CAPEC-616]
---

# CAPEC-616 - Establish Rogue Location

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-616](https://capec.mitre.org/data/definitions/616.html)

## Description
An adversary provides a malicious version of a resource at a location that is similar to the expected location of a legitimate resource. After establishing the rogue location, the adversary waits for a victim to visit the location and access the malicious resource.

## Prerequisites
- A resource is expected to available to the user.

## Skills required
- **Low**: Adversaries can often purchase low-cost technology to implement rogue access points.

## Consequences
- **Confidentiality**: Other (Successful attacks of this nature can result in a wide variety of consequences and negatively impact confidentiality and integrity based on the adversary's subsequent actions.)
- **Integrity**: Other (Successful attacks of this nature can result in a wide variety of consequences and negatively impact confidentiality and integrity based on the adversary's subsequent actions.)

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

## Related ATT&CK techniques
- T1036.005

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/616.html
