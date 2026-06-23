---
cwe_id: CWE-682
name: Incorrect Calculation
type: weakness
abstraction: Pillar
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-128, CAPEC-129]
url: https://cwe.mitre.org/data/definitions/682.html
tags: [mitre-cwe, weakness, CWE-682]
---

# CWE-682 - Incorrect Calculation

**Abstraction:** Pillar  -  **Status:** Draft  -  **CWE:** [CWE-682](https://cwe.mitre.org/data/definitions/682.html)

## Description
The product performs a calculation that generates incorrect or unintended results that are later used in security-critical decisions or resource management.

## Extended description
When product performs a security-critical calculation incorrectly, it might lead to incorrect resource allocations, incorrect privilege assignments, or failed comparisons among other things. Many of the direct results of an incorrect calculation can lead to even larger problems such as failed protection mechanisms or even arbitrary code execution.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Availability**: DoS: Crash, Exit, or Restart
- **Integrity, Confidentiality, Availability**: DoS: Crash, Exit, or Restart, DoS: Resource Consumption (Other), Execute Unauthorized Code or Commands
- **Access Control**: Gain Privileges or Assume Identity
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: Understand your programming language's underlying representation and how it interacts with numeric calculation. Pay close attention to byte size discrepancies, precision, signed/unsigned distinctions, truncation, conversion and casting between types, "not-a-number" calculations, and how your language handles numbers that are too large or too small for its underlying representation.
- **Implementation**: Perform input validation on any numeric input by ensuring that it is within the expected range. Enforce that the input meets both the minimum and maximum requirements for the expected range.
- **Implementation**: Use the appropriate type for the desired action. For example, in C/C++, only use unsigned types for values that could never be negative, such as height, width, or other numbers related to quantity.
- **Architecture and Design**: Use languages, libraries, or frameworks that make it easier to handle numbers without unexpected consequences. Examples include safe integer handling packages such as SafeInt (C++) or IntegerLib (C or C++).
- **Architecture and Design**: Use languages, libraries, or frameworks that make it easier to handle numbers without unexpected consequences. Examples include safe integer handling packages such as SafeInt (C++) or IntegerLib (C or C++).
- **Implementation**: Examine compiler warnings closely and eliminate problems with potential security implications, such as signed / unsigned mismatch in memory operations, or use of uninitialized variables. Even if the weakness is rarely exploitable, a single failure may lead to the compromise of the entire system.

## Related attack patterns (CAPEC)
- [CAPEC-128](https://capec.mitre.org/data/definitions/128.html)
- [CAPEC-129](https://capec.mitre.org/data/definitions/129.html)

## Related weaknesses
- CWE-170 (CanPrecede)

## Observed examples (CVE)
- **CVE-2020-0022**: chain: mobile phone Bluetooth implementation does not include offset when calculating packet length (CWE-682), leading to out-of-bounds write (CWE-787)
- **CVE-2010-1378**: Chain: incorrect calculation (CWE-682) allows attackers to bypass certificate checks (CWE-295)
- **CVE-2004-1363**: substitution overflow: buffer overflow using environment variables that are expanded after the length check is performed

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/682.html
