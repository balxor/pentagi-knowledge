---
cwe_id: CWE-471
name: Modification of Assumed-Immutable Data (MAID)
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, Web Based]
related_capec: [CAPEC-384, CAPEC-385, CAPEC-386, CAPEC-387, CAPEC-388]
url: https://cwe.mitre.org/data/definitions/471.html
tags: [mitre-cwe, weakness, CWE-471]
---

# CWE-471 - Modification of Assumed-Immutable Data (MAID)

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-471](https://cwe.mitre.org/data/definitions/471.html)

## Description
The product does not properly protect an assumed-immutable element from being modified by an attacker.

## Extended description
This occurs when a particular input is critical enough to the functioning of the application that it should not be modifiable at all, but it is. Certain resources are often assumed to be immutable when they are not, such as hidden form fields in web applications, cookies, and reverse DNS lookups.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based

## Common consequences
- **Integrity**: Modify Application Data
- **Integrity**: Unexpected State

## Potential mitigations
- **Architecture and Design, Operation, Implementation**: When the data is stored or transmitted through untrusted sources that could modify the data, implement integrity checks to detect unauthorized modification, or store/transmit the data in a trusted location that is free from external influence.

## Related attack patterns (CAPEC)
- [CAPEC-384](https://capec.mitre.org/data/definitions/384.html)
- [CAPEC-385](https://capec.mitre.org/data/definitions/385.html)
- [CAPEC-386](https://capec.mitre.org/data/definitions/386.html)
- [CAPEC-387](https://capec.mitre.org/data/definitions/387.html)
- [CAPEC-388](https://capec.mitre.org/data/definitions/388.html)

## Related weaknesses
- CWE-664 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-1757**: Relies on $PHP_SELF variable for authentication.
- **CVE-2005-1905**: Gain privileges by modifying assumed-immutable code addresses that are accessed by a driver.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/471.html
