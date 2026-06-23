---
cwe_id: CWE-754
name: Improper Check for Unusual or Exceptional Conditions
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/754.html
tags: [mitre-cwe, weakness, CWE-754]
---

# CWE-754 - Improper Check for Unusual or Exceptional Conditions

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-754](https://cwe.mitre.org/data/definitions/754.html)

## Description
The product does not check or incorrectly checks for unusual or exceptional conditions that are not expected to occur frequently during day to day operation of the product.

## Extended description
The programmer may assume that certain events or conditions will never occur or do not need to be worried about, such as low memory conditions, lack of access to resources due to restrictive permissions, or misbehaving clients or components. However, attackers may intentionally trigger these unusual conditions, thus violating the programmer's assumptions, possibly introducing instability, incorrect behavior, or a vulnerability. Note that this entry is not exclusively about the use of exceptions and exception handling, which are mechanisms for both checking and handling unusual or unexpected conditions.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Integrity, Availability**: DoS: Crash, Exit, or Restart, Unexpected State

## Potential mitigations
- **Requirements**: Use a language that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. Choose languages with features such as exception handling that force the programmer to anticipate unusual conditions that may generate exceptions. Custom exceptions may need to be developed to handle unusual business-logic conditions. Be careful not to pass sensitive exceptions back to the user (CWE-209, CWE-248).
- **Implementation**: Check the results of all functions that return a value and verify that the value is expected.
- **Implementation**: If using exception handling, catch and throw specific exceptions instead of overly-general exceptions (CWE-396, CWE-397). Catch and handle exceptions as locally as possible so that exceptions do not propagate too far up the call stack (CWE-705). Avoid unchecked or uncaught exceptions where feasible (CWE-248).
- **Implementation**: Ensure that error messages only contain minimal details that are useful to the intended audience and no one else. The messages need to strike the balance between being too cryptic (which can confuse users) or being too detailed (which may reveal more than intended). The messages should not reveal the methods that were used to determine the error. Attackers can use detailed information to refine or optimize their original attack, thereby increasing their chances of success. If errors must be captured in some detail, record them in log messages, but consider what could occur if the log messages can be viewed by attackers. Highly sensitive information such as passwords should never be saved to log files. Avoid inconsistent messaging that might accidentally tip off an attacker about internal state, such as whether a user account exists or not. Exposing additional information to a potential attacker in the context of an exceptional condition can help the attacker determine what attack vectors are most likely to succeed beyond DoS.
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- **Architecture and Design, Implementation**: If the program must fail, ensure that it fails gracefully (fails closed). There may be a temptation to simply let the program fail poorly in cases such as low memory conditions, but an attacker may be able to assert control before the software has fully exited. Alternately, an uncontrolled failure could cause cascading problems with other downstream components; for example, the program could send a signal to a downstream process so the process immediately knows that a problem has occurred and has a better chance of recovery.
- **Architecture and Design**: Use system limits, which should help to prevent resource exhaustion. However, the product should still handle low resource conditions since they may still occur.

## Related weaknesses
- CWE-703 (ChildOf)
- CWE-416 (CanPrecede)

## Observed examples (CVE)
- **CVE-2023-49286**: Chain: function in web caching proxy does not correctly check a return value (CWE-253) leading to a reachable assertion (CWE-617)
- **CVE-2007-3798**: Unchecked return value leads to resultant integer overflow and code execution.
- **CVE-2006-4447**: Program does not check return value when invoking functions to drop privileges, which could leave users with higher privileges than expected by forcing those functions to fail.
- **CVE-2006-2916**: Program does not check return value when invoking functions to drop privileges, which could leave users with higher privileges than expected by forcing those functions to fail.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/754.html
