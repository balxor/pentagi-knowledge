---
cwe_id: CWE-42
name: Path Equivalence: 'filename.' (Trailing Dot)
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/42.html
tags: [mitre-cwe, weakness, CWE-42]
---

# CWE-42 - Path Equivalence: 'filename.' (Trailing Dot)

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-42](https://cwe.mitre.org/data/definitions/42.html)

## Description
The product accepts path input in the form of trailing dot ('filedir.') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Related weaknesses
- CWE-41 (ChildOf)
- CWE-162 (ChildOf)

## Observed examples (CVE)
- **CVE-2000-1114**: Source code disclosure using trailing dot
- **CVE-2002-1986**: Source code disclosure using trailing dot
- **CVE-2004-2213**: Source code disclosure using trailing dot
- **CVE-2005-3293**: Source code disclosure using trailing dot
- **CVE-2004-0061**: Bypass directory access restrictions using trailing dot in URL
- **CVE-2000-1133**: Bypass directory access restrictions using trailing dot in URL
- **CVE-2001-1386**: Bypass check for ".lnk" extension using ".lnk."

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/42.html
