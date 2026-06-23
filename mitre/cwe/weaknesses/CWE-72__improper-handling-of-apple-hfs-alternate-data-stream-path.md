---
cwe_id: CWE-72
name: Improper Handling of Apple HFS+ Alternate Data Stream Path
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, macOS]
related_capec: []
url: https://cwe.mitre.org/data/definitions/72.html
tags: [mitre-cwe, weakness, CWE-72]
---

# CWE-72 - Improper Handling of Apple HFS+ Alternate Data Stream Path

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-72](https://cwe.mitre.org/data/definitions/72.html)

## Description
The product does not properly handle special paths that may identify the data or resource fork of a file on the HFS+ file system.

## Extended description
If the product chooses actions to take based on the file name, then if an attacker provides the data or resource fork, the product may take unexpected actions. Further, if the product intends to restrict access to a file, then an attacker might still be able to bypass intended access restrictions by requesting the data or resource fork for that file.

## Applicable platforms / languages
Not Language-Specific, macOS

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Related weaknesses
- CWE-66 (ChildOf)

## Observed examples (CVE)
- **CVE-2004-1084**: Server allows remote attackers to read files and resource fork content via HTTP requests to certain special file names related to multiple data streams in HFS+.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/72.html
