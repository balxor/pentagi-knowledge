---
cwe_id: CWE-1282
name: Assumed-Immutable Data is Stored in Writable Memory
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-458, CAPEC-679]
url: https://cwe.mitre.org/data/definitions/1282.html
tags: [mitre-cwe, weakness, CWE-1282]
---

# CWE-1282 - Assumed-Immutable Data is Stored in Writable Memory

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1282](https://cwe.mitre.org/data/definitions/1282.html)

## Description
Immutable data, such as a first-stage bootloader, device identifiers, and "write-once" configuration settings are stored in writable memory that can be re-programmed or updated in the field.

## Extended description
Security services such as secure boot, authentication of code and data, and device attestation all require assets such as the first stage bootloader, public keys, golden hash digests, etc. which are implicitly trusted. Storing these assets in read-only memory (ROM), fuses, or one-time programmable (OTP) memory provides strong integrity guarantees and provides a root of trust for securing the rest of the system. Security is lost if assets assumed to be immutable can be modified.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Integrity**: Varies by Context

## Potential mitigations
- **Implementation**: All immutable code or data should be programmed into ROM or write-once memory.

## Related attack patterns (CAPEC)
- [CAPEC-458](https://capec.mitre.org/data/definitions/458.html)
- [CAPEC-679](https://capec.mitre.org/data/definitions/679.html)

## Related weaknesses
- CWE-668 (ChildOf)
- CWE-471 (CanPrecede)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1282.html
