---
cwe_id: CWE-538
name: Insertion of Sensitive Information into Externally-Accessible File or Directory
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-95]
url: https://cwe.mitre.org/data/definitions/538.html
tags: [mitre-cwe, weakness, CWE-538]
---

# CWE-538 - Insertion of Sensitive Information into Externally-Accessible File or Directory

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-538](https://cwe.mitre.org/data/definitions/538.html)

## Description
The product places sensitive information into files or directories that are accessible to actors who are allowed to have access to the files, but not to the sensitive information.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Files or Directories

## Potential mitigations
- **Architecture and Design, Operation, System Configuration**: Do not expose file and directory information to the user.

## Related attack patterns (CAPEC)
- [CAPEC-95](https://capec.mitre.org/data/definitions/95.html)

## Related weaknesses
- CWE-200 (ChildOf)

## Observed examples (CVE)
- **CVE-2018-1999036**: SSH password for private key stored in build log

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/538.html
