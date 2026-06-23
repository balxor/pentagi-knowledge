---
cwe_id: CWE-1061
name: Insufficient Encapsulation
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1061.html
tags: [mitre-cwe, weakness, CWE-1061]
---

# CWE-1061 - Insufficient Encapsulation

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-1061](https://cwe.mitre.org/data/definitions/1061.html)

## Description
The product does not sufficiently hide the internal representation and implementation details of data or methods, which might allow external components or modules to modify data unexpectedly, invoke unexpected functionality, or introduce dependencies that the programmer did not intend.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Varies by Context, Bypass Protection Mechanism
- **Other**: Reduce Maintainability, Increase Analytical Complexity

## Related weaknesses
- CWE-710 (ChildOf)

## Observed examples (CVE)
- **CVE-2010-3860**: variables declared public allow remote read of system properties such as user name and home directory.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1061.html
