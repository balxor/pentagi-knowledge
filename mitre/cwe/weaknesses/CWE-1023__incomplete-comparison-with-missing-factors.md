---
cwe_id: CWE-1023
name: Incomplete Comparison with Missing Factors
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1023.html
tags: [mitre-cwe, weakness, CWE-1023]
---

# CWE-1023 - Incomplete Comparison with Missing Factors

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-1023](https://cwe.mitre.org/data/definitions/1023.html)

## Description
The product performs a comparison between entities that must consider multiple factors or characteristics of each entity, but the comparison does not include one or more of these factors.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Integrity, Access Control**: Alter Execution Logic, Bypass Protection Mechanism

## Related weaknesses
- CWE-697 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-2782**: PHP remote file inclusion in web application that filters "http" and "https" URLs, but not "ftp".
- **CVE-2014-6394**: Product does not prevent access to restricted directories due to partial string comparison with a public directory

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1023.html
