---
cwe_id: CWE-403
name: Exposure of File Descriptor to Unintended Control Sphere ('File Descriptor Leak')
type: weakness
abstraction: Base
status: Draft
languages: [C, Not Language-Specific, Unix]
related_capec: []
url: https://cwe.mitre.org/data/definitions/403.html
tags: [mitre-cwe, weakness, CWE-403]
---

# CWE-403 - Exposure of File Descriptor to Unintended Control Sphere ('File Descriptor Leak')

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-403](https://cwe.mitre.org/data/definitions/403.html)

## Description
A process does not close sensitive file descriptors before invoking a child process, which allows the child to perform unauthorized I/O operations using those descriptors.

## Extended description
When a new process is forked or executed, the child process inherits any open file descriptors. When the child process has fewer privileges than the parent process, this might introduce a vulnerability if the child process can access the file descriptor but does not have the privileges to access the associated file.

## Applicable platforms / languages
C, Not Language-Specific, Unix

## Common consequences
- **Confidentiality, Integrity**: Read Application Data, Modify Application Data

## Related weaknesses
- CWE-402 (ChildOf)

## Observed examples (CVE)
- **CVE-2003-0740**: Server leaks a privileged file descriptor, allowing the server to be hijacked.
- **CVE-2004-1033**: File descriptor leak allows read of restricted files.
- **CVE-2000-0094**: Access to restricted resource using modified file descriptor for stderr.
- **CVE-2002-0638**: Open file descriptor used as alternate channel in complex race condition.
- **CVE-2003-0489**: Program does not fully drop privileges after creating a file descriptor, which allows access to the descriptor via a separate vulnerability.
- **CVE-2003-0937**: User bypasses restrictions by obtaining a file descriptor then calling setuid program, which does not close the descriptor.
- **CVE-2004-2215**: Terminal manager does not properly close file descriptors, allowing attackers to access terminals of other users.
- **CVE-2006-5397**: Module opens a file for reading twice, allowing attackers to read files.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/403.html
