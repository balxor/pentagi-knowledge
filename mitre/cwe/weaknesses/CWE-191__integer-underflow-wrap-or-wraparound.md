---
cwe_id: CWE-191
name: Integer Underflow (Wrap or Wraparound)
type: weakness
abstraction: Base
status: Draft
languages: [C, C++, Java, C#]
related_capec: []
url: https://cwe.mitre.org/data/definitions/191.html
tags: [mitre-cwe, weakness, CWE-191]
---

# CWE-191 - Integer Underflow (Wrap or Wraparound)

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-191](https://cwe.mitre.org/data/definitions/191.html)

## Description
The product subtracts one value from another, such that the result is less than the minimum allowable integer value, which produces a value that is not equal to the correct result.

## Extended description
This can happen in signed and unsigned cases.

## Applicable platforms / languages
C, C++, Java, C#

## Common consequences
- **Availability**: DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Instability
- **Integrity**: Modify Memory
- **Confidentiality, Availability, Access Control**: Execute Unauthorized Code or Commands, Bypass Protection Mechanism

## Related weaknesses
- CWE-682 (ChildOf)
- CWE-682 (ChildOf)

## Observed examples (CVE)
- **CVE-2004-0816**: Integer underflow in firewall via malformed packet.
- **CVE-2004-1002**: Integer underflow by packet with invalid length.
- **CVE-2005-0199**: Long input causes incorrect length calculation.
- **CVE-2005-1891**: Malformed icon causes integer underflow in loop counter variable.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/191.html
