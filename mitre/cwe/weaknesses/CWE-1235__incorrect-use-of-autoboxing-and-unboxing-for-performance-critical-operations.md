---
cwe_id: CWE-1235
name: Incorrect Use of Autoboxing and Unboxing for Performance Critical Operations
type: weakness
abstraction: Base
status: Incomplete
languages: [Java, C#, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1235.html
tags: [mitre-cwe, weakness, CWE-1235]
---

# CWE-1235 - Incorrect Use of Autoboxing and Unboxing for Performance Critical Operations

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1235](https://cwe.mitre.org/data/definitions/1235.html)

## Description
The code uses boxed primitives, which may introduce inefficiencies into performance-critical operations.

## Applicable platforms / languages
Java, C#, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Availability**: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Resource Consumption (Other), Reduce Performance

## Potential mitigations
- **Implementation**: Use of boxed primitives should be limited to certain situations such as when calling methods with typed parameters. They should not be used for scientific computing or other performance critical operations. They are only suited to support "impedance mismatch" between reference types and primitives. Examine the use of boxed primitives prior to use. Use SparseArrays or ArrayMap instead of HashMap to avoid performance overhead.

## Related weaknesses
- CWE-400 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1235.html
