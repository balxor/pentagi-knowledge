---
capec_id: CAPEC-691
name: Spoof Open-Source Software Metadata
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: High
related_cwe: [CWE-494]
related_attack: [T1195.001, T1195.002]
url: https://capec.mitre.org/data/definitions/691.html
tags: [mitre-capec, attack-pattern, CAPEC-691]
---

# CAPEC-691 - Spoof Open-Source Software Metadata

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-691](https://capec.mitre.org/data/definitions/691.html)

## Description
<xhtml:p>An adversary spoofs open-source software metadata in an attempt to masquerade malicious software as popular, maintained, and trusted.</xhtml:p>

## Extended description
Due to open-source software's popularity, it serves as a desirable attack-vector for adversaries since a single malicious component may result in the exploitation of numerous systems/applications. Adversaries may, therefore, spoof the metadata pertaining to the open-source software in order to trick victims into downloading and using their malicious software. Examples of metadata that may be spoofed include: Owner of the software (e.g., repository or package owner) Author(s) of repository commits Frequency of repository commits Date/Time of repository commits Package or Repository "stars" Once the malicious software component has been integrated into an underlying application or executed on a system, the adversary is ultimately able to achieve numerous negative technical impacts within the system/application. This often occurs without any indication of compromise.

## Prerequisites
- Identification of a popular open-source component whose metadata is to be spoofed.

## Skills required
- **Medium**: Ability to spoof a variety of software metadata to convince victims the source is trusted.

## Consequences
- **Access_Control**: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges
- **Accountability**: Hide Activities
- **Authorization**: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges
- **Integrity**: Modify Data

## Mitigations
- Before downloading open-source software, perform precursory metadata checks to determine the author(s), frequency of updates, when the software was last updated, and if the software is widely leveraged.
- Within package managers, look for conflicting or non-unique repository references to determine if multiple packages share the same repository reference.
- Reference vulnerability databases to determine if the software contains known vulnerabilities.
- Only download open-source software from reputable hosting sites or package managers.
- Only download open-source software that has been adequately signed by the developer(s). For repository commits/tags, look for the "Verified" status and for developers leveraging "Vigilant Mode" (GitHub) or similar modes.
- After downloading open-source software, ensure integrity values have not changed.
- Before executing or incorporating the software, leverage automated testing techniques (e.g., static and dynamic analysis) to determine if the software behaves maliciously.

## Related weaknesses (CWE)
- [CWE-494](https://cwe.mitre.org/data/definitions/494.html)

## Related ATT&CK techniques
- T1195.001
- T1195.002

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/691.html
