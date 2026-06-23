---
cwe_id: CWE-215
name: Insertion of Sensitive Information Into Debugging Code
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/215.html
tags: [mitre-cwe, weakness, CWE-215]
---

# CWE-215 - Insertion of Sensitive Information Into Debugging Code

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-215](https://cwe.mitre.org/data/definitions/215.html)

## Description
The product inserts sensitive information into debugging code, which could expose this information if the debugging code is not disabled in production.

## Extended description
When debugging, it may be necessary to report detailed information to the programmer. However, if the debugging code is not disabled when the product is operating in a production environment, then this sensitive information may be exposed to attackers.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Implementation**: Do not leave debug statements that could be executed in the source code. Ensure that all debug information is eradicated before releasing the software.
- **Architecture and Design**: Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.

## Related weaknesses
- CWE-200 (ChildOf)

## Observed examples (CVE)
- **CVE-2004-2268**: Password exposed in debug information.
- **CVE-2002-0918**: CGI script includes sensitive information in debug messages when an error is triggered.
- **CVE-2003-1078**: FTP client with debug option enabled shows password to the screen.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/215.html
