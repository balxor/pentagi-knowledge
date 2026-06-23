---
capec_id: CAPEC-116
name: Excavation
type: attack-pattern
abstraction: Meta
likelihood: High
severity: Medium
related_cwe: [CWE-200, CWE-1243]
related_attack: []
url: https://capec.mitre.org/data/definitions/116.html
tags: [mitre-capec, attack-pattern, CAPEC-116]
---

# CAPEC-116 - Excavation

**Abstraction:** Meta  -  **Likelihood:** High  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-116](https://capec.mitre.org/data/definitions/116.html)

## Description
An adversary actively probes the target in a manner that is designed to solicit information that could be leveraged for malicious purposes.

## Extended description
This is achieved by exploring the target via ordinary interactions for the purpose of gathering intelligence about the target, or by sending data that is syntactically invalid or non-standard in an attempt to produce a response that contains the desired data. As a result of these interactions, the adversary is able to obtain information from the target that aids the attacker in making inferences about its security, configuration, or potential vulnerabilities. Examplar exchanges with the target may trigger unhandled exceptions or verbose error messages that reveal information like stack traces, configuration information, path information, or database design. This type of attack also includes the manipulation of query strings in a URI to produce invalid SQL queries, or by trying alternative path values in the hope that the server will return useful information.

## Prerequisites
- An adversary requires some way of interacting with the system.

## Resources required
- A tool, such as an Adversary in the Middle (CAPEC-94) Proxy or a fuzzer, that is capable of generating and injecting custom inputs to be used in the attack.

## Consequences
- **Confidentiality**: Read Data

## Mitigations
- Minimize error/response output to only what is necessary for functional use or corrective language.
- Remove potentially sensitive information that is not necessary for the application's functionality.

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)
- [CWE-1243](https://cwe.mitre.org/data/definitions/1243.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/116.html
