---
cwe_id: CWE-636
name: Not Failing Securely ('Failing Open')
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, ICS/OT]
related_capec: []
url: https://cwe.mitre.org/data/definitions/636.html
tags: [mitre-cwe, weakness, CWE-636]
---

# CWE-636 - Not Failing Securely ('Failing Open')

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-636](https://cwe.mitre.org/data/definitions/636.html)

## Description
When the product encounters an error condition or failure, its design requires it to fall back to a state that is less secure than other options that are available, such as selecting the weakest encryption algorithm or using the most permissive access control restrictions.

## Extended description
By entering a less secure state, the product inherits the weaknesses associated with that state, making it easier to compromise. At the least, it causes administrators to have a false sense of security. This weakness typically occurs as a result of wanting to "fail functional" to minimize administration and support costs, instead of "failing safe."

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, ICS/OT

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: Subdivide and allocate resources and components so that a failure in one part does not affect the entire product.

## Related weaknesses
- CWE-657 (ChildOf)
- CWE-755 (ChildOf)
- CWE-280 (PeerOf)

## Observed examples (CVE)
- **CVE-2007-5277**: The failure of connection attempts in a web browser resets DNS pin restrictions. An attacker can then bypass the same origin policy by rebinding a domain name to a different IP address. This was an attempt to "fail functional."
- **CVE-2006-4407**: Incorrect prioritization leads to the selection of a weaker cipher. Although it is not known whether this issue occurred in implementation or design, it is feasible that a poorly designed algorithm could be a factor.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/636.html
