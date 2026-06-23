---
capec_id: CAPEC-104
name: Cross Zone Scripting
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: High
related_cwe: [CWE-250, CWE-638, CWE-285, CWE-116, CWE-20]
related_attack: []
url: https://capec.mitre.org/data/definitions/104.html
tags: [mitre-capec, attack-pattern, CAPEC-104]
---

# CAPEC-104 - Cross Zone Scripting

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-104](https://capec.mitre.org/data/definitions/104.html)

## Description
An attacker is able to cause a victim to load content into their web-browser that bypasses security zone controls and gain access to increased privileges to execute scripting code or other web objects such as unsigned ActiveX controls or applets. This is a privilege elevation attack targeted at zone-based web-browser security.

## Extended description
In a zone-based model, pages belong to one of a set of zones corresponding to the level of privilege assigned to that page. Pages in an untrusted zone would have a lesser level of access to the system and/or be restricted in the types of executable content it was allowed to invoke. In a cross-zone scripting attack, a page that should be assigned to a less privileged zone is granted the privileges of a more trusted zone. This can be accomplished by exploiting bugs in the browser, exploiting incorrect configuration in the zone controls, through a cross-site scripting attack that causes the attackers' content to be treated as coming from a more trusted page, or by leveraging some piece of system functionality that is accessible from both the trusted and less trusted zone. This attack differs from "Restful Privilege Escalation" in that the latter correlates to the inadequate securing of RESTful access methods (such as HTTP DELETE) on the server, while cross-zone scripting attacks the concept of security zones as implemented by a browser.

## Prerequisites
- The target must be using a zone-aware browser.

## Skills required
- **Medium**: Ability to craft malicious scripts or find them elsewhere and ability to identify functionality that is running web controls in the local zone and to find an injection vector into that functionality

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Read Data, Gain Privileges, Execute Unauthorized Commands (Run Arbitrary Code)
- **Integrity**: Modify Data, Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Find systems susceptible to the attack: Find systems that contain functionality that is accessed from both the internet zone and the local zone. There needs to be a way to supply input to that functionality from the internet zone and that original input needs to be used later on a page from a local zone. Techniques Leverage knowledge of common local zone functionality on targeted platforms to guide attempted injection of code through relevant internet zone mechanisms. In some cases this may be due to standard system configurations enabling shared functionality between internet and local zones. The attacker can search for indicators that these standard configurations are in place. Experiment Find the insertion point for the payload: The attacker first needs to find some system functionality or possibly another weakness in the system (e.g. susceptibility to cross site scripting) that would provide the attacker with a mechanism to deliver the payload (i.e. the code to be executed) to the user. The location from which this code is executed in the user's browser needs to be within the local machine zone. Techniques Finding weaknesses in functionality used by both privileged and unprivileged users. Exploit Craft and inject the payload: Develop the payload to be executed in the higher privileged zone in the user's browser. Inject the payload and attempt to lure the victim (if possible) into executing the functionality which unleashes the payload. Techniques The attacker makes it as likely as possible that the vulnerable functionality into which they have injected the payload has a high likelihood of being used by the victim. Leverage cross-site scripting vulnerability to inject payload.

## Mitigations
- Disable script execution.
- Ensure that sufficient input validation is performed for any potentially untrusted data before it is used in any privileged context or zone
- Limit the flow of untrusted data into the privileged areas of the system that run in the higher trust zone
- Limit the sites that are being added to the local machine zone and restrict the privileges of the code running in that zone to the bare minimum
- Ensure proper HTML output encoding before writing user supplied data to the page

## Related weaknesses (CWE)
- [CWE-250](https://cwe.mitre.org/data/definitions/250.html)
- [CWE-638](https://cwe.mitre.org/data/definitions/638.html)
- [CWE-285](https://cwe.mitre.org/data/definitions/285.html)
- [CWE-116](https://cwe.mitre.org/data/definitions/116.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/104.html
