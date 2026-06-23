---
cwe_id: CWE-708
name: Incorrect Ownership Assignment
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/708.html
tags: [mitre-cwe, weakness, CWE-708]
---

# CWE-708 - Incorrect Ownership Assignment

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-708](https://cwe.mitre.org/data/definitions/708.html)

## Description
The product assigns an owner to a resource, but the owner is outside of the intended control sphere.

## Extended description
This may allow the resource to be manipulated by actors outside of the intended control sphere.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Application Data, Modify Application Data

## Potential mitigations
- **Policy**: Periodically review the privileges and their owners.

## Related weaknesses
- CWE-282 (ChildOf)
- CWE-345 (CanAlsoBe)

## Observed examples (CVE)
- **CVE-2024-43199**: product installs binaries with potentially insecure user/group ownership
- **CVE-2007-5101**: File system sets wrong ownership and group when creating a new file.
- **CVE-2007-4238**: OS installs program with bin owner/group, allowing modification.
- **CVE-2007-1716**: Manager does not properly restore ownership of a reusable resource when a user logs out, allowing privilege escalation.
- **CVE-2005-3148**: Backup software restores symbolic links with incorrect uid/gid.
- **CVE-2005-1064**: Product changes the ownership of files that a symlink points to, instead of the symlink itself.
- **CVE-2011-1551**: Component assigns ownership of sensitive directory tree to a user account, which can be leveraged to perform privileged operations.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/708.html
