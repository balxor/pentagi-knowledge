---
cwe_id: CWE-201
name: Insertion of Sensitive Information Into Sent Data
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-12, CAPEC-217, CAPEC-612, CAPEC-613, CAPEC-618, CAPEC-619, CAPEC-621, CAPEC-622, CAPEC-623]
url: https://cwe.mitre.org/data/definitions/201.html
tags: [mitre-cwe, weakness, CWE-201]
---

# CWE-201 - Insertion of Sensitive Information Into Sent Data

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-201](https://cwe.mitre.org/data/definitions/201.html)

## Description
The code transmits data to another actor, but a portion of the data includes sensitive information that should not be accessible to that actor.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Files or Directories, Read Memory, Read Application Data

## Potential mitigations
- **Requirements**: Specify which data in the software should be regarded as sensitive. Consider which types of users should have access to which types of data.
- **Implementation**: Ensure that any possibly sensitive data specified in the requirements is verified with designers to ensure that it is either a calculated risk or mitigated elsewhere. Any information that is not necessary to the functionality should be removed in order to lower both the overhead and the possibility of security sensitive data being sent.
- **System Configuration**: Setup default error messages so that unexpected errors do not disclose sensitive information.
- **Architecture and Design**: Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.

## Related attack patterns (CAPEC)
- [CAPEC-12](https://capec.mitre.org/data/definitions/12.html)
- [CAPEC-217](https://capec.mitre.org/data/definitions/217.html)
- [CAPEC-612](https://capec.mitre.org/data/definitions/612.html)
- [CAPEC-613](https://capec.mitre.org/data/definitions/613.html)
- [CAPEC-618](https://capec.mitre.org/data/definitions/618.html)
- [CAPEC-619](https://capec.mitre.org/data/definitions/619.html)
- [CAPEC-621](https://capec.mitre.org/data/definitions/621.html)
- [CAPEC-622](https://capec.mitre.org/data/definitions/622.html)
- [CAPEC-623](https://capec.mitre.org/data/definitions/623.html)

## Related weaknesses
- CWE-200 (ChildOf)
- CWE-209 (CanAlsoBe)
- CWE-202 (CanAlsoBe)

## Observed examples (CVE)
- **CVE-2023-27265**: collaboration platform does not honor a "show email address" setting for a response by an API endpoint
- **CVE-2023-32275**: RPC server for a VPN product returns an object that contains heap addresses
- **CVE-2022-0708**: Collaboration platform does not clear team emails in a response, allowing leak of email addresses

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/201.html
