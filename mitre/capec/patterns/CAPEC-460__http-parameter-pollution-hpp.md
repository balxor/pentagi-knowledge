---
capec_id: CAPEC-460
name: HTTP Parameter Pollution (HPP)
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-88, CWE-147, CWE-235]
related_attack: []
url: https://capec.mitre.org/data/definitions/460.html
tags: [mitre-capec, attack-pattern, CAPEC-460]
---

# CAPEC-460 - HTTP Parameter Pollution (HPP)

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-460](https://capec.mitre.org/data/definitions/460.html)

## Description
An adversary adds duplicate HTTP GET/POST parameters by injecting query string delimiters. Via HPP it may be possible to override existing hardcoded HTTP parameters, modify the application behaviors, access and, potentially exploit, uncontrollable variables, and bypass input validation checkpoints and WAF rules.

## Prerequisites
- HTTP protocol is used with some GET/POST parameters passed

## Resources required
- Any tool that enables intercepting and tampering with HTTP requests

## Execution flow
Execution Flow Explore Find User Input: The adversary finds anywhere in the web application that uses user-supplied input in a form or action. This can also be found by looking at parameters in the URL in the navigation bar of the browser Experiment Add Duplicate Parameter Values: Once the adversary has identified what user input is used as HTTP parameters, they will add duplicates to each parameter one by one to observe the results. If the response from the HTTP request shows the duplicate parameter value concatenated with the original parameter value in some way, or simply just the duplicate parameter value, then HPP is possible. Techniques In the URL, add a duplicate parameter by using the "&" delimiter. For example "par1=val1" becomes "par1=val1&par1=val2". Depending on the backend API, this could be treated as "par1=val1, val2", which could lead to par1 being set to val2, ignoring val1. If the request is created based on user input directly on the page, the adversary will test by adding an encoded delimiter to the input. For example, the adverary might supply "1000%26action=withdraw" and the backend might interpret a POST request with the paramters "action=deposit&amount=1000&action=withdraw" Exploit Leverage HPP: Once the adversary has identified how the backend handles duplicate parameters, they will leverage this by polluting the paramters in a way that benefits them. In some cases, hardcoded parameters will be disregarded by the backend. In others, the adversary can bypass a WAF that might only check a parameter before it has been concatenated by the backend, resulting in malicious queries getting through.

## Mitigations
- Configuration: If using a Web Application Firewall (WAF), filters should be carefully configured to detect abnormal HTTP requests
- Design: Perform URL encoding
- Implementation: Use strict regular expressions in URL rewriting
- Implementation: Beware of multiple occurrences of a parameter in a Query String

## Related weaknesses (CWE)
- [CWE-88](https://cwe.mitre.org/data/definitions/88.html)
- [CWE-147](https://cwe.mitre.org/data/definitions/147.html)
- [CWE-235](https://cwe.mitre.org/data/definitions/235.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/460.html
