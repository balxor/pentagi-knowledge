---
capec_id: CAPEC-591
name: Reflected XSS
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Very High
related_cwe: [CWE-79]
related_attack: []
url: https://capec.mitre.org/data/definitions/591.html
tags: [mitre-capec, attack-pattern, CAPEC-591]
---

# CAPEC-591 - Reflected XSS

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-591](https://capec.mitre.org/data/definitions/591.html)

## Description
This type of attack is a form of Cross-Site Scripting (XSS) where a malicious script is "reflected" off a vulnerable web application and then executed by a victim's browser. The process starts with an adversary delivering a malicious script to a victim and convincing the victim to send the script to the vulnerable web application.

## Extended description
The most common method of this is through a phishing email where the adversary embeds the malicious script with a URL that the victim then clicks on. In processing the subsequent request, the vulnerable web application incorrectly considers the malicious script as valid input and uses it to creates a reposnse that is then sent back to the victim. To launch a successful Reflected XSS attack, an adversary looks for places where user-input is used directly in the generation of a response. This often involves elements that are not expected to host scripts such as image tags ( ), or the addition of event attibutes such as onload and onmouseover. These elements are often not subject to the same input validation, output encoding, and other content filtering and checking routines.

## Prerequisites
- An application that leverages a client-side web browser with scripting enabled.
- An application that fail to adequately sanitize or encode untrusted input.

## Skills required
- **Medium**: Requires the ability to write malicious scripts and embed them into HTTP requests.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Access_Control**: Gain Privileges (A successful Reflected XSS attack can enable an adversary to elevate their privilege level and access functionality they should not otherwise be allowed to access.)
- **Authorization**: Gain Privileges (A successful Reflected XSS attack can enable an adversary to elevate their privilege level and access functionality they should not otherwise be allowed to access.)
- **Availability**: Execute Unauthorized Commands (A successful Reflected attack can enable an adversary run arbitrary code of their choosing, thus enabling a complete compromise of the application.)
- **Confidentiality**: Read Data (A successful Reflected XSS attack can enable an adversary to exfiltrate sensitive information from the application.), Gain Privileges (A successful Reflected XSS attack can enable an adversary to elevate their privilege level and access functionality they should not otherwise be allowed to access.), Execute Unauthorized Commands (A successful Reflected attack can enable an adversary run arbitrary code of their choosing, thus enabling a complete compromise of the application.)
- **Integrity**: Execute Unauthorized Commands (A successful Reflected attack can enable an adversary run arbitrary code of their choosing, thus enabling a complete compromise of the application.), Modify Data (A successful Reflected attack can allow an adversary to tamper with application data.)

## Execution flow
Execution Flow Explore Survey the application for user-controllable inputs: Using a browser or an automated tool, an adversary follows all public links and actions on a web site. They record all the links, the forms, the resources accessed and all other potential entry-points for the web application. Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Make special note of any links that include parameters in the URL. Use a proxy tool to record all links visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Experiment Probe identified potential entry points for reflected XSS vulnerability: The adversary uses the entry points gathered in the "Explore" phase as a target list and injects various common script payloads and special characters to determine if an entry point actually represents a vulnerability and to characterize the extent to which the vulnerability can be exploited. Techniques Use a list of XSS probe strings to inject script in parameters of known URLs. If possible, the probe strings contain a unique identifier. Use a proxy tool to record results of manual input of XSS probes in known URLs. Use a list of HTML special characters to inject into parameters of known URLs and check if they were properly encoded, replaced, or filtered out. Craft malicious XSS URL: Once the adversary has determined which parameters are vulnerable to XSS, they will craft a malicious URL containing the XSS exploit. The adversary can have many goals, from stealing session IDs, cookies, credentials, and page content from the victim. Techniques Change a URL parameter to include a malicious script tag. Send information gathered from the malicious script to a remote endpoint. Exploit Get victim to click URL: In order for the attack to be successful, the victim needs to access the malicious URL. Techniques Send a phishing email to the victim containing the malicious URL. This can be hidden in a hyperlink as to not show the full URL, which might draw suspicion. Put the malicious URL on a public forum, where many victims might accidentally click the link.

## Mitigations
- Use browser technologies that do not allow client-side scripting.
- Utilize strict type, character, and encoding enforcement.
- Ensure that all user-supplied input is validated before use.

## Related weaknesses (CWE)
- [CWE-79](https://cwe.mitre.org/data/definitions/79.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/591.html
