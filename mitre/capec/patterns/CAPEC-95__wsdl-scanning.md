---
capec_id: CAPEC-95
name: WSDL Scanning
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-538]
related_attack: []
url: https://capec.mitre.org/data/definitions/95.html
tags: [mitre-capec, attack-pattern, CAPEC-95]
---

# CAPEC-95 - WSDL Scanning

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-95](https://capec.mitre.org/data/definitions/95.html)

## Description
This attack targets the WSDL interface made available by a web service. The attacker may scan the WSDL interface to reveal sensitive information about invocation patterns, underlying technology implementations and associated vulnerabilities. This type of probing is carried out to perform more serious attacks (e.g. parameter tampering, malicious content injection, command injection, etc.). WSDL files provide detailed information about the services ports and bindings available to consumers. For instance, the attacker can submit special characters or malicious content to the Web service and can cause a denial of service condition or illegal access to database records. In addition, the attacker may try to guess other private methods by using the information provided in the WSDL files.

## Prerequisites
- A client program connecting to a web service can read the WSDL to determine what functions are available on the server.
- The target host exposes vulnerable functions within its WSDL interface.

## Skills required
- **Low**: This attack can be as simple as reading WSDL and starting sending invalid request.
- **Medium**: This attack can be used to perform more sophisticated attacks (SQL injection, etc.)

## Consequences
- **Confidentiality**: Read Data

## Execution flow
Execution Flow Explore Scan for WSDL Documents: The adversary scans for WSDL documents. The WDSL document written in XML is like a handbook on how to communicate with the web services provided by the target host. It provides an open view of the application (function details, purpose, functional break down, entry points, message types, etc.). This is very useful information for the adversary. Experiment Analyze WSDL files: An adversary will analyze the WSDL files and try to find potential weaknesses by sending messages matching the pattern described in the WSDL file. The adversary could run through all of the operations with different message request patterns until a breach is identified. Exploit Craft malicious content: Once an adversary finds a potential weakness, they can craft malicious content to be sent to the system. For instance the adversary may try to submit special characters and observe how the system reacts to an invalid request. The message sent by the adversary may not be XML validated and cause unexpected behavior.

## Mitigations
- It is important to protect WSDL file or provide limited access to it.
- Review the functions exposed by the WSDL interface (especially if you have used a tool to generate it). Make sure that none of them is vulnerable to injection.
- Ensure the WSDL does not expose functions and APIs that were not intended to be exposed.
- Pay attention to the function naming convention (within the WSDL interface). Easy to guess function name may be an entry point for attack.
- Validate the received messages against the WSDL Schema. Incomplete solution.

## Related weaknesses (CWE)
- [CWE-538](https://cwe.mitre.org/data/definitions/538.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/95.html
