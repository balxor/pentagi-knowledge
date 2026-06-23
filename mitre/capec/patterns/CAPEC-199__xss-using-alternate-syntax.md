---
capec_id: CAPEC-199
name: XSS Using Alternate Syntax
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-87]
related_attack: []
url: https://capec.mitre.org/data/definitions/199.html
tags: [mitre-capec, attack-pattern, CAPEC-199]
---

# CAPEC-199 - XSS Using Alternate Syntax

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-199](https://capec.mitre.org/data/definitions/199.html)

## Description
An adversary uses alternate forms of keywords or commands that result in the same action as the primary form but which may not be caught by filters. For example, many keywords are processed in a case insensitive manner. If the site's web filtering algorithm does not convert all tags into a consistent case before the comparison with forbidden keywords it is possible to bypass filters (e.g., incomplete black lists) by using an alternate case structure. For example, the "script" tag using the alternate forms of "Script" or "ScRiPt" may bypass filters where "script" is the only form tested. Other variants using different syntax representations are also possible as well as using pollution meta-characters or entities that are eventually ignored by the rendering engine. The attack can result in the execution of otherwise prohibited functionality.

## Prerequisites
- Target client software must allow scripting such as JavaScript.

## Skills required
- **High**: To bypass non trivial filters in the application
- **Low**: To inject the malicious payload in a web page

## Resources required
- Ability to send HTTP request to a web application.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Accountability**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges, Bypass Protection Mechanism
- **Confidentiality**: Read Data
- **Integrity**: Modify Data
- **Non-Repudiation**: Gain Privileges

## Execution flow
Execution Flow Explore Survey the application for user-controllable inputs: Using a browser or an automated tool, an adversary follows all public links and actions on a web site. They record all the links, the forms, the resources accessed and all other potential entry-points for the web application. Techniques Use a spidering tool to follow and record all links. Make special note of any links that include parameters in the URL. Use a proxy tool to record all links visited during a manual traversal of the web application. Make special note of any links that include parameters in the URL. Manual traversal of this type is frequently necessary to identify forms that are GET method forms rather than POST forms. Use a browser to manually explore the website and analyze how it is constructed. Many browser's plugins are available to facilitate the analysis or automate the URL discovery. Experiment Probe identified potential entry points for XSS vulnerability: Possibly using an automated tool, an adversary requests variations on the inputs they surveyed before using alternate syntax. These inputs are designed to bypass incomplete filtering (e.g., incomplete HTML encoding etc.) and try many variations of characters injection that would enable the XSS payload. They record all the responses from the server that include unmodified versions of their script. Techniques Use a list of XSS probe strings to inject in parameters of known URLs. If possible, the probe strings contain a unique identifier. Attempt numerous variations based on form, format, syntax & encoding. Use a proxy tool to record results of manual input of XSS probes in known URLs. Craft malicious XSS URL: Once the adversary has determined which parameters are vulnerable to XSS, they will craft a malicious URL containing the XSS exploit. The adversary can have many goals, from stealing session IDs, cookies, credentials, and page content from the victim. Techniques Change a URL parameter to include a malicious script tag created using alternate syntax to bypass filters. Send information gathered from the malicious script to a remote endpoint. Exploit Get victim to click URL: In order for the attack to be successful, the victim needs to access the malicious URL. Techniques Send a phishing email to the victim containing the malicious URL. This can be hidden in a hyperlink as to not show the full URL, which might draw suspicion. Put the malicious URL on a public forum, where many victims might accidentally click the link.

## Mitigations
- Design: Use browser technologies that do not allow client side scripting.
- Design: Utilize strict type, character, and encoding enforcement
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Ensure all content coming from the client is using the same encoding; if not, the server-side application must canonicalize the data before applying any filtering.
- Implementation: Perform input validation for all remote content, including remote and user-generated content
- Implementation: Perform output validation for all remote content.
- Implementation: Disable scripting languages such as JavaScript in browser
- Implementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.

## Related weaknesses (CWE)
- [CWE-87](https://cwe.mitre.org/data/definitions/87.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/199.html
