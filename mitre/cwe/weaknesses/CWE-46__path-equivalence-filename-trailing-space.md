---
cwe_id: CWE-46
name: Path Equivalence: 'filename ' (Trailing Space)
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific, Web Based]
related_capec: [CAPEC-649]
url: https://cwe.mitre.org/data/definitions/46.html
tags: [mitre-cwe, weakness, CWE-46]
---

# CWE-46 - Path Equivalence: 'filename ' (Trailing Space)

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-46](https://cwe.mitre.org/data/definitions/46.html)

## Description
The product accepts path input in the form of trailing space ('filedir ') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Related attack patterns (CAPEC)
- [CAPEC-649](https://capec.mitre.org/data/definitions/649.html)

## Related weaknesses
- CWE-41 (ChildOf)
- CWE-162 (ChildOf)
- CWE-289 (CanPrecede)

## Observed examples (CVE)
- **CVE-2001-0693**: Source disclosure via trailing encoded space "%20"
- **CVE-2001-0778**: Source disclosure via trailing encoded space "%20"
- **CVE-2001-1248**: Source disclosure via trailing encoded space "%20"
- **CVE-2004-0280**: Source disclosure via trailing encoded space "%20"
- **CVE-2004-2213**: Source disclosure via trailing encoded space "%20"
- **CVE-2005-0622**: Source disclosure via trailing encoded space "%20"
- **CVE-2005-1656**: Source disclosure via trailing encoded space "%20"
- **CVE-2002-1603**: Source disclosure via trailing encoded space "%20"
- **CVE-2001-0054**: Multi-Factor Vulnerability (MFV). directory traversal and other issues in FTP server using Web encodings such as "%20"; certain manipulations have unusual side effects.
- **CVE-2002-1451**: Trailing space ("+" in query string) leads to source code disclosure.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/46.html
