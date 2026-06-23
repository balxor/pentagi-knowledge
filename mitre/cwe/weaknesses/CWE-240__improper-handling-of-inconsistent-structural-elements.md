---
cwe_id: CWE-240
name: Improper Handling of Inconsistent Structural Elements
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/240.html
tags: [mitre-cwe, weakness, CWE-240]
---

# CWE-240 - Improper Handling of Inconsistent Structural Elements

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-240](https://cwe.mitre.org/data/definitions/240.html)

## Description
The product does not handle or incorrectly handles when two or more structural elements should be consistent, but are not.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Integrity, Other**: Varies by Context, Unexpected State

## Related weaknesses
- CWE-237 (ChildOf)
- CWE-707 (ChildOf)

## Observed examples (CVE)
- **CVE-2014-0160**: Chain: "Heartbleed" bug receives an inconsistent length parameter (CWE-130) enabling an out-of-bounds read (CWE-126), returning memory that could include private cryptographic keys and other sensitive data.
- **CVE-2009-2299**: Web application firewall consumes excessive memory when an HTTP request contains a large Content-Length value but no POST data.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/240.html
