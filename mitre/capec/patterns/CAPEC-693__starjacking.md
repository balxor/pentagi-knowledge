---
capec_id: CAPEC-693
name: StarJacking
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-494]
related_attack: []
url: https://capec.mitre.org/data/definitions/693.html
tags: [mitre-capec, attack-pattern, CAPEC-693]
---

# CAPEC-693 - StarJacking

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-693](https://capec.mitre.org/data/definitions/693.html)

## Description
<xhtml:p>An adversary spoofs software popularity metadata to deceive users into believing that a maliciously provided package is widely used and originates from a trusted source.</xhtml:p>

## Extended description
Many open-source software packages are hosted via third-party package managers (e.g., Node Package Manager, PyPi, Yarn, etc.) that allow for easy integration of software components into existing development environments. A package manager will typically include various metadata about the software and often include a link to the package's source code repository, to assist developers in determining the trustworthiness of the software. One common statistic used in this decision-making process is the popularity of the package. This entails checking the amount of "Stars" the package has received, which the package manager displays based on the provided source code repository URL. However, many package managers do not validate the connection between the package and source code repository being provided. Adversaries can thus spoof the popularity statistic of a malicious package by associating a popular source code repository URL with the package. This can ultimately trick developers into unintentionally incorporating the malicious package into their development environment.

## Prerequisites
- Identification of a popular open-source package whose popularity metadata is to be used for the malicious package.

## Skills required
- **Low**: Ability to provide a package to a package manager and associate a popular package's source code repository URL.

## Consequences
- **Access_Control**: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges
- **Accountability**: Hide Activities
- **Authorization**: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Identify target: The adversary must first identify a target package whose popularity statistics will be leveraged. This will be a popular and widely used package, as to increase the perceived pedigree of the malicious package. Experiment Spoof package popularity: The adversary provides their malicious package to a package manager and uses the source code repository URL identified in Step 1 to spoof the popularity of the package. This malicious package may also closely resemble the legitimate package whose statistics are being utilized. Exploit Exploit victims: The adversary infiltrates development environments with the goal of conducting additional attacks. Techniques Active: The adversary attempts to trick victims into downloading the malicious package by means such as phishing and social engineering. Passive: The adversary waits for victims to download and leverage the malicious package.

## Mitigations
- Before downloading open-source packages, perform precursory metadata checks to determine the author(s), frequency of updates, when the software was last updated, and if the software is widely leveraged.
- Look for conflicting or non-unique repository references to determine if multiple packages share the same repository reference.
- Reference vulnerability databases to determine if the software contains known vulnerabilities.
- Only download open-source packages from reputable package managers.
- After downloading open-source packages, ensure integrity values have not changed.
- Before executing or incorporating the package, leverage automated testing techniques (e.g., static and dynamic analysis) to determine if the software behaves maliciously.

## Related weaknesses (CWE)
- [CWE-494](https://cwe.mitre.org/data/definitions/494.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/693.html
