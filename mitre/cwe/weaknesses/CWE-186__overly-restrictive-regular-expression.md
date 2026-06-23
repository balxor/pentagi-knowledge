---
cwe_id: CWE-186
name: Overly Restrictive Regular Expression
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/186.html
tags: [mitre-cwe, weakness, CWE-186]
---

# CWE-186 - Overly Restrictive Regular Expression

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-186](https://cwe.mitre.org/data/definitions/186.html)

## Description
A regular expression is overly restrictive, which prevents dangerous values from being detected.

## Extended description
This weakness is not about regular expression complexity. Rather, it is about a regular expression that does not match all values that are intended. Consider the use of a regexp to identify acceptable values or to spot unwanted terms. An overly restrictive regexp misses some potentially security-relevant values leading to either false positives *or* false negatives, depending on how the regexp is being used within the code. Consider the expression /[0-8]/ where the intention was /[0-9]/. This expression is not "complex" but the value "9" is not matched when maybe the programmer planned to check for it.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: Regular expressions can become error prone when defining a complex language even for those experienced in writing grammars. Determine if several smaller regular expressions simplify one large regular expression. Also, subject your regular expression to thorough testing techniques such as equivalence partitioning, boundary value analysis, and robustness. After testing and a reasonable confidence level is achieved, a regular expression may not be foolproof. If an exploit is allowed to slip through, then record the exploit and refactor your regular expression.

## Related weaknesses
- CWE-185 (ChildOf)
- CWE-184 (CanAlsoBe)
- CWE-183 (CanAlsoBe)

## Observed examples (CVE)
- **CVE-2005-1604**: MIE. ".php.ns" bypasses ".php$" regexp but is still parsed as PHP by Apache. (manipulates an equivalence property under Apache)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/186.html
