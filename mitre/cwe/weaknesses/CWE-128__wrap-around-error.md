---
cwe_id: CWE-128
name: Wrap-around Error
type: weakness
abstraction: Base
status: Incomplete
languages: [C, C++]
related_capec: [CAPEC-92]
url: https://cwe.mitre.org/data/definitions/128.html
tags: [mitre-cwe, weakness, CWE-128]
---

# CWE-128 - Wrap-around Error

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-128](https://cwe.mitre.org/data/definitions/128.html)

## Description
Wrap around errors occur whenever a value is incremented past the maximum value for its type and therefore "wraps around" to a very small, negative, or undefined value.

## Applicable platforms / languages
C, C++

## Common consequences
- **Availability**: DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Instability
- **Integrity**: Modify Memory
- **Confidentiality, Availability, Access Control**: Execute Unauthorized Code or Commands, Bypass Protection Mechanism

## Potential mitigations
- **general**: Requirements specification: The choice could be made to use a language that is not susceptible to these issues.
- **Architecture and Design**: Provide clear upper and lower bounds on the scale of any protocols designed.
- **Implementation**: Perform validation on all incremented variables to ensure that they remain within reasonable bounds.

## Related attack patterns (CAPEC)
- [CAPEC-92](https://capec.mitre.org/data/definitions/92.html)

## Related weaknesses
- CWE-682 (ChildOf)
- CWE-119 (CanPrecede)
- CWE-190 (PeerOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/128.html
