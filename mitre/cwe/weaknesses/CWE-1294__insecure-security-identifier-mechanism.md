---
cwe_id: CWE-1294
name: Insecure Security Identifier Mechanism
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Bus/Interface Hardware, Not Technology-Specific]
related_capec: [CAPEC-121, CAPEC-681]
url: https://cwe.mitre.org/data/definitions/1294.html
tags: [mitre-cwe, weakness, CWE-1294]
---

# CWE-1294 - Insecure Security Identifier Mechanism

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-1294](https://cwe.mitre.org/data/definitions/1294.html)

## Description
The System-on-Chip (SoC) implements a Security Identifier mechanism to differentiate what actions are allowed or disallowed when a transaction originates from an entity. However, the Security Identifiers are not correctly implemented.

## Extended description
Systems-On-Chip (Integrated circuits and hardware engines) implement Security Identifiers to differentiate/identify actions originated from various agents. These actions could be 'read', 'write', 'program', 'reset', 'fetch', 'compute', etc. Security identifiers are generated and assigned to every agent in the System (SoC) that is either capable of generating an action or receiving an action from another agent. Every agent could be assigned a unique, Security Identifier based on its trust level or privileges. A broad class of flaws can exist in the Security Identifier process, including but not limited to missing security identifiers, improper conversion of security identifiers, incorrect generation of security identifiers, etc.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Bus/Interface Hardware, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Availability, Access Control**: Modify Memory, Read Memory, DoS: Resource Consumption (Other), Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity, Quality Degradation

## Potential mitigations
- **Architecture and Design**: Security Identifier Decoders must be reviewed for design inconsistency and common weaknesses.
- **Implementation**: Access and programming flows must be tested in pre-silicon and post-silicon testing.

## Related attack patterns (CAPEC)
- [CAPEC-121](https://capec.mitre.org/data/definitions/121.html)
- [CAPEC-681](https://capec.mitre.org/data/definitions/681.html)

## Related weaknesses
- CWE-284 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1294.html
