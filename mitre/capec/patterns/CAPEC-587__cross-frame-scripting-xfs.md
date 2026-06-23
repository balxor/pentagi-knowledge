---
capec_id: CAPEC-587
name: Cross Frame Scripting (XFS)
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: High
related_cwe: [CWE-1021]
related_attack: []
url: https://capec.mitre.org/data/definitions/587.html
tags: [mitre-capec, attack-pattern, CAPEC-587]
---

# CAPEC-587 - Cross Frame Scripting (XFS)

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** High  -  **CAPEC:** [CAPEC-587](https://capec.mitre.org/data/definitions/587.html)

## Description
This attack pattern combines malicious Javascript and a legitimate webpage loaded into a concealed iframe. The malicious Javascript is then able to interact with a legitimate webpage in a manner that is unknown to the user. This attack usually leverages some element of social engineering in that an attacker must convinces a user to visit a web page that the attacker controls.

## Prerequisites
- The user's browser must have vulnerabilities in its implementation of the same-origin policy. It allows certain data in a loaded page to originate from different servers/domains.

## Consequences
- **Confidentiality**: Read Data (Cross Frame Scripting allows an adversary to steal sensitive data from a legitimate site.)

## Mitigations
- Avoid clicking on untrusted links.
- Employ techniques such as frame busting, which is a method by which developers aim to prevent their site being loaded within a frame.

## Related weaknesses (CWE)
- [CWE-1021](https://cwe.mitre.org/data/definitions/1021.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/587.html
