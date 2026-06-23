---
capec_id: CAPEC-190
name: Reverse Engineer an Executable to Expose Assumed Hidden Functionality
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-912]
related_attack: []
url: https://capec.mitre.org/data/definitions/190.html
tags: [mitre-capec, attack-pattern, CAPEC-190]
---

# CAPEC-190 - Reverse Engineer an Executable to Expose Assumed Hidden Functionality

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-190](https://capec.mitre.org/data/definitions/190.html)

## Description
An attacker analyzes a binary file or executable for the purpose of discovering the structure, function, and possibly source-code of the file by using a variety of analysis techniques to effectively determine how the software functions and operates. This type of analysis is also referred to as Reverse Code Engineering, as techniques exist for extracting source code from an executable. Several techniques are often employed for this purpose, both black box and white box. The use of computer bus analyzers and packet sniffers allows the binary to be studied at a level of interactions with its computing environment, such as a host OS, inter-process communication, and/or network communication. This type of analysis falls into the 'black box' category because it involves behavioral analysis of the software without reference to source code, object code, or protocol specifications.

## Resources required
- Access to the target file such that it can be analyzed with the appropriate tools. A range of tools suitable for analyzing an executable or its operations

## Related weaknesses (CWE)
- [CWE-912](https://cwe.mitre.org/data/definitions/912.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/190.html
