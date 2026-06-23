---
cwe_id: CWE-96
name: Improper Neutralization of Directives in Statically Saved Code ('Static Code Injection')
type: weakness
abstraction: Base
status: Draft
languages: [PHP, Perl, Interpreted]
related_capec: [CAPEC-35, CAPEC-73, CAPEC-77, CAPEC-81, CAPEC-85]
url: https://cwe.mitre.org/data/definitions/96.html
tags: [mitre-cwe, weakness, CWE-96]
---

# CWE-96 - Improper Neutralization of Directives in Statically Saved Code ('Static Code Injection')

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-96](https://cwe.mitre.org/data/definitions/96.html)

## Description
The product receives input from an upstream component, but it does not neutralize or incorrectly neutralizes code syntax before inserting the input into an executable resource, such as a library, configuration file, or template.

## Applicable platforms / languages
PHP, Perl, Interpreted

## Common consequences
- **Confidentiality**: Read Files or Directories, Read Application Data
- **Access Control**: Bypass Protection Mechanism
- **Access Control**: Gain Privileges or Assume Identity
- **Integrity, Confidentiality, Availability, Other**: Execute Unauthorized Code or Commands
- **Non-Repudiation**: Hide Activities

## Potential mitigations
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- **Implementation**: Perform proper output validation and escaping to neutralize all code syntax from data written to code files.

## Related attack patterns (CAPEC)
- [CAPEC-35](https://capec.mitre.org/data/definitions/35.html)
- [CAPEC-73](https://capec.mitre.org/data/definitions/73.html)
- [CAPEC-77](https://capec.mitre.org/data/definitions/77.html)
- [CAPEC-81](https://capec.mitre.org/data/definitions/81.html)
- [CAPEC-85](https://capec.mitre.org/data/definitions/85.html)

## Related weaknesses
- CWE-94 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-0495**: Perl code directly injected into CGI library file from parameters to another CGI program.
- **CVE-2005-1876**: Direct PHP code injection into supporting template file.
- **CVE-2005-1894**: Direct code injection into PHP script that can be accessed by attacker.
- **CVE-2003-0395**: PHP code from User-Agent HTTP header directly inserted into log file implemented as PHP script.
- **CVE-2007-6652**: chain: execution after redirect allows non-administrator to perform static code injection.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/96.html
