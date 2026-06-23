---
capec_id: CAPEC-86
name: XSS Through HTTP Headers
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Very High
related_cwe: [CWE-80]
related_attack: []
url: https://capec.mitre.org/data/definitions/86.html
tags: [mitre-capec, attack-pattern, CAPEC-86]
---

# CAPEC-86 - XSS Through HTTP Headers

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-86](https://capec.mitre.org/data/definitions/86.html)

## Description
An adversary exploits web applications that generate web content, such as links in a HTML page, based on unvalidated or improperly validated data submitted by other actors. XSS in HTTP Headers attacks target the HTTP headers which are hidden from most users and may not be validated by web applications.

## Prerequisites
- Target software must be a client that allows scripting communication from remote hosts.

## Skills required
- **High**: Exploiting a client side vulnerability to inject malicious scripts into the browser's executable process.
- **Low**: To achieve a redirection and use of less trusted source, an adversary can simply edit HTTP Headers that are sent to client machine.

## Resources required
- The adversary must have the ability to deploy a custom hostile service for access by targeted clients and the abbility to communicate synchronously or asynchronously with client machine. The adversary must also control a remote site of some sort to redirect client and data to.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Read Data, Gain Privileges
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Survey the application for public links: Using a browser or an automated tool, an adversary follows all public links on a web site. They record all the entry points (input) that becomes part of generated HTTP header (not only GET/POST/COOKIE, but also Content-Type, etc.) Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Make special note of any links that include parameters used in the HTTP headers. Look for HTML meta tags that could be injectable Use a proxy tool to record all links visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Experiment [Probe identified potential entry points for XSS vulnerability] The adversary uses the entry points gathered in the "Explore" phase as a target list and injects various common script payloads to determine if an entry point actually represents a vulnerability and to characterize the extent to which the vulnerability can be exploited. They record all the responses from the server that include unmodified versions of their script. The adversary tries also to inject extra-parameter to the HTTP request to see if they are reflected back in the web page or in the HTTP response. Techniques Manually inject various script payloads into each identified entry point using a list of common script injection probes and observe system behavior to determine if script was executed. Use an automated injection attack tool to inject various script payloads into each identified entry point using a list of common script injection probes and observe system behavior to determine if script was executed. Use a proxy tool to record results of manual input of XSS probes in known URLs. Craft malicious XSS URL: Once the adversary has determined which parameters are vulnerable to XSS, they will craft a malicious URL containing the XSS exploit. The adversary can have many goals, from stealing session IDs, cookies, credentials, and page content from the victim. Techniques Change a URL parameter which is used in an HTTP header to include a malicious script tag. Because it is in the header it may bypass validation. Send information gathered from the malicious script to a remote endpoint. Exploit Get victim to click URL: In order for the attack to be successful, the victim needs to access the malicious URL. Techniques Send a phishing email to the victim containing the malicious URL. This can be hidden in a hyperlink as to not show the full URL, which might draw suspicion. Put the malicious URL on a public forum, where many victims might accidentally click the link.

## Mitigations
- Design: Use browser technologies that do not allow client side scripting.
- Design: Utilize strict type, character, and encoding enforcement
- Design: Server side developers should not proxy content via XHR or other means, if a http proxy for remote content is setup on the server side, the client's browser has no way of discerning where the data is originating from.
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Perform input validation for all remote content.
- Implementation: Perform output validation for all remote content.
- Implementation: Disable scripting languages such as JavaScript in browser
- Implementation: Session tokens for specific host
- Implementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.

## Related weaknesses (CWE)
- [CWE-80](https://cwe.mitre.org/data/definitions/80.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/86.html
