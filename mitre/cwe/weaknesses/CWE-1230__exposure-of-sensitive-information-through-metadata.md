---
cwe_id: CWE-1230
name: Exposure of Sensitive Information Through Metadata
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1230.html
tags: [mitre-cwe, weakness, CWE-1230]
---

# CWE-1230 - Exposure of Sensitive Information Through Metadata

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1230](https://cwe.mitre.org/data/definitions/1230.html)

## Description
The product prevents direct access to a resource containing sensitive information, but it does not sufficiently limit access to metadata that is derived from the original, sensitive information.

## Extended description
Developers might correctly prevent unauthorized access to a database or other resource containing sensitive information, but they might not consider that portions of the original information might also be recorded in metadata, search indices, statistical reports, or other resources. If these resources are not also restricted, then attackers might be able to extract some or all of the original information, or otherwise infer some details. For example, an attacker could specify search terms that are known to be unique to a particular person, or view metadata such as activity or creation dates in order to identify usage patterns.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Related weaknesses
- CWE-285 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1230.html
