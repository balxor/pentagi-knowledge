---
capec_id: CAPEC-579
name: Replace Winlogon Helper DLL
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: [CWE-15]
related_attack: [T1547.004]
url: https://capec.mitre.org/data/definitions/579.html
tags: [mitre-capec, attack-pattern, CAPEC-579]
---

# CAPEC-579 - Replace Winlogon Helper DLL

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-579](https://capec.mitre.org/data/definitions/579.html)

## Description
Winlogon is a part of Windows that performs logon actions. In Windows systems prior to Windows Vista, a registry key can be modified that causes Winlogon to load a DLL on startup. Adversaries may take advantage of this feature to load adversarial code at startup.

## Mitigations
- Changes to registry entries in "HKLM\Software\Microsoft\Windows NT\Winlogon\Notify" that do not correlate with known software, patch cycles, etc are suspicious. New DLLs written to System32 which do not correlate with known good software or patching may be suspicious.

## Related weaknesses (CWE)
- [CWE-15](https://cwe.mitre.org/data/definitions/15.html)

## Related ATT&CK techniques
- T1547.004

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/579.html
