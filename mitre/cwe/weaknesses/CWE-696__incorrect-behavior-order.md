---
cwe_id: CWE-696
name: Incorrect Behavior Order
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific, Web Based]
related_capec: [CAPEC-463]
url: https://cwe.mitre.org/data/definitions/696.html
tags: [mitre-cwe, weakness, CWE-696]
---

# CWE-696 - Incorrect Behavior Order

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-696](https://cwe.mitre.org/data/definitions/696.html)

## Description
The product performs multiple related behaviors, but the behaviors are performed in the wrong order in ways that may produce resultant weaknesses.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based

## Common consequences
- **Integrity**: Alter Execution Logic

## Related attack patterns (CAPEC)
- [CAPEC-463](https://capec.mitre.org/data/definitions/463.html)

## Related weaknesses
- CWE-691 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-9805**: Chain: Creation of the packet client occurs before initialization is complete (CWE-696) resulting in a read from uninitialized memory (CWE-908), causing memory corruption.
- **CVE-2007-5191**: file-system management programs call the setuid and setgid functions in the wrong order and do not check the return values, allowing attackers to gain unintended privileges
- **CVE-2007-1588**: C++ web server program calls Process::setuid before calling Process::setgid, preventing it from dropping privileges, potentially allowing CGI programs to be called with higher privileges than intended
- **CVE-2022-37734**: Chain: lexer in Java-based GraphQL server does not enforce maximum of tokens early enough (CWE-696), allowing excessive CPU consumption (CWE-1176)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/696.html
