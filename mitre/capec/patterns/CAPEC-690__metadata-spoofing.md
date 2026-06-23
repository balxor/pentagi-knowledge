---
capec_id: CAPEC-690
name: Metadata Spoofing
type: attack-pattern
abstraction: Meta
likelihood: Medium
severity: High
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/690.html
tags: [mitre-capec, attack-pattern, CAPEC-690]
---

# CAPEC-690 - Metadata Spoofing

**Abstraction:** Meta  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-690](https://capec.mitre.org/data/definitions/690.html)

## Description
<xhtml:p>An adversary alters the metadata of a resource (e.g., file, directory, repository, etc.) to present a malicious resource as legitimate/credible.</xhtml:p>

## Extended description
One approach to this attack entails the adversary altering a maliciously modified resource's metadata in order to hide their malicious activity. Another approach involves altering the metadata of an adversary-created resource to make the source appear more credible. Adversaries may spoof a variety of metadata across a number of resources, such as the following: Authors of Version Control System (VCS) repository commits Open source package statistics File attributes, such as when a file was last update The ultimate goal of a Metadata Spoofing attack is to trick victims into believing the malicious resource being provided originates from a reputable source. However, the victim instead leverages the malicious resource, which could result in a number of negative technical impacts.

## Prerequisites
- Identification of a resource whose metadata is to be spoofed

## Skills required
- **Medium**: Ability to spoof a variety of metadata to convince victims the source is trusted

## Consequences
- **Access_Control**: Execute Unauthorized Commands
- **Accountability**: Hide Activities
- **Authorization**: Execute Unauthorized Commands
- **Integrity**: Modify Data

## Mitigations
- Validate metadata of resources such as authors, timestamps, and statistics.
- Confirm the pedigree of open source packages and ensure the code being downloaded does not originate from another source.
- Even if the metadata is properly checked and a user believes it to be legitimate, there may still be a chance that they've been duped. Therefore, leverage automated testing techniques to determine where malicious areas of the code may exist.

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/690.html
