---
cwe_id: CWE-527
name: Exposure of Version-Control Repository to an Unauthorized Control Sphere
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific, Web Based]
related_capec: []
url: https://cwe.mitre.org/data/definitions/527.html
tags: [mitre-cwe, weakness, CWE-527]
---

# CWE-527 - Exposure of Version-Control Repository to an Unauthorized Control Sphere

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-527](https://cwe.mitre.org/data/definitions/527.html)

## Description
The product stores a CVS, git, or other repository in a directory, archive, or other resource that is stored, transferred, or otherwise made accessible to unauthorized actors.

## Extended description
Version control repositories such as CVS or git store version-specific metadata and other details within subdirectories. If these subdirectories are stored on a web server or added to an archive, then these could be used by an attacker. This information may include usernames, filenames, path root, IP addresses, and detailed "diff" data about how files have been changed - which could reveal source code snippets that were never intended to be made public.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based

## Common consequences
- **Confidentiality**: Read Application Data, Read Files or Directories

## Potential mitigations
- **Operation, Distribution, System Configuration**: Recommendations include removing any CVS directories and repositories from the production server, disabling the use of remote CVS repositories, and ensuring that the latest CVS patches and version updates have been performed.

## Related weaknesses
- CWE-552 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/527.html
