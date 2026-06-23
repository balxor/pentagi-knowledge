---
cwe_id: CWE-7
name: J2EE Misconfiguration: Missing Custom Error Page
type: weakness
abstraction: Variant
status: Incomplete
languages: [Java, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/7.html
tags: [mitre-cwe, weakness, CWE-7]
---

# CWE-7 - J2EE Misconfiguration: Missing Custom Error Page

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-7](https://cwe.mitre.org/data/definitions/7.html)

## Description
The default error page of a web application should not display sensitive information about the product.

## Extended description
A Web application must define a default error page for 4xx errors (e.g. 404), 5xx (e.g. 500) errors and catch java.lang.Throwable exceptions to prevent attackers from mining information from the application container's built-in error response. When an attacker explores a web site looking for vulnerabilities, the amount of information that the site provides is crucial to the eventual success or failure of any attempted attacks.

## Applicable platforms / languages
Java, Web Based, Web Server

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Implementation**: Handle exceptions appropriately in source code.
- **Implementation, System Configuration**: Always define appropriate error pages. The application configuration should specify a default error page in order to guarantee that the application will never leak error messages to an attacker. Handling standard HTTP error codes is useful and user-friendly in addition to being a good security practice, and a good configuration will also define a last-chance error handler that catches any exception that could possibly be thrown by the application.
- **Implementation**: Do not attempt to process an error or attempt to mask it.
- **Implementation**: Verify return values are correct and do not supply sensitive information about the system.

## Related weaknesses
- CWE-756 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/7.html
