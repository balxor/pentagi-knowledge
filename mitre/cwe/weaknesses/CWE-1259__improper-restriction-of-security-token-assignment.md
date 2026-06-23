---
cwe_id: CWE-1259
name: Improper Restriction of Security Token Assignment
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Processor Hardware, System on Chip]
related_capec: [CAPEC-121, CAPEC-681]
url: https://cwe.mitre.org/data/definitions/1259.html
tags: [mitre-cwe, weakness, CWE-1259]
---

# CWE-1259 - Improper Restriction of Security Token Assignment

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1259](https://cwe.mitre.org/data/definitions/1259.html)

## Description
The System-On-A-Chip (SoC) implements a Security Token mechanism to differentiate what actions are allowed or disallowed when a transaction originates from an entity. However, the Security Tokens are improperly protected.

## Extended description
Systems-On-A-Chip (Integrated circuits and hardware engines) implement Security Tokens to differentiate and identify which actions originated from which agent. These actions may be one of the directives: 'read', 'write', 'program', 'reset', 'fetch', 'compute', etc. Security Tokens are assigned to every agent in the System that is capable of generating an action or receiving an action from another agent. Multiple Security Tokens may be assigned to an agent and may be unique based on the agent's trust level or allowed privileges. Since the Security Tokens are integral for the maintenance of security in an SoC, they need to be protected properly. A common weakness afflicting Security Tokens is improperly restricting the assignment to trusted components.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Processor Hardware, System on Chip

## Common consequences
- **Confidentiality, Integrity, Availability, Access Control**: Modify Files or Directories, Execute Unauthorized Code or Commands, Bypass Protection Mechanism, Gain Privileges or Assume Identity, Modify Memory, Modify Memory, DoS: Crash, Exit, or Restart

## Potential mitigations
- **Architecture and Design, Implementation**: Security Token assignment review checks for design inconsistency and common weaknesses. Security-Token definition and programming flow is tested in both pre-silicon and post-silicon testing.

## Related attack patterns (CAPEC)
- [CAPEC-121](https://capec.mitre.org/data/definitions/121.html)
- [CAPEC-681](https://capec.mitre.org/data/definitions/681.html)

## Related weaknesses
- CWE-284 (ChildOf)
- CWE-1294 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1259.html
