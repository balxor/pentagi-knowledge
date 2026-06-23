---
capec_id: CAPEC-499
name: Android Intent Intercept
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: n/a
related_cwe: [CWE-925]
related_attack: []
url: https://capec.mitre.org/data/definitions/499.html
tags: [mitre-capec, attack-pattern, CAPEC-499]
---

# CAPEC-499 - Android Intent Intercept

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-499](https://capec.mitre.org/data/definitions/499.html)

## Description
An adversary, through a previously installed malicious application, intercepts messages from a trusted Android-based application in an attempt to achieve a variety of different objectives including denial of service, information disclosure, and data injection. An implicit intent sent from a trusted application can be received by any application that has declared an appropriate intent filter. If the intent is not protected by a permission that the malicious application lacks, then the attacker can gain access to the data contained within the intent. Further, the intent can be either blocked from reaching the intended destination, or modified and potentially forwarded along.

## Prerequisites
- An adversary must be able install a purpose built malicious application onto the Android device and convince the user to execute it. The malicious application is used to intercept implicit intents.

## Consequences
- **Availability**: Resource Consumption
- **Confidentiality**: Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Find an android application that uses implicit intents: Since this attack only works on android applications that use implicit intents, rather than explicit intents, an adversary must first identify an app that uses implicit intents. They must also determine what the contents of the intents being sent are such that a malicious application can get sent these intents. Experiment Create a malicious app: The adversary must create a malicious android app meant to intercept implicit intents from a target application Techniques Specify the type of intent wished to be intercepted in the malicious app's manifest file using an intent filter Get user to download malicious app: The adversary must get a user using the targeted app to download the malicious app by any means necessary Exploit Intercept Implicit Intents: Once the malicious app is downloaded, the android device will forward any implicit intents from the target application to the malicious application, allowing the adversary to gaina access to the contents of the intent. The adversary can proceed with any attack using the contents of the intent. Techniques Block the intent from reaching the desired location, causing a denial of service Gather sensitive information from the intercepted intent Modify the contents of the intent and forward along to another application

## Mitigations
- To mitigate this type of an attack, explicit intents should be used whenever sensitive data is being sent. An explicit intent is delivered to a specific application as declared within the intent, whereas the Android operating system determines who receives an implicit intent which could potentially be a malicious application. If an implicit intent must be used, then it should be assumed that the intent will be received by an unknown application and any response should be treated accordingly. Implicit intents should never be used for inter-application communication.

## Related weaknesses (CWE)
- [CWE-925](https://cwe.mitre.org/data/definitions/925.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/499.html
