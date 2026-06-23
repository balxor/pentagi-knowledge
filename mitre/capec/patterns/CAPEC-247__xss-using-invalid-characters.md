---
capec_id: CAPEC-247
name: XSS Using Invalid Characters
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-86]
related_attack: []
url: https://capec.mitre.org/data/definitions/247.html
tags: [mitre-capec, attack-pattern, CAPEC-247]
---

# CAPEC-247 - XSS Using Invalid Characters

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-247](https://capec.mitre.org/data/definitions/247.html)

## Description
An adversary inserts invalid characters in identifiers to bypass application filtering of input. Filters may not scan beyond invalid characters but during later stages of processing content that follows these invalid characters may still be processed. This allows the adversary to sneak prohibited commands past filters and perform normally prohibited operations. Invalid characters may include null, carriage return, line feed or tab in an identifier. Successful bypassing of the filter can result in a XSS attack, resulting in the disclosure of web cookies or possibly other results.

## Prerequisites
- The target must fail to remove invalid characters from input and fail to adequately scan beyond these characters.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Execution flow
Execution Flow Explore Survey the application for user-controllable inputs: Using a browser or an automated tool, an adversary follows all public links and actions on a web site. They record all the links, the forms, the resources accessed and all other potential entry-points for the web application. Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Make special note of any links that include parameters in the URL. Use a proxy tool to record all links visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Experiment Probe identified potential entry points for XSS vulnerabilities using invalid characters: The adversary uses the entry points gathered in the "Explore" phase as a target list and injects various common script payloads and special characters preceded by an invalid character(s) to determine if an entry point actually represents a vulnerability and to characterize the extent to which the vulnerability can be exploited. The adversary is looking for cases where an invalid character causes an input filter to stop processing, allowing the malicious input that follows to bypass the filter Techniques Use a list of XSS probe strings preceded by an invalid character(s) such as null, carriage return, line feed, or tab to inject script in parameters of known URLs. If possible, the probe strings contain a unique identifier. Use a proxy tool to record results of manual input of XSS probes in known URLs. Use a list of HTML special characters preceded by an invalid character(s) to inject into parameters of known URLs and check if they were properly encoded, replaced, or filtered out. Craft malicious XSS URL: Once the adversary has determined which parameters are vulnerable to XSS, they will craft a malicious URL containing the XSS exploit. The adversary can have many goals, from stealing session IDs, cookies, credentials, and page content from the victim. Techniques Change a URL parameter to include a malicious script tag preceded by invalid character(s). Send information gathered from the malicious script to a remote endpoint. Exploit Get victim to click URL: In order for the attack to be successful, the victim needs to access the malicious URL. Techniques Send a phishing email to the victim containing the malicious URL. This can be hidden in a hyperlink as to not show the full URL, which might draw suspicion. Put the malicious URL on a public forum, where many victims might accidentally click the link.

## Mitigations
- Design: Use libraries and templates that minimize unfiltered input.
- Implementation: Normalize, filter and use an allowlist for any input that will be included in any subsequent web pages or back end operations.
- Implementation: The victim should configure the browser to minimize active content from untrusted sources.

## Related weaknesses (CWE)
- [CWE-86](https://cwe.mitre.org/data/definitions/86.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/247.html
