---
cwe_id: CWE-1428
name: Reliance on HTTP instead of HTTPS
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1428.html
tags: [mitre-cwe, weakness, CWE-1428]
---

# CWE-1428 - Reliance on HTTP instead of HTTPS

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1428](https://cwe.mitre.org/data/definitions/1428.html)

## Description
The product provides or relies on use of HTTP communications when HTTPS is available.

## Extended description
Because HTTP communications are not encrypted, HTTP is subject to various attacks against confidentiality, integrity, and authenticity. However, unlike many other protocols, HTTPS is widely available as a more secure alternative, because it uses encryption.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Application Data, Modify Application Data

## Potential mitigations
- **Architecture and Design**: Explicitly require HTTPS or another mechanism that ensures that communication is encrypted [REF-1464].
- **Implementation**: Avoid using "mixed content," i.e., serving a web page over HTTPS in which the page includes elements that use "http:" URLs [REF-1466] [REF-1467]. This is often done for images or other resources that do not seem to have privacy or security implications.
- **Implementation, Operation**: Perform "HTTPS forcing," that is, redirecting HTTP requests to HTTPS.
- **Operation**: If the product supports multiple protocols, ensure that encrypted protocols (such as HTTPS) are required, and remove any unencrypted protocols (such as HTTP).

## Related weaknesses
- CWE-319 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1428.html
