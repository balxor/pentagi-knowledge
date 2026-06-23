---
cwe_id: CWE-1386
name: Insecure Operation on Windows Junction / Mount Point
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Windows]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1386.html
tags: [mitre-cwe, weakness, CWE-1386]
---

# CWE-1386 - Insecure Operation on Windows Junction / Mount Point

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1386](https://cwe.mitre.org/data/definitions/1386.html)

## Description
The product opens a file or directory, but it does not properly prevent the name from being associated with a junction or mount point to a destination that is outside of the intended control sphere.

## Extended description
Depending on the intended action being performed, this could allow an attacker to cause the product to read, write, delete, or otherwise operate on unauthorized files. In Windows, NTFS5 allows for file system objects called reparse points. Applications can create a hard link from one directory to another directory, called a junction point. They can also create a mapping from a directory to a drive letter, called a mount point. If a file is used by a privileged program, but it can be replaced with a hard link to a sensitive file (e.g., AUTOEXEC.BAT), an attacker could escalate privileges. When the process opens the file, the attacker can assume the privileges of that process, tricking the privileged process to read, modify, or delete the sensitive file, preventing the program from accurately processing data. Note that one can also point to registries and semaphores.

## Applicable platforms / languages
Not Language-Specific, Windows

## Common consequences
- **Confidentiality**: Read Files or Directories
- **Integrity**: Modify Files or Directories
- **Availability**: Modify Files or Directories

## Potential mitigations
- **Architecture and Design**: When designing software that will have different rights than the executer, the software should check that files that it is interacting with are not improper hard links or mount points. One way to do this in Windows is to use the functionality embedded in the following command: "dir /al /s /b" or, in PowerShell, use LinkType as a filter. In addition, some software uses authentication via signing to ensure that the file is the correct one to use. Make checks atomic with the file action, otherwise a TOCTOU weakness (CWE-367) can be introduced.

## Related weaknesses
- CWE-59 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-26426**: Privileged service allows attackers to delete unauthorized files using a directory junction, leading to arbitrary code execution as SYSTEM.
- **CVE-2020-0863**: By creating a mount point and hard links, an attacker can abuse a service to allow users arbitrary file read permissions.
- **CVE-2019-1161**: Chain: race condition (CWE-362) in anti-malware product allows deletion of files by creating a junction (CWE-1386) and using hard links during the time window in which a temporary file is created and deleted.
- **CVE-2014-0568**: Escape from sandbox for document reader by using a mountpoint [REF-1264]

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1386.html
