---
capec_id: CAPEC-103
name: Clickjacking
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: High
related_cwe: [CWE-1021]
related_attack: []
url: https://capec.mitre.org/data/definitions/103.html
tags: [mitre-capec, attack-pattern, CAPEC-103]
---

# CAPEC-103 - Clickjacking

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-103](https://capec.mitre.org/data/definitions/103.html)

## Description
An adversary tricks a victim into unknowingly initiating some action in one system while interacting with the UI from a seemingly completely different, usually an adversary controlled or intended, system.

## Extended description
While being logged in to some target system, the victim visits the adversary's malicious site which displays a UI that the victim wishes to interact with. In reality, the clickjacked page has a transparent layer above the visible UI with action controls that the adversary wishes the victim to execute. The victim clicks on buttons or other UI elements they see on the page which actually triggers the action controls in the transparent overlaying layer. Depending on what that action control is, the adversary may have just tricked the victim into executing some potentially privileged (and most certainly undesired) functionality in the target system to which the victim is authenticated. The basic problem here is that there is a dichotomy between what the victim thinks they are clicking on versus what they are actually clicking on.

## Prerequisites
- The victim is communicating with the target application via a web based UI and not a thick client
- The victim's browser security policies allow at least one of the following JavaScript, Flash, iFrames, ActiveX, or CSS.
- The victim uses a modern browser that supports UI elements like clickable buttons (i.e. not using an old text only browser)
- The victim has an active session with the target system.
- The target system's interaction window is open in the victim's browser and supports the ability for initiating sensitive actions on behalf of the user in the target system

## Skills required
- **High**: Crafting the proper malicious site and luring the victim to this site are not trivial tasks.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Unreliable Execution
- **Confidentiality**: Gain Privileges, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Experiment Craft a clickjacking page: The adversary utilizes web page layering techniques to try to craft a malicious clickjacking page Techniques The adversary leveraged iframe overlay capabilities to craft a malicious clickjacking page The adversary leveraged Flash file overlay capabilities to craft a malicious clickjacking page The adversary leveraged Silverlight overlay capabilities to craft a malicious clickjacking page The adversary leveraged cross-frame scripting to craft a malicious clickjacking page Exploit Adversary lures victim to clickjacking page: Adversary utilizes some form of temptation, misdirection or coercion to lure the victim to loading and interacting with the clickjacking page in a way that increases the chances that the victim will click in the right areas. Techniques Lure the victim to the malicious site by sending the victim an e-mail with a URL to the site. Lure the victim to the malicious site by manipulating URLs on a site trusted by the victim. Lure the victim to the malicious site through a cross-site scripting attack. Trick victim into interacting with the clickjacking page in the desired manner: The adversary tricks the victim into clicking on the areas of the UI which contain the hidden action controls and thereby interacts with the target system maliciously with the victim's level of privilege. Techniques Hide action controls over very commonly used functionality. Hide action controls over very psychologically tempting content.

## Mitigations
- If using the Firefox browser, use the NoScript plug-in that will help forbid iFrames.
- Turn off JavaScript, Flash and disable CSS.
- When maintaining an authenticated session with a privileged target system, do not use the same browser to navigate to unfamiliar sites to perform other activities. Finish working with the target system and logout first before proceeding to other tasks.

## Related weaknesses (CWE)
- [CWE-1021](https://cwe.mitre.org/data/definitions/1021.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/103.html
