---
capec_id: CAPEC-466
name: Leveraging Active Adversary in the Middle Attacks to Bypass Same Origin Policy
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Medium
related_cwe: [CWE-300]
related_attack: []
url: https://capec.mitre.org/data/definitions/466.html
tags: [mitre-capec, attack-pattern, CAPEC-466]
---

# CAPEC-466 - Leveraging Active Adversary in the Middle Attacks to Bypass Same Origin Policy

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-466](https://capec.mitre.org/data/definitions/466.html)

## Description
An attacker leverages an adversary in the middle attack (CAPEC-94) in order to bypass the same origin policy protection in the victim's browser. This active adversary in the middle attack could be launched, for instance, when the victim is connected to a public WIFI hot spot. An attacker is able to intercept requests and responses between the victim's browser and some non-sensitive website that does not use TLS.

## Extended description
When an attacker intercepts a response bound to the victim, an attacker adds an iFrame (which is possibly invisible) to the response referencing some domain with sensitive functionality and forwards the response to the victim. The victim's browser than automatically initiates an unauthorized request to the site with sensitive functionality. The same origin policy would prevent making these requests to a site other than the one from which the Java Script came, but the attacker once again uses active adversary in the middle to intercept these automatic requests and redirect them to the domain / service with sensitive functionality. Any persistent cookies that the victim has in their browser would be used for these unauthorized requests. The attacker thus actively directs the victim to a site with sensitive functionality. When the site with sensitive functionality responds back to the victim's request, an active adversary in the middle attacker intercepts these responses, injects their own malicious Java Script into these responses, and forwards to the victim's browser. In the victim's browser, that Java Script executes under the restrictions of the site with sensitive functionality and can be used to continue to interact with the sensitive site. So an attacker can execute scripts within the victim's browser on any domains the attacker desires. The attacker is able to use this technique to steal cookies from the victim's browser for whatever site the attacker wants. This applies to both persistent cookies and HTTP only cookies (unlike traditional XSS attacks). An attacker is also able to use this technique to steal authentication credentials for sites that only encrypt the login form, but do not require a secure channel for the initial request to get to the page with the login form. Further the attacker is also able to steal any autocompletion information. This attack pattern can also be used to enable session fixation and cache poisoning attacks. Additional attacks can be enabled as well.

## Prerequisites
- The victim and the attacker are both in an environment where an active adversary in the middle attack is possible (e.g., public WIFI hot spot)The victim visits at least one website that does not use TLS / SSL

## Skills required
- **Low**: Ability to intercept and modify requests / responses
- **Medium**: Solid understanding of the HTTP protocol

## Consequences
- **Authorization**: Execute Unauthorized Commands
- **Confidentiality**: Read Data

## Mitigations
- Design: Tunnel communications through a secure proxy
- Design: Trust level separation for privileged / non privileged interactions (e.g., two different browsers, two different users, two different operating systems, two different virtual machines)

## Related weaknesses (CWE)
- [CWE-300](https://cwe.mitre.org/data/definitions/300.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/466.html
