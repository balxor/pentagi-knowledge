---
capec_id: CAPEC-537
name: Infiltration of Hardware Development Environment
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: []
related_attack: [T1195.003]
url: https://capec.mitre.org/data/definitions/537.html
tags: [mitre-capec, attack-pattern, CAPEC-537]
---

# CAPEC-537 - Infiltration of Hardware Development Environment

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-537](https://capec.mitre.org/data/definitions/537.html)

## Description
An adversary, leveraging the ability to manipulate components of primary support systems and tools within the development and production environments, inserts malicious software within the hardware and/or firmware development environment. The infiltration purpose is to alter developed hardware components in a system destined for deployment at the victim's organization, for the purpose of disruption or further compromise.

## Prerequisites
- The victim must use email or removable media from systems running the IDE (or systems adjacent to the IDE systems).
- The victim must have a system running exploitable applications and/or a vulnerable configuration to allow for initial infiltration.
- The adversary must have working knowledge of some if not all of the components involved in the IDE system as well as the infrastructure.

## Skills required
- **High**: Development skills to construct malicious attachments that can be used to exploit vulnerabilities in typical desktop applications or system configurations. The malicious attachments should be crafted well enough to bypass typical defensive systems (IDS, anti-virus, etc)
- **Medium**: Intelligence about the manufacturer's operating environment and infrastructure.

## Mitigations
- Verify software downloads and updates to ensure they have not been modified be adversaries
- Leverage antivirus tools to detect known malware
- Do not download software from untrusted sources
- Educate designers, developers, engineers, etc. on social engineering attacks to avoid downloading malicious software via attacks such as phishing attacks

## Related ATT&CK techniques
- T1195.003

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/537.html
