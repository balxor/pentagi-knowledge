---
cwe_id: CWE-180
name: Incorrect Behavior Order: Validate Before Canonicalize
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-267, CAPEC-3, CAPEC-71, CAPEC-78, CAPEC-79, CAPEC-80]
url: https://cwe.mitre.org/data/definitions/180.html
tags: [mitre-cwe, weakness, CWE-180]
---

# CWE-180 - Incorrect Behavior Order: Validate Before Canonicalize

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-180](https://cwe.mitre.org/data/definitions/180.html)

## Description
The product validates input before it is canonicalized, which prevents the product from detecting data that becomes invalid after the canonicalization step.

## Extended description
This can be used by an attacker to bypass the validation and launch attacks that expose weaknesses that would otherwise be prevented, such as injection.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Related attack patterns (CAPEC)
- [CAPEC-267](https://capec.mitre.org/data/definitions/267.html)
- [CAPEC-3](https://capec.mitre.org/data/definitions/3.html)
- [CAPEC-71](https://capec.mitre.org/data/definitions/71.html)
- [CAPEC-78](https://capec.mitre.org/data/definitions/78.html)
- [CAPEC-79](https://capec.mitre.org/data/definitions/79.html)
- [CAPEC-80](https://capec.mitre.org/data/definitions/80.html)

## Related weaknesses
- CWE-179 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-0433**: List files in web server using "*.ext"
- **CVE-2003-0332**: Product modifies the first two letters of a filename extension after performing a security check, which allows remote attackers to bypass authentication via a filename with a .ats extension instead of a .hts extension.
- **CVE-2002-0802**: Database consumes an extra character when processing a character that cannot be converted, which could remove an escape character from the query and make the application subject to SQL injection attacks.
- **CVE-2000-0191**: Overlaps "fakechild/../realchild"
- **CVE-2004-2363**: Product checks URI for "<" and other literal characters, but does it before hex decoding the URI, so "%3E" and other sequences are allowed.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/180.html
