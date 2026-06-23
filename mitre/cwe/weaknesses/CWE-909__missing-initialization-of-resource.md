---
cwe_id: CWE-909
name: Missing Initialization of Resource
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/909.html
tags: [mitre-cwe, weakness, CWE-909]
---

# CWE-909 - Missing Initialization of Resource

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-909](https://cwe.mitre.org/data/definitions/909.html)

## Description
The product does not initialize a critical resource.

## Extended description
Many resources require initialization before they can be properly used. If a resource is not initialized, it could contain unpredictable or expired data, or it could be initialized to defaults that are invalid. This can have security implications when the resource is expected to have certain properties or values.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Memory, Read Application Data
- **Availability**: DoS: Crash, Exit, or Restart

## Potential mitigations
- **Implementation**: Explicitly initialize the resource before use. If this is performed through an API function or standard procedure, follow all specified steps.
- **Implementation**: Pay close attention to complex conditionals that affect initialization, since some branches might not perform the initialization.
- **Implementation**: Avoid race conditions (CWE-362) during initialization routines.
- **Build and Compilation**: Run or compile your product with settings that generate warnings about uninitialized variables or data.

## Related weaknesses
- CWE-665 (ChildOf)
- CWE-665 (ChildOf)
- CWE-908 (CanPrecede)

## Observed examples (CVE)
- **CVE-2020-20739**: A variable that has its value set in a conditional statement is sometimes used when the conditional fails, sometimes causing data leakage
- **CVE-2005-1036**: Chain: Bypass of access restrictions due to improper authorization (CWE-862) of a user results from an improperly initialized (CWE-909) I/O permission bitmap

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/909.html
