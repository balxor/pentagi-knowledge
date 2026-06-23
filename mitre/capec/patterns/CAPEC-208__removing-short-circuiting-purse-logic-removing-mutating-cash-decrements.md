---
capec_id: CAPEC-208
name: Removing/short-circuiting 'Purse' logic: removing/mutating 'cash' decrements
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-602]
related_attack: []
url: https://capec.mitre.org/data/definitions/208.html
tags: [mitre-capec, attack-pattern, CAPEC-208]
---

# CAPEC-208 - Removing/short-circuiting 'Purse' logic: removing/mutating 'cash' decrements

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-208](https://capec.mitre.org/data/definitions/208.html)

## Description
An attacker removes or modifies the logic on a client associated with monetary calculations resulting in incorrect information being sent to the server. A server may rely on a client to correctly compute monetary information. For example, a server might supply a price for an item and then rely on the client to correctly compute the total cost of a purchase given the number of items the user is buying. If the attacker can remove or modify the logic that controls these calculations, they can return incorrect values to the server. The attacker can use this to make purchases for a fraction of the legitimate cost or otherwise avoid correct billing for activities.

## Prerequisites
- The targeted server must rely on the client to correctly perform monetary calculations and must fail to detect errors in these calculations.

## Resources required
- The attacker must have access to the client for the targeted service (this step is trivial for most web-based services). The attacker must also be able to reverse engineer the client in order to locate and modify the client's purse logic. Reverse engineering tools would be necessary for this.

## Related weaknesses (CWE)
- [CWE-602](https://cwe.mitre.org/data/definitions/602.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/208.html
