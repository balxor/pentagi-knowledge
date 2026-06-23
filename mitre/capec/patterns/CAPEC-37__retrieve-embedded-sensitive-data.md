---
capec_id: CAPEC-37
name: Retrieve Embedded Sensitive Data
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Very High
related_cwe: [CWE-226, CWE-311, CWE-525, CWE-312, CWE-314, CWE-315, CWE-318, CWE-1239, CWE-1258, CWE-1266, CWE-1272, CWE-1278, CWE-1301, CWE-1330]
related_attack: [T1005, T1552.004]
url: https://capec.mitre.org/data/definitions/37.html
tags: [mitre-capec, attack-pattern, CAPEC-37]
---

# CAPEC-37 - Retrieve Embedded Sensitive Data

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-37](https://capec.mitre.org/data/definitions/37.html)

## Description
An attacker examines a target system to find sensitive data that has been embedded within it. This information can reveal confidential contents, such as account numbers or individual keys/credentials that can be used as an intermediate step in a larger attack.

## Prerequisites
- In order to feasibly execute this type of attack, some valuable data must be present in client software.
- Additionally, this information must be unprotected, or protected in a flawed fashion, or through a mechanism that fails to resist reverse engineering, statistical, or other attack.

## Skills required
- **Medium**: The attacker must possess knowledge of client code structure as well as ability to reverse-engineer or decompile it or probe it in other ways. This knowledge is specific to the technology and language used for the client distribution

## Resources required
- The attacker must possess access to the system or code being exploited. Such access, for this set of attacks, will likely be physical. The attacker will make use of reverse engineering technologies, perhaps for data or to extract functionality from the binary. Such tool use may be as simple as "Strings" or a hex editor. Removing functionality may require the use of only a hex editor, or may require aspects of the toolchain used to construct the application: for instance the Adobe Flash development environment. Attacks of this nature do not require network access or undue CPU, memory, or other hardware-based resources.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Read Data, Gain Privileges
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Identify Target: Attacker identifies client components to extract information from. These may be binary executables, class files, shared libraries (e.g., DLLs), configuration files, or other system files. Techniques Binary file extraction. The attacker extracts binary files from zips, jars, wars, PDFs or other composite formats. Package listing. The attacker uses a package manifest provided with the software installer, or the filesystem itself, to identify component files suitable for attack. Exploit Retrieve Embedded Data: The attacker then uses a variety of techniques, such as sniffing, reverse-engineering, and cryptanalysis to retrieve the information of interest. Techniques API Profiling. The attacker monitors the software's use of registry keys or other operating system-provided storage locations that can contain sensitive information. Execution in simulator. The attacker physically removes mass storage from the system and explores it using a simulator, external system, or other debugging harness. Common decoding methods. The attacker applies methods to decode such encodings and compressions as Base64, unzip, unrar, RLE decoding, gzip decompression and so on. Common data typing. The attacker looks for common file signatures for well-known file types (JPEG, TIFF, ASN.1, LDIF, etc.). If the signatures match, they attempt decoding in that format.

## Related weaknesses (CWE)
- [CWE-226](https://cwe.mitre.org/data/definitions/226.html)
- [CWE-311](https://cwe.mitre.org/data/definitions/311.html)
- [CWE-525](https://cwe.mitre.org/data/definitions/525.html)
- [CWE-312](https://cwe.mitre.org/data/definitions/312.html)
- [CWE-314](https://cwe.mitre.org/data/definitions/314.html)
- [CWE-315](https://cwe.mitre.org/data/definitions/315.html)
- [CWE-318](https://cwe.mitre.org/data/definitions/318.html)
- [CWE-1239](https://cwe.mitre.org/data/definitions/1239.html)
- [CWE-1258](https://cwe.mitre.org/data/definitions/1258.html)
- [CWE-1266](https://cwe.mitre.org/data/definitions/1266.html)
- [CWE-1272](https://cwe.mitre.org/data/definitions/1272.html)
- [CWE-1278](https://cwe.mitre.org/data/definitions/1278.html)
- [CWE-1301](https://cwe.mitre.org/data/definitions/1301.html)
- [CWE-1330](https://cwe.mitre.org/data/definitions/1330.html)

## Related ATT&CK techniques
- T1005
- T1552.004

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/37.html
