---
capec_id: CAPEC-456
name: Infected Memory
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: High
related_cwe: [CWE-1257, CWE-1260, CWE-1274, CWE-1312, CWE-1316]
related_attack: []
url: https://capec.mitre.org/data/definitions/456.html
tags: [mitre-capec, attack-pattern, CAPEC-456]
---

# CAPEC-456 - Infected Memory

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-456](https://capec.mitre.org/data/definitions/456.html)

## Description
An adversary inserts malicious logic into memory enabling them to achieve a negative impact. This logic is often hidden from the user of the system and works behind the scenes to achieve negative impacts. This pattern of attack focuses on systems already fielded and used in operation as opposed to systems that are still under development and part of the supply chain.

## Consequences
- **Authorization**: Execute Unauthorized Commands

## Mitigations
- Leverage anti-virus products to detect stop operations with known virus.

## Related weaknesses (CWE)
- [CWE-1257](https://cwe.mitre.org/data/definitions/1257.html)
- [CWE-1260](https://cwe.mitre.org/data/definitions/1260.html)
- [CWE-1274](https://cwe.mitre.org/data/definitions/1274.html)
- [CWE-1312](https://cwe.mitre.org/data/definitions/1312.html)
- [CWE-1316](https://cwe.mitre.org/data/definitions/1316.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/456.html
