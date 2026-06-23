---
cwe_id: CWE-1330
name: Remanent Data Readable after Memory Erase
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Security Hardware, Not Technology-Specific]
related_capec: [CAPEC-150, CAPEC-37, CAPEC-545]
url: https://cwe.mitre.org/data/definitions/1330.html
tags: [mitre-cwe, weakness, CWE-1330]
---

# CWE-1330 - Remanent Data Readable after Memory Erase

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-1330](https://cwe.mitre.org/data/definitions/1330.html)

## Description
Confidential information stored in memory circuits is readable or recoverable after being cleared or erased.

## Extended description
Data remanence occurs when stored, memory content is not fully lost after a memory-clear or -erase operation. Confidential memory contents can still be readable through data remanence in the hardware. Data remanence can occur because of performance optimization or memory organization during 'clear' or 'erase' operations, like a design that allows the memory-organization metadata (e.g., file pointers) to be erased without erasing the actual memory content. To protect against this weakness, memory devices will often support different commands for optimized memory erase and explicit secure erase. Data remanence can also happen because of the physical properties of memory circuits in use. For example, static, random-access-memory (SRAM) and dynamic, random-access-memory (DRAM) data retention is based on the charge retained in the memory cell, which depends on factors such as power supply, refresh rates, and temperature. Other than explicit erase commands, self-encrypting, secure-memory devices can also support secure erase through cryptographic erase commands. In such designs, only the decryption keys for encrypted data stored on the device are erased. That is, the stored data are always remnant in the media after a cryptographic erase. However, only the encrypted data can be extracted. Thus, protection against data recovery in such designs relies on the strength of the encryption algorithm.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Security Hardware, Not Technology-Specific

## Common consequences
- **Confidentiality**: Modify Memory, Read Memory

## Potential mitigations
- **Architecture and Design**: Support for secure-erase commands that apply multiple cycles of overwriting memory with known patterns and of erasing actual content. Support for cryptographic erase in self-encrypting, memory devices. External, physical tools to erase memory such as ultraviolet-rays-based erase of Electrically erasable, programmable, read-only memory (EEPROM). Physical destruction of media device. This is done for repurposed or scrapped devices that are no longer in use.

## Related attack patterns (CAPEC)
- [CAPEC-150](https://capec.mitre.org/data/definitions/150.html)
- [CAPEC-37](https://capec.mitre.org/data/definitions/37.html)
- [CAPEC-545](https://capec.mitre.org/data/definitions/545.html)

## Related weaknesses
- CWE-1301 (ChildOf)
- CWE-1301 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-8575**: Firmware Data Deletion Vulnerability in which a base station factory reset might not delete all user information. The impact of this enables a new owner of a used device that has been "factory-default reset" with a vulnerable firmware version can still retrieve, at least, the previous owner's wireless network name, and the previous owner's wireless security (such as WPA2) key. This issue was addressed with improved, data deletion.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1330.html
