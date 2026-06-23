---
capec_id: CAPEC-402
name: Bypassing ATA Password Security
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: [CWE-285]
related_attack: []
url: https://capec.mitre.org/data/definitions/402.html
tags: [mitre-capec, attack-pattern, CAPEC-402]
---

# CAPEC-402 - Bypassing ATA Password Security

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-402](https://capec.mitre.org/data/definitions/402.html)

## Description
An adversary exploits a weakness in ATA security on a drive to gain access to the information the drive contains without supplying the proper credentials. ATA Security is often employed to protect hard disk information from unauthorized access. The mechanism requires the user to type in a password before the BIOS is allowed access to drive contents. Some implementations of ATA security will accept the ATA command to update the password without the user having authenticated with the BIOS. This occurs because the security mechanism assumes the user has first authenticated via the BIOS prior to sending commands to the drive. Various methods exist for exploiting this flaw, the most common being installing the ATA protected drive into a system lacking ATA security features (a.k.a. hot swapping). Once the drive is installed into the new system the BIOS can be used to reset the drive password.

## Prerequisites
- Access to the system containing the ATA Drive so that the drive can be physically removed from the system.

## Mitigations
- Avoid using ATA password security when possible.
- Use full disk encryption to protect the entire contents of the drive or sensitive partitions on the drive.
- Leverage third-party utilities that interface with self-encrypting drives (SEDs) to provide authentication, while relying on the SED itself for data encryption.

## Related weaknesses (CWE)
- [CWE-285](https://cwe.mitre.org/data/definitions/285.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/402.html
