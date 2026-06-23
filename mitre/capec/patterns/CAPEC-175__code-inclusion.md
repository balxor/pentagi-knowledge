---
capec_id: CAPEC-175
name: Code Inclusion
type: attack-pattern
abstraction: Meta
likelihood: Medium
severity: Very High
related_cwe: [CWE-829]
related_attack: []
url: https://capec.mitre.org/data/definitions/175.html
tags: [mitre-capec, attack-pattern, CAPEC-175]
---

# CAPEC-175 - Code Inclusion

**Abstraction:** Meta  -  **Likelihood:** Medium  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-175](https://capec.mitre.org/data/definitions/175.html)

## Description
An adversary exploits a weakness on the target to force arbitrary code to be retrieved locally or from a remote location and executed. This differs from code injection in that code injection involves the direct inclusion of code while code inclusion involves the addition or replacement of a reference to a code file, which is subsequently loaded by the target and used as part of the code of some application.

## Prerequisites
- The target application must include external code/libraries that are executed when the application runs and the adversary must be able to influence the specific files that get included.
- The victim must run the targeted application, possibly using the crafted parameters that the adversary uses to identify the code to include.

## Resources required
- The adversary may need the capability to host code modules if they wish their own code files to be included.

## Related weaknesses (CWE)
- [CWE-829](https://cwe.mitre.org/data/definitions/829.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/175.html
