---
cwe_id: CWE-1270
name: Generation of Incorrect Security Tokens
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-121, CAPEC-633, CAPEC-681]
url: https://cwe.mitre.org/data/definitions/1270.html
tags: [mitre-cwe, weakness, CWE-1270]
---

# CWE-1270 - Generation of Incorrect Security Tokens

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1270](https://cwe.mitre.org/data/definitions/1270.html)

## Description
The product implements a Security Token mechanism to differentiate what actions are allowed or disallowed when a transaction originates from an entity. However, the Security Tokens generated in the system are incorrect.

## Extended description
Systems-On-a-Chip (SoC) (Integrated circuits and hardware engines) implement Security Tokens to differentiate and identify actions originated from various agents. These actions could be "read", "write", "program", "reset", "fetch", "compute", etc. Security Tokens are generated and assigned to every agent on the SoC that is either capable of generating an action or receiving an action from another agent. Every agent could be assigned a unique, Security Token based on its trust level or privileges.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Availability, Access Control**: Modify Files or Directories, Execute Unauthorized Code or Commands, Bypass Protection Mechanism, Gain Privileges or Assume Identity, Read Memory, Modify Memory, DoS: Crash, Exit, or Restart

## Potential mitigations
- **Architecture and Design, Implementation**: Generation of Security Tokens should be reviewed for design inconsistency and common weaknesses. Security-Token definition and programming flow should be tested in pre-silicon and post-silicon testing.

## Related attack patterns (CAPEC)
- [CAPEC-121](https://capec.mitre.org/data/definitions/121.html)
- [CAPEC-633](https://capec.mitre.org/data/definitions/633.html)
- [CAPEC-681](https://capec.mitre.org/data/definitions/681.html)

## Related weaknesses
- CWE-284 (ChildOf)
- CWE-1294 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1270.html
