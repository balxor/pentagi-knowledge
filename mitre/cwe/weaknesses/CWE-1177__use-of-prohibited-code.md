---
cwe_id: CWE-1177
name: Use of Prohibited Code
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1177.html
tags: [mitre-cwe, weakness, CWE-1177]
---

# CWE-1177 - Use of Prohibited Code

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-1177](https://cwe.mitre.org/data/definitions/1177.html)

## Description
The product uses a function, library, or third party component that has been explicitly prohibited, whether by the developer or the customer.

## Extended description
The developer - or customers - may wish to restrict or eliminate use of a function, library, or third party component for any number of reasons, including real or suspected vulnerabilities; difficulty to use securely; export controls or license requirements; obsolete or poorly-maintained code; internal code being scheduled for deprecation; etc. To reduce risk of vulnerabilities, the developer might maintain a list of "banned" functions that programmers must avoid using because the functions are difficult or impossible to use securely. This issue can also make the product more costly and difficult to maintain.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Maintainability

## Potential mitigations
- **Build and Compilation, Implementation**: Identify a list of prohibited API functions and prohibit developers from using these functions, providing safer alternatives. In some cases, automatic code analysis tools or the compiler can be instructed to spot use of prohibited functions, such as the "banned.h" include file from Microsoft's SDL. [REF-554] [REF-1009] [REF-7]

## Related weaknesses
- CWE-710 (ChildOf)

## Observed examples (CVE)
- **CVE-2007-1470**: Library has multiple buffer overflows using sprintf() and strcpy()
- **CVE-2007-4004**: FTP client uses inherently insecure gets() function and is setuid root on some systems, allowing buffer overflow

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1177.html
