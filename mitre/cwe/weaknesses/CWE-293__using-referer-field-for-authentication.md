---
cwe_id: CWE-293
name: Using Referer Field for Authentication
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/293.html
tags: [mitre-cwe, weakness, CWE-293]
---

# CWE-293 - Using Referer Field for Authentication

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-293](https://cwe.mitre.org/data/definitions/293.html)

## Description
The referer field in HTTP requests can be easily modified and, as such, is not a valid means of message integrity checking.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: In order to usefully check if a given action is authorized, some means of strong authentication and method protection must be used. Use other means of authorization that cannot be simply spoofed. Possibilities include a username/password or certificate.

## Related weaknesses
- CWE-290 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/293.html
