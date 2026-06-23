---
cwe_id: CWE-333
name: Improper Handling of Insufficient Entropy in TRNG
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/333.html
tags: [mitre-cwe, weakness, CWE-333]
---

# CWE-333 - Improper Handling of Insufficient Entropy in TRNG

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-333](https://cwe.mitre.org/data/definitions/333.html)

## Description
True random number generators (TRNG) generally have a limited source of entropy and therefore can fail or block.

## Extended description
The rate at which true random numbers can be generated is limited. It is important that one uses them only when they are needed for security.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability**: DoS: Crash, Exit, or Restart

## Potential mitigations
- **Implementation**: Rather than failing on a lack of random numbers, it is often preferable to wait for more numbers to be created.

## Related weaknesses
- CWE-331 (ChildOf)
- CWE-755 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/333.html
