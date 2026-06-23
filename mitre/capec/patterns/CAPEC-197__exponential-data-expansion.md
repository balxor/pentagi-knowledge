---
capec_id: CAPEC-197
name: Exponential Data Expansion
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Medium
related_cwe: [CWE-770, CWE-776]
related_attack: []
url: https://capec.mitre.org/data/definitions/197.html
tags: [mitre-capec, attack-pattern, CAPEC-197]
---

# CAPEC-197 - Exponential Data Expansion

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-197](https://capec.mitre.org/data/definitions/197.html)

## Description
An adversary submits data to a target application which contains nested exponential data expansion to produce excessively large output. Many data format languages allow the definition of macro-like structures that can be used to simplify the creation of complex structures. However, this capability can be abused to create excessive demands on a processor's CPU and memory. A small number of nested expansions can result in an exponential growth in demands on memory.

## Prerequisites
- This type of attack requires that the target must receive input but either fail to provide an upper limit for entity expansion or provide a limit that is so large that it does not preclude significant resource consumption.

## Skills required
- **Low**: Ability to craft nested data expansion messages.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Availability**: Unreliable Execution (Denial of Service), Resource Consumption (Denial of Service)

## Execution flow
Execution Flow Explore Survey the target: An adversary determines the input data stream that is being processed by a data parser that supports using subsitituion on the victim's side. Techniques Use an automated tool to record all instances of URLs to process requests. Use a browser to manually explore the website and analyze how the application processes requests. Experiment Craft malicious payload: The adversary crafts a malicious message containing nested exponential expansion that completely uses up available server resources. See the "Example Instances" section for details on how to craft this malicious payload. Exploit Send the message: Send the malicious crafted message to the target URL.

## Mitigations
- Design: Use libraries and templates that minimize unfiltered input. Use methods that limit entity expansion and throw exceptions on attempted entity expansion.
- Implementation: For XML based data - disable altogether the use of inline DTD schemas when parsing XML objects. If a DTD must be used, normalize, filter and use an allowlist and parse with methods and routines that will detect entity expansion from untrusted sources.

## Related weaknesses (CWE)
- [CWE-770](https://cwe.mitre.org/data/definitions/770.html)
- [CWE-776](https://cwe.mitre.org/data/definitions/776.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/197.html
