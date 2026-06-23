---
cwe_id: CWE-1268
name: Policy Privileges are not Assigned Consistently Between Control and Data Agents
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-180]
url: https://cwe.mitre.org/data/definitions/1268.html
tags: [mitre-cwe, weakness, CWE-1268]
---

# CWE-1268 - Policy Privileges are not Assigned Consistently Between Control and Data Agents

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1268](https://cwe.mitre.org/data/definitions/1268.html)

## Description
The product's hardware-enforced access control for a particular resource improperly accounts for privilege discrepancies between control and write policies.

## Extended description
Integrated circuits and hardware engines may provide access to resources (device-configuration, encryption keys, etc.) belonging to trusted firmware or software modules (commonly set by a BIOS or a bootloader). These accesses are typically controlled and limited by the hardware. Hardware design access control is sometimes implemented using a policy. A policy defines which entity or agent may or may not be allowed to perform an action. When a system implements multiple levels of policies, a control policy may allow direct access to a resource as well as changes to the policies themselves. Resources that include agents in their control policy but not in their write policy could unintentionally allow an untrusted agent to insert itself in the write policy register. Inclusion in the write policy register could allow a malicious or misbehaving agent write access to resources. This action could result in security compromises including leaked information, leaked encryption keys, or modification of device configuration.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Availability, Access Control**: Modify Memory, Read Memory, DoS: Crash, Exit, or Restart, Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity, Bypass Protection Mechanism, Read Files or Directories, Reduce Reliability

## Potential mitigations
- **Architecture and Design, Implementation**: Access-control-policy definition and programming flow must be sufficiently tested in pre-silicon and post-silicon testing.

## Related attack patterns (CAPEC)
- [CAPEC-180](https://capec.mitre.org/data/definitions/180.html)

## Related weaknesses
- CWE-266 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1268.html
