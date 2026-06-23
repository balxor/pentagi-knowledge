---
cwe_id: CWE-390
name: Detection of Error Condition Without Action
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/390.html
tags: [mitre-cwe, weakness, CWE-390]
---

# CWE-390 - Detection of Error Condition Without Action

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-390](https://cwe.mitre.org/data/definitions/390.html)

## Description
The product detects a specific error, but takes no actions to handle the error.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Other**: Varies by Context, Unexpected State, Alter Execution Logic

## Potential mitigations
- **Implementation**: Properly handle each exception. This is the recommended solution. Ensure that all exceptions are handled in such a way that you can be sure of the state of your system at any given moment.
- **Implementation**: If a function returns an error, it is important to either fix the problem and try again, alert the user that an error has happened and let the program continue, or alert the user and close and cleanup the program.
- **Testing**: Subject the product to extensive testing to discover some of the possible instances of where/how errors or return values are not handled. Consider testing techniques such as ad hoc, equivalence partitioning, robustness and fault tolerance, mutation, and fuzzing.

## Related weaknesses
- CWE-755 (ChildOf)
- CWE-401 (CanPrecede)

## Observed examples (CVE)
- **CVE-2022-21820**: A GPU data center manager detects an error due to a malformed request but does not act on it, leading to memory corruption.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/390.html
