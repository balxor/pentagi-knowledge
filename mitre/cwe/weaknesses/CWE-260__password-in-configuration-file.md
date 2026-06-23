---
cwe_id: CWE-260
name: Password in Configuration File
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/260.html
tags: [mitre-cwe, weakness, CWE-260]
---

# CWE-260 - Password in Configuration File

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-260](https://cwe.mitre.org/data/definitions/260.html)

## Description
The product stores a password in a configuration file that might be accessible to actors who do not know the password.

## Extended description
This can result in compromise of the system for which the password is used. An attacker could gain access to this file and learn the stored password or worse yet, change the password to one of their choosing.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Avoid storing passwords in easily accessible locations.
- **Architecture and Design**: Consider storing cryptographic hashes of passwords as an alternative to storing in plaintext.

## Related weaknesses
- CWE-522 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-38665**: A continuous delivery pipeline management tool stores an unencypted password in a configuration file.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/260.html
