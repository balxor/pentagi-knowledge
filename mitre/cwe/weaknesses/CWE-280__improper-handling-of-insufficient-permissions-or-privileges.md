---
cwe_id: CWE-280
name: Improper Handling of Insufficient Permissions or Privileges
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/280.html
tags: [mitre-cwe, weakness, CWE-280]
---

# CWE-280 - Improper Handling of Insufficient Permissions or Privileges

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-280](https://cwe.mitre.org/data/definitions/280.html)

## Description
The product does not handle or incorrectly handles when it has insufficient privileges to access resources or functionality as specified by their permissions. This may cause it to follow unexpected code paths that may leave the product in an invalid state.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Other, Alter Execution Logic

## Potential mitigations
- **Architecture and Design**: Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.
- **Implementation**: Always check to see if you have successfully accessed a resource or system functionality, and use proper error handling if it is unsuccessful. Do this even when you are operating in a highly privileged mode, because errors or environmental conditions might still cause a failure. For example, environments with highly granular permissions/privilege models, such as Windows or Linux capabilities, can cause unexpected failures.

## Related weaknesses
- CWE-755 (ChildOf)

## Observed examples (CVE)
- **CVE-2003-0501**: Special file system allows attackers to prevent ownership/permission change of certain entries by opening the entries before calling a setuid program.
- **CVE-2004-0148**: FTP server places a user in the root directory when the user's permissions prevent access to the their own home directory.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/280.html
