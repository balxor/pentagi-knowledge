---
capec_id: CAPEC-699
name: Eavesdropping on a Monitor
type: attack-pattern
abstraction: Meta
likelihood: Medium
severity: High
related_cwe: [CWE-1300]
related_attack: []
url: https://capec.mitre.org/data/definitions/699.html
tags: [mitre-capec, attack-pattern, CAPEC-699]
---

# CAPEC-699 - Eavesdropping on a Monitor

**Abstraction:** Meta  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-699](https://capec.mitre.org/data/definitions/699.html)

## Description
An Adversary can eavesdrop on the content of an external monitor through the air without modifying any cable or installing software, just capturing this signal emitted by the cable or video port, with this the attacker will be able to impact the confidentiality of the data without being detected by traditional security tools

## Extended description
This attack gives the adversary the ability to view an external monitor with an insignificant delay. There is also no indicator of compromise from the victim visible on the monitor. The eavesdrop is possible due to a signal leakage, that is produced at different points of the connection, including the source port, the connection between the cable and PC, the cable itself, and the connection between the cable and the monitor. That signal leakage can be captured near any of the leak points, but also in a near location, like the next room or a few meters away, using an SDR (Software-defined Radio) device and the correspondent software, that process and interpret the signal to show attackers what the monitor is displaying. From the victim’s point of view, this specified attack might cause a high risk, and from the other hand, from the attacker’s point of view, the attack is excellent, since the specified attack method can be used without investing too much effort or require too many skills, as long as the right attack tool is in right place, this allows attackers to completely compromise the confidentiality of the data; also giving the attacker the advantage of being undetectable by not only traditional security products but also from bug sweep because the SDR device is acting in passive mode.

## Prerequisites
- Victim should use an external monitor device
- Physical access to the target location and devices

## Skills required
- **Low**: Understanding of computing hardware, to identify the video cable and video ports
- **Medium**: Knowledge of how to use the SDR and related software: With this knowledge, the adversary will find the correct frequency where the signal is being leaked

## Resources required
- SDR device set with the correspondent antenna
- Computer with SDR Software

## Consequences
- **Confidentiality**: Read Data

## Execution flow
Execution Flow Explore Survey Target: The adversary surveys the target location, looking for exposed display cables and locations to hide an SDR. This also includes looking for display cables or monitors placed close to a wall, where the SDR can be in range while behind the wall. The adversary also attempts to discover the resolution and refresh rate of the targeted display. Experiment Find target using SDR: The adversary sets up an SDR near the target display cable or monitor. They use the SDR software to locate the corresponding frequency of the display cable. This is done by looking for interference peaks that change depending on what the screen is showing. The adversary notes down the possible frequencies of unintentional emission. Techniques An adversary can make use of many different commercially available SDR devices which are easy to setup such as a HackRF, Ubertooth, RTL-SDR, and many others. Exploit Visualize Monitor Image: Once the SDR software has been used to identify the target, the adversary will record the transmissions and visualize the monitor image using these transmissions, which allows them to eavesdrop on the information visible on the monitor. Techniques The TempestSDR software can be used in conjunction an SDR device to visualize the monitor image. The adversary will specify the known monitor resolution and refresh rate, or if those are not known they can use the provided auto-correlation graphs to help predict these values. The adversary will then try the different frequencies recorded from the experiment phase, looking for a viewing monitor display. Low pass filters and gain can be manipulated to make the display image clearer.

## Mitigations
- Enhance: Increase the number of electromagnetic shield layers in the display ports and cables to contain or reduce the intensity of the leaked signal.
- Implement: Use a protocol that encrypts the video signal; in case the signal is intercepted the signal is protected by the encryption.
- Design: Lock away the video cables, making it difficult for the attacker to access the cables and place the antenna near them (If the distance condition between the antenna and display port/cable is not satisfied, the attack will not be possible).
- Implement: Use wireless technologies to connect to external display devices.

## Related weaknesses (CWE)
- [CWE-1300](https://cwe.mitre.org/data/definitions/1300.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/699.html
