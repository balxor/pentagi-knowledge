---
cwe_id: CWE-605
name: Multiple Binds to the Same Port
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/605.html
tags: [mitre-cwe, weakness, CWE-605]
---

# CWE-605 - Multiple Binds to the Same Port

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-605](https://cwe.mitre.org/data/definitions/605.html)

## Description
When multiple sockets are allowed to bind to the same port, other services on that port may be stolen or spoofed.

## Extended description
On most systems, a combination of setting the SO_REUSEADDR socket option, and a call to bind() allows any process to bind to a port to which a previous process has bound with INADDR_ANY. This allows a user to bind to the specific address of a server bound to INADDR_ANY on an unprivileged port, and steal its UDP packets/TCP connection.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Application Data

## Potential mitigations
- **Policy**: Restrict server socket address to known local addresses.

## Related weaknesses
- CWE-675 (ChildOf)
- CWE-666 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/605.html
