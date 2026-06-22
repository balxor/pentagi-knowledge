---
attack_id: T1456
name: Drive-By Compromise
type: technique
parent: null
tactics: [Initial Access]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1456
tags: [mitre-attack, technique, T1456]
---

# T1456 - Drive-By Compromise

**Tactic(s):** Initial Access  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1456](https://attack.mitre.org/techniques/T1456)

## Summary
Adversaries may gain access to a system through a user visiting a website over the normal course of browsing. With this technique, the user's web browser is typically targeted for exploitation, but adversaries may also use compromised websites for non-exploitation behavior such as acquiring an [Application Access Token](https://attack.mitre.org/techniques/T1550/001).

Multiple ways of delivering exploit code to a browser exist, including:

* A legitimate website is compromised where adversaries have injected some form of malicious code such as JavaScript, iFrames, and cross-site scripting.
* Malicious ads are paid for and served through legitimate ad providers.
* Built-in web application interfaces are leveraged for the insertion of any other kind of object that can be used to display web content or contain a script that executes on the visiting client (e.g. forum posts, comments, and other user controllable web content).

Often the website used by an adversary is one visited by a specific community, such as government, a particular industry, or region, where the goal is to compromise a specific user or set of users based on a shared interest. This kind of targeted attack is referred to a strategic web compromise or watering hole attack. There are several known examples of this occurring.(Citation: Lookout-StealthMango)

Typical drive-by compromise process:

1. A user visits a website that is used to host the adversary controlled content.
2. Scripts automatically execute, typically searching versions of the browser and plugins for a potentially vulnerable version. 
    * The user may be required to assist in this process by enabling scripting or active website components and ignoring warning dialog boxes.
3. Upon finding a vulnerable version, exploit code is delivered to the browser.
4. If exploitation is successful, then it will give the adversary code execution on the user's system unless other protections are in place.
    * In some cases a second visit to the website after the initial scan is required before exploit code is delivered.

## Role in the attack flow
Used to achieve the **Initial Access** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

## Mitigations
- **M1001 Security Updates** - Install security updates in response to discovered vulnerabilities.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1456
