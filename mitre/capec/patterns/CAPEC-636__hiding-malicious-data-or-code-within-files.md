---
capec_id: CAPEC-636
name: Hiding Malicious Data or Code within Files
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: High
related_cwe: [CWE-506]
related_attack: [T1001.002, T1027.003, T1027.004, T1218.001, T1221]
url: https://capec.mitre.org/data/definitions/636.html
tags: [mitre-capec, attack-pattern, CAPEC-636]
---

# CAPEC-636 - Hiding Malicious Data or Code within Files

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** High  -  **CAPEC:** [CAPEC-636](https://capec.mitre.org/data/definitions/636.html)

## Description
Files on various operating systems can have a complex format which allows for the storage of other data, in addition to its contents. Often this is metadata about the file, such as a cached thumbnail for an image file. Unless utilities are invoked in a particular way, this data is not visible during the normal use of the file. It is possible for an attacker to store malicious data or code using these facilities, which would be difficult to discover.

## Prerequisites
- The operating system must support a file system that allows for alternate data storage for a file.

## Mitigations
- Many tools are available to search for the hidden data. Scan regularly for such data using one of these tools.

## Related weaknesses (CWE)
- [CWE-506](https://cwe.mitre.org/data/definitions/506.html)

## Related ATT&CK techniques
- T1001.002
- T1027.003
- T1027.004
- T1218.001
- T1221

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/636.html
