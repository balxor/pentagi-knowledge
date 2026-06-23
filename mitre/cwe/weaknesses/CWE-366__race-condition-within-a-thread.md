---
cwe_id: CWE-366
name: Race Condition within a Thread
type: weakness
abstraction: Base
status: Draft
languages: [C, C++, Java, C#, Not Technology-Specific]
related_capec: [CAPEC-26, CAPEC-29]
url: https://cwe.mitre.org/data/definitions/366.html
tags: [mitre-cwe, weakness, CWE-366]
---

# CWE-366 - Race Condition within a Thread

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-366](https://cwe.mitre.org/data/definitions/366.html)

## Description
If two threads of execution use a resource simultaneously, there exists the possibility that resources may be used while invalid, in turn making the state of execution undefined.

## Applicable platforms / languages
C, C++, Java, C#, Not Technology-Specific

## Common consequences
- **Integrity, Other**: Alter Execution Logic, Unexpected State

## Potential mitigations
- **Architecture and Design**: Use locking functionality. This is the recommended solution. Implement some form of locking mechanism around code which alters or reads persistent data in a multithreaded environment.
- **Architecture and Design**: Create resource-locking validation checks. If no inherent locking mechanisms exist, use flags and signals to enforce your own blocking scheme when resources are being used by other threads of execution.

## Related attack patterns (CAPEC)
- [CAPEC-26](https://capec.mitre.org/data/definitions/26.html)
- [CAPEC-29](https://capec.mitre.org/data/definitions/29.html)

## Related weaknesses
- CWE-362 (ChildOf)
- CWE-662 (ChildOf)
- CWE-662 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-2621**: Chain: two threads in a web browser use the same resource (CWE-366), but one of those threads can destroy the resource before the other has completed (CWE-416).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/366.html
