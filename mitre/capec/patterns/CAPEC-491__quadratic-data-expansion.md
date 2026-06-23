---
capec_id: CAPEC-491
name: Quadratic Data Expansion
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: [CWE-770]
related_attack: []
url: https://capec.mitre.org/data/definitions/491.html
tags: [mitre-capec, attack-pattern, CAPEC-491]
---

# CAPEC-491 - Quadratic Data Expansion

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-491](https://capec.mitre.org/data/definitions/491.html)

## Description
An adversary exploits macro-like substitution to cause a denial of service situation due to excessive memory being allocated to fully expand the data. The result of this denial of service could cause the application to freeze or crash. This involves defining a very large entity and using it multiple times in a single entity substitution. CAPEC-197 is a similar attack pattern, but it is easier to discover and defend against. This attack pattern does not perform multi-level substitution and therefore does not obviously appear to consume extensive resources.

## Prerequisites
- This type of attack requires a server that accepts serialization data which supports substitution and parses the data.

## Consequences
- **Availability**: Unreliable Execution (Denial of Service), Resource Consumption (Denial of Service)

## Execution flow
Execution Flow Explore Survey the target: An adversary determines the input data stream that is being processed by a data parser that supports using substituion on the victim's side. Techniques Use an automated tool to record all instances of URLs to process requests. Use a browser to manually explore the website and analyze how the application processes requests. Exploit Craft malicious payload: The adversary crafts malicious message containing nested quadratic expansion that completely uses up available server resource. Send the message: Send the malicious crafted message to the target URL.

## Mitigations
- Design: Use libraries and templates that minimize unfiltered input. Use methods that limit entity expansion and throw exceptions on attempted entity expansion.
- Implementation: For XML based data - disable altogether the use of inline DTD schemas when parsing XML objects. If a DTD must be used, normalize, filter and use an allowlist and parse with methods and routines that will detect entity expansion from untrusted sources.

## Related weaknesses (CWE)
- [CWE-770](https://cwe.mitre.org/data/definitions/770.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/491.html
