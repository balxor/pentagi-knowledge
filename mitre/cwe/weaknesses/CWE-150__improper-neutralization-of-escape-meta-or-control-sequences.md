---
cwe_id: CWE-150
name: Improper Neutralization of Escape, Meta, or Control Sequences
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, AI/ML]
related_capec: [CAPEC-134, CAPEC-41, CAPEC-81, CAPEC-93]
url: https://cwe.mitre.org/data/definitions/150.html
tags: [mitre-cwe, weakness, CWE-150]
---

# CWE-150 - Improper Neutralization of Escape, Meta, or Control Sequences

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-150](https://cwe.mitre.org/data/definitions/150.html)

## Description
The product receives input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could be interpreted as escape, meta, or control character sequences when they are sent to a downstream component.

## Applicable platforms / languages
Not Language-Specific, AI/ML

## Common consequences
- **Integrity**: Execute Unauthorized Code or Commands, Hide Activities, Unexpected State

## Potential mitigations
- **general**: Developers should anticipate that escape, meta and control characters/sequences will be injected/removed/manipulated in the input vectors of their product. Use an appropriate combination of denylists and allowlists to ensure only valid, expected and appropriate input is processed by the system.
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- **Implementation**: While it is risky to use dynamically-generated query strings, code, or commands that mix control and data together, sometimes it may be unavoidable. Properly quote arguments and escape any special characters within those arguments. The most conservative approach is to escape or filter all characters that do not pass an extremely strict allowlist (such as everything that is not alphanumeric or white space). If some special characters are still needed, such as white space, wrap each argument in quotes after the escaping/filtering step. Be careful of argument injection (CWE-88).
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.
- **Implementation**: When using output from an LLM, neutralize or strip escape codes before redirecting output to the terminal or other rendering engine that would process the codes. The neutralization could require that the character be printable and/or allowable whitespace, such as a carriage return or newline. Be deliberate about what to allow.
- **Build and Compilation**: When using an LLM: during tokenizer training, suppress escape codes from the tokenizer's vocabulary. Depending on context, this could be accomplished by removing the codes from input to the tokenizer, or removing the map from the string to its token ID. It is generally unlikely that this removal would adversely affect the quality or correctness of what is generated, e.g. advice requests for terminal settings to change colors.

## Related attack patterns (CAPEC)
- [CAPEC-134](https://capec.mitre.org/data/definitions/134.html)
- [CAPEC-41](https://capec.mitre.org/data/definitions/41.html)
- [CAPEC-81](https://capec.mitre.org/data/definitions/81.html)
- [CAPEC-93](https://capec.mitre.org/data/definitions/93.html)

## Related weaknesses
- CWE-138 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-27936**: Chain: JavaScript-based application removes ANSI escape sequences in a dialog that asks permission for a particular file, causing the wrong filename to be visually presented for user approval (CWE-451), but the filename still contains the ANSI escape sequences (CWE-150), potentially causing the user to grant access to the wrong file.
- **CVE-2002-0542**: The mail program processes special "~" escape sequence even when not in interactive mode.
- **CVE-2000-0703**: Setuid program does not filter escape sequences before calling mail program.
- **CVE-2002-0986**: Mail function does not filter control characters from arguments, allowing mail message content to be modified.
- **CVE-2003-0020**: Multi-channel issue. Terminal escape sequences not filtered from log files.
- **CVE-2003-0083**: Multi-channel issue. Terminal escape sequences not filtered from log files.
- **CVE-2003-0021**: Terminal escape sequences not filtered by terminals when displaying files.
- **CVE-2003-0022**: Terminal escape sequences not filtered by terminals when displaying files.
- **CVE-2003-0023**: Terminal escape sequences not filtered by terminals when displaying files.
- **CVE-2003-0063**: Terminal escape sequences not filtered by terminals when displaying files.
- **CVE-2000-0476**: Terminal escape sequences not filtered by terminals when displaying files.
- **CVE-2001-1556**: MFV. (multi-channel). Injection of control characters into log files that allow information hiding when using raw Unix programs to read the files.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/150.html
