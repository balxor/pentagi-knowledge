---
cwe_id: CWE-540
name: Inclusion of Sensitive Information in Source Code
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific, Web Based]
related_capec: []
url: https://cwe.mitre.org/data/definitions/540.html
tags: [mitre-cwe, weakness, CWE-540]
---

# CWE-540 - Inclusion of Sensitive Information in Source Code

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-540](https://cwe.mitre.org/data/definitions/540.html)

## Description
Source code on a web server or repository often contains sensitive information and should generally not be accessible to users.

## Extended description
There are situations where it is critical to remove source code from an area or server. For example, obtaining Perl source code on a system allows an attacker to understand the logic of the script and extract extremely useful information such as code bugs or logins and passwords.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design, System Configuration**: Recommendations include removing this script from the web server and moving it to a location not accessible from the Internet.

## Related weaknesses
- CWE-538 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-25512**: Server for Team Awareness Kit (TAK) application includes sensitive tokens in the JavaScript source code.
- **CVE-2022-24867**: The LDAP password might be visible in the html code of a rendered page in an IT Asset Management tool.
- **CVE-2007-6197**: Version numbers and internal hostnames leaked in HTML comments.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/540.html
