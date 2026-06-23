---
cwe_id: CWE-474
name: Use of Function with Inconsistent Implementations
type: weakness
abstraction: Base
status: Draft
languages: [C, PHP, Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/474.html
tags: [mitre-cwe, weakness, CWE-474]
---

# CWE-474 - Use of Function with Inconsistent Implementations

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-474](https://cwe.mitre.org/data/definitions/474.html)

## Description
The code uses a function that has inconsistent implementations across operating systems and versions.

## Extended description
The use of inconsistent implementations can cause changes in behavior when the code is ported or built under a different environment than the programmer expects, which can lead to security problems in some cases. The implementation of many functions varies by platform, and at times, even by different versions of the same platform. Implementation differences can include: Slight differences in the way parameters are interpreted leading to inconsistent results. Some implementations of the function carry significant security risks. The function might not be defined on all platforms. The function might change which return codes it can provide, or change the meaning of its return codes.

## Applicable platforms / languages
C, PHP, Not Language-Specific

## Common consequences
- **Other**: Quality Degradation, Varies by Context

## Potential mitigations
- **Architecture and Design, Requirements**: Do not accept inconsistent behavior from the API specifications when the deviant behavior increase the risk level.

## Related weaknesses
- CWE-758 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/474.html
