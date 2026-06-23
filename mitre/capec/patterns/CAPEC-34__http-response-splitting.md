---
capec_id: CAPEC-34
name: HTTP Response Splitting
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-74, CWE-113, CWE-138, CWE-436]
related_attack: []
url: https://capec.mitre.org/data/definitions/34.html
tags: [mitre-capec, attack-pattern, CAPEC-34]
---

# CAPEC-34 - HTTP Response Splitting

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-34](https://capec.mitre.org/data/definitions/34.html)

## Description
<xhtml:p>An adversary manipulates and injects malicious content, in the form of secret unauthorized HTTP responses, into a single HTTP response from a vulnerable or compromised back-end HTTP agent (e.g., web server) or into an already spoofed HTTP response from an adversary controlled domain/site.</xhtml:p>
            <xhtml:p>See CanPrecede relationships for possible consequences.</xhtml:p>

## Extended description
Malicious user input is injected into various standard and/or user defined HTTP headers within a HTTP Response through use of Carriage Return (CR), Line Feed (LF), Horizontal Tab (HT), Space (SP) characters as well as other valid/RFC compliant special characters, and unique character encoding. A single HTTP response ends up being split as two or more HTTP responses by the targeted client HTTP agent parsing the original maliciously manipulated HTTP response. This allows malicious HTTP responses to bypass security controls in order to implement malicious actions and provide malicious content that allows access to sensitive data and to compromise applications and users. This is performed by the abuse of interpretation and parsing discrepancies in different intermediary HTTP agents (load balancer, reverse proxy, web caching proxies, application firewalls, etc.) or client HTTP agents (e.g., web browser) in the path of the malicious HTTP responses. This attack is usually the result of the usage of outdated or incompatible HTTP protocol versions as well as lack of syntax checking and filtering of user input in the HTTP agents receiving HTTP messages in the path. This differs from CAPEC-105 HTTP Request Splitting, which is usually an attempt to compromise a back-end HTTP agent via HTTP Request messages. HTTP Response Splitting is an attempt to compromise a client agent (e.g., web browser) by sending malicious content in HTTP responses from back-end HTTP infrastructure. HTTP Smuggling (CAPEC-33 and CAPEC-273) is different from HTTP Splitting due to the fact it relies upon discrepancies in the interpretation of various HTTP Headers and message sizes and not solely user input of special characters and character encoding. HTTP Smuggling was established to circumvent mitigations against HTTP Request Splitting techniques.

## Prerequisites
- A vulnerable or compromised server or domain/site capable of allowing adversary to insert/inject malicious content that will appear in the server's response to target HTTP agents (e.g., proxies and users' web browsers).
- Differences in the way the two HTTP agents parse and interpret HTTP requests and its headers.
- HTTP headers capable of being user-manipulated.
- HTTP agents running on HTTP/1.0 or HTTP/1.1 that allow for Keep Alive mode, Pipelined queries, and Chunked queries and responses.

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
Execution Flow Explore Survey network to identify target: The adversary performs network reconnaissance by monitoring relevant traffic to identify the network path and parsing of the HTTP messages with the goal of identifying potential targets Techniques Scan networks to fingerprint HTTP infrastructure and monitor HTTP traffic to identify HTTP network path with a tool such as a Network Protocol Analyzer. Experiment Identify vulnerabilities in targeted HTTP infrastructure and technologies: The adversary sends a variety of benign/ambiguous HTTP requests to observe responses from HTTP infrastructure in order to identify differences/discrepancies in the interpretation and parsing of HTTP requests by examining supported HTTP protocol versions, HTTP headers, syntax checking and input filtering. Cause differential HTTP responses by experimenting with identified HTTP Request vulnerabilities: The adversary sends maliciously crafted HTTP request to back-end HTTP infrastructure to inject adversary data (in the form of HTTP headers with custom strings and embedded web scripts and objects) into HTTP responses (intended for intermediary and/or front-end client/victim HTTP agents communicating with back-end HTTP infrastructure) for the purpose of interfering with the parsing of HTTP responses by intermediary and front-end client/victim HTTP agents. The intended consequences of the malicious HTTP request and the subsequent adversary injection and manipulation of HTTP responses to intermediary and front-end client/victim HTTP agents, will be observed to confirm applicability of identified vulnerabilities in the adversary's plan of attack. Techniques Continue the monitoring of HTTP traffic. Utilize different sequences of special characters (CR - Carriage Return, LF - Line Feed, HT - Horizontal Tab, SP - Space and etc.) to bypass filtering and back-end encoding and to embed: additional HTTP Requests with their own headers malicious web scripts into parameters of HTTP Request headers (e.g., browser cookies like Set-Cookie or Ajax web/browser object parameters like XMLHttpRequest) adversary chosen encoding (e.g., UTF-7) to utilize additional special characters (e.g., > and Note that certain special characters and character encoding may be applicable only to intermediary and front-end agents with rare configurations or that are not RFC compliant. Follow an unrecognized (sometimes a RFC compliant) HTTP header with a subsequent HTTP request to potentially cause the HTTP request to be ignored and interpreted as part of the preceding HTTP request. Exploit Perform HTTP Response Splitting attack: Using knowledge discovered in the experiment section above, smuggle a message to cause one of the consequences. Techniques Leverage techniques identified in the Experiment Phase.

## Mitigations
- Design: evaluate HTTP agents prior to deployment for parsing/interpretation discrepancies.
- Configuration: front-end HTTP agents notice ambiguous requests.
- Configuration: back-end HTTP agents reject ambiguous requests and close the network connection.
- Configuration: Disable reuse of back-end connections.
- Configuration: Use HTTP/2 for back-end connections.
- Configuration: Use the same web server software for front-end and back-end server.
- Implementation: Utilize a Web Application Firewall (WAF) that has built-in mitigation to detect abnormal requests/responses.
- Configuration: Install latest vendor security patches available for both intermediary and back-end HTTP infrastructure (i.e. proxies and web servers)
- Configuration: Ensure that HTTP infrastructure in the chain or network path utilize a strict uniform parsing process.
- Implementation: Utilize intermediary HTTP infrastructure capable of filtering and/or sanitizing user-input.

## Related weaknesses (CWE)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-113](https://cwe.mitre.org/data/definitions/113.html)
- [CWE-138](https://cwe.mitre.org/data/definitions/138.html)
- [CWE-436](https://cwe.mitre.org/data/definitions/436.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/34.html
