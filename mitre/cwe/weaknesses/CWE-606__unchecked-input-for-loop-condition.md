---
cwe_id: CWE-606
name: Unchecked Input for Loop Condition
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/606.html
tags: [mitre-cwe, weakness, CWE-606]
---

# CWE-606 - Unchecked Input for Loop Condition

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-606](https://cwe.mitre.org/data/definitions/606.html)

## Description
The product does not properly check inputs that are used for loop conditions, potentially leading to a denial of service or other consequences because of excessive looping.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability**: DoS: Resource Consumption (CPU)

## Potential mitigations
- **Implementation**: Do not use user-controlled data for loop conditions.
- **Implementation**: Perform input validation.

## Related weaknesses
- CWE-1284 (ChildOf)
- CWE-834 (CanPrecede)

## Observed examples (CVE)
- **CVE-2025-32399**: Chain: library for implementing Profinet devices does not check an input for a loop condition (CWE-606), allowing an infinite loop (CWE-835) via a crafted RPC packet

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/606.html
