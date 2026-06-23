---
capec_id: CAPEC-261
name: Fuzzing for garnering other adjacent user/sensitive data
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-20]
related_attack: []
url: https://capec.mitre.org/data/definitions/261.html
tags: [mitre-capec, attack-pattern, CAPEC-261]
---

# CAPEC-261 - Fuzzing for garnering other adjacent user/sensitive data

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-261](https://capec.mitre.org/data/definitions/261.html)

## Description
An adversary who is authorized to send queries to a target sends variants of expected queries in the hope that these modified queries might return information (directly or indirectly through error logs) beyond what the expected set of queries should provide.

## Extended description
Many client applications use specific query templates when interacting with a server and often automatically fill in specific fields or attributes. If the server does not verify that the query matches one of the expected templates, an adversary who is allowed to send normal queries could modify their query to try to return additional information. The adversary may not know the names of fields to request or how other modifications will affect the server response, but by attempting multiple plausible variants, they might eventually trigger a server response that divulges sensitive information. Other possible outcomes include server crashes and resource consumption if the unexpected queries cause the server to enter an unstable state or perform excessive computation.

## Prerequisites
- The server must assume that the queries it receives follow specific templates and/or have fields or attributes that follow specific procedures. The server must process queries that it receives without adequately checking or sanitizing queries to ensure they follow these templates.

## Resources required
- The attacker must have sufficient privileges to send queries to the targeted server. A normal client might limit the nature of these queries, so the attacker must either have a modified client or their own application which allows them to modify the expected queries.

## Execution flow
Execution Flow Explore Observe communication and inputs: The fuzzing adversary observes the target system looking for inputs and communications between modules, subsystems, or systems. Techniques Network sniffing. Using a network sniffer such as wireshark, the adversary observes communications into and out of the target system. Monitor API execution. Using a tool such as ktrace, strace, APISpy, or another debugging tool, the adversary observes the system calls and API calls that are made by the target system, and the nature of their parameters. Observe inputs using web inspection tools (OWASP's WebScarab, Paros, TamperData, TamperIE, etc.) Experiment Generate fuzzed inputs: Given a fuzzing tool, a target input or protocol, and limits on time, complexity, and input variety, generate a list of inputs to try. Although fuzzing is random, it is not exhaustive. Parameters like length, composition, and how many variations to try are important to get the most cost-effective impact from the fuzzer. Techniques Boundary cases. Generate fuzz inputs that attack boundary cases of protocol fields, inputs, or other communications limits. Examples include 0xff and 0x00 for single-byte inputs. In binary situations, approach each bit of an individual field with on and off (e.g., 0x80). Attempt arguments to system calls or APIs. The variations include payloads that, if they were successful, could lead to a compromise on the system. Observe the outcome: Observe the outputs to the inputs fed into the system by fuzzers and see if there are any log or error messages that either provide user/sensitive data or give information about an expected template that could be used to produce this data. Exploit Craft exploit payloads: If the logs did not reveal any user/sensitive data, an adversary will attempt to make the fuzzing inputs form to an expected template Techniques Create variants of expected templates that request additional information Create variants that exclude limiting clauses Create variants that alter fields taht identify the requester in order to subvert access controls Repeat different fuzzing variants until sensitive information is divulged

## Related weaknesses (CWE)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/261.html
