---
capec_id: CAPEC-546
name: Incomplete Data Deletion in a Multi-Tenant Environment
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: Medium
related_cwe: [CWE-284, CWE-1266, CWE-1272]
related_attack: []
url: https://capec.mitre.org/data/definitions/546.html
tags: [mitre-capec, attack-pattern, CAPEC-546]
---

# CAPEC-546 - Incomplete Data Deletion in a Multi-Tenant Environment

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-546](https://capec.mitre.org/data/definitions/546.html)

## Description
An adversary obtains unauthorized information due to insecure or incomplete data deletion in a multi-tenant environment. If a cloud provider fails to completely delete storage and data from former cloud tenants' systems/resources, once these resources are allocated to new, potentially malicious tenants, the latter can probe the provided resources for sensitive information still there.

## Prerequisites
- The cloud provider must not assuredly delete part or all of the sensitive data for which they are responsible.The adversary must have the ability to interact with the system.

## Skills required
- **Low**: The adversary requires the ability to traverse directory structure.

## Consequences
- **Confidentiality**: Read Data (A successful attack that probes application memory will compromise the confidentiality of that data.)

## Mitigations
- Cloud providers should completely delete data to render it irrecoverable and inaccessible from any layer and component of infrastructure resources.
- Deletion of data should be completed promptly when requested.

## Related weaknesses (CWE)
- [CWE-284](https://cwe.mitre.org/data/definitions/284.html)
- [CWE-1266](https://cwe.mitre.org/data/definitions/1266.html)
- [CWE-1272](https://cwe.mitre.org/data/definitions/1272.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/546.html
