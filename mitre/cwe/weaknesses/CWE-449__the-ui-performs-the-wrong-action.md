---
cwe_id: CWE-449
name: The UI Performs the Wrong Action
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/449.html
tags: [mitre-cwe, weakness, CWE-449]
---

# CWE-449 - The UI Performs the Wrong Action

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-449](https://cwe.mitre.org/data/definitions/449.html)

## Description
The UI performs the wrong action with respect to the user's request.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Quality Degradation, Varies by Context

## Related weaknesses
- CWE-446 (ChildOf)

## Observed examples (CVE)
- **CVE-2001-1387**: Network firewall accidentally implements one command line option as if it were another, possibly leading to behavioral infoleak.
- **CVE-2001-0081**: Command line option correctly suppresses a user prompt but does not properly disable a feature, although when the product prompts the user, the feature is properly disabled.
- **CVE-2002-1977**: Product does not "time out" according to user specification, leaving sensitive data available after it has expired.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/449.html
