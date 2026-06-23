---
capec_id: CAPEC-664
name: Server Side Request Forgery
type: attack-pattern
abstraction: Standard
likelihood: High
severity: High
related_cwe: [CWE-918, CWE-20]
related_attack: []
url: https://capec.mitre.org/data/definitions/664.html
tags: [mitre-capec, attack-pattern, CAPEC-664]
---

# CAPEC-664 - Server Side Request Forgery

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-664](https://capec.mitre.org/data/definitions/664.html)

## Description
<xhtml:p>An adversary exploits improper input validation by submitting maliciously crafted input to a target application running on a server, with the goal of forcing the server to make a request either to itself, to web services running in the server’s internal network, or to external third parties. If successful, the adversary’s request will be made with the server’s privilege level, bypassing its authentication controls. This ultimately allows the adversary to access sensitive data, execute commands on the server’s network, and make external requests with the stolen identity of the server. Server Side Request Forgery attacks differ from Cross Site Request Forgery attacks in that they target the server itself, whereas CSRF attacks exploit an insecure user authentication mechanism to perform unauthorized actions on the user's behalf.</xhtml:p>

## Prerequisites
- Server must be running a web application that processes HTTP requests.

## Skills required
- **High**: The adversary will be required to access internal resources, extract information, or leverage the services running on the server to perform unauthorized actions such as traversing the local network or routing a reflected TCP DDoS through them.
- **Medium**: The adversary will have to detect the vulnerability through an intermediary service or specify maliciously crafted URLs and analyze the server response.

## Resources required
- [None] No specialized resources are required to execute this type of attack.

## Consequences
- **Availability**: Modify Data, Resource Consumption
- **Confidentiality**: Modify Data, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Find target application: Find target web application that accepts a user input and retrieves data from the server Experiment Examine existing application requests: Examine HTTP/GET requests to view the URL query format. Adversaries test to see if this type of attack is possible through weaknesses in an application's protection to Server Side Request Forgery Techniques Attempt manipulating the URL to retrieve an error response/code from the server to determine if URL/request validation is done. Use a list of XSS probe strings to specify as parameters to known URLs. If possible, use probe strings with unique identifiers. Create a GET request with a common server file path such as /etc/passwd as a parameter and examine output. Exploit Malicious request: Adversary crafts a malicious URL request that assumes the privilege level of the server to query internal or external network services and sends the request to the application

## Mitigations
- Handling incoming requests securely is the first line of action to mitigate this vulnerability. This can be done through URL validation.
- Further down the process flow, examining the response and verifying that it is as expected before sending would be another way to secure the server.
- Allowlist the DNS name or IP address of every service the web application is required to access is another effective security measure. This ensures the server cannot make external requests to arbitrary services.
- Requiring authentication for local services adds another layer of security between the adversary and internal services running on the server. By enforcing local authentication, an adversary will not gain access to all internal services only with access to the server.
- Enforce the usage of relevant URL schemas. By limiting requests be made only through HTTP or HTTPS, for example, attacks made through insecure schemas such as file://, ftp://, etc. can be prevented.

## Related weaknesses (CWE)
- [CWE-918](https://cwe.mitre.org/data/definitions/918.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/664.html
