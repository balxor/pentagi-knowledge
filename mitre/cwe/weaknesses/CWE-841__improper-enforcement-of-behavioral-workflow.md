---
cwe_id: CWE-841
name: Improper Enforcement of Behavioral Workflow
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/841.html
tags: [mitre-cwe, weakness, CWE-841]
---

# CWE-841 - Improper Enforcement of Behavioral Workflow

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-841](https://cwe.mitre.org/data/definitions/841.html)

## Description
The product supports a session in which more than one behavior must be performed by an actor, but it does not properly ensure that the actor performs the behaviors in the required sequence.

## Extended description
By performing actions in an unexpected order, or by omitting steps, an attacker could manipulate the business logic of the product or cause it to enter an invalid state. In some cases, this can also expose resultant weaknesses. For example, a file-sharing protocol might require that an actor perform separate steps to provide a username, then a password, before being able to transfer files. If the file-sharing server accepts a password command followed by a transfer command, without any username being provided, the product might still perform the transfer. Note that this is different than CWE-696, which focuses on when the product performs actions in the wrong sequence; this entry is closely related, but it is focused on ensuring that the actor performs actions in the correct sequence. Workflow-related behaviors include: Steps are performed in the expected order. Required steps are not omitted. Steps are not interrupted. Steps are performed in a timely fashion.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Alter Execution Logic

## Related weaknesses
- CWE-691 (ChildOf)

## Observed examples (CVE)
- **CVE-2011-0348**: Bypass of access/billing restrictions by sending traffic to an unrestricted destination before sending to a restricted destination.
- **CVE-2007-3012**: Attacker can access portions of a restricted page by canceling out of a dialog.
- **CVE-2009-5056**: Ticket-tracking system does not enforce a permission setting.
- **CVE-2004-2164**: Shopping cart does not close a database connection when user restores a previous order, leading to connection exhaustion.
- **CVE-2003-0777**: Chain: product does not properly handle dropped connections, leading to missing NULL terminator (CWE-170) and segmentation fault.
- **CVE-2005-3327**: Chain: Authentication bypass by skipping the first startup step as required by the protocol.
- **CVE-2004-0829**: Chain: File server crashes when sent a "find next" request without an initial "find first."
- **CVE-2010-2620**: FTP server allows remote attackers to bypass authentication by sending (1) LIST, (2) RETR, (3) STOR, or other commands without performing the required login steps first.
- **CVE-2005-3296**: FTP server allows remote attackers to list arbitrary directories as root by running the LIST command before logging in.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/841.html
