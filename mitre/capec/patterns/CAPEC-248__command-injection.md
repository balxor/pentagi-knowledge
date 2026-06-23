---
capec_id: CAPEC-248
name: Command Injection
type: attack-pattern
abstraction: Meta
likelihood: Medium
severity: High
related_cwe: [CWE-77]
related_attack: []
url: https://capec.mitre.org/data/definitions/248.html
tags: [mitre-capec, attack-pattern, CAPEC-248]
---

# CAPEC-248 - Command Injection

**Abstraction:** Meta  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-248](https://capec.mitre.org/data/definitions/248.html)

## Description
An adversary looking to execute a command of their choosing, injects new items into an existing command thus modifying interpretation away from what was intended. Commands in this context are often standalone strings that are interpreted by a downstream component and cause specific responses. This type of attack is possible when untrusted values are used to build these command strings. Weaknesses in input validation or command construction can enable the attack and lead to successful exploitation.

## Prerequisites
- The target application must accept input from the user and then use this input in the construction of commands to be executed. In virtually all cases, this is some form of string input that is concatenated to a constant string defined by the application to form the full command to be executed.

## Consequences
- **Availability**: Execute Unauthorized Commands (A successful command injection attack enables an adversary to alter the command being executed and achieve a variety of negative consequences depending on the makeup of the new command. This includes potential information disclosure or the corruption of application data.)
- **Confidentiality**: Execute Unauthorized Commands (A successful command injection attack enables an adversary to alter the command being executed and achieve a variety of negative consequences depending on the makeup of the new command. This includes potential information disclosure or the corruption of application data.)
- **Integrity**: Execute Unauthorized Commands (A successful command injection attack enables an adversary to alter the command being executed and achieve a variety of negative consequences depending on the makeup of the new command. This includes potential information disclosure or the corruption of application data.)

## Mitigations
- All user-controllable input should be validated and filtered for potentially unwanted characters. Using an allowlist for input is desired, but if use of a denylist approach is necessary, then focusing on command related terms and delimiters is necessary.
- Input should be encoded prior to use in commands to make sure command related characters are not treated as part of the command. For example, quotation characters may need to be encoded so that the application does not treat the quotation as a delimiter.
- Input should be parameterized, or restricted to data sections of a command, thus removing the chance that the input will be treated as part of the command itself.

## Related weaknesses (CWE)
- [CWE-77](https://cwe.mitre.org/data/definitions/77.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/248.html
