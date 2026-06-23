---
cwe_id: CWE-1038
name: Insecure Automated Optimizations
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1038.html
tags: [mitre-cwe, weakness, CWE-1038]
---

# CWE-1038 - Insecure Automated Optimizations

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-1038](https://cwe.mitre.org/data/definitions/1038.html)

## Description
The product uses a mechanism that automatically optimizes code, e.g. to improve a characteristic such as performance, but the optimizations can have an unintended side effect that might violate an intended security assumption.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Alter Execution Logic

## Related weaknesses
- CWE-435 (ChildOf)
- CWE-758 (ChildOf)

## Observed examples (CVE)
- **CVE-2017-5715**: Intel, ARM, and AMD processor optimizations related to speculative execution and branch prediction cause access control checks to be bypassed when placing data into the cache. Often known as "Spectre".
- **CVE-2008-1685**: C compiler optimization, as allowed by specifications, removes code that is used to perform checks to detect integer overflows.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1038.html
