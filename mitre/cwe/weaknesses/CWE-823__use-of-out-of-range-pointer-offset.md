---
cwe_id: CWE-823
name: Use of Out-of-range Pointer Offset
type: weakness
abstraction: Base
status: Incomplete
languages: [Memory-Unsafe, C, C++]
related_capec: [CAPEC-129]
url: https://cwe.mitre.org/data/definitions/823.html
tags: [mitre-cwe, weakness, CWE-823]
---

# CWE-823 - Use of Out-of-range Pointer Offset

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-823](https://cwe.mitre.org/data/definitions/823.html)

## Description
The product performs pointer arithmetic on a valid pointer, but it uses an offset that can point outside of the intended range of valid memory locations for the resulting pointer.

## Extended description
While a pointer can contain a reference to any arbitrary memory location, a program typically only intends to use the pointer to access limited portions of memory, such as contiguous memory used to access an individual array. Programs may use offsets in order to access fields or sub-elements stored within structured data. The offset might be out-of-range if it comes from an untrusted source, is the result of an incorrect calculation, or occurs because of another error. If an attacker can control or influence the offset so that it points outside of the intended boundaries of the structure, then the attacker may be able to read or write to memory locations that are used elsewhere in the product. As a result, the attack might change the state of the product as accessed through program variables, cause a crash or instable behavior, and possibly lead to code execution.

## Applicable platforms / languages
Memory-Unsafe, C, C++

## Common consequences
- **Confidentiality**: Read Memory
- **Availability**: DoS: Crash, Exit, or Restart
- **Integrity, Confidentiality, Availability**: Execute Unauthorized Code or Commands, Modify Memory

## Related attack patterns (CAPEC)
- [CAPEC-129](https://capec.mitre.org/data/definitions/129.html)

## Related weaknesses
- CWE-119 (ChildOf)
- CWE-119 (ChildOf)
- CWE-119 (ChildOf)
- CWE-125 (CanPrecede)
- CWE-787 (CanPrecede)

## Observed examples (CVE)
- **CVE-2010-2160**: Invalid offset in undocumented opcode leads to memory corruption.
- **CVE-2010-1281**: Multimedia player uses untrusted value from a file when using file-pointer calculations.
- **CVE-2009-3129**: Spreadsheet program processes a record with an invalid size field, which is later used as an offset.
- **CVE-2009-2694**: Instant messaging library does not validate an offset value specified in a packet.
- **CVE-2009-2687**: Language interpreter does not properly handle invalid offsets in JPEG image, leading to out-of-bounds memory access and crash.
- **CVE-2009-0690**: negative offset leads to out-of-bounds read
- **CVE-2008-4114**: untrusted offset in kernel
- **CVE-2010-2873**: "blind trust" of an offset value while writing heap memory allows corruption of function pointer,leading to code execution
- **CVE-2010-2866**: negative value (signed) causes pointer miscalculation
- **CVE-2010-2872**: signed values cause incorrect pointer calculation
- **CVE-2007-5657**: values used as pointer offsets
- **CVE-2010-2867**: a return value from a function is sign-extended if the value is signed, then used as an offset for pointer arithmetic
- **CVE-2009-1097**: portions of a GIF image used as offsets, causing corruption of an object pointer.
- **CVE-2008-1807**: invalid numeric field leads to a free of arbitrary memory locations, then code execution.
- **CVE-2007-2500**: large number of elements leads to a free of an arbitrary address

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/823.html
