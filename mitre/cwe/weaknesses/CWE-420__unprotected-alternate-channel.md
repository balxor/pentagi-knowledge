---
cwe_id: CWE-420
name: Unprotected Alternate Channel
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/420.html
tags: [mitre-cwe, weakness, CWE-420]
---

# CWE-420 - Unprotected Alternate Channel

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-420](https://cwe.mitre.org/data/definitions/420.html)

## Description
The product protects a primary channel, but it does not use the same level of protection for an alternate channel.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity, Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: Identify all alternate channels and use the same protection mechanisms that are used for the primary channels.

## Related weaknesses
- CWE-923 (ChildOf)

## Observed examples (CVE)
- **CVE-2020-8004**: When the internal flash is protected by blocking access on the Data Bus (DBUS), it can still be indirectly accessed through the Instruction Bus (IBUS).
- **CVE-2002-0567**: DB server assumes that local clients have performed authentication, allowing attacker to directly connect to a process to load libraries and execute commands; a socket interface also exists (another alternate channel), so attack can be remote.
- **CVE-2002-1578**: Product does not restrict access to underlying database, so attacker can bypass restrictions by directly querying the database.
- **CVE-2003-1035**: User can avoid lockouts by using an API instead of the GUI to conduct brute force password guessing.
- **CVE-2002-1863**: FTP service can not be disabled even when other access controls would require it.
- **CVE-2002-0066**: Windows named pipe created without authentication/access control, allowing configuration modification.
- **CVE-2004-1461**: Router management interface spawns a separate TCP connection after authentication, allowing hijacking by attacker coming from the same IP address.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/420.html
