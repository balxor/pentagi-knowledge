---
cwe_id: CWE-622
name: Improper Validation of Function Hook Arguments
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/622.html
tags: [mitre-cwe, weakness, CWE-622]
---

# CWE-622 - Improper Validation of Function Hook Arguments

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-622](https://cwe.mitre.org/data/definitions/622.html)

## Description
The product adds hooks to user-accessible API functions, but it does not properly validate the arguments. This could lead to resultant vulnerabilities.

## Extended description
Such hooks can be used in defensive software that runs with privileges, such as anti-virus or firewall, which hooks kernel calls. When the arguments are not validated, they could be used to bypass the protection scheme or attack the product itself.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Unexpected State

## Potential mitigations
- **Architecture and Design**: Ensure that all arguments are verified, as defined by the API you are protecting.
- **Architecture and Design**: Drop privileges before invoking such functions, if possible.

## Related weaknesses
- CWE-20 (ChildOf)

## Observed examples (CVE)
- **CVE-2007-0708**: DoS in firewall using standard Microsoft functions
- **CVE-2006-7160**: DoS in firewall using standard Microsoft functions
- **CVE-2007-1376**: function does not verify that its argument is the proper type, leading to arbitrary memory write
- **CVE-2007-1220**: invalid syscall arguments bypass code execution limits
- **CVE-2006-4541**: DoS in IDS via NULL argument

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/622.html
