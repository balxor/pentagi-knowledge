---
cwe_id: CWE-368
name: Context Switching Race Condition
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-26, CAPEC-29]
url: https://cwe.mitre.org/data/definitions/368.html
tags: [mitre-cwe, weakness, CWE-368]
---

# CWE-368 - Context Switching Race Condition

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-368](https://cwe.mitre.org/data/definitions/368.html)

## Description
A product performs a series of non-atomic actions to switch between contexts that cross privilege or other security boundaries, but a race condition allows an attacker to modify or misrepresent the product's behavior during the switch.

## Extended description
This is commonly seen in web browser vulnerabilities in which the attacker can perform certain actions while the browser is transitioning from a trusted to an untrusted domain, or vice versa, and the browser performs the actions on one domain using the trust level and resources of the other domain.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Integrity, Confidentiality**: Modify Application Data, Read Application Data

## Related attack patterns (CAPEC)
- [CAPEC-26](https://capec.mitre.org/data/definitions/26.html)
- [CAPEC-29](https://capec.mitre.org/data/definitions/29.html)

## Related weaknesses
- CWE-362 (ChildOf)
- CWE-364 (CanAlsoBe)

## Observed examples (CVE)
- **CVE-2009-1837**: Chain: race condition (CWE-362) from improper handling of a page transition in web client while an applet is loading (CWE-368) leads to use after free (CWE-416)
- **CVE-2004-2260**: Browser updates address bar as soon as user clicks on a link instead of when the page has loaded, allowing spoofing by redirecting to another page using onUnload method. ** this is one example of the role of "hooks" and context switches, and should be captured somehow - also a race condition of sorts **
- **CVE-2004-0191**: XSS when web browser executes Javascript events in the context of a new page while it's being loaded, allowing interaction with previous page in different domain.
- **CVE-2004-2491**: Web browser fills in address bar of clicked-on link before page has been loaded, and doesn't update afterward.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/368.html
