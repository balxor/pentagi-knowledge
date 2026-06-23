---
cwe_id: CWE-529
name: Exposure of Access Control List Files to an Unauthorized Control Sphere
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/529.html
tags: [mitre-cwe, weakness, CWE-529]
---

# CWE-529 - Exposure of Access Control List Files to an Unauthorized Control Sphere

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-529](https://cwe.mitre.org/data/definitions/529.html)

## Description
The product stores access control list files in a directory or other container that is accessible to actors outside of the intended control sphere.

## Extended description
Exposure of these access control list files may give the attacker information about the configuration of the site or system. This information may then be used to bypass the intended security policy or identify trusted systems from which an attack can be launched.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Access Control**: Read Application Data, Bypass Protection Mechanism

## Potential mitigations
- **System Configuration**: Protect access control list files.

## Related weaknesses
- CWE-552 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/529.html
