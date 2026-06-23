---
cwe_id: CWE-277
name: Insecure Inherited Permissions
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/277.html
tags: [mitre-cwe, weakness, CWE-277]
---

# CWE-277 - Insecure Inherited Permissions

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-277](https://cwe.mitre.org/data/definitions/277.html)

## Description
A product defines a set of insecure permissions that are inherited by objects that are created by the program.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Application Data, Modify Application Data

## Potential mitigations
- **Architecture and Design, Operation**: Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.
- **Architecture and Design**: Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.

## Related weaknesses
- CWE-732 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-1841**: User's umask is used when creating temp files.
- **CVE-2002-1786**: Insecure umask for core dumps [is the umask preserved or assigned?].

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/277.html
