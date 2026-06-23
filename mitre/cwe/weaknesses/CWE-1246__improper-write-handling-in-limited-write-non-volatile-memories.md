---
cwe_id: CWE-1246
name: Improper Write Handling in Limited-write Non-Volatile Memories
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip, Memory Hardware, Storage Hardware]
related_capec: [CAPEC-212]
url: https://cwe.mitre.org/data/definitions/1246.html
tags: [mitre-cwe, weakness, CWE-1246]
---

# CWE-1246 - Improper Write Handling in Limited-write Non-Volatile Memories

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1246](https://cwe.mitre.org/data/definitions/1246.html)

## Description
The product does not implement or incorrectly implements wear leveling operations in limited-write non-volatile memories.

## Extended description
Non-volatile memories such as NAND Flash, EEPROM, etc. have individually erasable segments, each of which can be put through a limited number of program/erase or write cycles. For example, the device can only endure a limited number of writes, after which the device becomes unreliable. In order to wear out the cells in a uniform manner, non-volatile memory and storage products based on the above-mentioned technologies implement a technique called wear leveling. Once a set threshold is reached, wear leveling maps writes of a logical block to a different physical block. This prevents a single physical block from prematurely failing due to a high concentration of writes.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip, Memory Hardware, Storage Hardware

## Common consequences
- **Availability**: DoS: Instability

## Potential mitigations
- **Architecture and Design, Implementation, Testing**: Include secure wear leveling algorithms and ensure they may not be bypassed.

## Related attack patterns (CAPEC)
- [CAPEC-212](https://capec.mitre.org/data/definitions/212.html)

## Related weaknesses
- CWE-400 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1246.html
