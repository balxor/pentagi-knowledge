---
cwe_id: CWE-444
name: Inconsistent Interpretation of HTTP Requests ('HTTP Request/Response Smuggling')
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: [CAPEC-273, CAPEC-33]
url: https://cwe.mitre.org/data/definitions/444.html
tags: [mitre-cwe, weakness, CWE-444]
---

# CWE-444 - Inconsistent Interpretation of HTTP Requests ('HTTP Request/Response Smuggling')

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-444](https://cwe.mitre.org/data/definitions/444.html)

## Description
The product acts as an intermediary HTTP agent (such as a proxy or firewall) in the data flow between two entities such as a client and server, but it does not interpret malformed HTTP requests or responses in ways that are consistent with how the messages will be processed by those entities that are at the ultimate destination.

## Extended description
HTTP requests or responses ("messages") can be malformed or unexpected in ways that cause web servers or clients to interpret the messages in different ways than intermediary HTTP agents such as load balancers, reverse proxies, web caching proxies, application firewalls, etc. For example, an adversary may be able to add duplicate or different header fields that a client or server might interpret as one set of messages, whereas the intermediary might interpret the same sequence of bytes as a different set of messages. For example, discrepancies can arise in how to handle duplicate headers like two Transfer-encoding (TE) or two Content-length (CL), or the malicious HTTP message will have different headers for TE and CL. The inconsistent parsing and interpretation of messages can allow the adversary to "smuggle" a message to the client/server without the intermediary being aware of it. This weakness is usually the result of the usage of outdated or incompatible HTTP protocol versions in the HTTP agents.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Integrity, Non-Repudiation, Access Control**: Unexpected State, Hide Activities, Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: Use a web server that employs a strict HTTP parsing procedure, such as Apache [REF-433].
- **Implementation**: Use only SSL communication.
- **Implementation**: Terminate the client session after each request.
- **System Configuration**: Turn all pages to non-cacheable.

## Related attack patterns (CAPEC)
- [CAPEC-273](https://capec.mitre.org/data/definitions/273.html)
- [CAPEC-33](https://capec.mitre.org/data/definitions/33.html)

## Related weaknesses
- CWE-436 (ChildOf)
- CWE-436 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-24766**: SSL/TLS-capable proxy allows HTTP smuggling when used in tandem with HTTP/1.0 services, due to inconsistent interpretation and input sanitization of HTTP messages within the body of another message
- **CVE-2021-37147**: Chain: caching proxy server has improper input validation (CWE-20) of headers, allowing HTTP response smuggling (CWE-444) using an "LF line ending"
- **CVE-2020-8287**: Node.js platform allows request smuggling via two Transfer-Encoding headers
- **CVE-2006-6276**: Web servers allow request smuggling via inconsistent HTTP headers.
- **CVE-2005-2088**: HTTP server allows request smuggling with both a "Transfer-Encoding: chunked" header and a Content-Length header
- **CVE-2005-2089**: HTTP server allows request smuggling with both a "Transfer-Encoding: chunked" header and a Content-Length header

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/444.html
