---
cwe_id: CWE-57
name: Path Equivalence: 'fakedir/../realdir/filename'
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/57.html
tags: [mitre-cwe, weakness, CWE-57]
---

# CWE-57 - Path Equivalence: 'fakedir/../realdir/filename'

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-57](https://cwe.mitre.org/data/definitions/57.html)

## Description
The product contains protection mechanisms to restrict access to 'realdir/filename', but it constructs pathnames using external input in the form of 'fakedir/../realdir/filename' that are not handled by those mechanisms. This allows attackers to perform unauthorized actions against the targeted file.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Potential mitigations
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Related weaknesses
- CWE-41 (ChildOf)

## Observed examples (CVE)
- **CVE-2001-1152**: Proxy allows remote attackers to bypass denylist restrictions and connect to unauthorized web servers by modifying the requested URL, including (1) a // (double slash), (2) a /SUBDIR/.. where the desired file is in the parentdir, (3) a /./, or (4) URL-encoded characters.
- **CVE-2000-0191**: application check access for restricted URL before canonicalization
- **CVE-2005-1366**: CGI source disclosure using "dirname/../cgi-bin"

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/57.html
