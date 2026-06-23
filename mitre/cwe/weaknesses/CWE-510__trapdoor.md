---
cwe_id: CWE-510
name: Trapdoor
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/510.html
tags: [mitre-cwe, weakness, CWE-510]
---

# CWE-510 - Trapdoor

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-510](https://cwe.mitre.org/data/definitions/510.html)

## Description
A trapdoor is a hidden piece of code that responds to a special input, allowing its user access to resources without passing through the normal security enforcement mechanism.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity, Availability, Access Control**: Execute Unauthorized Code or Commands, Bypass Protection Mechanism

## Potential mitigations
- **Installation**: Always verify the integrity of the software that is being installed.
- **Testing**: Identify and closely inspect the conditions for entering privileged areas of the code, especially those related to authentication, process invocation, and network communications.

## Related weaknesses
- CWE-506 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/510.html
