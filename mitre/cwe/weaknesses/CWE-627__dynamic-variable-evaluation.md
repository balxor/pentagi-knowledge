---
cwe_id: CWE-627
name: Dynamic Variable Evaluation
type: weakness
abstraction: Variant
status: Incomplete
languages: [PHP, Perl]
related_capec: []
url: https://cwe.mitre.org/data/definitions/627.html
tags: [mitre-cwe, weakness, CWE-627]
---

# CWE-627 - Dynamic Variable Evaluation

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-627](https://cwe.mitre.org/data/definitions/627.html)

## Description
In a language where the user can influence the name of a variable at runtime, if the variable names are not controlled, an attacker can read or write to arbitrary variables, or access arbitrary functions.

## Extended description
The resultant vulnerabilities depend on the behavior of the application, both at the crossover point and in any control/data flow that is reachable by the related variables or functions.

## Applicable platforms / languages
PHP, Perl

## Common consequences
- **Confidentiality, Integrity, Availability**: Modify Application Data, Execute Unauthorized Code or Commands

## Potential mitigations
- **Implementation**: Refactor the code to avoid dynamic variable evaluation whenever possible.
- **Implementation**: Use only allowlists of acceptable variable or function names.
- **Implementation**: For function names, ensure that you are only calling functions that accept the proper number of arguments, to avoid unexpected null arguments.

## Related weaknesses
- CWE-914 (ChildOf)
- CWE-183 (PeerOf)

## Observed examples (CVE)
- **CVE-2009-0422**: Chain: Dynamic variable evaluation allows resultant remote file inclusion and path traversal.
- **CVE-2007-2431**: Chain: dynamic variable evaluation in PHP program used to modify critical, unexpected $_SERVER variable for resultant XSS.
- **CVE-2006-4904**: Chain: dynamic variable evaluation in PHP program used to conduct remote file inclusion.
- **CVE-2006-4019**: Dynamic variable evaluation in mail program allows reading and modifying attachments and preferences of other users.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/627.html
