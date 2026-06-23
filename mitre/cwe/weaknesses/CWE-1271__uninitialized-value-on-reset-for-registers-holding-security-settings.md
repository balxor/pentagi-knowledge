---
cwe_id: CWE-1271
name: Uninitialized Value on Reset for Registers Holding Security Settings
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-74]
url: https://cwe.mitre.org/data/definitions/1271.html
tags: [mitre-cwe, weakness, CWE-1271]
---

# CWE-1271 - Uninitialized Value on Reset for Registers Holding Security Settings

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1271](https://cwe.mitre.org/data/definitions/1271.html)

## Description
Security-critical logic is not set to a known value on reset.

## Extended description
When the device is first brought out of reset, the state of registers will be indeterminate if they have not been initialized by the logic. Before the registers are initialized, there will be a window during which the device is in an insecure state and may be vulnerable to attack.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Access Control, Authentication, Authorization**: Varies by Context

## Potential mitigations
- **Implementation**: Design checks should be performed to identify any uninitialized flip-flops used for security-critical functions.
- **Architecture and Design**: All registers holding security-critical information should be set to a specific value on reset.

## Related attack patterns (CAPEC)
- [CAPEC-74](https://capec.mitre.org/data/definitions/74.html)

## Related weaknesses
- CWE-909 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1271.html
