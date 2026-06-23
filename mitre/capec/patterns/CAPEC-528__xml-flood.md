---
capec_id: CAPEC-528
name: XML Flood
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: Medium
related_cwe: [CWE-770]
related_attack: [T1499.002, T1498.001]
url: https://capec.mitre.org/data/definitions/528.html
tags: [mitre-capec, attack-pattern, CAPEC-528]
---

# CAPEC-528 - XML Flood

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-528](https://capec.mitre.org/data/definitions/528.html)

## Description
An adversary may execute a flooding attack using XML messages with the intent to deny legitimate users access to a web service. These attacks are accomplished by sending a large number of XML based requests and letting the service attempt to parse each one. In many cases this type of an attack will result in a XML Denial of Service (XDoS) due to an application becoming unstable, freezing, or crashing.

## Extended description
XDoS is most closely associated with web services, SOAP, and Rest, because remote service requesters can post malicious XML payloads to the service provider designed to exhaust the service provider's memory, CPU, and/or disk space. The main weakness in XDoS is that the service provider generally must inspect, parse, and validate the XML messages to determine routing, workflow, security considerations, and so on. It is exactly these inspection, parsing, and validation routines that XDoS targets. This attack exploits the loosely coupled nature of web services, where the service provider has little to no control over the service requester and any messages the service requester sends.

## Prerequisites
- The target must receive and process XML transactions.
- An adverssary must possess the ability to generate a large amount of XML based messages to send to the target service.

## Skills required
- **Low**: Denial of service

## Consequences
- **Availability**: Resource Consumption

## Execution flow
Execution Flow Explore Survey the target: Using a browser or an automated tool, an attacker records all instance of web services to process XML requests. Techniques Use an automated tool to record all instances of URLs to process XML requests. Use a browser to manually explore the website and analyze how the application processes XML requests. Experiment An adversary crafts input data that may have an adverse effect on the operation of the web service when the XML data sent to the service. Exploit Launch a resource depletion attack: The attacker delivers a large number of XML messages to the target URLs found in the explore phase at a sufficiently rapid rate. It causes denial of service to the target application. Techniques Send a large number of crafted XML messages to the target URL.

## Mitigations
- Design: Build throttling mechanism into the resource allocation. Provide for a timeout mechanism for allocated resources whose transaction does not complete within a specified interval.
- Implementation: Provide for network flow control and traffic shaping to control access to the resources.

## Related weaknesses (CWE)
- [CWE-770](https://cwe.mitre.org/data/definitions/770.html)

## Related ATT&CK techniques
- T1499.002
- T1498.001

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/528.html
