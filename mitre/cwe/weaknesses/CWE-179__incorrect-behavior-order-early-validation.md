---
cwe_id: CWE-179
name: Incorrect Behavior Order: Early Validation
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-3, CAPEC-43, CAPEC-71]
url: https://cwe.mitre.org/data/definitions/179.html
tags: [mitre-cwe, weakness, CWE-179]
---

# CWE-179 - Incorrect Behavior Order: Early Validation

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-179](https://cwe.mitre.org/data/definitions/179.html)

## Description
The product validates input before applying protection mechanisms that modify the input, which could allow an attacker to bypass the validation via dangerous inputs that only arise after the modification.

## Extended description
Product needs to validate data at the proper time, after data has been canonicalized and cleansed. Early validation is susceptible to various manipulations that result in dangerous inputs that are produced by canonicalization and cleansing.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control, Integrity**: Bypass Protection Mechanism, Execute Unauthorized Code or Commands

## Potential mitigations
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Related attack patterns (CAPEC)
- [CAPEC-3](https://capec.mitre.org/data/definitions/3.html)
- [CAPEC-43](https://capec.mitre.org/data/definitions/43.html)
- [CAPEC-71](https://capec.mitre.org/data/definitions/71.html)

## Related weaknesses
- CWE-20 (ChildOf)
- CWE-696 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-0433**: List files in web server using "*.ext"
- **CVE-2003-0332**: Product modifies the first two letters of a filename extension after performing a security check, which allows remote attackers to bypass authentication via a filename with a .ats extension instead of a .hts extension.
- **CVE-2002-0802**: Database consumes an extra character when processing a character that cannot be converted, which could remove an escape character from the query and make the application subject to SQL injection attacks.
- **CVE-2000-0191**: Overlaps "fakechild/../realchild"
- **CVE-2004-2363**: Product checks URI for "<" and other literal characters, but does it before hex decoding the URI, so "%3E" and other sequences are allowed.
- **CVE-2002-0934**: Directory traversal vulnerability allows remote attackers to read or modify arbitrary files via invalid characters between two . (dot) characters, which are filtered and result in a ".." sequence.
- **CVE-2003-0282**: Directory traversal vulnerability allows attackers to overwrite arbitrary files via invalid characters between two . (dot) characters, which are filtered and result in a ".." sequence.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/179.html
