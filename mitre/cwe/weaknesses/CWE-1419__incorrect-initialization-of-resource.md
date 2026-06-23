---
cwe_id: CWE-1419
name: Incorrect Initialization of Resource
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1419.html
tags: [mitre-cwe, weakness, CWE-1419]
---

# CWE-1419 - Incorrect Initialization of Resource

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-1419](https://cwe.mitre.org/data/definitions/1419.html)

## Description
The product attempts to initialize a resource but does not correctly do so, which might leave the resource in an unexpected, incorrect, or insecure state when it is accessed.

## Extended description
This can have security implications when the associated resource is expected to have certain properties or values. Examples include a variable that determines whether a user has been authenticated or not, or a register or fuse value that determines the security state of the product. For software, this weakness can frequently occur when implicit initialization is used, meaning the resource is not explicitly set to a specific value. For example, in C, memory is not necessarily cleared when it is allocated on the stack, and many scripting languages use a default empty, null value, or zero value when a variable is not explicitly initialized. For hardware, this weakness frequently appears with reset values and fuses. After a product reset, hardware may initialize registers incorrectly. During different phases of a product lifecycle, fuses may be set to incorrect values. Even if fuses are set to correct values, the lines to the fuse could be broken or there might be hardware on the fuse line that alters the fuse value to be incorrect.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality**: Read Memory, Read Application Data, Unexpected State
- **Authorization, Integrity**: Gain Privileges or Assume Identity
- **Other**: Varies by Context

## Potential mitigations
- **Implementation**: Choose the safest-possible initialization for security-related resources.
- **Implementation**: Ensure that each resource (whether variable, memory buffer, register, etc.) is fully initialized.
- **Implementation**: Pay close attention to complex conditionals or reset sources that affect initialization, since some paths might not perform the initialization.
- **Architecture and Design**: Ensure that the design and architecture clearly identify what the initialization should be, and that the initialization does not have security implications.

## Related weaknesses
- CWE-665 (ChildOf)

## Observed examples (CVE)
- **CVE-2020-27211**: Chain: microcontroller system-on-chip uses a register value stored in flash to set product protection state on the memory bus and does not contain protection against fault injection (CWE-1319) which leads to an incorrect initialization of the memory bus (CWE-1419) causing the product to be in an unprotected state.
- **CVE-2023-25815**: chain: a change in an underlying package causes the gettext function to use implicit initialization with a hard-coded path (CWE-1419) under the user-writable C:\ drive, introducing an untrusted search path element (CWE-427) that enables spoofing of messages.
- **CVE-2022-43468**: WordPress module sets internal variables based on external inputs, allowing false reporting of the number of views
- **CVE-2022-36349**: insecure default variable initialization in BIOS firmware for a hardware board allows DoS
- **CVE-2015-7763**: distributed filesystem only initializes part of the variable-length padding for a packet, allowing attackers to read sensitive information from previously-sent packets in the same memory location

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1419.html
