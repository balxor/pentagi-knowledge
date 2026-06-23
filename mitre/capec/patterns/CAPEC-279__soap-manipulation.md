---
capec_id: CAPEC-279
name: SOAP Manipulation
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-707]
related_attack: []
url: https://capec.mitre.org/data/definitions/279.html
tags: [mitre-capec, attack-pattern, CAPEC-279]
---

# CAPEC-279 - SOAP Manipulation

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-279](https://capec.mitre.org/data/definitions/279.html)

## Description
Simple Object Access Protocol (SOAP) is used as a communication protocol between a client and server to invoke web services on the server. It is an XML-based protocol, and therefore suffers from many of the same shortcomings as other XML-based protocols. Adversaries can make use of these shortcomings and manipulate the content of SOAP paramters, leading to undesirable behavior on the server and allowing the adversary to carry out a number of further attacks.

## Prerequisites
- An application uses SOAP-based web service api.
- An application does not perform sufficient input validation to ensure that user-controllable data is safe for an XML parser.
- The targeted server either fails to verify that data in SOAP messages conforms to the appropriate XML schema, or it fails to correctly handle the complete range of data allowed by the schema.

## Consequences
- **Availability**: Resource Consumption, Execute Unauthorized Commands
- **Confidentiality**: Read Data, Execute Unauthorized Commands
- **Integrity**: Execute Unauthorized Commands

## Execution flow
Execution Flow Exploit Find target application: The adversary needs to identify an application that uses SOAP as a communication protocol. Techniques Observe HTTP traffic to an application and look for SOAP headers. Experiment Detect Incorrect SOAP Parameter Handling: The adversary tampers with the SOAP message parameters and looks for indications that the tampering caused a change in behavior of the targeted application. Techniques Send more data than would seem reasonable for a field and see if the server complains. Send nonsense data in a field that expects a certain subset, such as product names or sequence numbers, and see if the server complains. Send XML metacharacters as data and see how the server responds. Manipulate SOAP parameters: The adversary manipulates SOAP parameters in a way that causes undesirable behavior for the server. This can result in denial of service, information disclosure, arbitrary code exection, and more. Techniques Create a recursive XML payload that will take up all of the memory on the server when parsed, resulting in a denial of service. This is known as the billion laughs attack. Insert XML metacharacters into data fields that could cause the server to go into an error state when parsing. This could lead to a denial of service. Insert a large amount of data into a field that should have a character limit, causing a buffer overflow.

## Related weaknesses (CWE)
- [CWE-707](https://cwe.mitre.org/data/definitions/707.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/279.html
