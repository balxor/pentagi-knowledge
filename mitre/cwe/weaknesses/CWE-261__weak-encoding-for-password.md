---
cwe_id: CWE-261
name: Weak Encoding for Password
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-55]
url: https://cwe.mitre.org/data/definitions/261.html
tags: [mitre-cwe, weakness, CWE-261]
---

# CWE-261 - Weak Encoding for Password

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-261](https://cwe.mitre.org/data/definitions/261.html)

## Description
Obscuring a password with a trivial encoding does not protect the password.

## Extended description
Password management issues occur when a password is stored in plaintext in an application's properties or configuration file. A programmer can attempt to remedy the password management problem by obscuring the password with an encoding function, such as base 64 encoding, but this effort does not adequately protect the password.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **general**: Passwords should be encrypted with keys that are at least 128 bits in length for adequate security.

## Related attack patterns (CAPEC)
- [CAPEC-55](https://capec.mitre.org/data/definitions/55.html)

## Related weaknesses
- CWE-522 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-45099**: network attached storage (NAS) product uses weak encoding for a password

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/261.html
