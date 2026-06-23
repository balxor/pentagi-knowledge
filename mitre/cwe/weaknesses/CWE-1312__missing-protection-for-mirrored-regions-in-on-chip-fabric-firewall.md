---
cwe_id: CWE-1312
name: Missing Protection for Mirrored Regions in On-Chip Fabric Firewall
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-456, CAPEC-679]
url: https://cwe.mitre.org/data/definitions/1312.html
tags: [mitre-cwe, weakness, CWE-1312]
---

# CWE-1312 - Missing Protection for Mirrored Regions in On-Chip Fabric Firewall

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1312](https://cwe.mitre.org/data/definitions/1312.html)

## Description
The firewall in an on-chip fabric protects the main addressed region, but it does not protect any mirrored memory or memory-mapped-IO (MMIO) regions.

## Extended description
Few fabrics mirror memory and address ranges, where mirrored regions contain copies of the original data. This redundancy is used to achieve fault tolerance. Whatever protections the fabric firewall implements for the original region should also apply to the mirrored regions. If not, an attacker could bypass existing read/write protections by reading from/writing to the mirrored regions to leak or corrupt the original data.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Access Control**: Modify Memory, Read Memory, Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: The fabric firewall should apply the same protections as the original region to the mirrored regions.
- **Implementation**: The fabric firewall should apply the same protections as the original region to the mirrored regions.

## Related attack patterns (CAPEC)
- [CAPEC-456](https://capec.mitre.org/data/definitions/456.html)
- [CAPEC-679](https://capec.mitre.org/data/definitions/679.html)

## Related weaknesses
- CWE-284 (ChildOf)
- CWE-1251 (PeerOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1312.html
