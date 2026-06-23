---
cwe_id: CWE-624
name: Executable Regular Expression Error
type: weakness
abstraction: Base
status: Incomplete
languages: [PHP, Perl]
related_capec: []
url: https://cwe.mitre.org/data/definitions/624.html
tags: [mitre-cwe, weakness, CWE-624]
---

# CWE-624 - Executable Regular Expression Error

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-624](https://cwe.mitre.org/data/definitions/624.html)

## Description
The product uses a regular expression that either (1) contains an executable component with user-controlled inputs, or (2) allows a user to enable execution by inserting pattern modifiers.

## Extended description
Case (2) is possible in the PHP preg_replace() function, and possibly in other languages when a user-controlled input is inserted into a string that is later parsed as a regular expression.

## Applicable platforms / languages
PHP, Perl

## Common consequences
- **Confidentiality, Integrity, Availability**: Execute Unauthorized Code or Commands

## Potential mitigations
- **Implementation**: The regular expression feature in some languages allows inputs to be quoted or escaped before insertion, such as \Q and \E in Perl.

## Related weaknesses
- CWE-77 (ChildOf)
- CWE-77 (ChildOf)
- CWE-77 (ChildOf)

## Observed examples (CVE)
- **CVE-2006-2059**: Executable regexp in PHP by inserting "e" modifier into first argument to preg_replace
- **CVE-2005-3420**: Executable regexp in PHP by inserting "e" modifier into first argument to preg_replace
- **CVE-2006-2878**: Complex curly syntax inserted into the replacement argument to PHP preg_replace(), which uses the "/e" modifier
- **CVE-2006-2908**: Function allows remote attackers to execute arbitrary PHP code via the username field, which is used in a preg_replace function call with a /e (executable) modifier.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/624.html
