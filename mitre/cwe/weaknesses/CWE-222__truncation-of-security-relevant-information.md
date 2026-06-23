---
cwe_id: CWE-222
name: Truncation of Security-relevant Information
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/222.html
tags: [mitre-cwe, weakness, CWE-222]
---

# CWE-222 - Truncation of Security-relevant Information

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-222](https://cwe.mitre.org/data/definitions/222.html)

## Description
The product truncates the display, recording, or processing of security-relevant information in a way that can obscure the source or nature of an attack.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Non-Repudiation**: Hide Activities

## Related weaknesses
- CWE-221 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-0585**: Web browser truncates long sub-domains or paths, facilitating phishing.
- **CVE-2004-2032**: Bypass URL filter via a long URL with a large number of trailing hex-encoded space characters.
- **CVE-2003-0412**: application server does not log complete URI of a long request (truncation).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/222.html
