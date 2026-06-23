---
cwe_id: CWE-353
name: Missing Support for Integrity Check
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-13, CAPEC-14, CAPEC-389, CAPEC-39, CAPEC-665, CAPEC-74, CAPEC-75]
url: https://cwe.mitre.org/data/definitions/353.html
tags: [mitre-cwe, weakness, CWE-353]
---

# CWE-353 - Missing Support for Integrity Check

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-353](https://cwe.mitre.org/data/definitions/353.html)

## Description
The product uses a transmission protocol that does not include a mechanism for verifying the integrity of the data during transmission, such as a checksum.

## Extended description
If integrity check values or "checksums" are omitted from a protocol, there is no way of determining if data has been corrupted in transmission. The lack of checksum functionality in a protocol removes the first application-level check of data that can be used. The end-to-end philosophy of checks states that integrity checks should be performed at the lowest level that they can be completely implemented. Excluding further sanity checks and input validation performed by applications, the protocol's checksum is the most important level of checksum, since it can be performed more completely than at any previous level and takes into account entire messages, as opposed to single packets.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Other**: Other
- **Non-Repudiation, Other**: Hide Activities, Other

## Potential mitigations
- **Architecture and Design**: Add an appropriately sized checksum to the protocol, ensuring that data received may be simply validated before it is parsed and used.
- **Implementation**: Ensure that the checksums present in the protocol design are properly implemented and added to each message before it is sent.

## Related attack patterns (CAPEC)
- [CAPEC-13](https://capec.mitre.org/data/definitions/13.html)
- [CAPEC-14](https://capec.mitre.org/data/definitions/14.html)
- [CAPEC-389](https://capec.mitre.org/data/definitions/389.html)
- [CAPEC-39](https://capec.mitre.org/data/definitions/39.html)
- [CAPEC-665](https://capec.mitre.org/data/definitions/665.html)
- [CAPEC-74](https://capec.mitre.org/data/definitions/74.html)
- [CAPEC-75](https://capec.mitre.org/data/definitions/75.html)

## Related weaknesses
- CWE-345 (ChildOf)
- CWE-354 (PeerOf)

## Observed examples (CVE)
- **CVE-2025-32890**: Mesh device uses a cryptographic algorithm without integrity checking, allowing modification of messages

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/353.html
