---
cwe_id: CWE-90
name: Improper Neutralization of Special Elements used in an LDAP Query ('LDAP Injection')
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Database Server]
related_capec: [CAPEC-136]
url: https://cwe.mitre.org/data/definitions/90.html
tags: [mitre-cwe, weakness, CWE-90]
---

# CWE-90 - Improper Neutralization of Special Elements used in an LDAP Query ('LDAP Injection')

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-90](https://cwe.mitre.org/data/definitions/90.html)

## Description
The product constructs all or part of an LDAP query using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended LDAP query when it is sent to a downstream component.

## Applicable platforms / languages
Not Language-Specific, Database Server

## Common consequences
- **Confidentiality, Integrity, Availability**: Execute Unauthorized Code or Commands, Read Application Data, Modify Application Data

## Potential mitigations
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.

## Related attack patterns (CAPEC)
- [CAPEC-136](https://capec.mitre.org/data/definitions/136.html)

## Related weaknesses
- CWE-943 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-41232**: Chain: authentication routine in Go-based agile development product does not escape user name (CWE-116), allowing LDAP injection (CWE-90)
- **CVE-2005-2301**: Server does not properly escape LDAP queries, which allows remote attackers to cause a DoS and possibly conduct an LDAP injection attack.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/90.html
