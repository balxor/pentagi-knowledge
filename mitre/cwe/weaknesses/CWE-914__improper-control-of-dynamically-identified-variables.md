---
cwe_id: CWE-914
name: Improper Control of Dynamically-Identified Variables
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Interpreted]
related_capec: []
url: https://cwe.mitre.org/data/definitions/914.html
tags: [mitre-cwe, weakness, CWE-914]
---

# CWE-914 - Improper Control of Dynamically-Identified Variables

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-914](https://cwe.mitre.org/data/definitions/914.html)

## Description
The product does not properly restrict reading from or writing to dynamically-identified variables.

## Extended description
Many languages offer powerful features that allow the programmer to access arbitrary variables that are specified by an input string. While these features can offer significant flexibility and reduce development time, they can be extremely dangerous if attackers can modify unintended variables that have security implications.

## Applicable platforms / languages
Not Language-Specific, Interpreted

## Common consequences
- **Integrity**: Modify Application Data
- **Integrity**: Execute Unauthorized Code or Commands
- **Other, Integrity**: Varies by Context, Alter Execution Logic

## Potential mitigations
- **Implementation**: For any externally-influenced input, check the input against an allowlist of internal program variables that are allowed to be modified.
- **Implementation, Architecture and Design**: Refactor the code so that internal program variables do not need to be dynamically identified.

## Related weaknesses
- CWE-99 (ChildOf)
- CWE-913 (ChildOf)

## Observed examples (CVE)
- **CVE-2006-7135**: extract issue enables file inclusion
- **CVE-2006-7079**: Chain: extract used for register_globals compatibility layer, enables path traversal (CWE-22)
- **CVE-2007-0649**: extract() buried in include files makes post-disclosure analysis confusing; original report had seemed incorrect.
- **CVE-2006-6661**: extract() enables static code injection
- **CVE-2006-2828**: import_request_variables() buried in include files makes post-disclosure analysis confusing
- **CVE-2009-0422**: Chain: Dynamic variable evaluation allows resultant remote file inclusion and path traversal.
- **CVE-2007-2431**: Chain: dynamic variable evaluation in PHP program used to modify critical, unexpected $_SERVER variable for resultant XSS.
- **CVE-2006-4904**: Chain: dynamic variable evaluation in PHP program used to conduct remote file inclusion.
- **CVE-2006-4019**: Dynamic variable evaluation in mail program allows reading and modifying attachments and preferences of other users.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/914.html
