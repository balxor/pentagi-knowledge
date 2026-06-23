---
cwe_id: CWE-256
name: Plaintext Storage of a Password
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, ICS/OT]
related_capec: []
url: https://cwe.mitre.org/data/definitions/256.html
tags: [mitre-cwe, weakness, CWE-256]
---

# CWE-256 - Plaintext Storage of a Password

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-256](https://cwe.mitre.org/data/definitions/256.html)

## Description
The product stores a password in plaintext within resources such as memory or files.

## Applicable platforms / languages
Not Language-Specific, ICS/OT

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Avoid storing passwords in easily accessible locations.
- **Architecture and Design**: Consider storing cryptographic hashes of passwords as an alternative to storing in plaintext.
- **general**: A programmer might attempt to remedy the password management problem by obscuring the password with an encoding function, such as base 64 encoding, but this effort does not adequately protect the password because the encoding can be detected and decoded easily.

## Related weaknesses
- CWE-522 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-30275**: Remote Terminal Unit (RTU) uses a driver that relies on a password stored in plaintext.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/256.html
