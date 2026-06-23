---
cwe_id: CWE-272
name: Least Privilege Violation
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-17, CAPEC-35, CAPEC-76]
url: https://cwe.mitre.org/data/definitions/272.html
tags: [mitre-cwe, weakness, CWE-272]
---

# CWE-272 - Least Privilege Violation

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-272](https://cwe.mitre.org/data/definitions/272.html)

## Description
The elevated privilege level required to perform operations such as chroot() should be dropped immediately after the operation is performed.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control, Confidentiality**: Gain Privileges or Assume Identity, Read Application Data, Read Files or Directories

## Potential mitigations
- **Architecture and Design, Operation**: Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.
- **Architecture and Design**: Follow the principle of least privilege when assigning access rights to entities in a software system.
- **Architecture and Design**: Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.

## Related attack patterns (CAPEC)
- [CAPEC-17](https://capec.mitre.org/data/definitions/17.html)
- [CAPEC-35](https://capec.mitre.org/data/definitions/35.html)
- [CAPEC-76](https://capec.mitre.org/data/definitions/76.html)

## Related weaknesses
- CWE-271 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/272.html
