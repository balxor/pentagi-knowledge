---
capec_id: CAPEC-273
name: HTTP Response Smuggling
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-74, CWE-436, CWE-444]
related_attack: []
url: https://capec.mitre.org/data/definitions/273.html
tags: [mitre-capec, attack-pattern, CAPEC-273]
---

# CAPEC-273 - HTTP Response Smuggling

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-273](https://capec.mitre.org/data/definitions/273.html)

## Description
<xhtml:p>An adversary manipulates and injects malicious content in the form of secret unauthorized HTTP responses, into a single HTTP response from a vulnerable or compromised back-end HTTP agent (e.g., server).</xhtml:p>
            <xhtml:p>See CanPrecede relationships for possible consequences.</xhtml:p>

## Extended description
In the maliciously manipulated HTTP response, an adversary can add duplicate header fields that HTTP agents interpret as belonging to separate responses. The combined HTTP response ends up being parsed or interpreted as two or more HTTP responses by the targeted client HTTP agent. This allows malicious HTTP responses to bypass security controls. This is performed by the abuse of interpretation and parsing discrepancies in different intermediary HTTP agents (e.g., load balancer, reverse proxy, web caching proxies, application firewalls, etc.) or client HTTP agents (e.g., web browser) in the path of the malicious HTTP responses. This attack usually involves the misuse of the HTTP headers: Content-Length and Transfer-Encoding. These abuses are discussed in RFC 2616 #4.4.3 and section #4.2 and are related to ordering and precedence of these headers. [REF-38] Additionally this attack can be performed through modification and/or fuzzing of parameters composing the request-line of HTTP messages. This attack is usually the result of the usage of outdated or incompatible HTTP protocol versions in the HTTP agents. This differs from CAPEC-33 HTTP Request Smuggling, which is usually an attempt to compromise a back-end HTTP agent via HTTP Request messages. HTTP Response Smuggling is an attempt to compromise a client agent (e.g., web browser) . HTTP Splitting (CAPEC-105 and CAPEC-34) is different from HTTP Smuggling due to the fact that during implementation of asynchronous requests, HTTP Splitting requires the embedding/injection of arbitrary HTML headers and content through user input into browser cookies or Ajax web/browser object parameters like XMLHttpRequest.

## Prerequisites
- A vulnerable or compromised server or domain/site capable of allowing adversary to insert/inject malicious content that will appear in the server's response to target HTTP agents (e.g., proxies and users' web browsers).
- Differences in the way the two HTTP agents parse and interpret HTTP responses and its headers.
- HTTP agents running on HTTP/1.1 that allow for Keep Alive mode, Pipelined queries, and Chunked queries and responses.

## Skills required
- **Medium**: Possess knowledge on the exact details in the discrepancies between several targeted HTTP agents in path of an HTTP message in parsing its message structure and individual headers.

## Resources required
- Tools capable of monitoring HTTP messages, and crafting malicious HTTP messages and/or injecting malicious content into HTTP messages.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands
- **Confidentiality**: Execute Unauthorized Commands, Gain Privileges
- **Integrity**: Execute Unauthorized Commands, Modify Data

## Execution flow
Execution Flow Explore Survey network to identify target: The adversary performs network reconnaissance by monitoring relevant traffic to identify the network path and parsing of the HTTP messages with the goal of identifying potential targets. Techniques Scan networks to fingerprint HTTP infrastructure and monitor HTTP traffic to identify HTTP network path with a tool such as a Network Protocol Analyzer. Experiment Identify vulnerabilities in targeted HTTP infrastructure and technologies: The adversary sends a variety of benign/ambiguous HTTP requests to observe responses from HTTP infrastructure to intended targets in order to identify differences/discrepancies in the interpretation and parsing of HTTP requests by examining supported HTTP protocol versions, message sizes, and HTTP headers. Cause differential HTTP responses by experimenting with identified HTTP Response vulnerabilities: The adversary sends maliciously crafted HTTP request to back-end HTTP infrastructure to inject adversary data into HTTP responses (intended for intermediary and/or front-end client/victim HTTP agents communicating with back-end HTTP infrastructure) for the purpose of interfering with the parsing of HTTP response. The intended consequences of the malicious HTTP request and the subsequent adversary injection and manipulation of HTTP responses will be observed to confirm applicability of identified vulnerabilities in the adversary's plan of attack. Techniques Continue the monitoring of HTTP traffic. Inject additional HTTP headers to utilize various combinations of HTTP Headers within a single HTTP message such as: Content-Length & Transfer-Encoding (CL;TE), Transfer-Encoding & Content-Length (TE;CL), or double Transfer-Encoding (TE;TE), so that additional embedded message or data in the body of the original message are unprocessed and treated as part of subsequent messages by the intended target HTTP agent. From these HTTP Header combinations the adversary observes any timing delays (usually in the form of HTTP 404 Error response) or any other unintended consequences. For CL;TE and TE;CL HTTP headers combination, the first HTTP agent, in the HTTP message path that receives the HTTP message, takes precedence or only processes the one header but not the other, while the second/final HTTP agent processes the opposite header allowing for embedded HTTP message to be ignored and smuggled to the intended target HTTP agent. For TE;TE HTTP headers combination, all HTTP agents in HTTP message path process Transfer-Encoding header, however, adversary obfuscation of one of the Transfer-Encoding headers, by not adhering strictly to the protocol specification, can cause it to be unprocessed/ignored by a designated HTTP agent, hence allowing embedded HTTP messages to be smuggled. See Mitigations for details. Construct a very large HTTP message via multiple Content-Length headers of various data lengths that can potentially cause subsequent messages to be ignored by an intermediary HTTP agent (e.g., firewall) and/or eventually parsed separately by the target HTTP agent. Note that most modern HTTP infrastructure reject HTTP messages with multiple Content-Length headers. Monitor HTTP traffic using a tool such as a Network Protocol Analyzer. Exploit Perform HTTP Response Smuggling attack: Using knowledge discovered in the experiment section above, smuggle a message to cause one of the consequences. Techniques Leverage techniques identified in the Experiment Phase.

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
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-436](https://cwe.mitre.org/data/definitions/436.html)
- [CWE-444](https://cwe.mitre.org/data/definitions/444.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/273.html
