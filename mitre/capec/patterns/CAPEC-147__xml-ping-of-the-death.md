---
capec_id: CAPEC-147
name: XML Ping of the Death
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: Medium
related_cwe: [CWE-400, CWE-770]
related_attack: []
url: https://capec.mitre.org/data/definitions/147.html
tags: [mitre-capec, attack-pattern, CAPEC-147]
---

# CAPEC-147 - XML Ping of the Death

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-147](https://capec.mitre.org/data/definitions/147.html)

## Description
An attacker initiates a resource depletion attack where a large number of small XML messages are delivered at a sufficiently rapid rate to cause a denial of service or crash of the target. Transactions such as repetitive SOAP transactions can deplete resources faster than a simple flooding attack because of the additional resources used by the SOAP protocol and the resources necessary to process SOAP messages. The transactions used are immaterial as long as they cause resource utilization on the target. In other words, this is a normal flooding attack augmented by using messages that will require extra processing on the target.

## Prerequisites
- The target must receive and process XML transactions.

## Skills required
- **High**: To use distributed network to launch the attack
- **Low**: To send small XML messages

## Resources required
- Transaction generator(s)/source(s) and ability to cause arrival of messages at the target with sufficient rapidity to overload target. Larger targets may be able to handle large volumes of requests so the attacker may require significant resources (such as a distributed network) to affect the target. However, the resources required of the attacker would be less than in the case of a simple flooding attack against the same target.

## Consequences
- **Availability**: Resource Consumption (DoS: resource consumption (other))

## Execution flow
Execution Flow Explore Survey the target: Using a browser or an automated tool, an attacker records all instance of web services to process XML requests. Techniques Use an automated tool to record all instances of URLs to process XML requests. Use a browser to manually explore the website and analyze how the application processes XML requests. Exploit Launch a resource depletion attack: The attacker delivers a large number of small XML messages to the target URLs found in the explore phase at a sufficiently rapid rate. It causes denial of service to the target application. Techniques Send a large number of crafted small XML messages to the target URL.

## Mitigations
- Design: Build throttling mechanism into the resource allocation. Provide for a timeout mechanism for allocated resources whose transaction does not complete within a specified interval.
- Implementation: Provide for network flow control and traffic shaping to control access to the resources.

## Related weaknesses (CWE)
- [CWE-400](https://cwe.mitre.org/data/definitions/400.html)
- [CWE-770](https://cwe.mitre.org/data/definitions/770.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/147.html
