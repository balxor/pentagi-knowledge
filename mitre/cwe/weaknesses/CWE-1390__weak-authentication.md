---
cwe_id: CWE-1390
name: Weak Authentication
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, ICS/OT, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1390.html
tags: [mitre-cwe, weakness, CWE-1390]
---

# CWE-1390 - Weak Authentication

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-1390](https://cwe.mitre.org/data/definitions/1390.html)

## Description
The product uses an authentication mechanism to restrict access to specific users or identities, but the mechanism does not sufficiently prove that the claimed identity is correct.

## Extended description
Attackers may be able to bypass weak authentication faster and/or with less effort than expected.

## Applicable platforms / languages
Not Language-Specific, ICS/OT, Not Technology-Specific

## Common consequences
- **Integrity, Confidentiality, Availability, Access Control**: Read Application Data, Gain Privileges or Assume Identity, Execute Unauthorized Code or Commands

## Related weaknesses
- CWE-287 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-48445**: Chain: e-commerce app relies on an easily-guessable timestamp (CWE-341) in a weak authentication algorithm (CWE-1390)
- **CVE-2022-30034**: Chain: Web UI for a Python RPC framework does not use regex anchors to validate user login emails (CWE-777), potentially allowing bypass of OAuth (CWE-1390).
- **CVE-2022-35248**: Chat application skips validation when Central Authentication Service (CAS) is enabled, effectively removing the second factor from two-factor authentication
- **CVE-2021-3116**: Chain: Python-based HTTP Proxy server uses the wrong boolean operators (CWE-480) causing an incorrect comparison (CWE-697) that identifies an authN failure if all three conditions are met instead of only one, allowing bypass of the proxy authentication (CWE-1390)
- **CVE-2022-29965**: Distributed Control System (DCS) uses a deterministic algorithm to generate utility passwords
- **CVE-2022-29959**: Initialization file contains credentials that can be decoded using a "simple string transformation"
- **CVE-2020-8994**: UART interface for AI speaker uses empty password for root shell

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1390.html
