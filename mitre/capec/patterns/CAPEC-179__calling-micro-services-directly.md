---
capec_id: CAPEC-179
name: Calling Micro-Services Directly
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Medium
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/179.html
tags: [mitre-capec, attack-pattern, CAPEC-179]
---

# CAPEC-179 - Calling Micro-Services Directly

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-179](https://capec.mitre.org/data/definitions/179.html)

## Description
An attacker is able to discover and query Micro-services at a web location and thereby expose the Micro-services to further exploitation by gathering information about their implementation and function. Micro-services in web pages allow portions of a page to connect to the server and update content without needing to cause the entire page to update. This allows user activity to change portions of the page more quickly without causing disruptions elsewhere.

## Extended description
However, these micro-services may not be subject to the same level of security review as other forms of content. For example, a micro-service that posts requests to a server that are turned into SQL queries may not adequately protect against SQL-injection attacks. As a result, micro-services may provide another vector for a range of attacks. It should be emphasized that the presence of micro-services does not necessarily make a site vulnerable to attack, but they do provide additional complexity to a web page and therefore may contain vulnerabilities that support other attack patterns.

## Prerequisites
- The target site must use micro-services that interact with the server and one or more of these micro-services must be vulnerable to some other attack pattern.

## Resources required
- The attacker usually needs to be able to invoke micro-services directly in order to control the parameters that are used in their attack. The attacker may require other resources depending on the nature of the flaw in the targeted micro-service.

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/179.html
