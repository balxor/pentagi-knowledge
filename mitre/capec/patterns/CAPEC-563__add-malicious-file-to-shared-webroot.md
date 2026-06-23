---
capec_id: CAPEC-563
name: Add Malicious File to Shared Webroot
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: [CWE-284]
related_attack: []
url: https://capec.mitre.org/data/definitions/563.html
tags: [mitre-capec, attack-pattern, CAPEC-563]
---

# CAPEC-563 - Add Malicious File to Shared Webroot

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-563](https://capec.mitre.org/data/definitions/563.html)

## Description
An adversaries may add malicious content to a website through the open file share and then browse to that content with a web browser to cause the server to execute the content. The malicious content will typically run under the context and permissions of the web server process, often resulting in local system or administrative privileges depending on how the web server is configured.

## Mitigations
- Ensure proper permissions on directories that are accessible through a web server. Disallow remote access to the web root. Disable execution on directories within the web root. Ensure that permissions of the web server process are only what is required by not using built-in accounts and instead create specific accounts to limit unnecessary access or permissions overlap across multiple systems.

## Related weaknesses (CWE)
- [CWE-284](https://cwe.mitre.org/data/definitions/284.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/563.html
