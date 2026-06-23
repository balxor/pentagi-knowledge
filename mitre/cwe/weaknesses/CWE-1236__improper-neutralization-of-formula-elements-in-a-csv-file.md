---
cwe_id: CWE-1236
name: Improper Neutralization of Formula Elements in a CSV File
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Other]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1236.html
tags: [mitre-cwe, weakness, CWE-1236]
---

# CWE-1236 - Improper Neutralization of Formula Elements in a CSV File

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1236](https://cwe.mitre.org/data/definitions/1236.html)

## Description
The product saves user-provided information into a Comma-Separated Value (CSV) file, but it does not neutralize or incorrectly neutralizes special elements that could be interpreted as a command when the file is opened by a spreadsheet product.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Other

## Common consequences
- **Confidentiality**: Read Application Data, Execute Unauthorized Code or Commands

## Potential mitigations
- **Implementation**: When generating CSV output, ensure that formula-sensitive metacharacters are effectively escaped or removed from all data before storage in the resultant CSV. Risky characters include '=' (equal), '+' (plus), '-' (minus), and '@' (at).
- **Implementation**: If a field starts with a formula character, prepend it with a ' (single apostrophe), which prevents Excel from executing the formula.
- **Architecture and Design**: Certain implementations of spreadsheet software might disallow formulas from executing if the file is untrusted, or if the file is not authored by the current user.

## Related weaknesses
- CWE-74 (ChildOf)
- CWE-74 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-12134**: Low privileged user can trigger CSV injection through a contact form field value
- **CVE-2019-4521**: Cloud management product allows arbitrary command execution via CSV injection
- **CVE-2019-17661**: CSV injection in content management system via formula code in a first or last name

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1236.html
