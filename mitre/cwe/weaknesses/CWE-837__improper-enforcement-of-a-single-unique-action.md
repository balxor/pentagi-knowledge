---
cwe_id: CWE-837
name: Improper Enforcement of a Single, Unique Action
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/837.html
tags: [mitre-cwe, weakness, CWE-837]
---

# CWE-837 - Improper Enforcement of a Single, Unique Action

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-837](https://cwe.mitre.org/data/definitions/837.html)

## Description
The product requires that an actor should only be able to perform an action once, or to have only one unique action, but the product does not enforce or improperly enforces this restriction.

## Extended description
In various applications, a user is only expected to perform a certain action once, such as voting, requesting a refund, or making a purchase. When this restriction is not enforced, sometimes this can have security implications. For example, in a voting application, an attacker could attempt to "stuff the ballot box" by voting multiple times. If these votes are counted separately, then the attacker could directly affect who wins the vote. This could have significant business impact depending on the purpose of the product.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based, Web Server

## Common consequences
- **Other**: Varies by Context

## Related weaknesses
- CWE-799 (ChildOf)

## Observed examples (CVE)
- **CVE-2008-0294**: Ticket-booking web application allows a user to lock a seat more than once.
- **CVE-2005-4051**: CMS allows people to rate downloads by voting more than once.
- **CVE-2002-216**: Polling software allows people to vote more than once by setting a cookie.
- **CVE-2003-1433**: Chain: lack of validation of a challenge key in a game allows a player to register multiple times and lock other players out of the game.
- **CVE-2002-1018**: Library feature allows attackers to check out the same e-book multiple times, preventing other users from accessing copies of the e-book.
- **CVE-2009-2346**: Protocol implementation allows remote attackers to cause a denial of service (call-number exhaustion) by initiating many message exchanges.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/837.html
