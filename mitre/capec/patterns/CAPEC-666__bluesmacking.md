---
capec_id: CAPEC-666
name: BlueSmacking
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: Medium
related_cwe: [CWE-404]
related_attack: [T1498.001, T1499.001]
url: https://capec.mitre.org/data/definitions/666.html
tags: [mitre-capec, attack-pattern, CAPEC-666]
---

# CAPEC-666 - BlueSmacking

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-666](https://capec.mitre.org/data/definitions/666.html)

## Description
An adversary uses Bluetooth flooding to transfer large packets to Bluetooth enabled devices over the L2CAP protocol with the goal of creating a DoS. This attack must be carried out within close proximity to a Bluetooth enabled device.

## Prerequisites
- The system/application has Bluetooth enabled.

## Skills required
- **Low**: An adversary only needs a Linux machine along with a Bluetooth adapter, which is extremely common.

## Consequences
- **Availability**: Unreliable Execution, Resource Consumption

## Execution flow
Execution Flow Explore Scan for Bluetooth Enabled Devices: Using BlueZ along with an antenna, an adversary searches for devices with Bluetooth on. Techniques Note the MAC address of the device you want to attack. Experiment Change L2CAP Packet Length: The adversary must change the L2CAP packet length to create packets that will overwhelm a Bluetooth enabled device. Techniques An adversary downloads and installs BlueZ, the standard Bluetooth utility package for Linux. Exploit Flood: An adversary sends the packets to the target device, and floods it until performance is degraded.

## Mitigations
- Disable Bluetooth when not being used.
- When using Bluetooth, set it to hidden or non-discoverable mode.

## Related weaknesses (CWE)
- [CWE-404](https://cwe.mitre.org/data/definitions/404.html)

## Related ATT&CK techniques
- T1498.001
- T1499.001

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/666.html
