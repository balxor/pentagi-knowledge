---
cwe_id: CWE-354
name: Improper Validation of Integrity Check Value
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-145, CAPEC-463, CAPEC-75]
url: https://cwe.mitre.org/data/definitions/354.html
tags: [mitre-cwe, weakness, CWE-354]
---

# CWE-354 - Improper Validation of Integrity Check Value

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-354](https://cwe.mitre.org/data/definitions/354.html)

## Description
The product does not validate or incorrectly validates the integrity check values or "checksums" of a message. This may prevent it from detecting if the data has been modified or corrupted in transmission.

## Extended description
Improper validation of checksums before use results in an unnecessary risk that can easily be mitigated. The protocol specification describes the algorithm used for calculating the checksum. It is then a simple matter of implementing the calculation and verifying that the calculated checksum and the received checksum match. Improper verification of the calculated checksum and the received checksum can lead to far greater consequences.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Other**: Modify Application Data, Other
- **Integrity, Other**: Other
- **Non-Repudiation, Other**: Hide Activities, Other

## Potential mitigations
- **Implementation**: Ensure that the checksums present in messages are properly checked in accordance with the protocol specification before they are parsed and used.

## Related attack patterns (CAPEC)
- [CAPEC-145](https://capec.mitre.org/data/definitions/145.html)
- [CAPEC-463](https://capec.mitre.org/data/definitions/463.html)
- [CAPEC-75](https://capec.mitre.org/data/definitions/75.html)

## Related weaknesses
- CWE-345 (ChildOf)
- CWE-345 (ChildOf)
- CWE-754 (ChildOf)
- CWE-353 (PeerOf)

## Observed examples (CVE)
- **CVE-2024-47573**: network analysis tool does not properly validate an integrity check value, allowing installation of malicious firmware

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/354.html
