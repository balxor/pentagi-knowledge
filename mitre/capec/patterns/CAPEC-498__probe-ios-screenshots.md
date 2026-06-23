---
capec_id: CAPEC-498
name: Probe iOS Screenshots
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: [CWE-359]
related_attack: []
url: https://capec.mitre.org/data/definitions/498.html
tags: [mitre-capec, attack-pattern, CAPEC-498]
---

# CAPEC-498 - Probe iOS Screenshots

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-498](https://capec.mitre.org/data/definitions/498.html)

## Description
An adversary examines screenshot images created by iOS in an attempt to obtain sensitive information. This attack targets temporary screenshots created by the underlying OS while the application remains open in the background.

## Extended description
These images are used by iOS to aid in the visual transition between open applications and improve the user's experience with a device. An application can be at risk even if it properly protects sensitive information when at rest. If the application displays sensitive information on the screen, then the potential exists for iOS to unintentionally record that information in an image file. An adversary can retrieve these images either by gaining access to the image files, or by physically obtaining the device and leveraging the multitasking switcher interface. This attack differs from CAPEC-648, which targets intentional screenshots initiated by an end-user that are stored in the device's storage.

## Prerequisites
- This type of an attack requires physical access to a device to either excavate the image files (potentially by leveraging a Jailbreak) or view the screenshots through the multitasking switcher (by double tapping the home button on the device).

## Mitigations
- To mitigate this type of an attack, an application that may display sensitive information should clear the screen contents before a screenshot is taken. This can be accomplished by setting the key window's hidden property to YES. This code to hide the contents should be placed in both the applicationWillResignActive() and applicationDidEnterBackground() methods.

## Related weaknesses (CWE)
- [CWE-359](https://cwe.mitre.org/data/definitions/359.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/498.html
