---
cwe_id: CWE-273
name: Improper Check for Dropped Privileges
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/273.html
tags: [mitre-cwe, weakness, CWE-273]
---

# CWE-273 - Improper Check for Dropped Privileges

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-273](https://cwe.mitre.org/data/definitions/273.html)

## Description
The product attempts to drop privileges but does not check or incorrectly checks to see if the drop succeeded.

## Extended description
If the drop fails, the product will continue to run with the raised privileges, which might provide additional access to unprivileged users.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity
- **Access Control, Non-Repudiation**: Gain Privileges or Assume Identity, Hide Activities

## Potential mitigations
- **Architecture and Design**: Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.
- **Implementation**: Check the results of all functions that return a value and verify that the value is expected.
- **Implementation**: In Windows, make sure that the process token has the SeImpersonatePrivilege(Microsoft Server 2003). Code that relies on impersonation for security must ensure that the impersonation succeeded, i.e., that a proper privilege demotion happened.

## Related weaknesses
- CWE-754 (ChildOf)
- CWE-754 (ChildOf)
- CWE-271 (ChildOf)
- CWE-252 (PeerOf)

## Observed examples (CVE)
- **CVE-2006-4447**: Program does not check return value when invoking functions to drop privileges, which could leave users with higher privileges than expected by forcing those functions to fail.
- **CVE-2006-2916**: Program does not check return value when invoking functions to drop privileges, which could leave users with higher privileges than expected by forcing those functions to fail.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/273.html
