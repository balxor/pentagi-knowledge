---
cwe_id: CWE-281
name: Improper Preservation of Permissions
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/281.html
tags: [mitre-cwe, weakness, CWE-281]
---

# CWE-281 - Improper Preservation of Permissions

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-281](https://cwe.mitre.org/data/definitions/281.html)

## Description
The product does not preserve permissions or incorrectly preserves permissions when copying, restoring, or sharing objects, which can cause them to have less restrictive permissions than intended.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Application Data, Modify Application Data

## Related weaknesses
- CWE-732 (ChildOf)
- CWE-732 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-2323**: Incorrect ACLs used when restoring backups from directories that use symbolic links.
- **CVE-2001-1515**: Automatic modification of permissions inherited from another file system.
- **CVE-2005-1920**: Permissions on backup file are created with defaults, possibly less secure than original file.
- **CVE-2001-0195**: File is made world-readable when being cloned.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/281.html
