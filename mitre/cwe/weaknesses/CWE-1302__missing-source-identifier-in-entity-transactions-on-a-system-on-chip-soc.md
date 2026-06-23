---
cwe_id: CWE-1302
name: Missing Source Identifier in Entity Transactions on a System-On-Chip (SOC)
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-121, CAPEC-681]
url: https://cwe.mitre.org/data/definitions/1302.html
tags: [mitre-cwe, weakness, CWE-1302]
---

# CWE-1302 - Missing Source Identifier in Entity Transactions on a System-On-Chip (SOC)

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1302](https://cwe.mitre.org/data/definitions/1302.html)

## Description
The product implements a security identifier mechanism to differentiate what actions are allowed or disallowed when a transaction originates from an entity. A transaction is sent without a security identifier.

## Extended description
In a System-On-Chip (SoC), various integrated circuits and hardware engines generate transactions such as to access (reads/writes) assets or perform certain actions (e.g., reset, fetch, compute). A typical transaction is comprised of source identity (to identify the originator of the transaction) and a destination identity (to route the transaction to the respective entity) in addition to much more information in the message. Sometimes the transactions are qualified with a Security Identifier. This Security Identifier helps the destination agent decide on the set of allowed or disallowed actions. A weakness that can exist in such transaction schemes is that the source agent does not consistently include the necessary Security Identifier with the transaction. If the Security Identifier is missing, the destination agent might drop the message (resulting in an inadvertent Denial-of-Service (DoS)) or take inappropriate action by default in its attempt to execute the transaction, resulting in privilege escalation or provision of unintended access.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Availability, Access Control**: Modify Memory, Read Memory, DoS: Crash, Exit, or Restart, Bypass Protection Mechanism, Execute Unauthorized Code or Commands

## Potential mitigations
- **Architecture and Design**: Transaction details must be reviewed for design inconsistency and common weaknesses.
- **Implementation**: Security identifier definition and programming flow must be tested in pre-silicon and post-silicon testing.

## Related attack patterns (CAPEC)
- [CAPEC-121](https://capec.mitre.org/data/definitions/121.html)
- [CAPEC-681](https://capec.mitre.org/data/definitions/681.html)

## Related weaknesses
- CWE-1294 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1302.html
