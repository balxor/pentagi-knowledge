---
capec_id: CAPEC-503
name: WebView Exposure
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: n/a
related_cwe: [CWE-284]
related_attack: []
url: https://capec.mitre.org/data/definitions/503.html
tags: [mitre-capec, attack-pattern, CAPEC-503]
---

# CAPEC-503 - WebView Exposure

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-503](https://capec.mitre.org/data/definitions/503.html)

## Description
An adversary, through a malicious web page, accesses application specific functionality by leveraging interfaces registered through WebView's addJavascriptInterface API. Once an interface is registered to WebView through addJavascriptInterface, it becomes global and all pages loaded in the WebView can call this interface.

## Prerequisites
- This type of an attack requires the adversary to convince the user to load the malicious web page inside the target application. Once loaded, the malicious web page will have the same permissions as the target application and will have access to all registered interfaces. Both the permission and the interface must be in place for the functionality to be exposed.

## Mitigations
- To mitigate this type of an attack, an application should limit permissions to only those required and should verify the origin of all web content it loads.

## Related weaknesses (CWE)
- [CWE-284](https://cwe.mitre.org/data/definitions/284.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/503.html
