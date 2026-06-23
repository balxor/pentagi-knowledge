---
capec_id: CAPEC-492
name: Regular Expression Exponential Blowup
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: n/a
related_cwe: [CWE-400, CWE-1333]
related_attack: []
url: https://capec.mitre.org/data/definitions/492.html
tags: [mitre-capec, attack-pattern, CAPEC-492]
---

# CAPEC-492 - Regular Expression Exponential Blowup

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-492](https://capec.mitre.org/data/definitions/492.html)

## Description
An adversary may execute an attack on a program that uses a poor Regular Expression(Regex) implementation by choosing input that results in an extreme situation for the Regex. A typical extreme situation operates at exponential time compared to the input size. This is due to most implementations using a Nondeterministic Finite Automaton(NFA) state machine to be built by the Regex algorithm since NFA allows backtracking and thus more complex regular expressions.

## Extended description
The algorithm builds a finite state machine and based on the input transitions through all the states until the end of the input is reached. NFA engines may evaluate each character in the input string multiple times during the backtracking. The algorithm tries each path through the NFA one by one until a match is found; the malicious input is crafted so every path is tried which results in a failure. Exploitation of the Regex results in programs hanging or taking a very long time to complete. These attacks may target various layers of the Internet due to regular expressions being used in validation.

## Prerequisites
- This type of an attack requires the ability to identify hosts running a poorly implemented Regex, and the ability to send crafted input to exploit the regular expression.

## Mitigations
- Test custom written Regex with fuzzing to determine if the Regex is a poor one. Add timeouts to processes that handle the Regex logic. If an evil Regex is found rewrite it as a good Regex.

## Related weaknesses (CWE)
- [CWE-400](https://cwe.mitre.org/data/definitions/400.html)
- [CWE-1333](https://cwe.mitre.org/data/definitions/1333.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/492.html
