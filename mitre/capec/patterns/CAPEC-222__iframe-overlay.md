---
capec_id: CAPEC-222
name: iFrame Overlay
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-1021]
related_attack: []
url: https://capec.mitre.org/data/definitions/222.html
tags: [mitre-capec, attack-pattern, CAPEC-222]
---

# CAPEC-222 - iFrame Overlay

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-222](https://capec.mitre.org/data/definitions/222.html)

## Description
In an iFrame overlay attack the victim is tricked into unknowingly initiating some action in one system while interacting with the UI from seemingly completely different system.

## Extended description
While being logged in to some target system, the victim visits the adversarys' malicious site which displays a UI that the victim wishes to interact with. In reality, the iFrame overlay page has a transparent layer above the visible UI with action controls that the adversary wishes the victim to execute. The victim clicks on buttons or other UI elements they see on the page which actually triggers the action controls in the transparent overlaying layer. Depending on what that action control is, the adversary may have just tricked the victim into executing some potentially privileged (and most undesired) functionality in the target system to which the victim is authenticated. The basic problem here is that there is a dichotomy between what the victim thinks they are clicking on versus what they are actually clicking on.

## Prerequisites
- The victim is communicating with the target application via a web based UI and not a thick client. The victim's browser security policies allow iFrames. The victim uses a modern browser that supports UI elements like clickable buttons (i.e. not using an old text only browser). The victim has an active session with the target system. The target system's interaction window is open in the victim's browser and supports the ability for initiating sensitive actions on behalf of the user in the target system.

## Skills required
- **High**: Crafting the proper malicious site and luring the victim to this site is not a trivial task.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Accountability**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges, Bypass Protection Mechanism
- **Confidentiality**: Read Data
- **Integrity**: Modify Data
- **Non-Repudiation**: Gain Privileges

## Execution flow
Execution Flow Explore Craft an iFrame Overlay page: The adversary crafts a malicious iFrame overlay page. Techniques The adversary leverages iFrame overlay capabilities to craft a malicious iFrame overlay page. Exploit adversary tricks victim to load the iFrame overlay page: adversary utilizes some form of temptation, misdirection or coercion to trick the victim to loading and interacting with the iFrame overlay page in a way that increases the chances that the victim will visit the malicious page. Techniques Trick the victim to the malicious site by sending the victim an e-mail with a URL to the site. Trick the victim to the malicious site by manipulating URLs on a site trusted by the victim. Trick the victim to the malicious site through a cross-site scripting attack. Trick victim into interacting with the iFrame overlay page in the desired manner: The adversary tricks the victim into clicking on the areas of the UI which contain the hidden action controls and thereby interacts with the target system maliciously with the victim's level of privilege. Techniques Hide action controls over very commonly used functionality. Hide action controls over very psychologically tempting content.

## Mitigations
- Configuration: Disable iFrames in the Web browser.
- Operation: When maintaining an authenticated session with a privileged target system, do not use the same browser to navigate to unfamiliar sites to perform other activities. Finish working with the target system and logout first before proceeding to other tasks.
- Operation: If using the Firefox browser, use the NoScript plug-in that will help forbid iFrames.

## Related weaknesses (CWE)
- [CWE-1021](https://cwe.mitre.org/data/definitions/1021.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/222.html
