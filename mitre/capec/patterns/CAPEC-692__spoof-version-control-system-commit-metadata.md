---
capec_id: CAPEC-692
name: Spoof Version Control System Commit Metadata
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-494]
related_attack: []
url: https://capec.mitre.org/data/definitions/692.html
tags: [mitre-capec, attack-pattern, CAPEC-692]
---

# CAPEC-692 - Spoof Version Control System Commit Metadata

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-692](https://capec.mitre.org/data/definitions/692.html)

## Description
<xhtml:p>An adversary spoofs metadata pertaining to a Version Control System (VCS) (e.g., Git) repository's commits to deceive users into believing that the maliciously provided software is frequently maintained and originates from a trusted source.</xhtml:p>

## Extended description
Version Control Systems are widely used by developers to host, track, and manage source code files in an easy and synchronous manner. These systems are often leveraged to host open-source software that other developers can incorporate into their own applications or use as standalone applications. To prevent downloading vulnerable and/or malicious code, developers will often check the metadata of VCS repository commits to determine the repository's overall pedigree. This may include a variety of information, such as the following: Owner of the repository Author(s) of commits Frequency of commits Date/Time of commits Repository activity graphs These precursory checks can assist developers in determining whether a trusted individual/organization is providing the source code, how often the code is updated, and the relative popularity of the software. However, an adversary can spoof this metadata to make a repository containing malicious code appear as originating from a trusted source, being frequently maintained, and being commonly used by other developers. Without performing additional security activities, unassuming developers may be duped by this spoofed metadata and include the malicious code within their systems/applications. The adversary is then ultimately able to achieve numerous negative technical impacts, while the victim remains unaware of any malicious activity.

## Prerequisites
- Identification of a popular open-source repository whose metadata is to be spoofed.

## Skills required
- **Medium**: Ability to spoof a variety of repository metadata to convince victims the source is trusted.

## Consequences
- **Access_Control**: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges
- **Accountability**: Hide Activities
- **Authorization**: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Identify target: The adversary must first identify a target repository for them to spoof. Typically, this will be a popular and widely used repository, as to increase the amount of victims a successful attack will exploit. Experiment Create malicious repository: The adversary must create a malicious repository that imitates the legitimate repository being spoofed. This may include creating a username that closely matches the legitimate repository owner; creating a repository name that closely matches the legitimate repository name; uploading the legitimate source code; and more. Spoof commit metadata: Once the malicious repository has been created, the adversary must then spoof the commit metadata to make the repository appear to be frequently maintained and originating from trusted sources. Techniques Git Commit Timestamps: The adversary generates numerous fake commits while setting the "GIT_AUTHOR_DATE" and "GIT_COMMITTER_DATE" environment variables to a date which is to be spoofed. Git Commit Contributors: The adversary obtains a legitimate and trusted user's email address and then sets this information via the "git config" command. The adversary can then commit changes leveraging this username. Exploit Exploit victims: The adversary infiltrates software and/or system environments with the goal of conducting additional attacks. Techniques Active: The adversary attempts to trick victims into downloading the malicious software by means such as phishing and social engineering. Passive: The adversary waits for victims to download and leverage malicious software.

## Mitigations
- Before downloading open-source software, perform precursory metadata checks to determine the author(s), frequency of updates, when the software was last updated, and if the software is widely leveraged.
- Reference vulnerability databases to determine if the software contains known vulnerabilities.
- Only download open-source software from reputable hosting sites or package managers.
- Only download open-source software that has been adequately signed by the developer(s). For repository commits/tags, look for the "Verified" status and for developers leveraging "Vigilant Mode" (GitHub) or similar modes.
- After downloading open-source software, ensure integrity values have not changed.
- Before executing or incorporating the software, leverage automated testing techniques (e.g., static and dynamic analysis) to determine if the software behaves maliciously.

## Related weaknesses (CWE)
- [CWE-494](https://cwe.mitre.org/data/definitions/494.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/692.html
