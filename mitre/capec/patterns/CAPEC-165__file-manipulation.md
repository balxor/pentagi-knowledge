---
capec_id: CAPEC-165
name: File Manipulation
type: attack-pattern
abstraction: Meta
likelihood: n/a
severity: Medium
related_cwe: []
related_attack: [T1036.003]
url: https://capec.mitre.org/data/definitions/165.html
tags: [mitre-capec, attack-pattern, CAPEC-165]
---

# CAPEC-165 - File Manipulation

**Abstraction:** Meta  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-165](https://capec.mitre.org/data/definitions/165.html)

## Description
An attacker modifies file contents or attributes (such as extensions or names) of files in a manner to cause incorrect processing by an application. Attackers use this class of attacks to cause applications to enter unstable states, overwrite or expose sensitive information, and even execute arbitrary code with the application's privileges. This class of attacks differs from attacks on configuration information (even if file-based) in that file manipulation causes the file processing to result in non-standard behaviors, such as buffer overflows or use of the incorrect interpreter. Configuration attacks rely on the application interpreting files correctly in order to insert harmful configuration information. Likewise, resource location attacks rely on controlling an application's ability to locate files, whereas File Manipulation attacks do not require the application to look in a non-default location, although the two classes of attacks are often combined.

## Prerequisites
- The target must use the affected file without verifying its integrity.

## Resources required
- None: No specialized resources are required to execute this type of attack. In some cases, tools can be used to better control the response of the targeted application to the modified file.

## Related ATT&CK techniques
- T1036.003

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/165.html
