---
cwe_id: CWE-766
name: Critical Data Element Declared Public
type: weakness
abstraction: Base
status: Incomplete
languages: [C++, C#, Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/766.html
tags: [mitre-cwe, weakness, CWE-766]
---

# CWE-766 - Critical Data Element Declared Public

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-766](https://cwe.mitre.org/data/definitions/766.html)

## Description
The product declares a critical variable, field, or member to be public when intended security policy requires it to be private.

## Extended description
This issue makes it more difficult to maintain the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.

## Applicable platforms / languages
C++, C#, Java

## Common consequences
- **Integrity, Confidentiality**: Read Application Data, Modify Application Data
- **Other**: Reduce Maintainability

## Potential mitigations
- **Implementation**: Data should be private, static, and final whenever possible. This will assure that your code is protected by instantiating early, preventing access, and preventing tampering.

## Related weaknesses
- CWE-732 (ChildOf)
- CWE-1061 (ChildOf)

## Observed examples (CVE)
- **CVE-2010-3860**: variables declared public allow remote read of system properties such as user name and home directory.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/766.html
