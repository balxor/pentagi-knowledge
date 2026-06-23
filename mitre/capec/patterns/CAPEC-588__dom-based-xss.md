---
capec_id: CAPEC-588
name: DOM-Based XSS
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Very High
related_cwe: [CWE-79, CWE-20, CWE-83]
related_attack: []
url: https://capec.mitre.org/data/definitions/588.html
tags: [mitre-capec, attack-pattern, CAPEC-588]
---

# CAPEC-588 - DOM-Based XSS

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-588](https://capec.mitre.org/data/definitions/588.html)

## Description
This type of attack is a form of Cross-Site Scripting (XSS) where a malicious script is inserted into the client-side HTML being parsed by a web browser. Content served by a vulnerable web application includes script code used to manipulate the Document Object Model (DOM). This script code either does not properly validate input, or does not perform proper output encoding, thus creating an opportunity for an adversary to inject a malicious script launch a XSS attack. A key distinction between other XSS attacks and DOM-based attacks is that in other XSS attacks, the malicious script runs when the vulnerable web page is initially loaded, while a DOM-based attack executes sometime after the page loads. Another distinction of DOM-based attacks is that in some cases, the malicious script is never sent to the vulnerable web server at all. An attack like this is guaranteed to bypass any server-side filtering attempts to protect users.

## Prerequisites
- An application that leverages a client-side web browser with scripting enabled.
- An application that manipulates the DOM via client-side scripting.
- An application that failS to adequately sanitize or encode untrusted input.

## Skills required
- **Medium**: Requires the ability to write scripts of some complexity and to inject it through user controlled fields in the system.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Access_Control**: Gain Privileges (A successful DOM-based XSS attack can enable an adversary to elevate their privilege level and access functionality they should not otherwise be allowed to access.)
- **Authorization**: Gain Privileges (A successful DOM-based XSS attack can enable an adversary to elevate their privilege level and access functionality they should not otherwise be allowed to access.)
- **Availability**: Execute Unauthorized Commands (A successful DOM-based XSS attack can enable an adversary run arbitrary code of their choosing, thus enabling a complete compromise of the application.)
- **Confidentiality**: Read Data (A successful DOM-based XSS attack can enable an adversary to exfiltrate sensitive information from the application.), Gain Privileges (A successful DOM-based XSS attack can enable an adversary to elevate their privilege level and access functionality they should not otherwise be allowed to access.), Execute Unauthorized Commands (A successful DOM-based XSS attack can enable an adversary run arbitrary code of their choosing, thus enabling a complete compromise of the application.)
- **Integrity**: Execute Unauthorized Commands (A successful DOM-based XSS attack can enable an adversary run arbitrary code of their choosing, thus enabling a complete compromise of the application.), Modify Data (A successful DOM-based XSS attack can allow an adversary to tamper with application data.)

## Execution flow
Execution Flow Explore Survey the application for user-controllable inputs: Using a browser or an automated tool, an adversary follows all public links and actions on a web site. They record all the links, the forms, the resources accessed and all other potential entry-points for the web application. Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Make special note of any links that include parameters in the URL. Use a proxy tool to record all links visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Experiment Probe identified potential entry points for DOM-based XSS vulnerability: The adversary uses the entry points gathered in the "Explore" phase as a target list and injects various common script payloads and special characters to determine if an entry point actually represents a vulnerability and to characterize the extent to which the vulnerability can be exploited. Specific to DOM-based XSS, the adversary is looking for areas where input is being used to directly change the DOM. Techniques Use a list of XSS probe strings to inject script in parameters of known URLs. If possible, the probe strings contain a unique identifier. Use a proxy tool to record results of manual input of XSS probes in known URLs. Use a list of HTML special characters to inject into parameters of known URLs and check if they were properly encoded, replaced, or filtered out. Craft malicious XSS URL: Once the adversary has determined which parameters are vulnerable to XSS, they will craft a malicious URL containing the XSS exploit. The adversary can have many goals, from stealing session IDs, cookies, credentials, and page content from the victim. In DOM-based XSS, the malicious script might not even be sent to the server, since the victim's browser will manipulate the DOM itself. This can help avoid serve-side detection mechanisms. Techniques Change a URL parameter to include a malicious script tag. Add a URL fragment to alter the value of the expected Document object URL. Send information gathered from the malicious script to a remote endpoint. Exploit Get victim to click URL: In order for the attack to be successful, the victim needs to access the malicious URL. Techniques Send a phishing email to the victim containing the malicious URL. This can be hidden in a hyperlink as to not show the full URL, which might draw suspicion. Put the malicious URL on a public forum, where many victims might accidentally click the link.

## Mitigations
- Use browser technologies that do not allow client-side scripting.
- Utilize proper character encoding for all output produced within client-site scripts manipulating the DOM.
- Ensure that all user-supplied input is validated before use.

## Related weaknesses (CWE)
- [CWE-79](https://cwe.mitre.org/data/definitions/79.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-83](https://cwe.mitre.org/data/definitions/83.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/588.html
