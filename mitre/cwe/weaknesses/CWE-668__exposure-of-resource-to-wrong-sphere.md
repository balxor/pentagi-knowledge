---
cwe_id: CWE-668
name: Exposure of Resource to Wrong Sphere
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/668.html
tags: [mitre-cwe, weakness, CWE-668]
---

# CWE-668 - Exposure of Resource to Wrong Sphere

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-668](https://cwe.mitre.org/data/definitions/668.html)

## Description
The product exposes a resource to the wrong control sphere, providing unintended actors with inappropriate access to the resource.

## Extended description
Resources such as files and directories may be inadvertently exposed through mechanisms such as insecure permissions, or when a program accidentally operates on the wrong object. For example, a program may intend that private files can only be provided to a specific user. This effectively defines a control sphere that is intended to prevent attackers from accessing these private files. If the file permissions are insecure, then parties other than the user will be able to access those files. A separate control sphere might effectively require that the user can only access the private files, but not any other files on the system. If the program does not ensure that the user is only requesting private files, then the user might be able to access other files on the system. In either case, the end result is that a resource has been exposed to the wrong party.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data
- **Integrity**: Modify Application Data
- **Other**: Varies by Context

## Related weaknesses
- CWE-664 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/668.html
