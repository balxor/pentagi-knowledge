---
cwe_id: CWE-394
name: Unexpected Status Code or Return Value
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/394.html
tags: [mitre-cwe, weakness, CWE-394]
---

# CWE-394 - Unexpected Status Code or Return Value

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-394](https://cwe.mitre.org/data/definitions/394.html)

## Description
The product does not properly check when a function or operation returns a value that is legitimate for the function, but is not expected by the product.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Other**: Unexpected State, Alter Execution Logic

## Related weaknesses
- CWE-754 (ChildOf)

## Observed examples (CVE)
- **CVE-2004-1395**: Certain packets (zero byte and other lengths) cause a recvfrom call to produce an unexpected return code that causes a server's listening loop to exit.
- **CVE-2002-2124**: Unchecked return code from recv() leads to infinite loop.
- **CVE-2005-2553**: Kernel function does not properly handle when a null is returned by a function call, causing it to call another function that it shouldn't.
- **CVE-2005-1858**: Memory not properly cleared when read() function call returns fewer bytes than expected.
- **CVE-2000-0536**: Bypass access restrictions when connecting from IP whose DNS reverse lookup does not return a hostname.
- **CVE-2001-0910**: Bypass access restrictions when connecting from IP whose DNS reverse lookup does not return a hostname.
- **CVE-2004-2371**: Game server doesn't check return values for functions that handle text strings and associated size values.
- **CVE-2005-1267**: Resultant infinite loop when function call returns -1 value.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/394.html
