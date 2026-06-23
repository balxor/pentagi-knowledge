---
cwe_id: CWE-12
name: ASP.NET Misconfiguration: Missing Custom Error Page
type: weakness
abstraction: Variant
status: Draft
languages: [ASP.NET]
related_capec: []
url: https://cwe.mitre.org/data/definitions/12.html
tags: [mitre-cwe, weakness, CWE-12]
---

# CWE-12 - ASP.NET Misconfiguration: Missing Custom Error Page

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-12](https://cwe.mitre.org/data/definitions/12.html)

## Description
An ASP .NET application must enable custom error pages in order to prevent attackers from mining information from the framework's built-in responses.

## Applicable platforms / languages
ASP.NET

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **System Configuration**: Handle exceptions appropriately in source code. ASP .NET applications should be configured to use custom error pages instead of the framework default page.
- **Architecture and Design**: Do not attempt to process an error or attempt to mask it.
- **Implementation**: Verify return values are correct and do not supply sensitive information about the system.

## Related weaknesses
- CWE-756 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/12.html
