---
capec_id: CAPEC-198
name: XSS Targeting Error Pages
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-81]
related_attack: []
url: https://capec.mitre.org/data/definitions/198.html
tags: [mitre-capec, attack-pattern, CAPEC-198]
---

# CAPEC-198 - XSS Targeting Error Pages

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-198](https://capec.mitre.org/data/definitions/198.html)

## Description
An adversary distributes a link (or possibly some other query structure) with a request to a third party web server that is malformed and also contains a block of exploit code in order to have the exploit become live code in the resulting error page.

## Extended description
When the third party web server receives the crafted request and notes the error it then creates an error message that echoes the malformed message, including the exploit. Doing this converts the exploit portion of the message into to valid language elements that are executed by the viewing browser. When a victim executes the query provided by the adversary the infected error message is returned including the exploit code which then runs in the victim's browser. XSS can result in execution of code as well as data leakage (e.g. session cookies can be sent to the attacker). This type of attack is especially dangerous since the exploit appears to come from the third party web server, who the victim may trust and hence be more vulnerable to deception.

## Prerequisites
- A third party web server which fails to adequately sanitize messages sent in error pages.
- The victim must be made to execute a query crafted by the adversary which results in the infected error report.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Execution flow
Execution Flow Explore Survey the application for user-controllable inputs as URL parameters: Using a browser or an automated tool, an adversary follows all public links and actions on a web site. They record all the links, the forms, the resources accessed and all other potential entry-points for the web application, looking for URLs which use parameters. Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Make note of any links that include parameters in the URL. Use a proxy tool to record all links visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Experiment Cause application to return error page: The adversary uses the URLs gathered in the "Explore" phase as a target list and injects various common script payloads and special characters into the parameters to see if an error page occurs, and if the injected payload is executed by the error page. Techniques Use a list of XSS probe strings to inject script in parameters of known URLs. If possible, the probe strings contain a unique identifier. Use a proxy tool to record results of manual input of XSS probes in known URLs. Use a list of HTML special characters to inject into parameters of known URLs and check if they caused errors Craft malicious XSS URL: Once the adversary has determined which parameters are vulnerable to XSS through an error page, they will craft a malicious URL containing the XSS exploit. The adversary can have many goals, from stealing session IDs, cookies, credentials, and page content from the victim. Techniques Change a URL parameter to include a malicious script tag. Send information gathered from the malicious script to a remote endpoint. Exploit Get victim to click URL: In order for the attack to be successful, the victim needs to access the malicious URL. Techniques Send a phishing email to the victim containing the malicious URL. This can be hidden in a hyperlink as to not show the full URL, which might draw suspicion. Put the malicious URL on a public forum, where many victims might accidentally click the link.

## Mitigations
- Design: Use libraries and templates that minimize unfiltered input.
- Implementation: Normalize, filter and use an allowlist for any input that will be used in error messages.
- Implementation: The victim should configure the browser to minimize active content from untrusted sources.

## Related weaknesses (CWE)
- [CWE-81](https://cwe.mitre.org/data/definitions/81.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/198.html
