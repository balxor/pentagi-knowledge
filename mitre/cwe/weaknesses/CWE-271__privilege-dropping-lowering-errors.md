---
cwe_id: CWE-271
name: Privilege Dropping / Lowering Errors
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/271.html
tags: [mitre-cwe, weakness, CWE-271]
---

# CWE-271 - Privilege Dropping / Lowering Errors

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-271](https://cwe.mitre.org/data/definitions/271.html)

## Description
The product does not drop privileges before passing control of a resource to an actor that does not have those privileges.

## Extended description
In some contexts, a system executing with elevated permissions will hand off a process/file/etc. to another process or user. If the privileges of an entity are not reduced, then elevated privileges are spread throughout a system and possibly to an attacker.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity
- **Access Control, Non-Repudiation**: Gain Privileges or Assume Identity, Hide Activities

## Potential mitigations
- **Architecture and Design**: Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.
- **Architecture and Design, Operation**: Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.
- **Architecture and Design**: Consider following the principle of separation of privilege. Require multiple conditions to be met before permitting access to a system resource.

## Related weaknesses
- CWE-269 (ChildOf)

## Observed examples (CVE)
- **CVE-2000-1213**: Program does not drop privileges after acquiring the raw socket.
- **CVE-2001-0559**: Setuid program does not drop privileges after a parsing error occurs, then calls another program to handle the error.
- **CVE-2001-0787**: Does not drop privileges in related groups when lowering privileges.
- **CVE-2002-0080**: Does not drop privileges in related groups when lowering privileges.
- **CVE-2001-1029**: Does not drop privileges before determining access to certain files.
- **CVE-1999-0813**: Finger daemon does not drop privileges when executing programs on behalf of the user being fingered.
- **CVE-1999-1326**: FTP server does not drop privileges if a connection is aborted during file transfer.
- **CVE-2000-0172**: Program only uses seteuid to drop privileges.
- **CVE-2004-2504**: Windows program running as SYSTEM does not drop privileges before executing other programs (many others like this, especially involving the Help facility).
- **CVE-2004-0213**: Utility Manager launches winhlp32.exe while running with raised privileges, which allows local users to gain system privileges.
- **CVE-2004-0806**: Setuid program does not drop privileges before executing program specified in an environment variable.
- **CVE-2004-0828**: Setuid program does not drop privileges before processing file specified on command line.
- **CVE-2004-2070**: Service on Windows does not drop privileges before using "view file" option, allowing code execution.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/271.html
