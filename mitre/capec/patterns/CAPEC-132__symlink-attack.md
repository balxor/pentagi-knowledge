---
capec_id: CAPEC-132
name: Symlink Attack
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: [CWE-59]
related_attack: [T1547.009]
url: https://capec.mitre.org/data/definitions/132.html
tags: [mitre-capec, attack-pattern, CAPEC-132]
---

# CAPEC-132 - Symlink Attack

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-132](https://capec.mitre.org/data/definitions/132.html)

## Description
An adversary positions a symbolic link in such a manner that the targeted user or application accesses the link's endpoint, assuming that it is accessing a file with the link's name.

## Extended description
The endpoint file may be either output or input. If the file is output, the result is that the endpoint is modified, instead of a file at the intended location. Modifications to the endpoint file may include appending, overwriting, corrupting, changing permissions, or other modifications. In some variants of this attack the adversary may be able to control the change to a file while in other cases they cannot. The former is especially damaging since the adversary may be able to grant themselves increased privileges or insert false information, but the latter can also be damaging as it can expose sensitive information or corrupt or destroy vital system or application files. Alternatively, the endpoint file may serve as input to the targeted application. This can be used to feed malformed input into the target or to cause the target to process different information, possibly allowing the adversary to control the actions of the target or to cause the target to expose information to the adversary. Moreover, the actions taken on the endpoint file are undertaken with the permissions of the targeted user or application, which may exceed the permissions that the adversary would normally have.

## Prerequisites
- The targeted application must perform the desired activities on a file without checking whether the file is a symbolic link or not. The adversary must be able to predict the name of the file the target application is modifying and be able to create a new symbolic link where that file would appear.

## Skills required
- **High**: To identify the files and create the symlinks during the file operation time window
- **Low**: To create symlinks

## Resources required
- None: No specialized resources are required to execute this type of attack. The only requirement is the ability to create the necessary symbolic link.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Accountability**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges, Bypass Protection Mechanism
- **Availability**: Unreliable Execution
- **Confidentiality**: Other (Information Leakage), Read Data
- **Integrity**: Modify Data, Modify Data
- **Non-Repudiation**: Gain Privileges

## Execution flow
Execution Flow Explore Identify Target: Adversary identifies the target application by determining whether there is sufficient check before writing data to a file and creating symlinks to files in different directories. Techniques The adversary writes to files in different directories to check whether the application has sufficient checking before file operations. The adversary creates symlinks to files in different directories. Experiment Try to create symlinks to different files: The adversary then uses a variety of techniques, such as monitoring or guessing to create symlinks to the files accessed by the target application in the directories which are identified in the explore phase. Techniques The adversary monitors the file operations performed by the target application using a tool like dtrace or FileMon. And the adversary can delay the operations by using "sleep(2)" and "usleep()" to prepare the appropriate conditions for the attack, or make the application perform expansive tasks (large files parsing, etc.) depending on the purpose of the application. The adversary may need a little guesswork on the filenames on which the target application would operate. The adversary tries to create symlinks to the various filenames. Exploit Target application operates on created symlinks to sensitive files: The adversary is able to create symlinks to sensitive files while the target application is operating on the file. Techniques Create the symlink to the sensitive file such as configuration files, etc.

## Mitigations
- Design: Check for the existence of files to be created, if in existence verify they are neither symlinks nor hard links before opening them.
- Implementation: Use randomly generated file names for temporary files. Give the files restrictive permissions.

## Related weaknesses (CWE)
- [CWE-59](https://cwe.mitre.org/data/definitions/59.html)

## Related ATT&CK techniques
- T1547.009

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/132.html
