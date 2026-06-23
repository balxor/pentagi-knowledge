---
cwe_id: CWE-331
name: Insufficient Entropy
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-59]
url: https://cwe.mitre.org/data/definitions/331.html
tags: [mitre-cwe, weakness, CWE-331]
---

# CWE-331 - Insufficient Entropy

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-331](https://cwe.mitre.org/data/definitions/331.html)

## Description
The product uses an algorithm or scheme that produces insufficient entropy, leaving patterns or clusters of values that are more likely to occur than others.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control, Other**: Bypass Protection Mechanism, Other

## Potential mitigations
- **Implementation**: Determine the necessary entropy to adequately provide for randomness and predictability. This can be achieved by increasing the number of bits of objects such as keys and seeds.

## Related attack patterns (CAPEC)
- [CAPEC-59](https://capec.mitre.org/data/definitions/59.html)

## Related weaknesses
- CWE-330 (ChildOf)
- CWE-330 (ChildOf)

## Observed examples (CVE)
- **CVE-2001-0950**: Insufficiently random data used to generate session tokens using C rand(). Also, for certificate/key generation, uses a source that does not block when entropy is low.
- **CVE-2008-2108**: Chain: insufficient precision (CWE-1339) in random-number generator causes some zero bits to be reliably generated, reducing the amount of entropy (CWE-331)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/331.html
