---
capec_id: CAPEC-243
name: XSS Targeting HTML Attributes
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-83]
related_attack: []
url: https://capec.mitre.org/data/definitions/243.html
tags: [mitre-capec, attack-pattern, CAPEC-243]
---

# CAPEC-243 - XSS Targeting HTML Attributes

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-243](https://capec.mitre.org/data/definitions/243.html)

## Description
An adversary inserts commands to perform cross-site scripting (XSS) actions in HTML attributes. Many filters do not adequately sanitize attributes against the presence of potentially dangerous commands even if they adequately sanitize tags. For example, dangerous expressions could be inserted into a style attribute in an anchor tag, resulting in the execution of malicious code when the resulting page is rendered. If a victim is tricked into viewing the rendered page the attack proceeds like a normal XSS attack, possibly resulting in the loss of sensitive cookies or other malicious activities.

## Prerequisites
- The target application must fail to adequately sanitize HTML attributes against the presence of dangerous commands.

## Resources required
- The adversary must trick the victim into following a crafted link to a vulnerable server or view a web post where the dangerous commands are executed.

## Execution flow
Execution Flow Explore Survey the application for user-controllable inputs: Using a browser or an automated tool, an adversary follows all public links and actions on a web site. They record all the links, the forms, the resources accessed and all other potential entry-points for the web application. Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Make special note of any links that include parameters in the URL. Use a proxy tool to record all links visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Experiment Probe identified potential entry points for XSS targeting HTML attributes: The adversary uses the entry points gathered in the "Explore" phase as a target list and injects various malicious expressions as input, hoping to embed them as HTML attributes. Techniques Inject single and double quotes into URL parameters or other inputs to see if they are filtered out. Also use URL encoding to bypass filters. Use single or double quotes to close attribute evaluation and enter a new attribute that contains an expression. Craft malicious XSS URL: Once the adversary has determined which parameters are vulnerable to XSS, they will craft a malicious URL containing the XSS exploit. The adversary can have many goals, from stealing session IDs, cookies, credentials, and page content from the victim. Techniques Execute a script using an expression embedded in an HTML attribute, which avoids needing to inject a script tag. Send information gathered from the malicious script to a remote endpoint. Exploit Get victim to click URL: In order for the attack to be successful, the victim needs to access the malicious URL. Techniques Send a phishing email to the victim containing the malicious URL. This can be hidden in a hyperlink as to not show the full URL, which might draw suspicion. Put the malicious URL on a public forum, where many victims might accidentally click the link.

## Mitigations
- Design: Use libraries and templates that minimize unfiltered input.
- Implementation: Normalize, filter and use an allowlist for all input including that which is not expected to have any scripting content.
- Implementation: The victim should configure the browser to minimize active content from untrusted sources.

## Related weaknesses (CWE)
- [CWE-83](https://cwe.mitre.org/data/definitions/83.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/243.html
