---
capec_id: CAPEC-57
name: Utilizing REST's Trust in the System Resource to Obtain Sensitive Data
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Very High
related_cwe: [CWE-300, CWE-287, CWE-693]
related_attack: [T1040]
url: https://capec.mitre.org/data/definitions/57.html
tags: [mitre-capec, attack-pattern, CAPEC-57]
---

# CAPEC-57 - Utilizing REST's Trust in the System Resource to Obtain Sensitive Data

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-57](https://capec.mitre.org/data/definitions/57.html)

## Description
This attack utilizes a REST(REpresentational State Transfer)-style applications' trust in the system resources and environment to obtain sensitive data once SSL is terminated.

## Extended description
Rest applications premise is that they leverage existing infrastructure to deliver web services functionality. An example of this is a Rest application that uses HTTP Get methods and receives a HTTP response with an XML document. These Rest style web services are deployed on existing infrastructure such as Apache and IIS web servers with no SOAP stack required. Unfortunately from a security standpoint, there frequently is no interoperable identity security mechanism deployed, so Rest developers often fall back to SSL to deliver security. In large data centers, SSL is typically terminated at the edge of the network - at the firewall, load balancer, or router. Once the SSL is terminated the HTTP request is in the clear (unless developers have hashed or encrypted the values, but this is rare). The adversary can utilize a sniffer such as Wireshark to snapshot the credentials, such as username and password that are passed in the clear once SSL is terminated. Once the adversary gathers these credentials, they can submit requests to the web service provider just as authorized user do. There is not typically an authentication on the client side, beyond what is passed in the request itself so once this is compromised, then this is generally sufficient to compromise the service's authentication scheme.

## Prerequisites
- Opportunity to intercept must exist beyond the point where SSL is terminated.
- The adversary must be able to insert a listener actively (proxying the communication) or passively (sniffing the communication) in the client-server communication path.

## Skills required
- **Low**: To insert a network sniffer or other listener into the communication stream

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges

## Execution flow
Execution Flow Explore Find a REST-style application that uses SSL: The adversary must first find a REST-style application that uses SSL to target. Because this attack is easier to carry out from inside of a server network, it is likely that an adversary could have inside knowledge of how services operate. Experiment Insert a listener to sniff client-server communication: The adversary inserts a listener that must exist beyond the point where SSL is terminated. This can be placed on the client side if it is believed that sensitive information is being sent to the client as a response, although most often the listener will be placed on the server side to listen for client authentication information. Techniques Run wireshark or tcpdump on a device that is on the inside of a firewall, load balancer, or router of a network and capture traffic after SSL has been terminated Exploit Gather information passed in the clear: If developers have not hashed or encrypted data sent in the sniffed request, the adversary will be able to read this data in the clear. Most commonly, they will now have a username or password that they can use to submit requests to the web service just as an authorized user

## Mitigations
- Implementation: Implement message level security such as HMAC in the HTTP communication
- Design: Utilize defense in depth, do not rely on a single security mechanism like SSL
- Design: Enforce principle of least privilege

## Related weaknesses (CWE)
- [CWE-300](https://cwe.mitre.org/data/definitions/300.html)
- [CWE-287](https://cwe.mitre.org/data/definitions/287.html)
- [CWE-693](https://cwe.mitre.org/data/definitions/693.html)

## Related ATT&CK techniques
- T1040

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/57.html
