---
cwe_id: CWE-402
name: Transmission of Private Resources into a New Sphere ('Resource Leak')
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/402.html
tags: [mitre-cwe, weakness, CWE-402]
---

# CWE-402 - Transmission of Private Resources into a New Sphere ('Resource Leak')

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-402](https://cwe.mitre.org/data/definitions/402.html)

## Description
The product makes resources available to untrusted parties when those resources are only intended to be accessed by the product.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Related weaknesses
- CWE-668 (ChildOf)

## Observed examples (CVE)
- **CVE-2003-0740**: Server leaks a privileged file descriptor, allowing the server to be hijacked.
- **CVE-2004-1033**: File descriptor leak allows read of restricted files.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/402.html
