---
capec_id: CAPEC-678
name: System Build Data Maliciously Altered
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: []
related_attack: [T1195.002]
url: https://capec.mitre.org/data/definitions/678.html
tags: [mitre-capec, attack-pattern, CAPEC-678]
---

# CAPEC-678 - System Build Data Maliciously Altered

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-678](https://capec.mitre.org/data/definitions/678.html)

## Description
<xhtml:p>During the system build process, the system is deliberately misconfigured by the alteration of the build data. Access to system configuration data files and build processes is susceptible to deliberate misconfiguration of the system.</xhtml:p>

## Prerequisites
- An adversary has access to the data files and processes used for executing system configuration and performing the build.

## Consequences
- **Access_Control**: Gain Privileges
- **Confidentiality**: Modify Data, Read Data
- **Integrity**: Execute Unauthorized Commands

## Mitigations
- Implement configuration management security practices that protect the integrity of software and associated data.
- Monitor and control access to the configuration management system.
- Harden centralized repositories against attack.
- Establish acceptance criteria for configuration management check-in to assure integrity.
- Plan for and audit the security of configuration management administration processes.
- Maintain configuration control over operational systems.

## Related ATT&CK techniques
- T1195.002

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/678.html
