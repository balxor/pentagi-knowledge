---
cwe_id: CWE-440
name: Expected Behavior Violation
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, ICS/OT]
related_capec: []
url: https://cwe.mitre.org/data/definitions/440.html
tags: [mitre-cwe, weakness, CWE-440]
---

# CWE-440 - Expected Behavior Violation

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-440](https://cwe.mitre.org/data/definitions/440.html)

## Description
A feature, API, or function does not perform according to its specification.

## Applicable platforms / languages
Not Language-Specific, ICS/OT

## Common consequences
- **Other**: Quality Degradation, Varies by Context

## Related weaknesses
- CWE-684 (ChildOf)

## Observed examples (CVE)
- **CVE-2003-0187**: Program uses large timeouts on unconfirmed connections resulting from inconsistency in linked lists implementations.
- **CVE-2003-0465**: "strncpy" in Linux kernel acts different than libc on x86, leading to expected behavior difference - sort of a multiple interpretation error?
- **CVE-2005-3265**: Buffer overflow in product stems the use of a third party library function that is expected to have internal protection against overflows, but doesn't.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/440.html
