---
cwe_id: CWE-1267
name: Policy Uses Obsolete Encoding
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-121, CAPEC-681]
url: https://cwe.mitre.org/data/definitions/1267.html
tags: [mitre-cwe, weakness, CWE-1267]
---

# CWE-1267 - Policy Uses Obsolete Encoding

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1267](https://cwe.mitre.org/data/definitions/1267.html)

## Description
The product uses an obsolete encoding mechanism to implement access controls.

## Extended description
Within a System-On-a-Chip (SoC), various circuits and hardware engines generate transactions for the purpose of accessing (read/write) assets or performing various actions (e.g., reset, fetch, compute, etc.). Among various types of message information, a typical transaction is comprised of source identity (identifying the originator of the transaction) and a destination identity (routing the transaction to the respective entity). Sometimes the transactions are qualified with a Security Token. This Security Token helps the destination agent decide on the set of allowed actions (e.g., access to an asset for reads and writes). A policy encoder is used to map the bus transactions to Security Tokens that in turn are used as access-controls/protection mechanisms. A common weakness involves using an encoding which is no longer trusted, i.e., an obsolete encoding.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Availability, Access Control**: Modify Memory, Read Memory, Modify Files or Directories, Read Files or Directories, DoS: Resource Consumption (Other), Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity, Bypass Protection Mechanism, Reduce Reliability

## Potential mitigations
- **Architecture and Design, Implementation**: Security Token Decoders should be reviewed for design inconsistency and common weaknesses. Access and programming flows should be tested in both pre-silicon and post-silicon testing.

## Related attack patterns (CAPEC)
- [CAPEC-121](https://capec.mitre.org/data/definitions/121.html)
- [CAPEC-681](https://capec.mitre.org/data/definitions/681.html)

## Related weaknesses
- CWE-284 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1267.html
