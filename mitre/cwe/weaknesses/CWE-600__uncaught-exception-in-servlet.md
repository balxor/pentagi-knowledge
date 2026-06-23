---
cwe_id: CWE-600
name: Uncaught Exception in Servlet
type: weakness
abstraction: Variant
status: Draft
languages: [Java, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/600.html
tags: [mitre-cwe, weakness, CWE-600]
---

# CWE-600 - Uncaught Exception in Servlet

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-600](https://cwe.mitre.org/data/definitions/600.html)

## Description
The Servlet does not catch all exceptions, which may reveal sensitive debugging information.

## Extended description
When a Servlet throws an exception, the default error response the Servlet container sends back to the user typically includes debugging information. This information is of great value to an attacker. For example, a stack trace might show the attacker a malformed SQL query string, the type of database being used, and the version of the application container. This information enables the attacker to target known vulnerabilities in these components.

## Applicable platforms / languages
Java, Web Server

## Common consequences
- **Confidentiality, Availability**: Read Application Data, DoS: Crash, Exit, or Restart

## Potential mitigations
- **Implementation**: Implement Exception blocks to handle all types of Exceptions.

## Related weaknesses
- CWE-248 (ChildOf)
- CWE-209 (CanPrecede)
- CWE-390 (PeerOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/600.html
