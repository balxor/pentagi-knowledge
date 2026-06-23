---
cwe_id: CWE-185
name: Incorrect Regular Expression
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-15, CAPEC-6, CAPEC-79]
url: https://cwe.mitre.org/data/definitions/185.html
tags: [mitre-cwe, weakness, CWE-185]
---

# CWE-185 - Incorrect Regular Expression

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-185](https://cwe.mitre.org/data/definitions/185.html)

## Description
The product specifies a regular expression in a way that causes data to be improperly matched or compared.

## Extended description
When the regular expression is used in protection mechanisms such as filtering or validation, this may allow an attacker to bypass the intended restrictions on the incoming data.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Unexpected State, Varies by Context
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: Regular expressions can become error prone when defining a complex language even for those experienced in writing grammars. Determine if several smaller regular expressions simplify one large regular expression. Also, subject the regular expression to thorough testing techniques such as equivalence partitioning, boundary value analysis, and robustness. After testing and a reasonable confidence level is achieved, a regular expression may not be foolproof. If an exploit is allowed to slip through, then record the exploit and refactor the regular expression.

## Related attack patterns (CAPEC)
- [CAPEC-15](https://capec.mitre.org/data/definitions/15.html)
- [CAPEC-6](https://capec.mitre.org/data/definitions/6.html)
- [CAPEC-79](https://capec.mitre.org/data/definitions/79.html)

## Related weaknesses
- CWE-697 (ChildOf)
- CWE-187 (CanPrecede)
- CWE-182 (CanPrecede)

## Observed examples (CVE)
- **CVE-2002-2109**: Regexp isn't "anchored" to the beginning or end, which allows spoofed values that have trusted values as substrings.
- **CVE-2005-1949**: Regexp for IP address isn't anchored at the end, allowing appending of shell metacharacters.
- **CVE-2001-1072**: Bypass access restrictions via multiple leading slash, which causes a regular expression to fail.
- **CVE-2000-0115**: Local user DoS via invalid regular expressions.
- **CVE-2002-1527**: chain: Malformed input generates a regular expression error that leads to information exposure.
- **CVE-2005-1061**: Certain strings are later used in a regexp, leading to a resultant crash.
- **CVE-2005-2169**: MFV. Regular expression intended to protect against directory traversal reduces ".../...//" to "../".
- **CVE-2005-0603**: Malformed regexp syntax leads to information exposure in error message.
- **CVE-2005-1820**: Code injection due to improper quoting of regular expression.
- **CVE-2005-3153**: Null byte bypasses PHP regexp check.
- **CVE-2005-4155**: Null byte bypasses PHP regexp check.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/185.html
