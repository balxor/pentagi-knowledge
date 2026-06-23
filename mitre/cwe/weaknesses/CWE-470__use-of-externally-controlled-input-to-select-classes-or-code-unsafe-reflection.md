---
cwe_id: CWE-470
name: Use of Externally-Controlled Input to Select Classes or Code ('Unsafe Reflection')
type: weakness
abstraction: Base
status: Draft
languages: [Java, PHP, Interpreted]
related_capec: [CAPEC-138]
url: https://cwe.mitre.org/data/definitions/470.html
tags: [mitre-cwe, weakness, CWE-470]
---

# CWE-470 - Use of Externally-Controlled Input to Select Classes or Code ('Unsafe Reflection')

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-470](https://cwe.mitre.org/data/definitions/470.html)

## Description
The product uses external input with reflection to select which classes or code to use, but it does not sufficiently prevent the input from selecting improper classes or code.

## Extended description
If the product uses external inputs to determine which class to instantiate or which method to invoke, then an attacker could supply values to select unexpected classes or methods. If this occurs, then the attacker could create control flow paths that were not intended by the developer. These paths could bypass authentication or access control checks, or otherwise cause the product to behave in an unexpected manner. This situation becomes a doomsday scenario if the attacker can upload files into a location that appears on the product's classpath (CWE-427) or add new entries to the product's classpath (CWE-426). Under either of these conditions, the attacker can use reflection to introduce new, malicious behavior into the product.

## Applicable platforms / languages
Java, PHP, Interpreted

## Common consequences
- **Integrity, Confidentiality, Availability, Other**: Execute Unauthorized Code or Commands, Alter Execution Logic
- **Availability, Other**: DoS: Crash, Exit, or Restart, Other
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design**: Refactor your code to avoid using reflection.
- **Architecture and Design**: Do not use user-controlled inputs to select and load classes or code.
- **Implementation**: Apply strict input validation by using allowlists or indirect selection to ensure that the user is only selecting allowable classes or code.

## Related attack patterns (CAPEC)
- [CAPEC-138](https://capec.mitre.org/data/definitions/138.html)

## Related weaknesses
- CWE-913 (ChildOf)
- CWE-913 (ChildOf)
- CWE-610 (ChildOf)
- CWE-20 (ChildOf)

## Observed examples (CVE)
- **CVE-2018-1000613**: Cryptography API uses unsafe reflection when deserializing a private key
- **CVE-2004-2331**: Database system allows attackers to bypass sandbox restrictions by using the Reflection API.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/470.html
