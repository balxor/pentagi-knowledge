---
cwe_id: CWE-269
name: Improper Privilege Management
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-122, CAPEC-233, CAPEC-58]
url: https://cwe.mitre.org/data/definitions/269.html
tags: [mitre-cwe, weakness, CWE-269]
---

# CWE-269 - Improper Privilege Management

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-269](https://cwe.mitre.org/data/definitions/269.html)

## Description
The product does not properly assign, modify, track, or check privileges for an actor, creating an unintended sphere of control for that actor.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design, Operation**: Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.
- **Architecture and Design**: Follow the principle of least privilege when assigning access rights to entities in a software system.
- **Architecture and Design**: Consider following the principle of separation of privilege. Require multiple conditions to be met before permitting access to a system resource.

## Related attack patterns (CAPEC)
- [CAPEC-122](https://capec.mitre.org/data/definitions/122.html)
- [CAPEC-233](https://capec.mitre.org/data/definitions/233.html)
- [CAPEC-58](https://capec.mitre.org/data/definitions/58.html)

## Related weaknesses
- CWE-284 (ChildOf)

## Observed examples (CVE)
- **CVE-2001-1555**: Terminal privileges are not reset when a user logs out.
- **CVE-2001-1514**: Does not properly pass security context to child processes in certain cases, allows privilege escalation.
- **CVE-2001-0128**: Does not properly compute roles.
- **CVE-1999-1193**: untrusted user placed in unix "wheel" group
- **CVE-2005-2741**: Product allows users to grant themselves certain rights that can be used to escalate privileges.
- **CVE-2005-2496**: Product uses group ID of a user instead of the group, causing it to run with different privileges. This is resultant from some other unknown issue.
- **CVE-2004-0274**: Product mistakenly assigns a particular status to an entity, leading to increased privileges.
- **CVE-2007-4217**: FTP client program on a certain OS runs with setuid privileges and has a buffer overflow. Most clients do not need extra privileges, so an overflow is not a vulnerability for those clients.
- **CVE-2007-5159**: OS incorrectly installs a program with setuid privileges, allowing users to gain privileges.
- **CVE-2008-4638**: Composite: application running with high privileges (CWE-250) allows user to specify a restricted file to process, which generates a parsing error that leaks the contents of the file (CWE-209).
- **CVE-2007-3931**: Installation script installs some programs as setuid when they shouldn't be.
- **CVE-2002-1981**: Roles have access to dangerous procedures (Accessible entities).
- **CVE-2002-1671**: Untrusted object/method gets access to clipboard (Accessible entities).
- **CVE-2000-0315**: Traceroute program allows unprivileged users to modify source address of packet (Accessible entities).
- **CVE-2000-0506**: User with capability can prevent setuid program from dropping privileges (Unsafe privileged actions).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/269.html
