---
capec_id: CAPEC-471
name: Search Order Hijacking
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-427]
related_attack: [T1574.001, T1574.004, T1574.008]
url: https://capec.mitre.org/data/definitions/471.html
tags: [mitre-capec, attack-pattern, CAPEC-471]
---

# CAPEC-471 - Search Order Hijacking

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-471](https://capec.mitre.org/data/definitions/471.html)

## Description
An adversary exploits a weakness in an application's specification of external libraries to exploit the functionality of the loader where the process loading the library searches first in the same directory in which the process binary resides and then in other directories. Exploitation of this preferential search order can allow an attacker to make the loading process load the adversary's rogue library rather than the legitimate library. This attack can be leveraged with many different libraries and with many different loading processes. No forensic trails are left in the system's registry or file system that an incorrect library had been loaded.

## Prerequisites
- Attacker has a mechanism to place its malicious libraries in the needed location on the file system.

## Skills required
- **Medium**: Ability to create a malicious library.

## Execution flow
Execution Flow Explore Identify target general susceptibility: An attacker uses an automated tool or manually finds whether the target application uses dynamically linked libraries and the configuration file or look up table (such as Procedure Linkage Table) which contains the entries for dynamically linked libraries. Techniques The attacker uses a tool such as the OSX "otool" utility or manually probes whether the target application uses dynamically linked libraries. The attacker finds the configuration files containing the entries to the dynamically linked libraries and modifies the entries to point to the malicious libraries the attacker crafted. Experiment Craft malicious libraries: The attacker uses knowledge gained in the Explore phase to craft malicious libraries that they will redirect the target to leverage. These malicious libraries could have the same APIs as the legitimate library and additional malicious code. Techniques The attacker monitors the file operations performed by the target application using a tool like dtrace or FileMon. And the attacker can delay the operations by using "sleep(2)" and "usleep()" to prepare the appropriate conditions for the attack, or make the application perform expansive tasks (large files parsing, etc.) depending on the purpose of the application. Exploit Redirect the access to libraries to the malicious libraries: The attacker redirects the target to the malicious libraries they crafted in the Experiment phase. The attacker will be able to force the targeted application to execute arbitrary code when the application attempts to access the legitimate libraries. Techniques The attacker modifies the entries in the configuration files pointing to the malicious libraries they crafted. The attacker leverages symlink/timing issues to redirect the target to access the malicious libraries they crafted. See also: CAPEC-132. The attacker leverages file search path order issues to redirect the target to access the malicious libraries they crafted. See also: CAPEC-38.

## Mitigations
- Design: Fix the Windows loading process to eliminate the preferential search order by looking for DLLs in the precise location where they are expected
- Design: Sign system DLLs so that unauthorized DLLs can be detected.

## Related weaknesses (CWE)
- [CWE-427](https://cwe.mitre.org/data/definitions/427.html)

## Related ATT&CK techniques
- T1574.001
- T1574.004
- T1574.008

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/471.html
