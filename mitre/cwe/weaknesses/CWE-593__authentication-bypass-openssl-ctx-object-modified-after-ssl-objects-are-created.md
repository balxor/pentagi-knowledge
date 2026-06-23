---
cwe_id: CWE-593
name: Authentication Bypass: OpenSSL CTX Object Modified after SSL Objects are Created
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-94]
url: https://cwe.mitre.org/data/definitions/593.html
tags: [mitre-cwe, weakness, CWE-593]
---

# CWE-593 - Authentication Bypass: OpenSSL CTX Object Modified after SSL Objects are Created

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-593](https://cwe.mitre.org/data/definitions/593.html)

## Description
The product modifies the SSL context after connection creation has begun.

## Extended description
If the program modifies the SSL_CTX object after creating SSL objects from it, there is the possibility that older SSL objects created from the original context could all be affected by that change.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design**: Use a language or a library that provides a cryptography framework at a higher level of abstraction.
- **Implementation**: Most SSL_CTX functions have SSL counterparts that act on SSL-type objects.
- **Implementation**: Applications should set up an SSL_CTX completely, before creating SSL objects from it.

## Related attack patterns (CAPEC)
- [CAPEC-94](https://capec.mitre.org/data/definitions/94.html)

## Related weaknesses
- CWE-666 (ChildOf)
- CWE-1390 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/593.html
