---
cwe_id: CWE-123
name: Write-what-where Condition
type: weakness
abstraction: Base
status: Draft
languages: [Memory-Unsafe, C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/123.html
tags: [mitre-cwe, weakness, CWE-123]
---

# CWE-123 - Write-what-where Condition

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-123](https://cwe.mitre.org/data/definitions/123.html)

## Description
Any condition where the attacker has the ability to write an arbitrary value to an arbitrary location, often as the result of a buffer overflow.

## Applicable platforms / languages
Memory-Unsafe, C, C++

## Common consequences
- **Integrity, Confidentiality, Availability, Access Control**: Modify Memory, Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity, DoS: Crash, Exit, or Restart, Bypass Protection Mechanism
- **Integrity, Availability**: DoS: Crash, Exit, or Restart, Modify Memory
- **Access Control, Other**: Bypass Protection Mechanism, Other

## Potential mitigations
- **Architecture and Design**: Use a language that provides appropriate memory abstractions.
- **Operation**: Use OS-level preventative functionality integrated after the fact. Not a complete solution.

## Related weaknesses
- CWE-787 (ChildOf)
- CWE-787 (ChildOf)
- CWE-119 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-19911**: Chain: Python library does not limit the resources used to process images that specify a very large number of bands (CWE-1284), leading to excessive memory consumption (CWE-789) or an integer overflow (CWE-190).
- **CVE-2022-0545**: Chain: 3D renderer has an integer overflow (CWE-190) leading to write-what-where condition (CWE-123) using a crafted image.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/123.html
