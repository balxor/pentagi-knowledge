---
cwe_id: CWE-598
name: Use of HTTP Request With Sensitive Query String
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/598.html
tags: [mitre-cwe, weakness, CWE-598]
---

# CWE-598 - Use of HTTP Request With Sensitive Query String

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-598](https://cwe.mitre.org/data/definitions/598.html)

## Description
The web application uses an HTTP method to process a request, but the request includes sensitive information in the query string.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Implementation**: When sending sensitive information, only include it in the request body or request headers instead of the query string. This may require avoiding use of GET requests.

## Related weaknesses
- CWE-201 (ChildOf)

## Observed examples (CVE)
- **CVE-2025-1738**: Security camera includes a password in its query string
- **CVE-2025-31954**: ML/NLP-based automation product calls a GET method with sensitive information in the query string.
- **CVE-2024-31842**: Web-based communication product includes an access token in the query string of a GET request
- **CVE-2022-23546**: A discussion platform leaks private information in GET requests.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/598.html
