---
cwe_id: CWE-377
name: Insecure Temporary File
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-149, CAPEC-155]
url: https://cwe.mitre.org/data/definitions/377.html
tags: [mitre-cwe, weakness, CWE-377]
---

# CWE-377 - Insecure Temporary File

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-377](https://cwe.mitre.org/data/definitions/377.html)

## Description
Creating and using insecure temporary files can leave application and system data vulnerable to attack.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Related attack patterns (CAPEC)
- [CAPEC-149](https://capec.mitre.org/data/definitions/149.html)
- [CAPEC-155](https://capec.mitre.org/data/definitions/155.html)

## Related weaknesses
- CWE-668 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-41954**: A library uses the Java File.createTempFile() method which creates a file with "-rw-r--r--" default permissions on Unix-like operating systems

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/377.html
