---
cwe_id: CWE-755
name: Improper Handling of Exceptional Conditions
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/755.html
tags: [mitre-cwe, weakness, CWE-755]
---

# CWE-755 - Improper Handling of Exceptional Conditions

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-755](https://cwe.mitre.org/data/definitions/755.html)

## Description
The product does not handle or incorrectly handles an exceptional condition.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Other

## Related weaknesses
- CWE-703 (ChildOf)

## Observed examples (CVE)
- **CVE-2023-41151**: SDK for OPC Unified Architecture (OPC UA) server has uncaught exception when a socket is blocked for writing but the server tries to send an error
- **[REF-1374]**: Chain: JavaScript-based cryptocurrency library can fall back to the insecure Math.random() function instead of reporting a failure (CWE-392), thus reducing the entropy (CWE-332) and leading to generation of non-unique cryptographic keys for Bitcoin wallets (CWE-1391)
- **CVE-2021-3011**: virtual interrupt controller in a virtualization product allows crash of host by writing a certain invalid value to a register, which triggers a fatal error instead of returning an error code
- **CVE-2008-4302**: Chain: OS kernel does not properly handle a failure of a function call (CWE-755), leading to an unlock of a resource that was not locked (CWE-832), with resultant crash.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/755.html
