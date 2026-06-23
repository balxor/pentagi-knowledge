---
cwe_id: CWE-424
name: Improper Protection of Alternate Path
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, Web Based]
related_capec: [CAPEC-127, CAPEC-554]
url: https://cwe.mitre.org/data/definitions/424.html
tags: [mitre-cwe, weakness, CWE-424]
---

# CWE-424 - Improper Protection of Alternate Path

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-424](https://cwe.mitre.org/data/definitions/424.html)

## Description
The product does not sufficiently protect all possible paths that a user can take to access restricted functionality or resources.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based

## Common consequences
- **Access Control**: Bypass Protection Mechanism, Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Deploy different layers of protection to implement security in depth.

## Related attack patterns (CAPEC)
- [CAPEC-127](https://capec.mitre.org/data/definitions/127.html)
- [CAPEC-554](https://capec.mitre.org/data/definitions/554.html)

## Related weaknesses
- CWE-693 (ChildOf)
- CWE-638 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-29238**: Access-control setting in web-based document collaboration tool is not properly implemented by the code, which prevents listing hidden directories but does not prevent direct requests to files in those directories.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/424.html
