---
capec_id: CAPEC-670
name: Software Development Tools Maliciously Altered
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: []
related_attack: [T1127, T1195.001]
url: https://capec.mitre.org/data/definitions/670.html
tags: [mitre-capec, attack-pattern, CAPEC-670]
---

# CAPEC-670 - Software Development Tools Maliciously Altered

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-670](https://capec.mitre.org/data/definitions/670.html)

## Description
An adversary with the ability to alter tools used in a development environment causes software to be developed with maliciously modified tools. Such tools include requirements management and database tools, software design tools, configuration management tools, compilers, system build tools, and software performance testing and load testing tools. The adversary then carries out malicious acts once the software is deployed including malware infection of other systems to support further compromises.

## Prerequisites
- An adversary would need to have access to a targeted developer’s development environment and in particular to tools used to design, create, test and manage software, where the adversary could ensure malicious code is included in software packages built through alteration or substitution of tools in the environment used in the development of software.

## Skills required
- **High**: Ability to leverage common delivery mechanisms (e.g., email attachments, removable media) to infiltrate a development environment to gain access to software development tools for the purpose of malware insertion into an existing tool or replacement of an existing tool with a maliciously altered copy.

## Consequences
- **Access_Control**: Gain Privileges
- **Confidentiality**: Modify Data, Read Data
- **Integrity**: Execute Unauthorized Commands

## Mitigations
- Have a security concept of operations (CONOPS) for the development environment that includes: Maintaining strict security administration and configuration management of requirements management and database tools, software design tools, configuration management tools, compilers, system build tools, and software performance testing and load testing tools.
- Avoid giving elevated privileges to developers.

## Related ATT&CK techniques
- T1127
- T1195.001

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/670.html
