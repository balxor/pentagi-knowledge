---
capec_id: CAPEC-63
name: Cross-Site Scripting (XSS)
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Very High
related_cwe: [CWE-79, CWE-20]
related_attack: []
url: https://capec.mitre.org/data/definitions/63.html
tags: [mitre-capec, attack-pattern, CAPEC-63]
---

# CAPEC-63 - Cross-Site Scripting (XSS)

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-63](https://capec.mitre.org/data/definitions/63.html)

## Description
An adversary embeds malicious scripts in content that will be served to web browsers. The goal of the attack is for the target software, the client-side browser, to execute the script with the users' privilege level. An attack of this type exploits a programs' vulnerabilities that are brought on by allowing remote hosts to execute code and scripts. Web browsers, for example, have some simple security controls in place, but if a remote attacker is allowed to execute scripts (through injecting them in to user-generated content like bulletin boards) then these controls may be bypassed. Further, these attacks are very difficult for an end user to detect.

## Prerequisites
- Target client software must be a client that allows scripting communication from remote hosts, such as a JavaScript-enabled Web Browser.

## Skills required
- **High**: Exploiting a client side vulnerability to inject malicious scripts into the browser's executable process.
- **Low**: To achieve a redirection and use of less trusted source, an attacker can simply place a script in bulletin board, blog, wiki, or other user-generated content site that are echoed back to other client machines.

## Resources required
- Ability to deploy a custom hostile service for access by targeted clients. Ability to communicate synchronously or asynchronously with client machine.

## Consequences
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Read Data
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code), Modify Data

## Execution flow
Execution Flow Explore Survey the application for user-controllable inputs: Using a browser or an automated tool, an attacker follows all public links and actions on a web site. They record all the links, the forms, the resources accessed and all other potential entry-points for the web application. Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Make special note of any links that include parameters in the URL. Use a proxy tool to record all links visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Experiment Probe identified potential entry points for XSS vulnerability: The attacker uses the entry points gathered in the "Explore" phase as a target list and injects various common script payloads to determine if an entry point actually represents a vulnerability and to characterize the extent to which the vulnerability can be exploited. Techniques Use a list of XSS probe strings to inject script in parameters of known URLs. If possible, the probe strings contain a unique identifier. Use a proxy tool to record results of manual input of XSS probes in known URLs. Use a list of XSS probe strings to inject script into UI entry fields. If possible, the probe strings contain a unique identifier. Use a list of XSS probe strings to inject script into resources accessed by the application. If possible, the probe strings contain a unique identifier. Exploit Steal session IDs, credentials, page content, etc.: As the attacker succeeds in exploiting the vulnerability, they can choose to steal user's credentials in order to reuse or to analyze them later on. Techniques Develop malicious JavaScript that is injected through vectors identified during the Experiment Phase and loaded by the victim's browser and sends document information to the attacker. Develop malicious JavaScript that injected through vectors identified during the Experiment Phase and takes commands from an attacker's server and then causes the browser to execute appropriately. Forceful browsing: When the attacker targets the current application or another one (through CSRF vulnerabilities), the user will then be the one who perform the attacks without being aware of it. These attacks are mostly targeting application logic flaws, but it can also be used to create a widespread attack against a particular website on the user's current network (Internet or not). Techniques Develop malicious JavaScript that is injected through vectors identified during the Experiment Phase and loaded by the victim's browser and performs actions on the same web site Develop malicious JavaScript that injected through vectors identified during the Experiment Phase and takes commands from an attacker's server and then causes the browser to execute request to other web sites (especially the web applications that have CSRF vulnerabilities). Content spoofing: By manipulating the content, the attacker targets the information that the user would like to get from the website. Techniques Develop malicious JavaScript that is injected through vectors identified during the Experiment Phase and loaded by the victim's browser and exposes attacker-modified invalid information to the user on the current web page.

## Mitigations
- Design: Use browser technologies that do not allow client side scripting.
- Design: Utilize strict type, character, and encoding enforcement
- Design: Server side developers should not proxy content via XHR or other means, if a http proxy for remote content is setup on the server side, the client's browser has no way of discerning where the data is originating from.
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Perform input validation for all remote content.
- Implementation: Perform output validation for all remote content.
- Implementation: Session tokens for specific host
- Implementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.

## Related weaknesses (CWE)
- [CWE-79](https://cwe.mitre.org/data/definitions/79.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/63.html
