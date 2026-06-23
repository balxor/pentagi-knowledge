---
capec_id: CAPEC-464
name: Evercookie
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Medium
related_cwe: [CWE-359]
related_attack: [T1606.001]
url: https://capec.mitre.org/data/definitions/464.html
tags: [mitre-capec, attack-pattern, CAPEC-464]
---

# CAPEC-464 - Evercookie

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-464](https://capec.mitre.org/data/definitions/464.html)

## Description
An attacker creates a very persistent cookie that stays present even after the user thinks it has been removed. The cookie is stored on the victim's machine in over ten places. When the victim clears the cookie cache via traditional means inside the browser, that operation removes the cookie from certain places but not others. The malicious code then replicates the cookie from all of the places where it was not deleted to all of the possible storage locations once again. So the victim again has the cookie in all of the original storage locations. In other words, failure to delete the cookie in even one location will result in the cookie's resurrection everywhere. The evercookie will also persist across different browsers because certain stores (e.g., Local Shared Objects) are shared between different browsers.

## Extended description
The places a persistent cookie is stored on a victim's machine include: Standard HTTP Cookies, Local Shared Objects (Flash Cookies), Silverlight Isolated Storage, Storing cookies in RGB values of auto-generated, force-cached, PNGs using HTML5 Canvas tag to read pixels (cookies) back out, Storing cookies in Web History, Storing cookies in HTTP ETags, Storing cookies in Web cache, window.name caching, Internet Explorer userData storage, HTML5 Session Storage, HTML5 Local Storage, HTML5 Global Storage, HTML5 Database Storage via SQLite, among others.

## Prerequisites
- The victim's browser is not configured to reject all cookiesThe victim visits a website that serves the attackers' evercookie

## Resources required
- Evercookie source code

## Mitigations
- Design: Browser's design needs to be changed to limit where cookies can be stored on the client side and provide an option to clear these cookies in all places, as well as another option to stop these cookies from being written in the first place.
- Design: Safari browser's private browsing mode is currently effective against evercookies.

## Related weaknesses (CWE)
- [CWE-359](https://cwe.mitre.org/data/definitions/359.html)

## Related ATT&CK techniques
- T1606.001

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/464.html
