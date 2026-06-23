---
cwe_id: CWE-842
name: Placement of User into Incorrect Group
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/842.html
tags: [mitre-cwe, weakness, CWE-842]
---

# CWE-842 - Placement of User into Incorrect Group

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-842](https://cwe.mitre.org/data/definitions/842.html)

## Description
The product or the administrator places a user into an incorrect group.

## Extended description
If the incorrect group has more access or privileges than the intended group, the user might be able to bypass intended security policy to access unexpected resources or perform unexpected actions. The access-control system might not be able to detect malicious usage of this group membership.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Related weaknesses
- CWE-286 (ChildOf)

## Observed examples (CVE)
- **CVE-1999-1193**: Operating system assigns user to privileged wheel group, allowing the user to gain root privileges.
- **CVE-2010-3716**: Chain: drafted web request allows the creation of users with arbitrary group membership.
- **CVE-2008-5397**: Chain: improper processing of configuration options causes users to contain unintended group memberships.
- **CVE-2007-6644**: CMS does not prevent remote administrators from promoting other users to the administrator group, in violation of the intended security model.
- **CVE-2007-3260**: Product assigns members to the root group, allowing escalation of privileges.
- **CVE-2002-0080**: Chain: daemon does not properly clear groups before dropping privileges.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/842.html
