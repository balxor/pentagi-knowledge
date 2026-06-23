---
cwe_id: CWE-239
name: Failure to Handle Incomplete Element
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/239.html
tags: [mitre-cwe, weakness, CWE-239]
---

# CWE-239 - Failure to Handle Incomplete Element

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-239](https://cwe.mitre.org/data/definitions/239.html)

## Description
The product does not properly handle when a particular element is not completely specified.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Other**: Varies by Context, Unexpected State

## Related weaknesses
- CWE-237 (ChildOf)
- CWE-404 (PeerOf)

## Observed examples (CVE)
- **CVE-2002-1532**: HTTP GET without \r\n\r\n CRLF sequences causes product to wait indefinitely and prevents other users from accessing it.
- **CVE-2003-0195**: Partial request is not timed out.
- **CVE-2005-2526**: MFV. CPU exhaustion in printer via partial printing request then early termination of connection.
- **CVE-2002-1906**: CPU consumption by sending incomplete HTTP requests and leaving the connections open.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/239.html
