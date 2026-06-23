---
cwe_id: CWE-13
name: ASP.NET Misconfiguration: Password in Configuration File
type: weakness
abstraction: Variant
status: Draft
languages: [ASP.NET]
related_capec: []
url: https://cwe.mitre.org/data/definitions/13.html
tags: [mitre-cwe, weakness, CWE-13]
---

# CWE-13 - ASP.NET Misconfiguration: Password in Configuration File

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-13](https://cwe.mitre.org/data/definitions/13.html)

## Description
Storing a plaintext password in a configuration file allows anyone who can read the file access to the password-protected resource making them an easy target for attackers.

## Applicable platforms / languages
ASP.NET

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Implementation**: Credentials stored in configuration files should be encrypted, Use standard APIs and industry accepted algorithms to encrypt the credentials stored in configuration files.

## Related weaknesses
- CWE-260 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/13.html
