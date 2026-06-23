---
cwe_id: CWE-279
name: Incorrect Execution-Assigned Permissions
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-81]
url: https://cwe.mitre.org/data/definitions/279.html
tags: [mitre-cwe, weakness, CWE-279]
---

# CWE-279 - Incorrect Execution-Assigned Permissions

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-279](https://cwe.mitre.org/data/definitions/279.html)

## Description
While it is executing, the product sets the permissions of an object in a way that violates the intended permissions that have been specified by the user.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Application Data, Modify Application Data

## Potential mitigations
- **Architecture and Design, Operation**: Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.
- **Architecture and Design**: Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.

## Related attack patterns (CAPEC)
- [CAPEC-81](https://capec.mitre.org/data/definitions/81.html)

## Related weaknesses
- CWE-732 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-0265**: Log files opened read/write.
- **CVE-2003-0876**: Log files opened read/write.
- **CVE-2002-1694**: Log files opened read/write.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/279.html
