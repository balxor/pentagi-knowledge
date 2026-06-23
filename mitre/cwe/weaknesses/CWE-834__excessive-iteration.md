---
cwe_id: CWE-834
name: Excessive Iteration
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/834.html
tags: [mitre-cwe, weakness, CWE-834]
---

# CWE-834 - Excessive Iteration

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-834](https://cwe.mitre.org/data/definitions/834.html)

## Description
The product performs an iteration or loop without sufficiently limiting the number of times that the loop is executed.

## Extended description
If the iteration can be influenced by an attacker, this weakness could allow attackers to consume excessive resources such as CPU or memory. In many cases, a loop does not need to be infinite in order to cause enough resource consumption to adversely affect the product or its host system; it depends on the amount of resources consumed per iteration.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Availability**: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Amplification, DoS: Crash, Exit, or Restart

## Related weaknesses
- CWE-691 (ChildOf)

## Observed examples (CVE)
- **CVE-2011-1027**: Chain: off-by-one error (CWE-193) leads to infinite loop (CWE-835) using invalid hex-encoded characters.
- **CVE-2006-6499**: Chain: web browser crashes due to infinite loop - "bad looping logic [that relies on] floating point math [CWE-1339] to exit the loop [CWE-835]"

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/834.html
