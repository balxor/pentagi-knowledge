---
cwe_id: CWE-1229
name: Creation of Emergent Resource
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1229.html
tags: [mitre-cwe, weakness, CWE-1229]
---

# CWE-1229 - Creation of Emergent Resource

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-1229](https://cwe.mitre.org/data/definitions/1229.html)

## Description
The product manages resources or behaves in a way that indirectly creates a new, distinct resource that can be used by attackers in violation of the intended policy.

## Extended description
A product is only expected to behave in a way that was specifically intended by the developer. Resource allocation and management is expected to be performed explicitly by the associated code. However, in systems with complex behavior, the product might indirectly produce new kinds of resources that were never intended in the original design. For example, a covert channel is a resource that was never explicitly intended by the developer, but it is useful to attackers. "Parasitic computing," while not necessarily malicious in nature, effectively tricks a product into performing unintended computations on behalf of another party.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific

## Common consequences
- **Other**: Varies by Context

## Related weaknesses
- CWE-664 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1229.html
