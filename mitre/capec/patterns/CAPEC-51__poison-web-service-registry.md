---
capec_id: CAPEC-51
name: Poison Web Service Registry
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Very High
related_cwe: [CWE-285, CWE-74, CWE-693]
related_attack: []
url: https://capec.mitre.org/data/definitions/51.html
tags: [mitre-capec, attack-pattern, CAPEC-51]
---

# CAPEC-51 - Poison Web Service Registry

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-51](https://capec.mitre.org/data/definitions/51.html)

## Description
SOA and Web Services often use a registry to perform look up, get schema information, and metadata about services. A poisoned registry can redirect (think phishing for servers) the service requester to a malicious service provider, provide incorrect information in schema or metadata, and delete information about service provider interfaces.

## Extended description
WS-Addressing is used to virtualize services, provide return addresses and other routing information, however, unless the WS-Addressing headers are protected they are vulnerable to rewriting. Content in a registry is deployed by the service provider. The registry in an SOA or Web Services system can be accessed by the service requester via UDDI or other protocol.

## Prerequisites
- The attacker must be able to write to resources or redirect access to the service registry.

## Skills required
- **Low**: To identify and execute against an over-privileged system interface

## Resources required
- Capability to directly or indirectly modify registry resources

## Consequences
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Read Data
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code), Modify Data

## Execution flow
Execution Flow Explore Find a target SOA or Web Service: The adversary must first indentify a target SOA or Web Service. Experiment Determine desired outcome: Because poisoning a web service registry can have different outcomes, the adversary must decide how they wish to effect the webservice. Techniques An adversary can perform a denial of service attack on a web service. An adversary can redirect requests or responses to a malicious service. Determine if a malicious service needs to be created: If the adversary wishes to redirect requests or responses, they will need to create a malicious service to redirect to. Techniques Create a service to that requests are sent to in addition to the legitimate service and simply record the requests. Create a service that will give malicious responses to a service provider. Act as a malicious service provider and respond to requests in an arbitrary way. Exploit Poison Web Service Registry: Based on the desired outcome, poison the web service registry. This is done by altering the data at rest in the registry or uploading malicious content by spoofing a service provider. Techniques Intercept and change WS-Adressing headers to route to a malicious service or service provider. Provide incorrect information in schema or metadata to cause a denial of service. Delete information about service procider interfaces to cause a denial of service.

## Mitigations
- Design: Enforce principle of least privilege
- Design: Harden registry server and file access permissions
- Implementation: Implement communications to and from the registry using secure protocols

## Related weaknesses (CWE)
- [CWE-285](https://cwe.mitre.org/data/definitions/285.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-693](https://cwe.mitre.org/data/definitions/693.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/51.html
