---
capec_id: CAPEC-244
name: XSS Targeting URI Placeholders
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-83]
related_attack: []
url: https://capec.mitre.org/data/definitions/244.html
tags: [mitre-capec, attack-pattern, CAPEC-244]
---

# CAPEC-244 - XSS Targeting URI Placeholders

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-244](https://capec.mitre.org/data/definitions/244.html)

## Description
An attack of this type exploits the ability of most browsers to interpret "data", "javascript" or other URI schemes as client-side executable content placeholders. This attack consists of passing a malicious URI in an anchor tag HREF attribute or any other similar attributes in other HTML tags. Such malicious URI contains, for example, a base64 encoded HTML content with an embedded cross-site scripting payload. The attack is executed when the browser interprets the malicious content i.e., for example, when the victim clicks on the malicious link.

## Prerequisites
- Target client software must allow scripting such as JavaScript and allows executable content delivered using a data URI scheme.

## Skills required
- **Medium**: To inject the malicious payload in a web page

## Resources required
- Ability to send HTTP request to a web application

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Accountability**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges, Bypass Protection Mechanism
- **Confidentiality**: Read Data
- **Integrity**: Modify Data
- **Non-Repudiation**: Gain Privileges

## Execution flow
Execution Flow Explore Survey the application for user-controllable inputs: Using a browser or an automated tool, an adversary follows all public links and actions on a web site. They record all the links, the forms, the resources accessed and all other potential entry-points for the web application. Techniques Use a spidering tool to follow and record all links. Make special note of any links that include parameters in the URL. Use a proxy tool to record all links visited during a manual traversal of the web application. Make special note of any links that include parameters in the URL. Manual traversal of this type is frequently necessary to identify forms that are GET method forms rather than POST forms. Use a browser to manually explore the website and analyze how it is constructed. Many browser's plugins are available to facilitate the analysis or automate the URL discovery. Experiment Probe identified potential entry points for reflected XSS vulnerability: The adversary uses the entry points gathered in the "Explore" phase as a target list and injects various payloads formatted as data URI schemes using base to determine if an entry point actually represents a vulnerability and to characterize the extent to which the vulnerability can be exploited. Techniques Use a list of XSS probe strings using different URI schemes to inject in parameters of known URLs. If possible, the probe strings contain a unique identifier to trace the injected string back to the entry point. Use a proxy tool to record results of manual input of XSS probes in known URLs. Craft malicious XSS URL: Once the adversary has determined which parameters are vulnerable to XSS, they will craft a malicious URL containing the XSS exploit. The adversary can have many goals, from stealing session IDs, cookies, credentials, and page content from the victim. Techniques Change a URL parameter to include a malicious payload formatted as a URI scheme, or use the URL returned when the URI scheme was given as input to the web application. Send information gathered from the malicious script to a remote endpoint. Exploit Get victim to click URL: In order for the attack to be successful, the victim needs to access the malicious URL. Techniques Send a phishing email to the victim containing the malicious URL. This can be hidden in a hyperlink as to not show the full URL, which might draw suspicion. Put the malicious URL on a public forum, where many victims might accidentally click the link.

## Mitigations
- Design: Use browser technologies that do not allow client side scripting.
- Design: Utilize strict type, character, and encoding enforcement.
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Ensure all content coming from the client is using the same encoding; if not, the server-side application must canonicalize the data before applying any filtering.
- Implementation: Perform input validation for all remote content, including remote and user-generated content
- Implementation: Perform output validation for all remote content.
- Implementation: Disable scripting languages such as JavaScript in browser
- Implementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.

## Related weaknesses (CWE)
- [CWE-83](https://cwe.mitre.org/data/definitions/83.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/244.html
