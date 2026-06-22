---
attack_id: T0849
name: Masquerading
type: technique
parent: null
tactics: [Evasion]
platforms: [None]
url: https://attack.mitre.org/techniques/T0849
tags: [mitre-attack, technique, T0849]
---

# T0849 - Masquerading

**Tactic(s):** Evasion  -  **Platforms:** None  -  **ATT&CK:** [T0849](https://attack.mitre.org/techniques/T0849)

## Summary
Adversaries may use masquerading to disguise a malicious application or executable as another file, to avoid operator and engineer suspicion. Possible disguises of these masquerading files can include commonly found programs, expected vendor executables and configuration files, and other commonplace application and naming conventions. By impersonating expected and vendor-relevant files and applications, operators and engineers may not notice the presence of the underlying malicious content and possibly end up running those masquerading as legitimate functions. 

Applications and other files commonly found on Windows systems or in engineering workstations have been impersonated before. This can be as simple as renaming a file to effectively disguise it in the ICS environment.

## Role in the attack flow
Used to achieve the **Evasion** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0945 Code Signing** - Enforce binary and application integrity with digital signature verification to prevent untrusted code from executing.
- **M0938 Execution Prevention** - Block execution of code on a system through application control, and/or script blocking.
- **M0922 Restrict File and Directory Permissions** - Restrict access by setting directory and file permissions that are not specific to users or privileged accounts.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0849
