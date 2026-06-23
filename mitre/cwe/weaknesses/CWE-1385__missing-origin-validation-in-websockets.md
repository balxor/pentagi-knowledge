---
cwe_id: CWE-1385
name: Missing Origin Validation in WebSockets
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1385.html
tags: [mitre-cwe, weakness, CWE-1385]
---

# CWE-1385 - Missing Origin Validation in WebSockets

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-1385](https://cwe.mitre.org/data/definitions/1385.html)

## Description
The product uses a WebSocket, but it does not properly verify that the source of data or communication is valid.

## Extended description
WebSockets provide a bi-directional low latency communication (near real-time) between a client and a server. WebSockets are different than HTTP in that the connections are long-lived, as the channel will remain open until the client or the server is ready to send the message, whereas in HTTP, once the response occurs (which typically happens immediately), the transaction completes. A WebSocket can leverage the existing HTTP protocol over ports 80 and 443, but it is not limited to HTTP. WebSockets can make cross-origin requests that are not restricted by browser-based protection mechanisms such as the Same Origin Policy (SOP) or Cross-Origin Resource Sharing (CORS). Without explicit origin validation, this makes CSRF attacks more powerful.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Confidentiality, Integrity, Availability, Non-Repudiation, Access Control**: Varies by Context, Gain Privileges or Assume Identity, Bypass Protection Mechanism, Read Application Data, Modify Application Data, DoS: Crash, Exit, or Restart

## Potential mitigations
- **Implementation**: Enable CORS-like access restrictions by verifying the 'Origin' header during the WebSocket handshake.
- **Implementation**: Use a randomized CSRF token to verify requests.
- **Implementation**: Use TLS to securely communicate using 'wss' (WebSocket Secure) instead of 'ws'.
- **Architecture and Design, Implementation**: Require user authentication prior to the WebSocket connection being established. For example, the WS library in Node has a 'verifyClient' function.
- **Implementation**: Leverage rate limiting to prevent against DoS. Use of the leaky bucket algorithm can help with this.
- **Implementation**: Use a library that provides restriction of the payload size. For example, WS library for Node includes 'maxPayloadoption' that can be set.
- **Implementation**: Treat data/input as untrusted in both directions and apply the same data/input sanitization as XSS, SQLi, etc.

## Related weaknesses
- CWE-346 (ChildOf)

## Observed examples (CVE)
- **CVE-2020-25095**: web console for SIEM product does not check Origin header, allowing Cross Site WebSocket Hijacking (CSWH)
- **CVE-2018-6651**: Chain: gaming client attempts to validate the Origin header, but only uses a substring, allowing Cross-Site WebSocket hijacking by forcing requests from an origin whose hostname is a substring of the valid origin.
- **CVE-2018-14730**: WebSocket server does not check the origin of requests, allowing attackers to steal developer's code using a ws://127.0.0.1:3123/ connection.
- **CVE-2018-14731**: WebSocket server does not check the origin of requests, allowing attackers to steal developer's code using a ws://127.0.0.1/ connection to a randomized port number.
- **CVE-2018-14732**: WebSocket server does not check the origin of requests, allowing attackers to steal developer's code using a ws://127.0.0.1:8080/ connection.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1385.html
