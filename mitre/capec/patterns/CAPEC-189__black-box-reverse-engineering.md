---
capec_id: CAPEC-189
name: Black Box Reverse Engineering
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Low
related_cwe: [CWE-203, CWE-1255, CWE-1300]
related_attack: []
url: https://capec.mitre.org/data/definitions/189.html
tags: [mitre-capec, attack-pattern, CAPEC-189]
---

# CAPEC-189 - Black Box Reverse Engineering

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-189](https://capec.mitre.org/data/definitions/189.html)

## Description
An adversary discovers the structure, function, and composition of a type of computer software through black box analysis techniques. 'Black Box' methods involve interacting with the software indirectly, in the absence of direct access to the executable object. Such analysis typically involves interacting with the software at the boundaries of where the software interfaces with a larger execution environment, such as input-output vectors, libraries, or APIs. Black Box Reverse Engineering also refers to gathering physical side effects of a hardware device, such as electromagnetic radiation or sounds.

## Resources required
- Black box methods require (at minimum) the ability to interact with the functional boundaries where the software communicates with a larger processing environment, such as inter-process communication on a host operating system, or via networking protocols.

## Related weaknesses (CWE)
- [CWE-203](https://cwe.mitre.org/data/definitions/203.html)
- [CWE-1255](https://cwe.mitre.org/data/definitions/1255.html)
- [CWE-1300](https://cwe.mitre.org/data/definitions/1300.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/189.html
