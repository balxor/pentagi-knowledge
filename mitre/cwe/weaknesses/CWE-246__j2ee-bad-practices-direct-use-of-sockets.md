---
cwe_id: CWE-246
name: J2EE Bad Practices: Direct Use of Sockets
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/246.html
tags: [mitre-cwe, weakness, CWE-246]
---

# CWE-246 - J2EE Bad Practices: Direct Use of Sockets

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-246](https://cwe.mitre.org/data/definitions/246.html)

## Description
The J2EE application directly uses sockets instead of using framework method calls.

## Extended description
The J2EE standard permits the use of sockets only for the purpose of communication with legacy systems when no higher-level protocol is available. Authoring your own communication protocol requires wrestling with difficult security issues. Without significant scrutiny by a security expert, chances are good that a custom communication protocol will suffer from security problems. Many of the same issues apply to a custom implementation of a standard protocol. While there are usually more resources available that address security concerns related to implementing a standard protocol, these resources are also available to attackers.

## Applicable platforms / languages
Java

## Common consequences
- **Other**: Quality Degradation

## Potential mitigations
- **Architecture and Design**: Use framework method calls instead of using sockets directly.

## Related weaknesses
- CWE-695 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/246.html
