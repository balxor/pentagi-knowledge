---
cwe_id: CWE-556
name: ASP.NET Misconfiguration: Use of Identity Impersonation
type: weakness
abstraction: Variant
status: Incomplete
languages: [ASP.NET]
related_capec: []
url: https://cwe.mitre.org/data/definitions/556.html
tags: [mitre-cwe, weakness, CWE-556]
---

# CWE-556 - ASP.NET Misconfiguration: Use of Identity Impersonation

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-556](https://cwe.mitre.org/data/definitions/556.html)

## Description
Configuring an ASP.NET application to run with impersonated credentials may give the application unnecessary privileges.

## Extended description
The use of impersonated credentials allows an ASP.NET application to run with either the privileges of the client on whose behalf it is executing or with arbitrary privileges granted in its configuration.

## Applicable platforms / languages
ASP.NET

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Use the least privilege principle.

## Related weaknesses
- CWE-266 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/556.html
