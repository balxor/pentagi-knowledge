---
cwe_id: CWE-392
name: Missing Report of Error Condition
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/392.html
tags: [mitre-cwe, weakness, CWE-392]
---

# CWE-392 - Missing Report of Error Condition

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-392](https://cwe.mitre.org/data/definitions/392.html)

## Description
The product encounters an error but does not provide a status code or return value to indicate that an error has occurred.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Other**: Varies by Context, Unexpected State

## Related weaknesses
- CWE-755 (ChildOf)
- CWE-684 (ChildOf)
- CWE-703 (ChildOf)
- CWE-703 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-52316**: Web-based product can throw an exception during authentication but does not report the failure in the HTTP status code, allowing authentication bypass.
- **[REF-1374]**: Chain: JavaScript-based cryptocurrency library can fall back to the insecure Math.random() function instead of reporting a failure (CWE-392), thus reducing the entropy (CWE-332) and leading to generation of non-unique cryptographic keys for Bitcoin wallets (CWE-1391)
- **CVE-2004-0063**: Function returns "OK" even if another function returns a different status code than expected, leading to accepting an invalid PIN number.
- **CVE-2002-1446**: Error checking routine in PKCS#11 library returns "OK" status even when invalid signature is detected, allowing spoofed messages.
- **CVE-2002-0499**: Kernel function truncates long pathnames without generating an error, leading to operation on wrong directory.
- **CVE-2005-2459**: Function returns non-error value when a particular erroneous condition is encountered, leading to resultant NULL dereference.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/392.html
