---
cwe_id: CWE-15
name: External Control of System or Configuration Setting
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Technology-Specific, ICS/OT]
related_capec: [CAPEC-13, CAPEC-146, CAPEC-176, CAPEC-203, CAPEC-270, CAPEC-271, CAPEC-579, CAPEC-69, CAPEC-76, CAPEC-77]
url: https://cwe.mitre.org/data/definitions/15.html
tags: [mitre-cwe, weakness, CWE-15]
---

# CWE-15 - External Control of System or Configuration Setting

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-15](https://cwe.mitre.org/data/definitions/15.html)

## Description
One or more system settings or configuration elements can be externally controlled by a user.

## Extended description
Allowing external control of system settings can disrupt service or cause an application to behave in unexpected, and potentially malicious ways.

## Applicable platforms / languages
Not Technology-Specific, ICS/OT

## Common consequences
- **Other**: Varies by Context

## Potential mitigations
- **Architecture and Design**: Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.
- **Implementation, Architecture and Design**: Because setting manipulation covers a diverse set of functions, any attempt at illustrating it will inevitably be incomplete. Rather than searching for a tight-knit relationship between the functions addressed in the setting manipulation category, take a step back and consider the sorts of system values that an attacker should not be allowed to control.
- **Implementation, Architecture and Design**: In general, do not allow user-provided or otherwise untrusted data to control sensitive values. The leverage that an attacker gains by controlling these values is not always immediately obvious, but do not underestimate the creativity of the attacker.

## Related attack patterns (CAPEC)
- [CAPEC-13](https://capec.mitre.org/data/definitions/13.html)
- [CAPEC-146](https://capec.mitre.org/data/definitions/146.html)
- [CAPEC-176](https://capec.mitre.org/data/definitions/176.html)
- [CAPEC-203](https://capec.mitre.org/data/definitions/203.html)
- [CAPEC-270](https://capec.mitre.org/data/definitions/270.html)
- [CAPEC-271](https://capec.mitre.org/data/definitions/271.html)
- [CAPEC-579](https://capec.mitre.org/data/definitions/579.html)
- [CAPEC-69](https://capec.mitre.org/data/definitions/69.html)
- [CAPEC-76](https://capec.mitre.org/data/definitions/76.html)
- [CAPEC-77](https://capec.mitre.org/data/definitions/77.html)

## Related weaknesses
- CWE-642 (ChildOf)
- CWE-610 (ChildOf)
- CWE-20 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/15.html
