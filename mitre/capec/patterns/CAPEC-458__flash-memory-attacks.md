---
capec_id: CAPEC-458
name: Flash Memory Attacks
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: [CWE-1282]
related_attack: []
url: https://capec.mitre.org/data/definitions/458.html
tags: [mitre-capec, attack-pattern, CAPEC-458]
---

# CAPEC-458 - Flash Memory Attacks

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-458](https://capec.mitre.org/data/definitions/458.html)

## Description
An adversary inserts malicious logic into a product or technology via flashing the on-board memory with a code-base that contains malicious logic. Various attacks exist against the integrity of flash memory, the most direct being rootkits coded into the BIOS or chipset of a device.

## Extended description
Such attacks are very difficult to detect because the malicious code resides outside the filesystem or RAM, and in the underlying byte-code that drives the processor. Many devices, such as the recent attacks against digital picture frames, contain only a microprocessor and a small amount of solid-state memory, rendering these devices ideal for "flash" based malware or malicious logic. One of the pernicious characteristics of flash memory based attacks is that the malicious code can survive even a total format of the hard-drive and reinstallation of the host operating system. Virtually any device which can be integrated into a computer system is susceptible to these attacks. Additionally, any peripheral device which interfaces with the computer bus could extract or sniff confidential data, even on systems employing full-disk encryption. Trojan code placed into a video card's chipset would continue to perform its function irrespective of the host operating system, and would be invisible to all known antivirus. The threats extend to consumer products such as camcorders, digital cameras, or any consumer electronic device with an embedded microcontroller.

## Related weaknesses (CWE)
- [CWE-1282](https://cwe.mitre.org/data/definitions/1282.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/458.html
