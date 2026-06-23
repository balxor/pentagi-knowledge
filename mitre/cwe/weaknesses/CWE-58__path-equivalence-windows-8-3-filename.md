---
cwe_id: CWE-58
name: Path Equivalence: Windows 8.3 Filename
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Windows, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/58.html
tags: [mitre-cwe, weakness, CWE-58]
---

# CWE-58 - Path Equivalence: Windows 8.3 Filename

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-58](https://cwe.mitre.org/data/definitions/58.html)

## Description
The product contains a protection mechanism that restricts access to a long filename on a Windows operating system, but it does not properly restrict access to the equivalent short "8.3" filename.

## Applicable platforms / languages
Not Language-Specific, Windows, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Potential mitigations
- **System Configuration**: Disable Windows from supporting 8.3 filenames by editing the Windows registry. Preventing 8.3 filenames will not remove previously generated 8.3 filenames.

## Related weaknesses
- CWE-41 (ChildOf)

## Observed examples (CVE)
- **CVE-1999-0012**: Multiple web servers allow restriction bypass using 8.3 names instead of long names
- **CVE-2001-0795**: Source code disclosure using 8.3 file name.
- **CVE-2005-0471**: Multi-Factor Vulnerability. Product generates temporary filenames using long filenames, which become predictable in 8.3 format.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/58.html
