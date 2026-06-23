---
cwe_id: CWE-395
name: Use of NullPointerException Catch to Detect NULL Pointer Dereference
type: weakness
abstraction: Base
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/395.html
tags: [mitre-cwe, weakness, CWE-395]
---

# CWE-395 - Use of NullPointerException Catch to Detect NULL Pointer Dereference

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-395](https://cwe.mitre.org/data/definitions/395.html)

## Description
Catching NullPointerException should not be used as an alternative to programmatic checks to prevent dereferencing a null pointer.

## Extended description
Programmers typically catch NullPointerException under three circumstances: The program contains a null pointer dereference. Catching the resulting exception was easier than fixing the underlying problem. The program explicitly throws a NullPointerException to signal an error condition. The code is part of a test harness that supplies unexpected input to the classes under test. Of these three circumstances, only the last is acceptable.

## Applicable platforms / languages
Java

## Common consequences
- **Availability**: DoS: Resource Consumption (CPU)

## Potential mitigations
- **Architecture and Design, Implementation**: Do not extensively rely on catching exceptions (especially for validating user input) to handle errors. Handling exceptions can decrease the performance of an application.

## Related weaknesses
- CWE-705 (ChildOf)
- CWE-755 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/395.html
