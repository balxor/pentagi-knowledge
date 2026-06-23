---
cwe_id: CWE-324
name: Use of a Key Past its Expiration Date
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/324.html
tags: [mitre-cwe, weakness, CWE-324]
---

# CWE-324 - Use of a Key Past its Expiration Date

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-324](https://cwe.mitre.org/data/definitions/324.html)

## Description
The product uses a cryptographic key or password past its expiration date, which diminishes its safety significantly by increasing the timing window for cracking attacks against that key.

## Extended description
While the expiration of keys does not necessarily ensure that they are compromised, it is a significant concern that keys which remain in use for prolonged periods of time have a decreasing probability of integrity. For this reason, it is important to replace keys within a period of time proportional to their strength.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism, Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Adequate consideration should be put in to the user interface in order to notify users previous to the key's expiration, to explain the importance of new key generation and to walk users through the process as painlessly as possible.

## Related weaknesses
- CWE-672 (ChildOf)
- CWE-298 (PeerOf)

## Observed examples (CVE)
- **CVE-2021-33020**: Picture Archiving and Communication System (PACS) system for hospitals uses a cryptographic key or password past its expiration date

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/324.html
