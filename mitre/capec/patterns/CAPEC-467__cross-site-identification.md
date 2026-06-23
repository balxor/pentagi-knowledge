---
capec_id: CAPEC-467
name: Cross Site Identification
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-352, CWE-359]
related_attack: []
url: https://capec.mitre.org/data/definitions/467.html
tags: [mitre-capec, attack-pattern, CAPEC-467]
---

# CAPEC-467 - Cross Site Identification

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-467](https://capec.mitre.org/data/definitions/467.html)

## Description
An attacker harvests identifying information about a victim via an active session that the victim's browser has with a social networking site. A victim may have the social networking site open in one tab or perhaps is simply using the "remember me" feature to keep their session with the social networking site active. An attacker induces a payload to execute in the victim's browser that transparently to the victim initiates a request to the social networking site (e.g., via available social network site APIs) to retrieve identifying information about a victim. While some of this information may be public, the attacker is able to harvest this information in context and may use it for further attacks on the user (e.g., spear phishing).

## Extended description
There are many other ways in which the attacker may get the payload to execute in the victim's browser mainly by finding a way to hide it in some reputable site that the victim visits. The attacker could also send the link to the victim in an e-mail and trick the victim into clicking on the link. This attack is basically a cross site request forgery attack with two main differences. First, there is no action that is performed on behalf of the user aside from harvesting information. So standard CSRF protection may not work in this situation. Second, what is important in this attack pattern is the nature of the data being harvested, which is identifying information that can be obtained and used in context. This real time harvesting of identifying information can be used as a prelude for launching real time targeted social engineering attacks on the victim.

## Prerequisites
- The victim has an active session with the social networking site.

## Skills required
- **High**: An attacker should be able to create a payload and deliver it to the victim's browser.
- **Medium**: An attacker needs to know how to interact with various social networking sites (e.g., via available APIs) to request information and how to send the harvested data back to the attacker.

## Mitigations
- Usage: Users should always explicitly log out from the social networking sites when done using them.
- Usage: Users should not open other tabs in the browser when using a social networking site.

## Related weaknesses (CWE)
- [CWE-352](https://cwe.mitre.org/data/definitions/352.html)
- [CWE-359](https://cwe.mitre.org/data/definitions/359.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/467.html
