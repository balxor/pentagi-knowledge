---
cwe_id: CWE-154
name: Improper Neutralization of Variable Name Delimiters
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-15]
url: https://cwe.mitre.org/data/definitions/154.html
tags: [mitre-cwe, weakness, CWE-154]
---

# CWE-154 - Improper Neutralization of Variable Name Delimiters

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-154](https://cwe.mitre.org/data/definitions/154.html)

## Description
The product receives input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could be interpreted as variable name delimiters when they are sent to a downstream component.

## Extended description
As data is parsed, an injected delimiter may cause the process to take unexpected actions that result in an attack. Example: "$" for an environment variable.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Unexpected State

## Potential mitigations
- **general**: Developers should anticipate that variable name delimiters will be injected/removed/manipulated in the input vectors of their product. Use an appropriate combination of denylists and allowlists to ensure only valid, expected and appropriate input is processed by the system.
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- **Implementation**: While it is risky to use dynamically-generated query strings, code, or commands that mix control and data together, sometimes it may be unavoidable. Properly quote arguments and escape any special characters within those arguments. The most conservative approach is to escape or filter all characters that do not pass an extremely strict allowlist (such as everything that is not alphanumeric or white space). If some special characters are still needed, such as white space, wrap each argument in quotes after the escaping/filtering step. Be careful of argument injection (CWE-88).
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Related attack patterns (CAPEC)
- [CAPEC-15](https://capec.mitre.org/data/definitions/15.html)

## Related weaknesses
- CWE-138 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-0129**: "%" variable is expanded by wildcard function into disallowed commands.
- **CVE-2002-0770**: Server trusts client to expand macros, allows macro characters to be expanded to trigger resultant information exposure.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/154.html
