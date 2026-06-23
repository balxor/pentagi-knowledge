---
capec_id: CAPEC-140
name: Bypassing of Intermediate Forms in Multiple-Form Sets
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Medium
related_cwe: [CWE-372]
related_attack: []
url: https://capec.mitre.org/data/definitions/140.html
tags: [mitre-capec, attack-pattern, CAPEC-140]
---

# CAPEC-140 - Bypassing of Intermediate Forms in Multiple-Form Sets

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-140](https://capec.mitre.org/data/definitions/140.html)

## Description
Some web applications require users to submit information through an ordered sequence of web forms. This is often done if there is a very large amount of information being collected or if information on earlier forms is used to pre-populate fields or determine which additional information the application needs to collect. An attacker who knows the names of the various forms in the sequence may be able to explicitly type in the name of a later form and navigate to it without first going through the previous forms. This can result in incomplete collection of information, incorrect assumptions about the information submitted by the attacker, or other problems that can impair the functioning of the application.

## Prerequisites
- The target must collect information from the user in a series of forms where each form has its own URL that the attacker can anticipate and the application must fail to detect attempts to access intermediate forms without first filling out the previous forms.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Related weaknesses (CWE)
- [CWE-372](https://cwe.mitre.org/data/definitions/372.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/140.html
