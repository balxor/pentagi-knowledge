---
capec_id: CAPEC-153
name: Input Data Manipulation
type: attack-pattern
abstraction: Meta
likelihood: n/a
severity: Medium
related_cwe: [CWE-20]
related_attack: []
url: https://capec.mitre.org/data/definitions/153.html
tags: [mitre-capec, attack-pattern, CAPEC-153]
---

# CAPEC-153 - Input Data Manipulation

**Abstraction:** Meta  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-153](https://capec.mitre.org/data/definitions/153.html)

## Description
An attacker exploits a weakness in input validation by controlling the format, structure, and composition of data to an input-processing interface. By supplying input of a non-standard or unexpected form an attacker can adversely impact the security of the target.

## Extended description
For example, using a different character encoding might cause dangerous text to be treated as safe text. Alternatively, the attacker may use certain flags, such as file extensions, to make a target application believe that provided data should be handled using a certain interpreter when the data is not actually of the appropriate type. This can lead to bypassing protection mechanisms, forcing the target to use specific components for input processing, or otherwise causing the user's data to be handled differently than might otherwise be expected. This attack differs from Variable Manipulation in that Variable Manipulation attempts to subvert the target's processing through the value of the input while Input Data Manipulation seeks to control how the input is processed.

## Prerequisites
- The target must accept user data for processing and the manner in which this data is processed must depend on some aspect of the format or flags that the attacker can control.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Related weaknesses (CWE)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/153.html
