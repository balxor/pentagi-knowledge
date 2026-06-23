---
capec_id: CAPEC-549
name: Local Execution of Code
type: attack-pattern
abstraction: Meta
likelihood: Medium
severity: High
related_cwe: [CWE-829]
related_attack: []
url: https://capec.mitre.org/data/definitions/549.html
tags: [mitre-capec, attack-pattern, CAPEC-549]
---

# CAPEC-549 - Local Execution of Code

**Abstraction:** Meta  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-549](https://capec.mitre.org/data/definitions/549.html)

## Description
An adversary installs and executes malicious code on the target system in an effort to achieve a negative technical impact. Examples include rootkits, ransomware, spyware, adware, and others.

## Prerequisites
- Knowledge of the target system's vulnerabilities that can be capitalized on with malicious code.The adversary must be able to place the malicious code on the target system.

## Resources required
- The means by which the adversary intends to place the malicious code on the system dictates the tools required. For example, suppose the adversary wishes to leverage social engineering and convince a legitimate user to open a malicious file attached to a seemingly legitimate email. In this case, the adversary might require a tool capable of wrapping malicious code into an innocuous filetype (e.g., PDF, .doc, etc.)

## Consequences
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code), Other (Depending on the type of code executed by the adversary, the consequences of this attack pattern can vary widely.)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Other (Depending on the type of code executed by the adversary, the consequences of this attack pattern can vary widely.)
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code), Other (Depending on the type of code executed by the adversary, the consequences of this attack pattern can vary widely.)

## Mitigations
- Employ robust cybersecurity training for all employees.
- Implement system antivirus software that scans all attachments before opening them.
- Regularly patch all software.
- Execute all suspicious files in a sandbox environment.

## Related weaknesses (CWE)
- [CWE-829](https://cwe.mitre.org/data/definitions/829.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/549.html
