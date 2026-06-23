---
cwe_id: CWE-689
name: Permission Race Condition During Resource Copy
type: weakness
abstraction: Compound
status: Draft
languages: [C, Perl]
related_capec: [CAPEC-26, CAPEC-27]
url: https://cwe.mitre.org/data/definitions/689.html
tags: [mitre-cwe, weakness, CWE-689]
---

# CWE-689 - Permission Race Condition During Resource Copy

**Abstraction:** Compound  -  **Status:** Draft  -  **CWE:** [CWE-689](https://cwe.mitre.org/data/definitions/689.html)

## Description
The product, while copying or cloning a resource, does not set the resource's permissions or access control until the copy is complete, leaving the resource exposed to other spheres while the copy is taking place.

## Applicable platforms / languages
C, Perl

## Common consequences
- **Confidentiality, Integrity**: Read Application Data, Modify Application Data

## Related attack patterns (CAPEC)
- [CAPEC-26](https://capec.mitre.org/data/definitions/26.html)
- [CAPEC-27](https://capec.mitre.org/data/definitions/27.html)

## Related weaknesses
- CWE-362 (ChildOf)
- CWE-362 (Requires)
- CWE-732 (Requires)

## Observed examples (CVE)
- **CVE-2002-0760**: Archive extractor decompresses files with world-readable permissions, then later sets permissions to what the archive specified.
- **CVE-2005-2174**: Product inserts a new object into database before setting the object's permissions, introducing a race condition.
- **CVE-2006-5214**: Error file has weak permissions before a chmod is performed.
- **CVE-2005-2475**: Archive permissions issue using hard link.
- **CVE-2003-0265**: Database product creates files world-writable before initializing the setuid bits, leading to modification of executables.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/689.html
