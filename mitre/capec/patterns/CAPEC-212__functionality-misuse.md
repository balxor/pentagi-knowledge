---
capec_id: CAPEC-212
name: Functionality Misuse
type: attack-pattern
abstraction: Meta
likelihood: Medium
severity: Medium
related_cwe: [CWE-1242, CWE-1246, CWE-1281]
related_attack: []
url: https://capec.mitre.org/data/definitions/212.html
tags: [mitre-capec, attack-pattern, CAPEC-212]
---

# CAPEC-212 - Functionality Misuse

**Abstraction:** Meta  -  **Likelihood:** Medium  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-212](https://capec.mitre.org/data/definitions/212.html)

## Description
An adversary leverages a legitimate capability of an application in such a way as to achieve a negative technical impact. The system functionality is not altered or modified but used in a way that was not intended. This is often accomplished through the overuse of a specific functionality or by leveraging functionality with design flaws that enables the adversary to gain access to unauthorized, sensitive data.

## Prerequisites
- The adversary has the capability to interact with the application directly.The target system does not adequately implement safeguards to prevent misuse of authorized actions/processes.

## Skills required
- **Low**: General computer knowledge about how applications are launched, how they interact with input/output, and how they are configured.

## Consequences
- **Availability**: Other (Depending on the adversary's intended technical impact, a successful attack of this kind can compromise any or all elements of the security triad.)
- **Confidentiality**: Gain Privileges (A successful attack of this kind can compromise the confidentiality of an authorized user's credentials.), Other (Depending on the adversary's intended technical impact, a successful attack of this kind can compromise any or all elements of the security triad.)
- **Integrity**: Other (Depending on the adversary's intended technical impact, a successful attack of this kind can compromise any or all elements of the security triad.)

## Mitigations
- Perform comprehensive threat modeling, a process of identifying, evaluating, and mitigating potential threats to the application. This effort can help reveal potentially obscure application functionality that can be manipulated for malicious purposes.
- When implementing security features, consider how they can be misused and compromised.

## Related weaknesses (CWE)
- [CWE-1242](https://cwe.mitre.org/data/definitions/1242.html)
- [CWE-1246](https://cwe.mitre.org/data/definitions/1246.html)
- [CWE-1281](https://cwe.mitre.org/data/definitions/1281.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/212.html
