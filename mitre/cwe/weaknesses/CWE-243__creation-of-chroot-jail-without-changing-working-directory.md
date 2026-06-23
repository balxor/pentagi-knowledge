---
cwe_id: CWE-243
name: Creation of chroot Jail Without Changing Working Directory
type: weakness
abstraction: Variant
status: Draft
languages: [C, C++, Unix]
related_capec: []
url: https://cwe.mitre.org/data/definitions/243.html
tags: [mitre-cwe, weakness, CWE-243]
---

# CWE-243 - Creation of chroot Jail Without Changing Working Directory

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-243](https://cwe.mitre.org/data/definitions/243.html)

## Description
The product uses the chroot() system call to create a jail, but does not change the working directory afterward. This does not prevent access to files outside of the jail.

## Extended description
Improper use of chroot() may allow attackers to escape from the chroot jail. The chroot() function call does not change the process's current working directory, so relative paths may still refer to file system resources outside of the chroot jail after chroot() has been called.

## Applicable platforms / languages
C, C++, Unix

## Common consequences
- **Confidentiality**: Read Files or Directories

## Related weaknesses
- CWE-573 (ChildOf)
- CWE-669 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/243.html
