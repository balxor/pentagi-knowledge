---
cwe_id: CWE-94
name: Improper Control of Generation of Code ('Code Injection')
type: weakness
abstraction: Base
status: Draft
languages: [Interpreted, AI/ML]
related_capec: [CAPEC-242, CAPEC-35, CAPEC-77]
url: https://cwe.mitre.org/data/definitions/94.html
tags: [mitre-cwe, weakness, CWE-94]
---

# CWE-94 - Improper Control of Generation of Code ('Code Injection')

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-94](https://cwe.mitre.org/data/definitions/94.html)

## Description
The product constructs all or part of a code segment using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the syntax or behavior of the intended code segment.

## Applicable platforms / languages
Interpreted, AI/ML

## Common consequences
- **Access Control**: Bypass Protection Mechanism
- **Access Control**: Gain Privileges or Assume Identity
- **Integrity, Confidentiality, Availability**: Execute Unauthorized Code or Commands
- **Non-Repudiation**: Hide Activities

## Potential mitigations
- **Architecture and Design**: Refactor your program so that you do not have to dynamically generate code.
- **Architecture and Design**: Run your code in a "jail" or similar sandbox environment that enforces strict boundaries between the process and the operating system. This may effectively restrict which code can be executed by your product. Examples include the Unix chroot jail and AppArmor. In general, managed code may provide some protection. This may not be a feasible solution, and it only limits the impact to the operating system; the rest of your application may still be subject to compromise. Be careful to avoid CWE-243 and other weaknesses related to jails.
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright. To reduce the likelihood of code injection, use stringent allowlists that limit which constructs are allowed. If you are dynamically constructing code that invokes a function, then verifying that the input is alphanumeric might be insufficient. An attacker might still be able to reference a dangerous function that you did not intend to allow, such as system(), exec(), or exit().
- **Testing**: Use dynamic tools and techniques that interact with the product using large test suites with many diverse inputs, such as fuzz testing (fuzzing), robustness testing, and fault injection. The product's operation may slow down, but it should not become unstable, crash, or generate incorrect results.
- **Operation**: Run the code in an environment that performs automatic taint propagation and prevents any command execution that uses tainted variables, such as Perl's "-T" switch. This will force the program to perform validation steps that remove the taint, although you must be careful to correctly validate your inputs so that you do not accidentally mark dangerous inputs as untainted (see CWE-183 and CWE-184).
- **Operation**: Run the code in an environment that performs automatic taint propagation and prevents any command execution that uses tainted variables, such as Perl's "-T" switch. This will force the program to perform validation steps that remove the taint, although you must be careful to correctly validate your inputs so that you do not accidentally mark dangerous inputs as untainted (see CWE-183 and CWE-184).
- **Implementation**: For Python programs, it is frequently encouraged to use the ast.literal_eval() function instead of eval, since it is intentionally designed to avoid executing code. However, an adversary could still cause excessive memory or stack consumption via deeply nested structures [REF-1372], so the python documentation discourages use of ast.literal_eval() on untrusted data [REF-1373].

## Related attack patterns (CAPEC)
- [CAPEC-242](https://capec.mitre.org/data/definitions/242.html)
- [CAPEC-35](https://capec.mitre.org/data/definitions/35.html)
- [CAPEC-77](https://capec.mitre.org/data/definitions/77.html)

## Related weaknesses
- CWE-74 (ChildOf)
- CWE-74 (ChildOf)
- CWE-913 (ChildOf)

## Observed examples (CVE)
- **CVE-2023-29374**: Math component in an LLM framework translates user input into a Python expression that is input into the Python exec() method, allowing code execution - one variant of a "prompt injection" attack.
- **CVE-2024-5565**: Python-based library uses an LLM prompt containing user input to dynamically generate code that is then fed as input into the Python exec() method, allowing code execution - one variant of a "prompt injection" attack.
- **CVE-2024-4181**: Framework for LLM applications allows eval injection via a crafted response from a hosting provider.
- **CVE-2022-2054**: Python compiler uses eval() to execute malicious strings as Python code.
- **CVE-2021-22204**: Chain: regex in EXIF processor code does not correctly determine where a string ends (CWE-625), enabling eval injection (CWE-95), as exploited in the wild per CISA KEV.
- **CVE-2020-8218**: "Code injection" in VPN product, as exploited in the wild per CISA KEV.
- **CVE-2008-5071**: Eval injection in PHP program.
- **CVE-2002-1750**: Eval injection in Perl program.
- **CVE-2008-5305**: Eval injection in Perl program using an ID that should only contain hyphens and numbers.
- **CVE-2002-1752**: Direct code injection into Perl eval function.
- **CVE-2002-1753**: Eval injection in Perl program.
- **CVE-2005-1527**: Direct code injection into Perl eval function.
- **CVE-2005-2837**: Direct code injection into Perl eval function.
- **CVE-2005-1921**: MFV. code injection into PHP eval statement using nested constructs that should not be nested.
- **CVE-2005-2498**: MFV. code injection into PHP eval statement using nested constructs that should not be nested.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/94.html
