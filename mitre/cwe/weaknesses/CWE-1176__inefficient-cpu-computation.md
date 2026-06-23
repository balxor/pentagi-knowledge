---
cwe_id: CWE-1176
name: Inefficient CPU Computation
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1176.html
tags: [mitre-cwe, weakness, CWE-1176]
---

# CWE-1176 - Inefficient CPU Computation

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-1176](https://cwe.mitre.org/data/definitions/1176.html)

## Description
The product performs CPU computations using algorithms that are not as efficient as they could be for the needs of the developer, i.e., the computations can be optimized further.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability**: Reduce Performance, DoS: Resource Consumption (CPU)

## Related weaknesses
- CWE-405 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-37734**: Chain: lexer in Java-based GraphQL server does not enforce maximum of tokens early enough (CWE-696), allowing excessive CPU consumption (CWE-1176)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1176.html
