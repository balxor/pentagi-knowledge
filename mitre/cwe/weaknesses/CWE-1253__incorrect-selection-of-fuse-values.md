---
cwe_id: CWE-1253
name: Incorrect Selection of Fuse Values
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-74]
url: https://cwe.mitre.org/data/definitions/1253.html
tags: [mitre-cwe, weakness, CWE-1253]
---

# CWE-1253 - Incorrect Selection of Fuse Values

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1253](https://cwe.mitre.org/data/definitions/1253.html)

## Description
The logic level used to set a system to a secure state relies on a fuse being unblown.

## Extended description
Fuses are often used to store secret data, including security configuration data. When not blown, a fuse is considered to store a logic 0, and, when blown, it indicates a logic 1. Fuses are generally considered to be one-directional, i.e., once blown to logic 1, it cannot be reset to logic 0.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Access Control, Authorization**: Bypass Protection Mechanism, Gain Privileges or Assume Identity
- **Availability**: DoS: Crash, Exit, or Restart
- **Confidentiality**: Read Memory
- **Integrity**: Modify Memory, Execute Unauthorized Code or Commands

## Potential mitigations
- **Architecture and Design**: Logic should be designed in a way that blown fuses do not put the product into an insecure state that can be leveraged by an attacker.

## Related attack patterns (CAPEC)
- [CAPEC-74](https://capec.mitre.org/data/definitions/74.html)

## Related weaknesses
- CWE-693 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1253.html
