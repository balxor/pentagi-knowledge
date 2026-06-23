---
capec_id: CAPEC-638
name: Altered Component Firmware
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: Very High
related_cwe: []
related_attack: [T1542.002]
url: https://capec.mitre.org/data/definitions/638.html
tags: [mitre-capec, attack-pattern, CAPEC-638]
---

# CAPEC-638 - Altered Component Firmware

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-638](https://capec.mitre.org/data/definitions/638.html)

## Description
An adversary exploits systems features and/or improperly protected firmware of hardware components, such as Hard Disk Drives (HDD), with the goal of executing malicious code from within the component's Master Boot Record (MBR). Conducting this type of attack entails the adversary infecting the target with firmware altering malware, using known tools, and a payload. Once this malware is executed, the MBR is modified to include instructions to execute the payload at desired intervals and when the system is booted up. A successful attack will obtain persistence within the victim system even if the operating system is reinstalled and/or if the component is formatted or has its data erased.

## Prerequisites
- Advanced knowledge about the target component's firmware
- Advanced knowledge about Master Boot Records (MBR)
- Advanced knowledge about tools used to insert firmware altering malware.
- Advanced knowledge about component shipments to the target organization.

## Skills required
- **High**: Ability to intercept components in transit.
- **Low**: Ability to leverage known malware tools to infect target system and insert firmware altering malware/payload
- **Medium**: Ability to create malicious payload to be executed from MBR.

## Resources required
- Manufacturer source code for hardware components.
- Malware tools used to insert malware and payload onto target component.
- Either remote or physical access to the target component.

## Consequences
- **Access_Control**: Read Data, Modify Data
- **Authentication**: Gain Privileges, Execute Unauthorized Commands, Bypass Protection Mechanism, Hide Activities
- **Authorization**: Gain Privileges, Execute Unauthorized Commands, Bypass Protection Mechanism, Hide Activities
- **Confidentiality**: Read Data, Modify Data

## Execution flow
Execution Flow Explore Select Target: The adversary searches for a suitable target to attack, such as government and/or private industry organizations. Techniques Conduct reconnaissance to determine potential targets to exploit. Identify Components: After selecting a target, the adversary determines whether a vulnerable component, such as a specific make and model of a HDD, is contained within the target system. Techniques [Remote Access Vector] The adversary gains remote access to the target, typically via additional malware, and explores the system to determine hardware components that are being leveraged. [Physical Access Vector] The adversary intercepts components in transit and determines if the component is vulnerable to attack. Experiment Optional: Create Payload: If not using an already existing payload, the adversary creates their own to be executed at defined intervals and upon system boot processes. This payload may then be tested on the target system or a test system to confirm its functionality. Exploit Insert Firmware Altering Malware: Once a vulnerable component has been identified, the adversary leverages known malware tools to infect the component's firmware and drop the payload within the component's MBR. This allows the adversary to maintain persistence on the target and execute the payload without being detected. Techniques The adversary inserts the firmware altering malware on the target component, via the use of known malware tools. [Physical Access Vector] The adversary then sends the component to its original intended destination, where it will be installed onto a victim system.

## Mitigations
- Leverage hardware components known to not be susceptible to these types of attacks.
- Implement hardware RAID infrastructure.

## Related ATT&CK techniques
- T1542.002

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/638.html
