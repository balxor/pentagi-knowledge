---
cwe_id: CWE-672
name: Operation on a Resource after Expiration or Release
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific, Mobile]
related_capec: []
url: https://cwe.mitre.org/data/definitions/672.html
tags: [mitre-cwe, weakness, CWE-672]
---

# CWE-672 - Operation on a Resource after Expiration or Release

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-672](https://cwe.mitre.org/data/definitions/672.html)

## Description
The product uses, accesses, or otherwise operates on a resource after that resource has been expired, released, or revoked.

## Applicable platforms / languages
Not Language-Specific, Mobile

## Common consequences
- **Integrity, Confidentiality**: Modify Application Data, Read Application Data
- **Other, Availability**: Other, DoS: Crash, Exit, or Restart

## Related weaknesses
- CWE-666 (ChildOf)

## Observed examples (CVE)
- **CVE-2009-3547**: Chain: race condition (CWE-362) might allow resource to be released before operating on it, leading to NULL dereference (CWE-476)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/672.html
