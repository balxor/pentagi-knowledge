---
cwe_id: CWE-572
name: Call to Thread run() instead of start()
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/572.html
tags: [mitre-cwe, weakness, CWE-572]
---

# CWE-572 - Call to Thread run() instead of start()

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-572](https://cwe.mitre.org/data/definitions/572.html)

## Description
The product calls a thread's run() method instead of calling start(), which causes the code to run in the thread of the caller instead of the callee.

## Extended description
In most cases a direct call to a Thread object's run() method is a bug. The programmer intended to begin a new thread of control, but accidentally called run() instead of start(), so the run() method will execute in the caller's thread of control.

## Applicable platforms / languages
Java

## Common consequences
- **Other**: Quality Degradation, Varies by Context

## Potential mitigations
- **Implementation**: Use the start() method instead of the run() method.

## Related weaknesses
- CWE-821 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/572.html
