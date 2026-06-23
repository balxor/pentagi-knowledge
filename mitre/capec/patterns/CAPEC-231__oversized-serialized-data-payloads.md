---
capec_id: CAPEC-231
name: Oversized Serialized Data Payloads
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: High
related_cwe: [CWE-112, CWE-20, CWE-674, CWE-770]
related_attack: []
url: https://capec.mitre.org/data/definitions/231.html
tags: [mitre-capec, attack-pattern, CAPEC-231]
---

# CAPEC-231 - Oversized Serialized Data Payloads

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-231](https://capec.mitre.org/data/definitions/231.html)

## Description
An adversary injects oversized serialized data payloads into a parser during data processing to produce adverse effects upon the parser such as exhausting system resources and arbitrary code execution.

## Extended description
Applications often need to transform data in and out of serialized data formats, such as XML and YAML, by using a data parser. It may be possible for an adversary to inject data that may have an adverse effect on the parser when it is being processed. By supplying oversized payloads in input vectors that will be processed by the parser, an adversary can cause the parser to consume more resources while processing, causing excessive memory consumption and CPU utilization, and potentially cause execution of arbitrary code. An adversary's goal is to leverage parser failure to their advantage. DoS is most closely associated with web services, SOAP, and Rest, because remote service requesters can post malicious data payloads to the service provider designed to exhaust the service provider's memory, CPU, and/or disk space. This attack exploits the loosely coupled nature of web services, where the service provider has little to no control over the service requester and any messages the service requester sends.

## Prerequisites
- An application uses an parser for serialized data to perform transformation on user-controllable data.
- An application does not perform sufficient validation to ensure that user-controllable data is safe for a data parser.

## Skills required
- **High**: Arbitrary code execution
- **Low**: Denial of service

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Resource Consumption, Execute Unauthorized Commands
- **Confidentiality**: Read Data, Execute Unauthorized Commands, Gain Privileges
- **Integrity**: Execute Unauthorized Commands

## Execution flow
Execution Flow Explore An adversary determines the input data stream that is being processed by an serialized data parser on the victim's side. Experiment An adversary crafts input data that may have an adverse effect on the operation of the data parser when the data is parsed on the victim's system.

## Mitigations
- Carefully validate and sanitize all user-controllable serialized data prior to passing it to the parser routine. Ensure that the resultant data is safe to pass to the parser.
- Perform validation on canonical data.
- Pick a robust implementation of the serialized data parser.
- Validate data against a valid schema or DTD prior to parsing.

## Related weaknesses (CWE)
- [CWE-112](https://cwe.mitre.org/data/definitions/112.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-674](https://cwe.mitre.org/data/definitions/674.html)
- [CWE-770](https://cwe.mitre.org/data/definitions/770.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/231.html
