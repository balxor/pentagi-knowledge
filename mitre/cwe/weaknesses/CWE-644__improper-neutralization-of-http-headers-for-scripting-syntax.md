---
cwe_id: CWE-644
name: Improper Neutralization of HTTP Headers for Scripting Syntax
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/644.html
tags: [mitre-cwe, weakness, CWE-644]
---

# CWE-644 - Improper Neutralization of HTTP Headers for Scripting Syntax

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-644](https://cwe.mitre.org/data/definitions/644.html)

## Description
The product does not neutralize or incorrectly neutralizes web scripting syntax in HTTP headers that can be used by web browser components that can process raw headers, such as Flash.

## Extended description
An attacker may be able to conduct cross-site scripting and other attacks against users who have these components enabled. If a product does not neutralize user controlled data being placed in the header of an HTTP response coming from the server, the header may contain a script that will get executed in the client's browser context, potentially resulting in a cross site scripting vulnerability or possibly an HTTP response splitting attack. It is important to carefully control data that is being placed both in HTTP response header and in the HTTP response body to ensure that no scripting syntax is present, taking various encodings into account.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Integrity, Confidentiality, Availability**: Execute Unauthorized Code or Commands
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design**: Perform output validation in order to filter/escape/encode unsafe data that is being passed from the server in an HTTP response header.
- **Architecture and Design**: Disable script execution functionality in the clients' browser.

## Related weaknesses
- CWE-116 (ChildOf)

## Observed examples (CVE)
- **CVE-2006-3918**: Web server does not remove the Expect header from an HTTP request when it is reflected back in an error message, allowing a Flash SWF file to perform XSS attacks.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/644.html
