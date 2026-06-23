---
capec_id: CAPEC-400
name: RFID Chip Deactivation or Destruction
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/400.html
tags: [mitre-capec, attack-pattern, CAPEC-400]
---

# CAPEC-400 - RFID Chip Deactivation or Destruction

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-400](https://capec.mitre.org/data/definitions/400.html)

## Description
An attacker uses methods to deactivate a passive RFID tag for the purpose of rendering the tag, badge, card, or object containing the tag unresponsive. RFID tags are used primarily for access control, inventory, or anti-theft devices. The purpose of attacking the RFID chip is to disable or damage the chip without causing damage to the object housing it.

## Extended description
When correctly performed the RFID chip can be disabled or destroyed without visible damage or marking to whatever item or device containing the chip. Attacking the chip directly allows for the security device or method to be bypassed without directly damaging the device itself, such as an alarm system or computer system. Various methods exist for damaging or deactivating RFID tags. For example, most common RFID chips can be permanently destroyed by creating a small electromagnetic pulse near the chip itself. One method employed requires the modifying a disposable camera by disconnecting the flash bulb and soldering a copper coil to the capacitor. Firing the camera in this configuration near any RFID chip-based device creates an EMP pulse sufficient to destroy the chip without leaving evidence of tampering. So far this attack has been demonstrated to work against RFID chips in the 13.56 MHz range.

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/400.html
