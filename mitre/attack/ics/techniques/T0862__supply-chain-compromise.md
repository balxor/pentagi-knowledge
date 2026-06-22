---
attack_id: T0862
name: Supply Chain Compromise
type: technique
parent: null
tactics: [Initial Access]
platforms: [None]
url: https://attack.mitre.org/techniques/T0862
tags: [mitre-attack, technique, T0862]
---

# T0862 - Supply Chain Compromise

**Tactic(s):** Initial Access  -  **Platforms:** None  -  **ATT&CK:** [T0862](https://attack.mitre.org/techniques/T0862)

## Summary
Adversaries may perform supply chain compromise to gain control systems environment access by means of infected products, software, and workflows. Supply chain compromise is the manipulation of products, such as devices or software, or their delivery mechanisms before receipt by the end consumer. Adversary compromise of these products and mechanisms is done for the goal of data or system compromise, once infected products are introduced to the target environment. 

Supply chain compromise can occur at all stages of the supply chain, from manipulation of development tools and environments to manipulation of developed products and tools distribution mechanisms. This may involve the compromise and replacement of legitimate software and patches, such as on third party or vendor websites. Targeting of supply chain compromise can be done in attempts to infiltrate the environments of a specific audience. In control systems environments with assets in both the IT and OT networks, it is possible a supply chain compromise affecting the IT environment could enable further access to the OT environment.   

Counterfeit devices may be introduced to the global supply chain posing safety and cyber risks to asset owners and operators. These devices may not meet the safety, engineering and manufacturing requirements of regulatory bodies but may feature tagging indicating conformance with industry standards. Due to the lack of adherence to standards and overall lesser quality, the counterfeit products may pose a serious safety and operational risk. (Citation: Control Global May 2019) 

Yokogawa identified instances in which their customers received counterfeit differential pressure transmitters using the Yokogawa logo. The counterfeit transmitters were nearly indistinguishable with a semblance of functionality and interface that mimics the genuine product. (Citation: Control Global May 2019) 

F-Secure Labs analyzed the approach the adversary used to compromise victim systems with Havex. (Citation: Daavid Hentunen, Antti Tikkanen June 2014) The adversary planted trojanized software installers available on legitimate ICS/SCADA vendor websites. After being downloaded, this software infected the host computer with a Remote Access Trojan (RAT).

## Role in the attack flow
Used to achieve the **Initial Access** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0951 Update Software** - Perform regular software updates to mitigate exploitation risk. Software updates may need to be scheduled around operational down times.
- **M0947 Audit** - Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses. Perform periodic integrity checks of the device to validate the correctness of the firmware, software, programs, and configurations. Integrity checks, which typically include cryptographic hashes or digital signatures, should be compared to those obtained at known valid states, especially after events like device reboots, program downloads, or program restarts.
- **M0916 Vulnerability Scanning** - Vulnerability scanning is used to find potentially exploitable software vulnerabilities to remediate them.
- **M0817 Supply Chain Management** - Implement a supply chain management program, including policies and procedures to ensure all devices and components originate from a trusted supplier and are tested to verify their integrity.
- **M0945 Code Signing** - Enforce binary and application integrity with digital signature verification to prevent untrusted code from executing.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0862
