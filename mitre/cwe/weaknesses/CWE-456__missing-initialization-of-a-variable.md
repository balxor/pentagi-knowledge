---
cwe_id: CWE-456
name: Missing Initialization of a Variable
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/456.html
tags: [mitre-cwe, weakness, CWE-456]
---

# CWE-456 - Missing Initialization of a Variable

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-456](https://cwe.mitre.org/data/definitions/456.html)

## Description
The product does not initialize critical variables, which causes the execution environment to use unexpected values.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Other**: Unexpected State, Quality Degradation, Varies by Context

## Potential mitigations
- **Implementation**: Ensure that critical variables are initialized before first use [REF-1485].
- **Requirements**: Choose a language that is not susceptible to these issues.

## Related weaknesses
- CWE-909 (ChildOf)
- CWE-665 (ChildOf)
- CWE-665 (ChildOf)
- CWE-89 (CanPrecede)
- CWE-120 (CanPrecede)
- CWE-98 (CanPrecede)
- CWE-457 (CanPrecede)

## Observed examples (CVE)
- **CVE-2020-6078**: Chain: The return value of a function returning a pointer is not checked for success (CWE-252) resulting in the later use of an uninitialized variable (CWE-456) and a null pointer dereference (CWE-476)
- **CVE-2019-3836**: Chain: secure communications library does not initialize a local variable for a data structure (CWE-456), leading to access of an uninitialized pointer (CWE-824).
- **CVE-2018-14641**: Chain: C union member is not initialized (CWE-456), leading to access of invalid pointer (CWE-824)
- **CVE-2009-2692**: Chain: Use of an unimplemented network socket operation pointing to an uninitialized handler function (CWE-456) causes a crash because of a null pointer dereference (CWE-476)
- **CVE-2020-20739**: A variable that has its value set in a conditional statement is sometimes used when the conditional fails, sometimes causing data leakage
- **CVE-2005-2978**: Product uses uninitialized variables for size and index, leading to resultant buffer overflow.
- **CVE-2005-2109**: Internal variable in PHP application is not initialized, allowing external modification.
- **CVE-2005-2193**: Array variable not initialized in PHP application, leading to resultant SQL injection.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/456.html
