---
cwe_id: CWE-95
name: Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')
type: weakness
abstraction: Variant
status: Incomplete
languages: [Java, JavaScript, Python, Perl, PHP, Ruby, Interpreted, AI/ML]
related_capec: [CAPEC-35]
url: https://cwe.mitre.org/data/definitions/95.html
tags: [mitre-cwe, weakness, CWE-95]
---

# CWE-95 - Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-95](https://cwe.mitre.org/data/definitions/95.html)

## Description
The product receives input from an upstream component, but it does not neutralize or incorrectly neutralizes code syntax before using the input in a dynamic evaluation call (e.g. "eval").

## Applicable platforms / languages
Java, JavaScript, Python, Perl, PHP, Ruby, Interpreted, AI/ML

## Common consequences
- **Confidentiality**: Read Files or Directories, Read Application Data
- **Access Control**: Bypass Protection Mechanism
- **Access Control**: Gain Privileges or Assume Identity
- **Integrity, Confidentiality, Availability, Other**: Execute Unauthorized Code or Commands
- **Non-Repudiation**: Hide Activities

## Potential mitigations
- **Architecture and Design, Implementation**: If possible, refactor your code so that it does not need to use eval() at all.
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180, CWE-181). Make sure that your application does not inadvertently decode the same input twice (CWE-174). Such errors could be used to bypass allowlist schemes by introducing dangerous inputs after they have been checked. Use libraries such as the OWASP ESAPI Canonicalization control. Consider performing repeated canonicalization until your input does not change any more. This will avoid double-decoding and similar scenarios, but it might inadvertently modify inputs that are allowed to contain properly-encoded dangerous content.
- **Implementation**: For Python programs, it is frequently encouraged to use the ast.literal_eval() function instead of eval, since it is intentionally designed to avoid executing code. However, an adversary could still cause excessive memory or stack consumption via deeply nested structures [REF-1372], so the python documentation discourages use of ast.literal_eval() on untrusted data [REF-1373].

## Related attack patterns (CAPEC)
- [CAPEC-35](https://capec.mitre.org/data/definitions/35.html)

## Related weaknesses
- CWE-94 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-4181**: Framework for LLM applications allows eval injection via a crafted response from a hosting provider.
- **CVE-2022-2054**: Python compiler uses eval() to execute malicious strings as Python code.
- **CVE-2021-22204**: Chain: regex in EXIF processor code does not correctly determine where a string ends (CWE-625), enabling eval injection (CWE-95), as exploited in the wild per CISA KEV.
- **CVE-2021-22205**: Chain: backslash followed by a newline can bypass a validation step (CWE-20), leading to eval injection (CWE-95), as exploited in the wild per CISA KEV.
- **CVE-2008-5071**: Eval injection in PHP program.
- **CVE-2002-1750**: Eval injection in Perl program.
- **CVE-2008-5305**: Eval injection in Perl program using an ID that should only contain hyphens and numbers.
- **CVE-2002-1752**: Direct code injection into Perl eval function.
- **CVE-2002-1753**: Eval injection in Perl program.
- **CVE-2005-1527**: Direct code injection into Perl eval function.
- **CVE-2005-2837**: Direct code injection into Perl eval function.
- **CVE-2005-1921**: MFV. code injection into PHP eval statement using nested constructs that should not be nested.
- **CVE-2005-2498**: MFV. code injection into PHP eval statement using nested constructs that should not be nested.
- **CVE-2005-3302**: Code injection into Python eval statement from a field in a formatted file.
- **CVE-2007-1253**: Eval injection in Python program.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/95.html
