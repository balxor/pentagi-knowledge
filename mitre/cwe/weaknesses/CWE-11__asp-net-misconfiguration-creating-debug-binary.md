---
cwe_id: CWE-11
name: ASP.NET Misconfiguration: Creating Debug Binary
type: weakness
abstraction: Variant
status: Draft
languages: [ASP.NET]
related_capec: []
url: https://cwe.mitre.org/data/definitions/11.html
tags: [mitre-cwe, weakness, CWE-11]
---

# CWE-11 - ASP.NET Misconfiguration: Creating Debug Binary

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-11](https://cwe.mitre.org/data/definitions/11.html)

## Description
Debugging messages help attackers learn about the system and plan a form of attack.

## Extended description
ASP .NET applications can be configured to produce debug binaries. These binaries give detailed debugging messages and should not be used in production environments. Debug binaries are meant to be used in a development or testing environment and can pose a security risk if they are deployed to production.

## Applicable platforms / languages
ASP.NET

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **System Configuration**: Avoid releasing debug binaries into the production environment. Change the debug mode to false when the application is deployed into production.

## Related weaknesses
- CWE-489 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/11.html
