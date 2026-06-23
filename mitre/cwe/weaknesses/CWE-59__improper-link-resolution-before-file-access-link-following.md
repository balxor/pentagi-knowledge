---
cwe_id: CWE-59
name: Improper Link Resolution Before File Access ('Link Following')
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Windows, Unix, Not Technology-Specific]
related_capec: [CAPEC-132, CAPEC-17, CAPEC-35, CAPEC-76]
url: https://cwe.mitre.org/data/definitions/59.html
tags: [mitre-cwe, weakness, CWE-59]
---

# CWE-59 - Improper Link Resolution Before File Access ('Link Following')

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-59](https://cwe.mitre.org/data/definitions/59.html)

## Description
The product attempts to access a file based on the filename, but it does not properly prevent that filename from identifying a link or shortcut that resolves to an unintended resource.

## Applicable platforms / languages
Not Language-Specific, Windows, Unix, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Access Control**: Read Files or Directories, Modify Files or Directories, Bypass Protection Mechanism
- **Other**: Execute Unauthorized Code or Commands

## Potential mitigations
- **Architecture and Design**: Follow the principle of least privilege when assigning access rights to entities in a software system. Denying access to a file can prevent an attacker from replacing that file with a link to a sensitive file. Ensure good compartmentalization in the system to provide protected areas that can be trusted.

## Related attack patterns (CAPEC)
- [CAPEC-132](https://capec.mitre.org/data/definitions/132.html)
- [CAPEC-17](https://capec.mitre.org/data/definitions/17.html)
- [CAPEC-35](https://capec.mitre.org/data/definitions/35.html)
- [CAPEC-76](https://capec.mitre.org/data/definitions/76.html)

## Related weaknesses
- CWE-706 (ChildOf)
- CWE-706 (ChildOf)

## Observed examples (CVE)
- **CVE-1999-1386**: Some versions of Perl follow symbolic links when running with the -e option, which allows local users to overwrite arbitrary files via a symlink attack.
- **CVE-2000-1178**: Text editor follows symbolic links when creating a rescue copy during an abnormal exit, which allows local users to overwrite the files of other users.
- **CVE-2004-0217**: Antivirus update allows local users to create or append to arbitrary files via a symlink attack on a logfile.
- **CVE-2003-0517**: Symlink attack allows local users to overwrite files.
- **CVE-2004-0689**: Window manager does not properly handle when certain symbolic links point to "stale" locations, which could allow local users to create or truncate arbitrary files.
- **CVE-2005-1879**: Second-order symlink vulnerabilities
- **CVE-2005-1880**: Second-order symlink vulnerabilities
- **CVE-2005-1916**: Symlink in Python program
- **CVE-2000-0972**: Setuid product allows file reading by replacing a file being edited with a symlink to the targeted file, leaking the result in error messages when parsing fails.
- **CVE-2005-0824**: Signal causes a dump that follows symlinks.
- **CVE-2001-1494**: Hard link attack, file overwrite; interesting because program checks against soft links
- **CVE-2002-0793**: Hard link and possibly symbolic link following vulnerabilities in embedded operating system allow local users to overwrite arbitrary files.
- **CVE-2003-0578**: Server creates hard links and unlinks files as root, which allows local users to gain privileges by deleting and overwriting arbitrary files.
- **CVE-1999-0783**: Operating system allows local users to conduct a denial of service by creating a hard link from a device special file to a file on an NFS file system.
- **CVE-2004-1603**: Web hosting manager follows hard links, which allows local users to read or modify arbitrary files.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/59.html
