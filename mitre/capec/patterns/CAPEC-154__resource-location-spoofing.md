---
capec_id: CAPEC-154
name: Resource Location Spoofing
type: attack-pattern
abstraction: Meta
likelihood: Medium
severity: Medium
related_cwe: [CWE-451]
related_attack: []
url: https://capec.mitre.org/data/definitions/154.html
tags: [mitre-capec, attack-pattern, CAPEC-154]
---

# CAPEC-154 - Resource Location Spoofing

**Abstraction:** Meta  -  **Likelihood:** Medium  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-154](https://capec.mitre.org/data/definitions/154.html)

## Description
An adversary deceives an application or user and convinces them to request a resource from an unintended location. By spoofing the location, the adversary can cause an alternate resource to be used, often one that the adversary controls and can be used to help them achieve their malicious goals.

## Prerequisites
- None. All applications rely on file paths and therefore, in theory, they or their resources could be affected by this type of attack.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Authorization**: Execute Unauthorized Commands (Run Arbitrary Code)

## Mitigations
- Monitor network activity to detect any anomalous or unauthorized communication exchanges.

## Related weaknesses (CWE)
- [CWE-451](https://cwe.mitre.org/data/definitions/451.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/154.html
