---
capec_id: CAPEC-501
name: Android Activity Hijack
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-923]
related_attack: []
url: https://capec.mitre.org/data/definitions/501.html
tags: [mitre-capec, attack-pattern, CAPEC-501]
---

# CAPEC-501 - Android Activity Hijack

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-501](https://capec.mitre.org/data/definitions/501.html)

## Description
An adversary intercepts an implicit intent sent to launch a Android-based trusted activity and instead launches a counterfeit activity in its place. The malicious activity is then used to mimic the trusted activity's user interface and prompt the target to enter sensitive data as if they were interacting with the trusted activity.

## Prerequisites
- The adversary must have previously installed the malicious application onto the Android device that will run in place of the trusted activity.

## Skills required
- **High**: The adversary must typically overcome network and host defenses in order to place malware on the system.

## Resources required
- Malware capable of acting on the adversary's objectives.

## Consequences
- **Confidentiality**: Read Data

## Execution flow
Execution Flow Explore Find an android application that uses implicit intents: Since this attack only works on android applications that use implicit intents, rather than explicit intents, an adversary must first identify an app that uses implicit intents to launch an Android-based trusted activity, and what that activity is. Experiment Create a malicious app: The adversary must create a malicious android app meant to intercept implicit intents to launch an Adroid-based trusted activity. This malicious app will mimic the trusted activiy's user interface to get the user to enter sensitive data. Techniques Specify the type of intent wished to be intercepted in the malicious app's manifest file using an intent filter Get user to download malicious app: The adversary must get a user using the targeted app to download the malicious app by any means necessary Exploit Gather sensitive data through malicious app: Once the target application sends an implicit intent to launch a trusted activity, the malicious app will be launched instead that looks identical to the interface of that activity. When the user enters sensitive information it will be captured by the malicious app. Techniques Gather login information from a user using a malicious app

## Mitigations
- To mitigate this type of an attack, explicit intents should be used whenever sensitive data is being sent. An 'explicit intent' is delivered to a specific application as declared within the intent, whereas an 'implicit intent' is directed to an application as defined by the Android operating system. If an implicit intent must be used, then it should be assumed that the intent will be received by an unknown application and any response should be treated accordingly (i.e., with appropriate security controls).
- Never use implicit intents for inter-application communication.

## Related weaknesses (CWE)
- [CWE-923](https://cwe.mitre.org/data/definitions/923.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/501.html
