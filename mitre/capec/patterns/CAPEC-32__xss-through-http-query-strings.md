---
capec_id: CAPEC-32
name: XSS Through HTTP Query Strings
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-80]
related_attack: []
url: https://capec.mitre.org/data/definitions/32.html
tags: [mitre-capec, attack-pattern, CAPEC-32]
---

# CAPEC-32 - XSS Through HTTP Query Strings

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-32](https://capec.mitre.org/data/definitions/32.html)

## Description
An adversary embeds malicious script code in the parameters of an HTTP query string and convinces a victim to submit the HTTP request that contains the query string to a vulnerable web application. The web application then procedes to use the values parameters without properly validation them first and generates the HTML code that will be executed by the victim's browser.

## Prerequisites
- Target client software must allow scripting such as JavaScript. Server software must allow display of remote generated HTML without sufficient input or output validation.

## Skills required
- **High**: Exploiting any information gathered by HTTP Query on script host
- **Low**: To place malicious payload on server via HTTP

## Resources required
- Ability to send HTTP post to scripting host and collect output

## Consequences
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Read Data, Execute Unauthorized Commands (Run Arbitrary Code)
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Survey the application for public links: Using a browser or an automated tool, an adversary follows all public links on a web site. They record all the links they find. Techniques Use a spidering tool to follow and record all links. Make special note of any links that include parameters in the URL. Use a proxy tool to record all links visited during a manual traversal of the web application. Make special note of any links that include parameters in the URL. Manual traversal of this type is frequently necessary to identify forms that are GET method forms rather than POST forms. Use a browser to manually explore the website and analyze how it is constructed. Many browser's plugins are available to facilitate the analysis or automate the URL discovery. Experiment Probe public links for XSS vulnerability: The adversary uses the public links gathered in the "Explore" phase as a target list and requests variations on the URLs they spidered before. They send parameters that include variations of payloads. They record all the responses from the server that include unmodified versions of their script. Techniques Use a list of XSS probe strings to inject in parameters of known URLs. If possible, the probe strings contain a unique identifier. Use a proxy tool to record results of manual input of XSS probes in known URLs. Craft malicious XSS URL: Once the adversary has determined which parameters are vulnerable to XSS, they will craft a malicious URL containing the XSS exploit. The adversary can have many goals, from stealing session IDs, cookies, credentials, and page content from the victim. Techniques Change a URL parameter to include a malicious script tag. Send information gathered from the malicious script to a remote endpoint. Exploit Get victim to click URL: In order for the attack to be successful, the victim needs to access the malicious URL. Techniques Send a phishing email to the victim containing the malicious URL. This can be hidden in a hyperlink as to not show the full URL, which might draw suspicion. Put the malicious URL on a public forum, where many victims might accidentally click the link.

## Mitigations
- Design: Use browser technologies that do not allow client side scripting.
- Design: Utilize strict type, character, and encoding enforcement
- Design: Server side developers should not proxy content via XHR or other means, if a http proxy for remote content is setup on the server side, the client's browser has no way of discerning where the data is originating from.
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Perform input validation for all remote content, including remote and user-generated content
- Implementation: Perform output validation for all remote content.
- Implementation: Disable scripting languages such as JavaScript in browser
- Implementation: Session tokens for specific host
- Implementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.
- Implementation: Privileges are constrained, if a script is loaded, ensure system runs in chroot jail or other limited authority mode

## Related weaknesses (CWE)
- [CWE-80](https://cwe.mitre.org/data/definitions/80.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/32.html
