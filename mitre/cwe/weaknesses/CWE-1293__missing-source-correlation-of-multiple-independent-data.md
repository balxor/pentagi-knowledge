---
cwe_id: CWE-1293
name: Missing Source Correlation of Multiple Independent Data
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1293.html
tags: [mitre-cwe, weakness, CWE-1293]
---

# CWE-1293 - Missing Source Correlation of Multiple Independent Data

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1293](https://cwe.mitre.org/data/definitions/1293.html)

## Description
The product relies on one source of data, preventing the ability to detect if an adversary has compromised a data source.

## Extended description
To operate successfully, a product sometimes has to implicitly trust the integrity of an information source. When information is implicitly signed, one can ensure that the data was not tampered in transit. This does not ensure that the information source was not compromised when responding to a request. By requesting information from multiple sources, one can check if all of the data is the same. If they are not, the system should report the information sources that respond with a different or minority value as potentially compromised. If there are not enough answers to provide a majority or plurality of responses, the system should report all of the sources as potentially compromised. As the seriousness of the impact of incorrect integrity increases, so should the number of independent information sources that would need to be queried.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Application Data, Modify Application Data, Gain Privileges or Assume Identity

## Potential mitigations
- **Requirements**: Design system to use a Practical Byzantine fault method, to request information from multiple sources to verify the data and report on potentially compromised information sources.
- **Implementation**: Failure to use a Practical Byzantine fault method when requesting data. Lack of place to report potentially compromised information sources. Relying on non-independent information sources for integrity checking. Failure to report information sources that respond in the minority to incident response procedures.

## Related weaknesses
- CWE-345 (ChildOf)
- CWE-654 (PeerOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1293.html
