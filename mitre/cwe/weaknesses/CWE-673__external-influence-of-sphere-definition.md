---
cwe_id: CWE-673
name: External Influence of Sphere Definition
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/673.html
tags: [mitre-cwe, weakness, CWE-673]
---

# CWE-673 - External Influence of Sphere Definition

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-673](https://cwe.mitre.org/data/definitions/673.html)

## Description
The product does not prevent the definition of control spheres from external actors.

## Extended description
Typically, a product defines its control sphere within the code itself, or through configuration by the product's administrator. In some cases, an external party can change the definition of the control sphere. This is typically a resultant weakness.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Other

## Related weaknesses
- CWE-664 (ChildOf)

## Observed examples (CVE)
- **CVE-2008-2613**: setuid program allows compromise using path that finds and loads a malicious library.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/673.html
