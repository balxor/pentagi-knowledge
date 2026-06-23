---
cwe_id: CWE-253
name: Incorrect Check of Function Return Value
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/253.html
tags: [mitre-cwe, weakness, CWE-253]
---

# CWE-253 - Incorrect Check of Function Return Value

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-253](https://cwe.mitre.org/data/definitions/253.html)

## Description
The product incorrectly checks a return value from a function, which prevents it from detecting errors or exceptional conditions.

## Extended description
Important and common functions will return some value about the success of its actions. This will alert the program whether or not to handle any errors caused by that function.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Availability, Integrity**: Unexpected State, DoS: Crash, Exit, or Restart

## Potential mitigations
- **Architecture and Design**: Use a language or compiler that uses exceptions and requires the catching of those exceptions.
- **Implementation**: Properly check all functions which return a value.
- **Implementation**: When designing any function make sure you return a value or throw an exception in case of an error.

## Related weaknesses
- CWE-573 (ChildOf)
- CWE-754 (ChildOf)

## Observed examples (CVE)
- **CVE-2023-49286**: Chain: function in web caching proxy does not correctly check a return value (CWE-253) leading to a reachable assertion (CWE-617)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/253.html
