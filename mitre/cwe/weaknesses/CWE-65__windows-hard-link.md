---
cwe_id: CWE-65
name: Windows Hard Link
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Windows, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/65.html
tags: [mitre-cwe, weakness, CWE-65]
---

# CWE-65 - Windows Hard Link

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-65](https://cwe.mitre.org/data/definitions/65.html)

## Description
The product, when opening a file or directory, does not sufficiently handle when the name is associated with a hard link to a target that is outside of the intended control sphere. This could allow an attacker to cause the product to operate on unauthorized files.

## Extended description
Failure for a system to check for hard links can result in vulnerability to different types of attacks. For example, an attacker can escalate their privileges if a file used by a privileged program is replaced with a hard link to a sensitive file (e.g. AUTOEXEC.BAT). When the process opens the file, the attacker can assume the privileges of that process, or prevent the program from accurately processing data.

## Applicable platforms / languages
Not Language-Specific, Windows, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Potential mitigations
- **Architecture and Design**: Follow the principle of least privilege when assigning access rights to entities in a software system. Denying access to a file can prevent an attacker from replacing that file with a link to a sensitive file. Ensure good compartmentalization in the system to provide protected areas that can be trusted.

## Related weaknesses
- CWE-59 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-0725**: File system allows local attackers to hide file usage activities via a hard link to the target file, which causes the link to be recorded in the audit trail instead of the target file.
- **CVE-2003-0844**: Web server plugin allows local users to overwrite arbitrary files via a symlink attack on predictable temporary filenames.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/65.html
