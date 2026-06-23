---
capec_id: CAPEC-28
name: Fuzzing
type: attack-pattern
abstraction: Meta
likelihood: High
severity: Medium
related_cwe: [CWE-74, CWE-20]
related_attack: []
url: https://capec.mitre.org/data/definitions/28.html
tags: [mitre-capec, attack-pattern, CAPEC-28]
---

# CAPEC-28 - Fuzzing

**Abstraction:** Meta  -  **Likelihood:** High  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-28](https://capec.mitre.org/data/definitions/28.html)

## Description
In this attack pattern, the adversary leverages fuzzing to try to identify weaknesses in the system. Fuzzing is a software security and functionality testing method that feeds randomly constructed input to the system and looks for an indication that a failure in response to that input has occurred. Fuzzing treats the system as a black box and is totally free from any preconceptions or assumptions about the system. Fuzzing can help an attacker discover certain assumptions made about user input in the system. Fuzzing gives an attacker a quick way of potentially uncovering some of these assumptions despite not necessarily knowing anything about the internals of the system. These assumptions can then be turned against the system by specially crafting user input that may allow an attacker to achieve their goals.

## Skills required
- **Low**: There is a wide variety of fuzzing tools available.

## Resources required
- Fuzzing tools.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Unreliable Execution, Alter Execution Logic
- **Confidentiality**: Read Data, Gain Privileges, Alter Execution Logic
- **Integrity**: Modify Data, Alter Execution Logic

## Execution flow
Execution Flow Explore Observe communication and inputs: The fuzzing attacker observes the target system looking for inputs and communications between modules, subsystems, or systems. Techniques Network sniffing. Using a network sniffer such as wireshark, the attacker observes communications into and out of the target system. Monitor API execution. Using a tool such as ktrace, strace, APISpy, or another debugging tool, the attacker observes the system calls and API calls that are made by the target system, and the nature of their parameters. Observe inputs using web inspection tools (OWASP's WebScarab, Paros, TamperData, TamperIE, etc.) Experiment Generate fuzzed inputs: Given a fuzzing tool, a target input or protocol, and limits on time, complexity, and input variety, generate a list of inputs to try. Although fuzzing is random, it is not exhaustive. Parameters like length, composition, and how many variations to try are important to get the most cost-effective impact from the fuzzer. Techniques Boundary cases. Generate fuzz inputs that attack boundary cases of protocol fields, inputs, or other communications limits. Examples include 0xff and 0x00 for single-byte inputs. In binary situations, approach each bit of an individual field with on and off (e.g., 0x80). Attempt arguments to system calls or APIs. The variations include payloads that, if they were successful, could lead to a compromise on the system. Observe the outcome: Observe the outputs to the inputs fed into the system by fuzzers and see if anything interesting happens. If failure occurs, determine why that happened. Figure out the underlying assumption that was invalidated by the input. Exploit Craft exploit payloads: Put specially crafted input into the system that leverages the weakness identified through fuzzing and allows to achieve the goals of the attacker. Fuzzers often reveal ways to slip through the input validation filters and introduce unwanted data into the system. Techniques Identify and embed shell code for the target system. Embed higher level attack commands in the payload. (e.g., SQL, PHP, server-side includes, etc.) Induce denial of service by exploiting resource leaks or bad error handling.

## Mitigations
- Test to ensure that the software behaves as per specification and that there are no unintended side effects. Ensure that no assumptions about the validity of data are made.
- Use fuzz testing during the software QA process to uncover any surprises, uncover any assumptions or unexpected behavior.

## Related weaknesses (CWE)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/28.html
