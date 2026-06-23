---
capec_id: CAPEC-33
name: HTTP Request Smuggling
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-444]
related_attack: []
url: https://capec.mitre.org/data/definitions/33.html
tags: [mitre-capec, attack-pattern, CAPEC-33]
---

# CAPEC-33 - HTTP Request Smuggling

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-33](https://capec.mitre.org/data/definitions/33.html)

## Description
<xhtml:p>An adversary abuses the flexibility and discrepancies in the parsing and interpretation of HTTP Request messages using various HTTP headers, request-line and body parameters as well as message sizes (denoted by the end of message signaled by a given HTTP header) by different intermediary HTTP agents (e.g., load balancer, reverse proxy, web caching proxies, application firewalls, etc.) to secretly send unauthorized and malicious HTTP requests to a back-end HTTP agent (e.g., web server).</xhtml:p>
            <xhtml:p>See CanPrecede relationships for possible consequences.</xhtml:p>

## Extended description
A maliciously crafted HTTP request, which contains a second secretly embedded HTTP request is interpreted by an intermediary web proxy as single benign HTTP request, is forwarded to a back-end server, that interprets and parses the HTTP request as two authorized benign HTTP requests bypassing security controls. This attack usually involves the misuse of the HTTP headers: Content-Length and Transfer-Encoding. These abuses are discussed in RFC 2616 #4.4.3 and section #4.2 and are related to ordering and precedence of these headers. [REF-38] Additionally this attack can be performed through modification and/or fuzzing of parameters composing the request-line of HTTP messages. This attack is usually the result of the usage of outdated or incompatible HTTP protocol versions in the HTTP agents. This differs from CAPEC-273 HTTP Response Smuggling, which is usually an attempt to compromise a client agent (e.g., web browser) by sending malicious content in HTTP responses from back-end HTTP infrastructure. HTTP Request Smuggling is an attempt to compromise a back-end HTTP agent via HTTP Request messages. HTTP Splitting (CAPEC-105 and CAPEC-34) is different from HTTP Smuggling due to the fact that during implementation of asynchronous requests, HTTP Splitting requires the embedding/injection of arbitrary HTML headers and content through user input into browser cookies or Ajax web/browser object parameters like XMLHttpRequest.

## Prerequisites
- An additional intermediary HTTP agent such as an application firewall or a web caching proxy between the adversary and the second agent such as a web server, that sends multiple HTTP messages over same network connection.
- Differences in the way the two HTTP agents parse and interpret HTTP requests and its headers.
- HTTP agents running on HTTP/1.1 that allow for Keep Alive mode, Pipelined queries, and Chunked queries and responses.

## Skills required
- **Medium**: Possess knowledge on the exact details in the discrepancies between several targeted HTTP agents in path of an HTTP message in parsing its message structure and individual headers.

## Resources required
- Tools capable of crafting malicious HTTP messages and monitoring HTTP message responses.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands
- **Confidentiality**: Execute Unauthorized Commands, Gain Privileges
- **Integrity**: Execute Unauthorized Commands, Modify Data

## Execution flow
Execution Flow Explore Survey network to identify target: The adversary performs network reconnaissance by monitoring relevant traffic to identify the network path and parsing of the HTTP messages with the goal of identifying potential targets. Techniques Scan networks to fingerprint HTTP infrastructure and monitor HTTP traffic to identify HTTP network path with a tool such as a Network Protocol Analyzer. Experiment Identify vulnerabilities in targeted HTTP infrastructure and technologies: The adversary sends a variety of benign/ambiguous HTTP requests to observe responses from HTTP infrastructure in order to identify differences/discrepancies in the interpretation and parsing of HTTP requests by examining supported HTTP protocol versions, message sizes, and HTTP headers. Cause differential HTTP responses by experimenting with identified HTTP Request vulnerabilities: The adversary sends maliciously crafted HTTP requests to interfere with the parsing of intermediary and back-end HTTP infrastructure, followed by normal/benign HTTP request from the adversary or a random user. The intended consequences of the malicious HTTP requests will be observed in the HTTP infrastructure response to the normal/benign HTTP request to confirm applicability of identified vulnerabilities in the adversary's plan of attack. Techniques Continue the monitoring of HTTP traffic. Utilize various combinations of HTTP Headers within a single HTTP Request such as: Content-Length & Transfer-Encoding (CL;TE), Transfer-Encoding & Content-Length (TE;CL), or double Transfer-Encoding (TE;TE), so that additional embedded requests or data in the body of the original request are unprocessed and treated as part of subsequent requests by the intended target HTTP agent. From these HTTP Header combinations the adversary observes any timing delays (usually in the form of HTTP 404 Error response) or any other unintended consequences. For CL;TE and TE;CL HTTP header combinations, the first HTTP agent, in the HTTP message path that receives the HTTP request, takes precedence or only processes one header but not the other, while the second/final HTTP agent processes the opposite header, allowing for embedded HTTP requests to be ignored and smuggled to the intended target HTTP agent. For TE;TE HTTP headers combination, all HTTP agents in HTTP message path process Transfer-Encoding header, however, adversary obfuscation (see Mitigations for details) of one of the Transfer-Encoding headers, by not adhering strictly to the protocol specification, can cause it to be unprocessed/ignored by a designated HTTP agent, hence allowing embedded HTTP requests to be smuggled. . Construct a very large HTTP request using multiple Content-Length headers of various data lengths that can potentially cause subsequent requests to be ignored by an intermediary HTTP agent (firewall) and/or eventually parsed separately by the target HTTP agent (web server). Note that most modern HTTP infrastructure reject HTTP requests with multiple Content-Length headers. Follow an unrecognized (sometimes a RFC compliant) HTTP header with a subsequent HTTP request to potentially cause the HTTP request to be ignored and interpreted as part of the preceding HTTP request. Exploit Perform HTTP Request Smuggling attack: Using knowledge discovered in the experiment section above, smuggle a message to cause one of the consequences. Techniques Leverage techniques identified in the Experiment Phase.

## Mitigations
- Design: evaluate HTTP agents prior to deployment for parsing/interpretation discrepancies.
- Configuration: front-end HTTP agents notice ambiguous requests.
- Configuration: back-end HTTP agents reject ambiguous requests and close the network connection.
- Configuration: Disable reuse of back-end connections.
- Configuration: Use HTTP/2 for back-end connections.
- Configuration: Use the same web server software for front-end and back-end server.
- Implementation: Utilize a Web Application Firewall (WAF) that has built-in mitigation to detect abnormal requests/responses.
- Configuration: Prioritize Transfer-Encoding header over Content-Length, whenever an HTTP message contains both.
- Configuration: Disallow HTTP messages with both Transfer-Encoding and Content-Length or Double Content-Length Headers.
- Configuration: Disallow Malformed/Invalid Transfer-Encoding Headers used in obfuscation, such as: Headers with no space before the value “chunked” Headers with extra spaces Headers beginning with trailing characters Headers providing a value “chunk” instead of “chunked” (the server normalizes this as chunked encoding) Headers with multiple spaces before the value “chunked” Headers with quoted values (whether single or double quotations) Headers with CRLF characters before the value “chunked” Values with invalid characters
- Configuration: Install latest vendor security patches available for both intermediary and back-end HTTP infrastructure (i.e. proxies and web servers)
- Configuration: Ensure that HTTP infrastructure in the chain or network path utilize a strict uniform parsing process.
- Implementation: Utilize intermediary HTTP infrastructure capable of filtering and/or sanitizing user-input.

## Related weaknesses (CWE)
- [CWE-444](https://cwe.mitre.org/data/definitions/444.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/33.html
