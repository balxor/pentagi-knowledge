---
capec_id: CAPEC-230
name: Serialized Data with Nested Payloads
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: High
related_cwe: [CWE-112, CWE-20, CWE-674, CWE-770]
related_attack: []
url: https://capec.mitre.org/data/definitions/230.html
tags: [mitre-capec, attack-pattern, CAPEC-230]
---

# CAPEC-230 - Serialized Data with Nested Payloads

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-230](https://capec.mitre.org/data/definitions/230.html)

## Description
Applications often need to transform data in and out of a data format (e.g., XML and YAML) by using a parser. It may be possible for an adversary to inject data that may have an adverse effect on the parser when it is being processed. Many data format languages allow the definition of macro-like structures that can be used to simplify the creation of complex structures. By nesting these structures, causing the data to be repeatedly substituted, an adversary can cause the parser to consume more resources while processing, causing excessive memory consumption and CPU utilization.

## Extended description
An adversary's goal is to leverage parser failure to their advantage. In most cases this type of an attack will result in a Denial of Service due to an application becoming unstable, freezing, or crashing. However it may be possible to cause a crash resulting in arbitrary code execution, leading to a jump from the data plane to the control plane [REF-89]. This attack is most closely associated with web services using SOAP or a Rest API, because remote service requesters can post malicious payloads to the service provider. The main weakness is that the service provider generally must inspect, parse, and validate the messages to determine routing, workflow, security considerations, and so on. It is exactly these inspection, parsing, and validation routines that this attack targets. This attack exploits the loosely coupled nature of web services, where the service provider has little to no control over the service requester and any messages the service requester sends.

## Prerequisites
- An application's user-controllable data is expressed in a language that supports subsitution.
- An application does not perform sufficient validation to ensure that user-controllable data is not malicious.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Resource Consumption, Execute Unauthorized Commands
- **Confidentiality**: Read Data, Execute Unauthorized Commands, Gain Privileges
- **Integrity**: Execute Unauthorized Commands

## Execution flow
Execution Flow Explore An adversary determines the input data stream that is being processed by a data parser that supports using substitution on the victim's side. Exploit An adversary crafts input data that may have an adverse effect on the operation of the parser when the data is parsed on the victim's system.

## Mitigations
- Carefully validate and sanitize all user-controllable data prior to passing it to the data parser routine. Ensure that the resultant data is safe to pass to the data parser.
- Perform validation on canonical data.
- Pick a robust implementation of the data parser.

## Related weaknesses (CWE)
- [CWE-112](https://cwe.mitre.org/data/definitions/112.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-674](https://cwe.mitre.org/data/definitions/674.html)
- [CWE-770](https://cwe.mitre.org/data/definitions/770.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/230.html
