---
capec_id: CAPEC-539
name: ASIC With Malicious Functionality
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: []
related_attack: [T1195.003]
url: https://capec.mitre.org/data/definitions/539.html
tags: [mitre-capec, attack-pattern, CAPEC-539]
---

# CAPEC-539 - ASIC With Malicious Functionality

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-539](https://capec.mitre.org/data/definitions/539.html)

## Description
An attacker with access to the development environment process of an application-specific integrated circuit (ASIC) for a victim system being developed or maintained after initial deployment can insert malicious functionality into the system for the purpose of disruption or further compromise.

## Prerequisites
- The attacker must have working knowledge of some if not all of the components involved in the target system as well as the infrastructure and development environment of the manufacturer.
- Advanced knowledge about the ASIC installed within the target system.

## Skills required
- **High**: Able to develop and manufacture malicious subroutines for an ASIC environment without degradation of existing functions and processes.

## Related ATT&CK techniques
- T1195.003

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/539.html
