---
cwe_id: CWE-549
name: Missing Password Field Masking
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, Web Based]
related_capec: []
url: https://cwe.mitre.org/data/definitions/549.html
tags: [mitre-cwe, weakness, CWE-549]
---

# CWE-549 - Missing Password Field Masking

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-549](https://cwe.mitre.org/data/definitions/549.html)

## Description
The product does not mask passwords during entry, increasing the potential for attackers to observe and capture passwords.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Implementation, Requirements**: Recommendations include requiring all password fields in your web application be masked to prevent other users from seeing this information.

## Related weaknesses
- CWE-522 (ChildOf)

## Observed examples (CVE)
- **CVE-2025-0148**: Jenkins plugin for a video meeting product does not mask passwords

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/549.html
