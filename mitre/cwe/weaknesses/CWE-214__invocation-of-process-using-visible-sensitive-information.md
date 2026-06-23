---
cwe_id: CWE-214
name: Invocation of Process Using Visible Sensitive Information
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/214.html
tags: [mitre-cwe, weakness, CWE-214]
---

# CWE-214 - Invocation of Process Using Visible Sensitive Information

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-214](https://cwe.mitre.org/data/definitions/214.html)

## Description
A process is invoked with sensitive command-line arguments, environment variables, or other elements that can be seen by other processes on the operating system.

## Extended description
Many operating systems allow a user to list information about processes that are owned by other users. Other users could see information such as command line arguments or environment variable settings. When this data contains sensitive information such as credentials, it might allow other users to launch an attack against the product or related resources.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Related weaknesses
- CWE-497 (ChildOf)

## Observed examples (CVE)
- **CVE-2023-38994**: IAM product includes LDAP password in a process call, allowing local users to obtain the password
- **CVE-2005-1387**: password passed on command line
- **CVE-2005-2291**: password passed on command line
- **CVE-2001-1565**: username/password on command line allows local users to view via "ps" or other process listing programs
- **CVE-2004-1948**: Username/password on command line allows local users to view via "ps" or other process listing programs.
- **CVE-1999-1270**: PGP passphrase provided as command line argument.
- **CVE-2004-1058**: Kernel race condition allows reading of environment variables of a process that is still spawning.
- **CVE-2021-32638**: Code analysis product passes access tokens as a command-line parameter or through an environment variable, making them visible to other processes via the ps command.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/214.html
