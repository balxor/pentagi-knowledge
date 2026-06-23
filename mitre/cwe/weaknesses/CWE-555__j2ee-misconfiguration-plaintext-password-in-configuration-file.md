---
cwe_id: CWE-555
name: J2EE Misconfiguration: Plaintext Password in Configuration File
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/555.html
tags: [mitre-cwe, weakness, CWE-555]
---

# CWE-555 - J2EE Misconfiguration: Plaintext Password in Configuration File

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-555](https://cwe.mitre.org/data/definitions/555.html)

## Description
The J2EE application stores a plaintext password in a configuration file.

## Extended description
Storing a plaintext password in a configuration file allows anyone who can read the file to access the password-protected resource, making it an easy target for attackers.

## Applicable platforms / languages
Java

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: Do not hardwire passwords into your software.
- **Architecture and Design**: Use industry standard libraries to encrypt passwords before storage in configuration files.

## Related weaknesses
- CWE-260 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/555.html
