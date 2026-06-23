---
capec_id: CAPEC-85
name: AJAX Footprinting
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Low
related_cwe: [CWE-79, CWE-113, CWE-348, CWE-96, CWE-20, CWE-116, CWE-184, CWE-86, CWE-692]
related_attack: []
url: https://capec.mitre.org/data/definitions/85.html
tags: [mitre-capec, attack-pattern, CAPEC-85]
---

# CAPEC-85 - AJAX Footprinting

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Low  -  **CAPEC:** [CAPEC-85](https://capec.mitre.org/data/definitions/85.html)

## Description
This attack utilizes the frequent client-server roundtrips in Ajax conversation to scan a system. While Ajax does not open up new vulnerabilities per se, it does optimize them from an attacker point of view. A common first step for an attacker is to footprint the target environment to understand what attacks will work. Since footprinting relies on enumeration, the conversational pattern of rapid, multiple requests and responses that are typical in Ajax applications enable an attacker to look for many vulnerabilities, well-known ports, network locations and so on. The knowledge gained through Ajax fingerprinting can be used to support other attacks, such as XSS.

## Prerequisites
- The user must allow JavaScript to execute in their browser

## Skills required
- **Medium**: To land and launch a script on victim's machine with appropriate footprinting logic for enumerating services and vulnerabilities in JavaScript

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Confidentiality**: Read Data

## Execution flow
Execution Flow Explore Send request to target webpage and analyze HTML: Using a browser or an automated tool, an adversary sends requests to a webpage and records the received HTML response. Adversaries then analyze the HTML to identify any known underlying JavaScript architectures. This can aid in mappiong publicly known vulnerabilities to the webpage and can also helpo the adversary guess application architecture and the inner workings of a system. Techniques Record all "src" values inside script tags. These JavaScript files are compared to lists of files for known architectures. If there is a large match between the "src" values and architecture files, then it can be assumed that particular architecture is being used.

## Mitigations
- Design: Use browser technologies that do not allow client side scripting.
- Implementation: Perform input validation for all remote content.

## Related weaknesses (CWE)
- [CWE-79](https://cwe.mitre.org/data/definitions/79.html)
- [CWE-113](https://cwe.mitre.org/data/definitions/113.html)
- [CWE-348](https://cwe.mitre.org/data/definitions/348.html)
- [CWE-96](https://cwe.mitre.org/data/definitions/96.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-116](https://cwe.mitre.org/data/definitions/116.html)
- [CWE-184](https://cwe.mitre.org/data/definitions/184.html)
- [CWE-86](https://cwe.mitre.org/data/definitions/86.html)
- [CWE-692](https://cwe.mitre.org/data/definitions/692.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/85.html
