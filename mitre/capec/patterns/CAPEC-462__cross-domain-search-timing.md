---
capec_id: CAPEC-462
name: Cross-Domain Search Timing
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-385, CWE-352, CWE-208]
related_attack: []
url: https://capec.mitre.org/data/definitions/462.html
tags: [mitre-capec, attack-pattern, CAPEC-462]
---

# CAPEC-462 - Cross-Domain Search Timing

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-462](https://capec.mitre.org/data/definitions/462.html)

## Description
An attacker initiates cross domain HTTP / GET requests and times the server responses. The timing of these responses may leak important information on what is happening on the server. Browser's same origin policy prevents the attacker from directly reading the server responses (in the absence of any other weaknesses), but does not prevent the attacker from timing the responses to requests that the attacker issued cross domain.

## Extended description
For GET requests an attacker could for instance leverage the "img" tag in conjunction with "onload() / onerror()" javascript events. For the POST requests, an attacker could leverage the "iframe" element and leverage the "onload()" event. There is nothing in the current browser security model that prevents an attacker to use these methods to time responses to the attackers' cross domain requests. The timing for these responses leaks information. For instance, if a victim has an active session with their online e-mail account, an attacker could issue search requests in the victim's mailbox. While the attacker is not able to view the responses, based on the timings of the responses, the attacker could ask yes / no questions as to the content of victim's e-mails, who the victim e-mailed, when, etc. This is but one example; There are other scenarios where an attacker could infer potentially sensitive information from cross domain requests by timing the responses while asking the right questions that leak information.

## Prerequisites
- Ability to issue GET / POST requests cross domainJava Script is enabled in the victim's browserThe victim has an active session with the site from which the attacker would like to receive informationThe victim's site does not protect search functionality with cross site request forgery (CSRF) protection

## Skills required
- **Low**: Some knowledge of Java Script

## Resources required
- Ability to issue GET / POST requests cross domain

## Consequences
- **Confidentiality**: Read Data

## Execution flow
Execution Flow Explore Determine service to send cross domain requests to: The adversary first determines which service they will be sending the requests to Experiment Send and time various cross domain requests: Adversaries will send a variety of cross domain requests to the target, timing the time it takes for the target to respond. Although they won't be able to read the response, the adversary can use the time to infer information about what the service did upon receiving the request. Techniques Using a GET request, leverage the "img" tag in conjunction with "onload() / onerror()" javascript events to time a response Using a POST request, leverage the "iframe" element and use the "onload()" event to time a response Exploit Infer information from the response time: After obtaining reponse times to various requests, the adversary will compare these times and infer potentially sensitive information. An example of this could be asking a service to retrieve information and random usernames. If one request took longer to process, it is likely that a user with that username exists, which could be useful knowledge to an adversary. Techniques Compare timing of different requests to infer potentially sensitive information about a target service

## Mitigations
- Design: The victim's site could protect all potentially sensitive functionality (e.g. search functions) with cross site request forgery (CSRF) protection and not perform any work on behalf of forged requests
- Design: The browser's security model could be fixed to not leak timing information for cross domain requests

## Related weaknesses (CWE)
- [CWE-385](https://cwe.mitre.org/data/definitions/385.html)
- [CWE-352](https://cwe.mitre.org/data/definitions/352.html)
- [CWE-208](https://cwe.mitre.org/data/definitions/208.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/462.html
