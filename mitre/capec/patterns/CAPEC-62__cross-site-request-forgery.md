---
capec_id: CAPEC-62
name: Cross Site Request Forgery
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Very High
related_cwe: [CWE-352, CWE-306, CWE-664, CWE-732, CWE-1275]
related_attack: []
url: https://capec.mitre.org/data/definitions/62.html
tags: [mitre-capec, attack-pattern, CAPEC-62]
---

# CAPEC-62 - Cross Site Request Forgery

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-62](https://capec.mitre.org/data/definitions/62.html)

## Description
An attacker crafts malicious web links and distributes them (via web pages, email, etc.), typically in a targeted manner, hoping to induce users to click on the link and execute the malicious action against some third-party application. If successful, the action embedded in the malicious link will be processed and accepted by the targeted application with the users' privilege level. This type of attack leverages the persistence and implicit trust placed in user session cookies by many web applications today. In such an architecture, once the user authenticates to an application and a session cookie is created on the user's system, all following transactions for that session are authenticated using that cookie including potential actions initiated by an attacker and simply "riding" the existing session cookie.

## Skills required
- **Medium**: The attacker needs to figure out the exact invocation of the targeted malicious action and then craft a link that performs the said action. Having the user click on such a link is often accomplished by sending an email or posting such a link to a bulletin board or the likes.

## Resources required
- All the attacker needs is the exact representation of requests to be made to the application and to be able to get the malicious link across to a victim.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Explore target website: The attacker first explores the target website to determine pieces of functionality that are of interest to them (e.g. money transfers). The attacker will need a legitimate user account on the target website. It would help to have two accounts. Techniques Use web application debugging tool such as WebScarab, Tamper Data or TamperIE to analyze the information exchanged between the client and the server Use network sniffing tool such as Wireshark to analyze the information exchanged between the client and the server View HTML source of web pages that contain links or buttons that perform actions of interest. Experiment Create a link that when clicked on, will execute the interesting functionality.: The attacker needs to create a link that will execute some interesting functionality such as transfer money, change a password, etc. Techniques Create a GET request containing all required parameters (e.g. https://www.somebank.com/members/transfer.asp?to=012345678901&amt=10000) Create a form that will submit a POST request (e.g. Exploit Convince user to click on link: Finally, the attacker needs to convince a user that is logged into the target website to click on a link to execute the CSRF attack. Techniques Execute a phishing attack and send the user an e-mail convincing them to click on a link. Execute a stored XSS attack on a website to permanently embed the malicious link into the website. Execute a stored XSS attack on a website where an XMLHTTPRequest object will automatically execute the attack as soon as a user visits the page. This removes the step of convincing a user to click on a link. Include the malicious link on the attackers' own website where the user may have to click on the link, or where an XMLHTTPRequest object may automatically execute the attack when a user visits the site.

## Mitigations
- Use cryptographic tokens to associate a request with a specific action. The token can be regenerated at every request so that if a request with an invalid token is encountered, it can be reliably discarded. The token is considered invalid if it arrived with a request other than the action it was supposed to be associated with.
- Although less reliable, the use of the optional HTTP Referrer header can also be used to determine whether an incoming request was actually one that the user is authorized for, in the current context.
- Additionally, the user can also be prompted to confirm an action every time an action concerning potentially sensitive data is invoked. This way, even if the attacker manages to get the user to click on a malicious link and request the desired action, the user has a chance to recover by denying confirmation. This solution is also implicitly tied to using a second factor of authentication before performing such actions.
- In general, every request must be checked for the appropriate authentication token as well as authorization in the current session context.

## Related weaknesses (CWE)
- [CWE-352](https://cwe.mitre.org/data/definitions/352.html)
- [CWE-306](https://cwe.mitre.org/data/definitions/306.html)
- [CWE-664](https://cwe.mitre.org/data/definitions/664.html)
- [CWE-732](https://cwe.mitre.org/data/definitions/732.html)
- [CWE-1275](https://cwe.mitre.org/data/definitions/1275.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/62.html
