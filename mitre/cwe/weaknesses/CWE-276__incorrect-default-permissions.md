---
cwe_id: CWE-276
name: Incorrect Default Permissions
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, ICS/OT]
related_capec: [CAPEC-1, CAPEC-127, CAPEC-81]
url: https://cwe.mitre.org/data/definitions/276.html
tags: [mitre-cwe, weakness, CWE-276]
---

# CWE-276 - Incorrect Default Permissions

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-276](https://cwe.mitre.org/data/definitions/276.html)

## Description
During installation, installed file permissions are set to allow anyone to modify those files.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, ICS/OT

## Common consequences
- **Confidentiality, Integrity**: Read Application Data, Modify Application Data

## Potential mitigations
- **Architecture and Design, Operation**: The architecture needs to access and modification attributes for files to only those users who actually require those actions.
- **Architecture and Design**: Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.

## Related attack patterns (CAPEC)
- [CAPEC-1](https://capec.mitre.org/data/definitions/1.html)
- [CAPEC-127](https://capec.mitre.org/data/definitions/127.html)
- [CAPEC-81](https://capec.mitre.org/data/definitions/81.html)

## Related weaknesses
- CWE-732 (ChildOf)
- CWE-732 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-1941**: Executables installed world-writable.
- **CVE-2002-1713**: Home directories installed world-readable.
- **CVE-2001-1550**: World-writable log files allow information loss; world-readable file has cleartext passwords.
- **CVE-2002-1711**: World-readable directory.
- **CVE-2002-1844**: Windows product uses insecure permissions when installing on Solaris (genesis: port error).
- **CVE-2001-0497**: Insecure permissions for a shared secret key file. Overlaps cryptographic problem.
- **CVE-1999-0426**: Default permissions of a device allow IP spoofing.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/276.html
