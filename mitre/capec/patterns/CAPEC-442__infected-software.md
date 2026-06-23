---
capec_id: CAPEC-442
name: Infected Software
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: High
related_cwe: [CWE-506]
related_attack: [T1195.001, T1195.002]
url: https://capec.mitre.org/data/definitions/442.html
tags: [mitre-capec, attack-pattern, CAPEC-442]
---

# CAPEC-442 - Infected Software

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-442](https://capec.mitre.org/data/definitions/442.html)

## Description
An adversary adds malicious logic, often in the form of a computer virus, to otherwise benign software. This logic is often hidden from the user of the software and works behind the scenes to achieve negative impacts. Many times, the malicious logic is inserted into empty space between legitimate code, and is then called when the software is executed. This pattern of attack focuses on software already fielded and used in operation as opposed to software that is still under development and part of the supply chain.

## Prerequisites
- Access to the software currently deployed at a victim location. This access is often obtained by leveraging another attack pattern to gain permissions that the adversary wouldn't normally have.

## Consequences
- **Authorization**: Execute Unauthorized Commands

## Mitigations
- Leverage anti-virus products to detect and quarantine software with known virus.

## Related weaknesses (CWE)
- [CWE-506](https://cwe.mitre.org/data/definitions/506.html)

## Related ATT&CK techniques
- T1195.001
- T1195.002

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/442.html
