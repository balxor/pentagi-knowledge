---
cwe_id: CWE-305
name: Authentication Bypass by Primary Weakness
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/305.html
tags: [mitre-cwe, weakness, CWE-305]
---

# CWE-305 - Authentication Bypass by Primary Weakness

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-305](https://cwe.mitre.org/data/definitions/305.html)

## Description
The authentication algorithm is sound, but the implemented mechanism can be bypassed as the result of a separate weakness that is primary to the authentication error.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Related weaknesses
- CWE-1390 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-1374**: The provided password is only compared against the first character of the real password.
- **CVE-2000-0979**: The password is not properly checked, which allows remote attackers to bypass access controls by sending a 1-byte password that matches the first character of the real password.
- **CVE-2001-0088**: Chain: Forum software does not properly initialize an array, which inadvertently sets the password to a single character, allowing remote attackers to easily guess the password and gain administrative privileges.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/305.html
