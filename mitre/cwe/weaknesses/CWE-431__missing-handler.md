---
cwe_id: CWE-431
name: Missing Handler
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/431.html
tags: [mitre-cwe, weakness, CWE-431]
---

# CWE-431 - Missing Handler

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-431](https://cwe.mitre.org/data/definitions/431.html)

## Description
A handler is not available or implemented.

## Extended description
When an exception is thrown and not caught, the process has given up an opportunity to decide if a given failure or event is worth a change in execution.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Varies by Context

## Potential mitigations
- **Implementation**: Handle all possible situations (e.g. error condition).
- **Implementation**: If an operation can throw an Exception, implement a handler for that specific exception.

## Related weaknesses
- CWE-691 (ChildOf)
- CWE-433 (CanPrecede)

## Observed examples (CVE)
- **CVE-2022-25302**: SDK for OPC Unified Architecture (OPC UA) is missing a handler for when a cast fails, allowing for a crash

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/431.html
