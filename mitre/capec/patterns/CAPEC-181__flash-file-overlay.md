---
capec_id: CAPEC-181
name: Flash File Overlay
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-1021]
related_attack: []
url: https://capec.mitre.org/data/definitions/181.html
tags: [mitre-capec, attack-pattern, CAPEC-181]
---

# CAPEC-181 - Flash File Overlay

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-181](https://capec.mitre.org/data/definitions/181.html)

## Description
An attacker creates a transparent overlay using flash in order to intercept user actions for the purpose of performing a clickjacking attack. In this technique, the Flash file provides a transparent overlay over HTML content. Because the Flash application is on top of the content, user actions, such as clicks, are caught by the Flash application rather than the underlying HTML. The action is then interpreted by the overlay to perform the actions the attacker wishes.

## Prerequisites
- The victim must be tricked into navigating to the attackers' decoy site and performing the actions on the decoy page.
- The victim's browser must support invisible Flash overlays.

## Resources required
- The attacker must be able to force the Flash overlay over the decoy content.

## Related weaknesses (CWE)
- [CWE-1021](https://cwe.mitre.org/data/definitions/1021.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/181.html
