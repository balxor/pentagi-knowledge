---
cwe_id: CWE-1104
name: Use of Unmaintained Third Party Components
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific, ICS/OT]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1104.html
tags: [mitre-cwe, weakness, CWE-1104]
---

# CWE-1104 - Use of Unmaintained Third Party Components

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1104](https://cwe.mitre.org/data/definitions/1104.html)

## Description
The product relies on third-party components that are not actively supported or maintained by the original developer or a trusted proxy for the original developer.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, ICS/OT

## Common consequences
- **Other**: Reduce Maintainability, Varies by Context

## Related weaknesses
- CWE-1357 (ChildOf)

## Observed examples (CVE)
- **CVE-2025-40906**: Perl module for BSON serialization includes a component that reached end-of-life approximately five years previously, but has multiple vulnerabilities.
- **CVE-2024-35252**: Closed-source cloud storage product includes an unmaintained third-party component that allows denial of service

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1104.html
