---
cwe_id: CWE-528
name: Exposure of Core Dump File to an Unauthorized Control Sphere
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/528.html
tags: [mitre-cwe, weakness, CWE-528]
---

# CWE-528 - Exposure of Core Dump File to an Unauthorized Control Sphere

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-528](https://cwe.mitre.org/data/definitions/528.html)

## Description
The product generates a core dump file in a directory, archive, or other resource that is stored, transferred, or otherwise made accessible to unauthorized actors.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data, Read Files or Directories

## Potential mitigations
- **System Configuration**: Protect the core dump files from unauthorized access.

## Related weaknesses
- CWE-552 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-10403**: SAN firmware OS includes SFTP/FTP server password in a core dump

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/528.html
