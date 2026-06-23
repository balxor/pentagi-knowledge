---
capec_id: CAPEC-228
name: DTD Injection
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-829]
related_attack: []
url: https://capec.mitre.org/data/definitions/228.html
tags: [mitre-capec, attack-pattern, CAPEC-228]
---

# CAPEC-228 - DTD Injection

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-228](https://capec.mitre.org/data/definitions/228.html)

## Description
An attacker injects malicious content into an application's DTD in an attempt to produce a negative technical impact. DTDs are used to describe how XML documents are processed. Certain malformed DTDs (for example, those with excessive entity expansion as described in CAPEC 197) can cause the XML parsers that process the DTDs to consume excessive resources resulting in resource depletion.

## Prerequisites
- The target must be running an XML based application that leverages DTDs.

## Execution flow
Execution Flow Explore Survey the target: Using a browser or an automated tool, an attacker records all instances of web services to process XML requests. Techniques Use an automated tool to record all instances of URLs to process XML requests. Use a browser to manually explore the website and analyze how the application processes XML requests. Determine use of XML with DTDs: Examine application input to identify XML input that leverage the use of one or more DTDs. Techniques Examine any available documentation for the application that discusses expected XML input. Exercise the application using XML input with and without a DTD specified. Failure without DTD likely indicates use of DTD. Exploit [Craft and inject XML containg malicious DTD payload] Techniques Inject XML expansion attack that creates a Denial of Service impact on the targeted server using its DTD. Inject XML External Entity (XEE) attack that can cause the disclosure of confidential information, execute abitrary code, create a Denial of Service of the targeted server, or several other malicious impacts.

## Mitigations
- Design: Sanitize incoming DTDs to prevent excessive expansion or other actions that could result in impacts like resource depletion.
- Implementation: Disallow the inclusion of DTDs as part of incoming messages.
- Implementation: Use XML parsing tools that protect against DTD attacks.

## Related weaknesses (CWE)
- [CWE-829](https://cwe.mitre.org/data/definitions/829.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/228.html
