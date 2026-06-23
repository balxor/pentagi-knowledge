---
capec_id: CAPEC-472
name: Browser Fingerprinting
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/472.html
tags: [mitre-capec, attack-pattern, CAPEC-472]
---

# CAPEC-472 - Browser Fingerprinting

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-472](https://capec.mitre.org/data/definitions/472.html)

## Description
An attacker carefully crafts small snippets of Java Script to efficiently detect the type of browser the potential victim is using. Many web-based attacks need prior knowledge of the web browser including the version of browser to ensure successful exploitation of a vulnerability. Having this knowledge allows an attacker to target the victim with attacks that specifically exploit known or zero day weaknesses in the type and version of the browser used by the victim. Automating this process via Java Script as a part of the same delivery system used to exploit the browser is considered more efficient as the attacker can supply a browser fingerprinting method and integrate it with exploit code, all contained in Java Script and in response to the same web page request by the browser.

## Prerequisites
- Victim's browser visits a website that contains attacker's Java ScriptJava Script is not disabled in the victim's browser

## Mitigations
- Configuration: Disable Java Script in the browser

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/472.html
