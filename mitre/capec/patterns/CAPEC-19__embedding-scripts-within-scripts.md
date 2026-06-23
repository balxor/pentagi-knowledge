---
capec_id: CAPEC-19
name: Embedding Scripts within Scripts
type: attack-pattern
abstraction: Standard
likelihood: High
severity: High
related_cwe: [CWE-284]
related_attack: [T1027.009, T1546.004, T1546.016]
url: https://capec.mitre.org/data/definitions/19.html
tags: [mitre-capec, attack-pattern, CAPEC-19]
---

# CAPEC-19 - Embedding Scripts within Scripts

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-19](https://capec.mitre.org/data/definitions/19.html)

## Description
An adversary leverages the capability to execute their own script by embedding it within other scripts that the target software is likely to execute due to programs' vulnerabilities that are brought on by allowing remote hosts to execute scripts.

## Extended description
The adversary must have the ability to inject their script into a script that is likely to be executed. If this is done, then the adversary can potentially launch a variety of probes and attacks against the web server's local environment, in many cases the so-called DMZ, back end resources the web server can communicate with, and other hosts. With the proliferation of intermediaries, such as Web App Firewalls, network devices, and even printers having JVMs and Web servers, there are many locales where an adversary can inject malicious scripts. Since this attack pattern defines scripts within scripts, there are likely privileges to execute said attack on the host. These attacks are not solely limited to the server side, client side scripts like Ajax and client side JavaScript can contain malicious scripts as well.

## Prerequisites
- Target software must be able to execute scripts, and also grant the adversary privilege to write/upload scripts.

## Skills required
- **Low**: To load malicious script into open, e.g. world writable directory
- **Medium**: Executing remote scripts on host and collecting output

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Spider: Using a browser or an automated tool, an adversary records all entry points for inputs that happen to be reflected in a client-side script element. These script elements can be located in the HTML content (head, body, comments), in an HTML tag, XML, CSS, etc. Techniques Use a spidering tool to follow and record all non-static links that are likely to have input parameters (through forms, URL, fragments, etc.) actively used by the Web application. Use a proxy tool to record all links visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Experiment Probe identified potential entry points for XSS vulnerability: The adversary uses the entry points gathered in the "Explore" phase as a target list and injects various common script payloads to determine if an entry point actually represents a vulnerability and to characterize the extent to which the vulnerability can be exploited. Techniques Manually inject various script payloads into each identified entry point using a list of common script injection probes that typically work in a client-side script elements context and observe system behavior to determine if script was executed. Manually inject various script payloads into each identified entry point using a list of common script injection probes that typically work in a server-side script elements context and observe system behavior to determine if script was executed. Use an automated injection attack tool to inject various script payloads into each identified entry point using a list of common script injection probes that typically work in a client-side script elements context and observe system behavior to determine if script was executed. Use an automated injection attack tool to inject various script payloads into each identified entry point using a list of common script injection probes that typically work in a server-side script elements context and observe system behavior to determine if script was executed. Use a proxy tool to record results of the created requests. Exploit Steal session IDs, credentials, page content, etc.: As the adversary succeeds in exploiting the vulnerability, they can choose to steal user's credentials in order to reuse or to analyze them later on. Techniques Develop malicious JavaScript that is injected through vectors identified during the Experiment Phase and loaded by the victim's browser and sends document information to the adversary. Develop malicious JavaScript that injected through vectors identified during the Experiment Phase and takes commands from an adversary's server and then causes the browser to execute appropriately. Forceful browsing: When the adversary targets the current application or another one (through CSRF vulnerabilities), the user will then be the one who perform the attacks without being aware of it. These attacks are mostly targeting application logic flaws, but it can also be used to create a widespread attack against a particular website on the user's current network (Internet or not). Techniques Develop malicious JavaScript that is injected through vectors identified during the Experiment Phase and loaded by the victim's browser and performs actions on the same web site Develop malicious JavaScript that injected through vectors identified during the Experiment Phase and takes commands from an adversary's server and then causes the browser to execute request to other web sites (especially the web applications that have CSRF vulnerabilities). Content spoofing: By manipulating the content, the adversary targets the information that the user would like to get from the website. Techniques Develop malicious JavaScript that is injected through vectors identified during the Experiment Phase and loaded by the victim's browser and exposes adversary-modified invalid information to the user on the current web page.

## Mitigations
- Use browser technologies that do not allow client side scripting.
- Utilize strict type, character, and encoding enforcement.
- Server side developers should not proxy content via XHR or other means. If a HTTP proxy for remote content is setup on the server side, the client's browser has no way of discerning where the data is originating from.
- Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Perform input validation for all remote content.
- Perform output validation for all remote content.
- Disable scripting languages such as JavaScript in browser
- Session tokens for specific host
- Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.
- Privileges are constrained, if a script is loaded, ensure system runs in chroot jail or other limited authority mode

## Related weaknesses (CWE)
- [CWE-284](https://cwe.mitre.org/data/definitions/284.html)

## Related ATT&CK techniques
- T1027.009
- T1546.004
- T1546.016

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/19.html
