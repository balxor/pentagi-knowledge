---
cwe_id: CWE-267
name: Privilege Defined With Unsafe Actions
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-58, CAPEC-634, CAPEC-637, CAPEC-643, CAPEC-648]
url: https://cwe.mitre.org/data/definitions/267.html
tags: [mitre-cwe, weakness, CWE-267]
---

# CWE-267 - Privilege Defined With Unsafe Actions

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-267](https://cwe.mitre.org/data/definitions/267.html)

## Description
A particular privilege, role, capability, or right can be used to perform unsafe actions that were not intended, even when it is assigned to the correct entity.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design, Operation**: Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.
- **Architecture and Design, Operation**: Run your code using the lowest privileges that are required to accomplish the necessary tasks [REF-76]. If possible, create isolated accounts with limited privileges that are only used for a single task. That way, a successful attack will not immediately give the attacker access to the rest of the software or its environment. For example, database applications rarely need to run as the database administrator, especially in day-to-day operations.

## Related attack patterns (CAPEC)
- [CAPEC-58](https://capec.mitre.org/data/definitions/58.html)
- [CAPEC-634](https://capec.mitre.org/data/definitions/634.html)
- [CAPEC-637](https://capec.mitre.org/data/definitions/637.html)
- [CAPEC-643](https://capec.mitre.org/data/definitions/643.html)
- [CAPEC-648](https://capec.mitre.org/data/definitions/648.html)

## Related weaknesses
- CWE-269 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-1981**: Roles have access to dangerous procedures (Accessible entities).
- **CVE-2002-1671**: Untrusted object/method gets access to clipboard (Accessible entities).
- **CVE-2004-2204**: Gain privileges using functions/tags that should be restricted (Accessible entities).
- **CVE-2000-0315**: Traceroute program allows unprivileged users to modify source address of packet (Accessible entities).
- **CVE-2004-0380**: Bypass domain restrictions using a particular file that references unsafe URI schemes (Accessible entities).
- **CVE-2002-1154**: Script does not restrict access to an update command, leading to resultant disk consumption and filled error logs (Accessible entities).
- **CVE-2002-1145**: "public" database user can use stored procedure to modify data controlled by the database owner (Unsafe privileged actions).
- **CVE-2000-0506**: User with capability can prevent setuid program from dropping privileges (Unsafe privileged actions).
- **CVE-2002-2042**: Allows attachment to and modification of privileged processes (Unsafe privileged actions).
- **CVE-2000-1212**: User with privilege can edit raw underlying object using unprotected method (Unsafe privileged actions).
- **CVE-2005-1742**: Inappropriate actions allowed by a particular role(Unsafe privileged actions).
- **CVE-2001-1480**: Untrusted entity allowed to access the system clipboard (Unsafe privileged actions).
- **CVE-2001-1551**: Extra Linux capability allows bypass of system-specified restriction (Unsafe privileged actions).
- **CVE-2001-1166**: User with debugging rights can read entire process (Unsafe privileged actions).
- **CVE-2005-1816**: Non-root admins can add themselves or others to the root admin group (Unsafe privileged actions).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/267.html
