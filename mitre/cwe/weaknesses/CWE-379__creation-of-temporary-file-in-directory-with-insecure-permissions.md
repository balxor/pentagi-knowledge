---
cwe_id: CWE-379
name: Creation of Temporary File in Directory with Insecure Permissions
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/379.html
tags: [mitre-cwe, weakness, CWE-379]
---

# CWE-379 - Creation of Temporary File in Directory with Insecure Permissions

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-379](https://cwe.mitre.org/data/definitions/379.html)

## Description
The product creates a temporary file in a directory whose permissions allow unintended actors to determine the file's existence or otherwise access that file.

## Extended description
On some operating systems, the fact that the temporary file exists may be apparent to any user with sufficient privileges to access that directory. Since the file is visible, the application that is using the temporary file could be known. If one has access to list the processes on the system, the attacker has gained information about what the user is doing at that time. By correlating this with the applications the user is running, an attacker could potentially discover what a user's actions are. From this, higher levels of security could be breached.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Requirements**: Many contemporary languages have functions which properly handle this condition. Older C temp file functions are especially susceptible.
- **Implementation**: Try to store sensitive tempfiles in a directory which is not world readable -- i.e., per-user directories.
- **Implementation**: Avoid using vulnerable temp file functions.

## Related weaknesses
- CWE-377 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-27818**: A hotkey daemon written in Rust creates a domain socket file underneath /tmp, which is accessible by any user.
- **CVE-2021-41989**: analytic platform's repair functionality uses the %TEMP% folder of a user while running with higher privileges
- **CVE-2021-21290**: A Java-based application for a rapid-development framework uses File.createTempFile() to create a random temporary file with insecure default permissions.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/379.html
