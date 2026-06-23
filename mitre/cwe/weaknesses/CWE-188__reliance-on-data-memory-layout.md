---
cwe_id: CWE-188
name: Reliance on Data/Memory Layout
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/188.html
tags: [mitre-cwe, weakness, CWE-188]
---

# CWE-188 - Reliance on Data/Memory Layout

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-188](https://cwe.mitre.org/data/definitions/188.html)

## Description
The product makes invalid assumptions about how protocol data or memory is organized at a lower level, resulting in unintended program behavior.

## Extended description
When changing platforms or protocol versions, in-memory organization of data may change in unintended ways. For example, some architectures may place local variables A and B right next to each other with A on top; some may place them next to each other with B on top; and others may add some padding to each. The padding size may vary to ensure that each variable is aligned to a proper word size. In protocol implementations, it is common to calculate an offset relative to another field to pick out a specific piece of data. Exceptional conditions, often involving new protocol versions, may add corner cases that change the data layout in an unusual way. The result can be that an implementation accesses an unintended field in the packet, treating data of one type as data of another type.

## Applicable platforms / languages
Not Language-Specific, C, C++

## Common consequences
- **Integrity, Confidentiality**: Modify Memory, Read Memory

## Potential mitigations
- **Implementation, Architecture and Design**: In flat address space situations, never allow computing memory addresses as offsets from another memory address.
- **Architecture and Design**: Fully specify protocol layout unambiguously, providing a structured grammar (e.g., a compilable yacc grammar).
- **Testing**: Testing: Test that the implementation properly handles each case in the protocol grammar.

## Related weaknesses
- CWE-1105 (ChildOf)
- CWE-435 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/188.html
