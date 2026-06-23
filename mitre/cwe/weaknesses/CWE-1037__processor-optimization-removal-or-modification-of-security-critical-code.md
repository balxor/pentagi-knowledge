---
cwe_id: CWE-1037
name: Processor Optimization Removal or Modification of Security-critical Code
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Processor Hardware]
related_capec: [CAPEC-663]
url: https://cwe.mitre.org/data/definitions/1037.html
tags: [mitre-cwe, weakness, CWE-1037]
---

# CWE-1037 - Processor Optimization Removal or Modification of Security-critical Code

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1037](https://cwe.mitre.org/data/definitions/1037.html)

## Description
The developer builds a security-critical protection mechanism into the software, but the processor optimizes the execution of the program such that the mechanism is removed or modified.

## Applicable platforms / languages
Not Language-Specific, Processor Hardware

## Common consequences
- **Integrity**: Bypass Protection Mechanism

## Related attack patterns (CAPEC)
- [CAPEC-663](https://capec.mitre.org/data/definitions/663.html)

## Related weaknesses
- CWE-1038 (ChildOf)

## Observed examples (CVE)
- **CVE-2017-5715**: Intel, ARM, and AMD processor optimizations related to speculative execution and branch prediction cause access control checks to be bypassed when placing data into the cache. Often known as "Spectre".
- **CVE-2017-5753**: Intel, ARM, and AMD processor optimizations related to speculative execution and branch prediction cause access control checks to be bypassed when placing data into the cache. Often known as "Spectre".
- **CVE-2017-5754**: Intel processor optimizations related to speculative execution cause access control checks to be bypassed when placing data into the cache. Often known as "Meltdown".

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1037.html
