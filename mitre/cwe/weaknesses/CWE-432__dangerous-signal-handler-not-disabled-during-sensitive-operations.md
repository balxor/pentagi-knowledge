---
cwe_id: CWE-432
name: Dangerous Signal Handler not Disabled During Sensitive Operations
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/432.html
tags: [mitre-cwe, weakness, CWE-432]
---

# CWE-432 - Dangerous Signal Handler not Disabled During Sensitive Operations

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-432](https://cwe.mitre.org/data/definitions/432.html)

## Description
The product uses a signal handler that shares state with other signal handlers, but it does not properly mask or prevent those signal handlers from being invoked while the original signal handler is still running.

## Extended description
During the execution of a signal handler, it can be interrupted by another handler when a different signal is sent. If the two handlers share state - such as global variables - then an attacker can corrupt the state by sending another signal before the first handler has completed execution.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Modify Application Data

## Potential mitigations
- **Implementation**: Turn off dangerous handlers when performing sensitive operations.

## Related weaknesses
- CWE-364 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/432.html
