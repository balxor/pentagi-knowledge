---
capec_id: CAPEC-105
name: HTTP Request Splitting
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-74, CWE-113, CWE-138, CWE-436]
related_attack: []
url: https://capec.mitre.org/data/definitions/105.html
tags: [mitre-capec, attack-pattern, CAPEC-105]
---

# CAPEC-105 - HTTP Request Splitting

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-105](https://capec.mitre.org/data/definitions/105.html)

## Description
<xhtml:p>An adversary abuses the flexibility and discrepancies in the parsing and interpretation of HTTP Request messages by different intermediary HTTP agents (e.g., load balancer, reverse proxy, web caching proxies, application firewalls, etc.) to split a single HTTP request into multiple unauthorized and malicious HTTP requests to a back-end HTTP agent (e.g., web server).</xhtml:p>
            <xhtml:p>See CanPrecede relationships for possible consequences.</xhtml:p>

## Extended description
This entails the adversary injecting malicious user input into various standard and/or user defined HTTP headers within a HTTP Request through user input of Carriage Return (CR), Line Feed (LF), Horizontal Tab (HT), Space (SP) characters as well as other valid/RFC compliant special characters and unique character encoding. This malicious user input allows for web script to be injected in HTTP headers as well as into browser cookies or Ajax web/browser object parameters like XMLHttpRequest during implementation of asynchronous requests. This attack is usually the result of the usage of outdated or incompatible HTTP protocol versions as well as lack of syntax checking and filtering of user input in the HTTP agents receiving HTTP messages in the path. This differs from CAPEC-34 HTTP Response Splitting, which is usually an attempt to compromise a client agent (e.g., web browser) by sending malicious content in HTTP responses from back-end HTTP infrastructure. HTTP Request Splitting is an attempt to compromise a back-end HTTP agent via HTTP Request messages. HTTP Smuggling (CAPEC-33 and CAPEC-273) is different from HTTP Splitting due to the fact it relies upon discrepancies in the interpretation of various HTTP Headers and message sizes and not solely user input of special characters and character encoding. HTTP Smuggling was established to circumvent mitigations against HTTP Request Splitting techniques.

## Prerequisites
- An additional intermediary HTTP agent such as an application firewall or a web caching proxy between the adversary and the second agent such as a web server, that sends multiple HTTP messages over same network connection.
- Differences in the way the two HTTP agents parse and interpret HTTP requests and its headers.
- HTTP headers capable of being user-manipulated.
- HTTP agents running on HTTP/1.0 or HTTP/1.1 that allow for Keep Alive mode, Pipelined queries, and Chunked queries and responses.

## Skills required
- **Medium**: Possess knowledge on the exact details in the discrepancies between several targeted HTTP agents in path of an HTTP message in parsing its message structure and individual headers.

## Resources required
- Tools capable of crafting malicious HTTP messages and monitoring HTTP messages responses.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands
- **Confidentiality**: Execute Unauthorized Commands, Gain Privileges, Read Data
- **Integrity**: Execute Unauthorized Commands, Modify Data

## Execution flow
Execution Flow Explore Survey network to identify target: The adversary performs network reconnaissance by monitoring relevant traffic to identify the network path and parsing of the HTTP messages with the goal of identifying potential targets. Techniques Scan networks to fingerprint HTTP infrastructure and monitor HTTP traffic to identify HTTP network path with a tool such as a Network Protocol Analyzer. Experiment Identify vulnerabilities in targeted HTTP infrastructure and technologies: The adversary sends a variety of benign/ambiguous HTTP requests to observe responses from HTTP infrastructure in order to identify differences/discrepancies in the interpretation and parsing of HTTP requests by examining supported HTTP protocol versions, HTTP headers, syntax checking and input filtering. Cause differential HTTP responses by experimenting with identified HTTP Request vulnerabilities: The adversary sends maliciously crafted HTTP requests with custom strings and embedded web scripts and objects in HTTP headers to interfere with the parsing of intermediary and back-end HTTP infrastructure, followed by normal/benign HTTP request from the adversary or a random user. The intended consequences of the malicious HTTP requests will be observed in the HTTP infrastructure response to the normal/benign HTTP request to confirm applicability of identified vulnerabilities in the adversary's plan of attack. Techniques Continue the monitoring of HTTP traffic. Utilize different sequences of special characters (CR - Carriage Return, LF - Line Feed, HT - Horizontal Tab, SP - Space and etc.) to bypass filtering and back-end encoding and to embed: additional HTTP Requests with their own headers malicious web scripts into parameters of HTTP Request headers (e.g., browser cookies like Set-Cookie or Ajax web/browser object parameters like XMLHttpRequest) adversary chosen encoding (e.g., UTF-7) to utilize additional special characters (e.g., > and Note that certain special characters and character encoding may be applicable only to intermediary and front-end agents with rare configurations or that are not RFC compliant. Follow an unrecognized (sometimes a RFC compliant) HTTP header with a subsequent HTTP request to potentially cause the HTTP request to be ignored and interpreted as part of the preceding HTTP request. Exploit Perform HTTP Request Splitting attack: Using knowledge discovered in the experiment section above, smuggle a message to cause one of the consequences. Techniques Leverage techniques identified in the Experiment Phase.

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

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/105.html
