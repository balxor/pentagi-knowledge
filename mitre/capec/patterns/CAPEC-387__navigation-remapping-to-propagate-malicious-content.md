---
capec_id: CAPEC-387
name: Navigation Remapping To Propagate Malicious Content
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-471, CWE-345, CWE-346, CWE-602, CWE-311]
related_attack: []
url: https://capec.mitre.org/data/definitions/387.html
tags: [mitre-capec, attack-pattern, CAPEC-387]
---

# CAPEC-387 - Navigation Remapping To Propagate Malicious Content

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-387](https://capec.mitre.org/data/definitions/387.html)

## Description
An adversary manipulates either egress or ingress data from a client within an application framework in order to change the content of messages and thereby circumvent the expected application logic.

## Extended description
Performing this attack allows the adversary to manipulate content in such a way as to produce messages or content that look authentic but may contain deceptive links, spam-like content, or links to the adversarys' code. In general, content-spoofing within an application API can be employed to stage many different types of attacks varied based on the adversarys' intent. When the goal is to spread malware, deceptive content is created such as modified links, buttons, or images, that entice users to click on those items, all of which point to a malicious URI. The techniques require use of specialized software that allow the adversary to use adversary-in-the-middle (CAPEC-94) communications between the web browser and the remote system in order to change the destination of various application interface elements.

## Prerequisites
- Targeted software is utilizing application framework APIs

## Resources required
- A software program that allows the use of adversary-in-the-middle communications between the client and server, such as a man-in-the-middle proxy.

## Related weaknesses (CWE)
- [CWE-471](https://cwe.mitre.org/data/definitions/471.html)
- [CWE-345](https://cwe.mitre.org/data/definitions/345.html)
- [CWE-346](https://cwe.mitre.org/data/definitions/346.html)
- [CWE-602](https://cwe.mitre.org/data/definitions/602.html)
- [CWE-311](https://cwe.mitre.org/data/definitions/311.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/387.html
