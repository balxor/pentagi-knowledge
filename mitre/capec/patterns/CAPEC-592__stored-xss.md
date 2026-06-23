---
capec_id: CAPEC-592
name: Stored XSS
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Very High
related_cwe: [CWE-79]
related_attack: []
url: https://capec.mitre.org/data/definitions/592.html
tags: [mitre-capec, attack-pattern, CAPEC-592]
---

# CAPEC-592 - Stored XSS

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-592](https://capec.mitre.org/data/definitions/592.html)

## Description
An adversary utilizes a form of Cross-site Scripting (XSS) where a malicious script is persistently "stored" within the data storage of a vulnerable web application as valid input.

## Extended description
Initially presented by an adversary to the vulnerable web application, the malicious script is incorrectly considered valid input and is not properly encoded by the web application. A victim is then convinced to use the web application in a way that creates a response that includes the malicious script. This response is subsequently sent to the victim and the malicious script is executed by the victim's browser. To launch a successful Stored XSS attack, an adversary looks for places where stored input data is used in the generation of a response. This often involves elements that are not expected to host scripts such as image tags ( ), or the addition of event attributes such as onload and onmouseover. These elements are often not subject to the same input validation, output encoding, and other content filtering and checking routines.

## Prerequisites
- An application that leverages a client-side web browser with scripting enabled.
- An application that fails to adequately sanitize or encode untrusted input.
- An application that stores information provided by the user in data storage of some kind.

## Skills required
- **Medium**: Requires the ability to write scripts of varying complexity and to inject them through user controlled fields within the application.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Access_Control**: Gain Privileges (A successful Stored XSS attack can enable an adversary to elevate their privilege level and access functionality they should not otherwise be allowed to access.)
- **Authorization**: Gain Privileges (A successful Stored XSS attack can enable an adversary to elevate their privilege level and access functionality they should not otherwise be allowed to access.)
- **Availability**: Execute Unauthorized Commands (A successful Stored XSS attack can enable an adversary run arbitrary code of their choosing, thus enabling a complete compromise of the application.)
- **Confidentiality**: Read Data (A successful Stored XSS attack can enable an adversary to exfiltrate sensitive information from the application.), Gain Privileges (A successful Stored XSS attack can enable an adversary to elevate their privilege level and access functionality they should not otherwise be allowed to access.), Execute Unauthorized Commands (A successful Stored XSS attack can enable an adversary run arbitrary code of their choosing, thus enabling a complete compromise of the application.)
- **Integrity**: Execute Unauthorized Commands (A successful Stored XSS attack can enable an adversary run arbitrary code of their choosing, thus enabling a complete compromise of the application.), Modify Data (A successful Stored XSS attack can allow an adversary to tamper with application data.)

## Execution flow
Execution Flow Explore Survey the application for stored user-controllable inputs: Using a browser or an automated tool, an adversary follows all public links and actions on a web site. They record all the links, the forms, the resources accessed and all other potential entry-points for the web application. The adversary is looking for areas where user input is stored, such as user profiles, shopping carts, file managers, forums, blogs, and logs. Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Use a proxy tool to record all links visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Experiment Probe identified potential entry points for stored XSS vulnerability: The adversary uses the entry points gathered in the "Explore" phase as a target list and injects various common script payloads and special characters to determine if an entry point actually represents a vulnerability and to characterize the extent to which the vulnerability can be exploited. Techniques Use a list of XSS probe strings to submit script in input fields that could be stored by the web application. If possible, the probe strings contain a unique identifier so they can be queried for after submitting to see if they are stored. Use a list of HTML special characters to submit in input fields that could be stored by the web application and check if they were properly encoded, replaced, or filtered out. Store malicious XSS content: Once the adversary has determined which stored locations are vulnerable to XSS, they will interact with the web application to store the malicious content. The adversary can have many goals, from stealing session IDs, cookies, credentials, and page content from a victim. Techniques Store a malicious script on a page that will execute when viewed by the victim. Use a tool such as BeEF to store a hook into the web application. This will alert the adversary when the victim has accessed the content and will give the adversary control over the victim's browser, allowing them access to cookies, user screenshot, user clipboard, and more complex XSS attacks. Exploit Get victim to view stored content: In order for the attack to be successful, the victim needs to view the stored malicious content on the webpage. Techniques Send a phishing email to the victim containing a URL that will direct them to the malicious stored content. Simply wait for a victim to view the content. This is viable in situations where content is posted to a popular public forum.

## Mitigations
- Use browser technologies that do not allow client-side scripting.
- Utilize strict type, character, and encoding enforcement.
- Ensure that all user-supplied input is validated before being stored.

## Related weaknesses (CWE)
- [CWE-79](https://cwe.mitre.org/data/definitions/79.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/592.html
