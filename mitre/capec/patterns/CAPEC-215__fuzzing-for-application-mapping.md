---
capec_id: CAPEC-215
name: Fuzzing for application mapping
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Low
related_cwe: [CWE-209, CWE-532]
related_attack: []
url: https://capec.mitre.org/data/definitions/215.html
tags: [mitre-capec, attack-pattern, CAPEC-215]
---

# CAPEC-215 - Fuzzing for application mapping

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Low  -  **CAPEC:** [CAPEC-215](https://capec.mitre.org/data/definitions/215.html)

## Description
An attacker sends random, malformed, or otherwise unexpected messages to a target application and observes the application's log or error messages returned. The attacker does not initially know how a target will respond to individual messages but by attempting a large number of message variants they may find a variant that trigger's desired behavior. In this attack, the purpose of the fuzzing is to observe the application's log and error messages, although fuzzing a target can also sometimes cause the target to enter an unstable state, causing a crash.

## Extended description
By observing logs and error messages, the attacker can learn details about the configuration of the target application and might be able to cause the target to disclose sensitive information. In applications that return a stack trace along with the error, this can enumerate the chain of methods that led up to the point where the error was encountered. This can not only reveal the names of the methods (some of which may have known weaknesses) but possibly also the location of class files and libraries as well as parameter values. In some cases, the stack trace might even disclose sensitive configuration or user information.

## Prerequisites
- The target application must fail to sanitize incoming messages adequately before processing.

## Skills required
- **Medium**: Although fuzzing parameters is not difficult, and often possible with automated fuzzing tools, interpreting the error conditions and modifying the parameters so as to move further in the process of mapping the application requires detailed knowledge of target platform, the languages and packages used as well as software design.

## Resources required
- Fuzzing tools, which automatically generate and send message variants, are necessary for this attack. The attacker must have sufficient access to send messages to the target. The attacker must also have the ability to observe the target application's log and/or error messages in order to collect information about the target.

## Consequences
- **Confidentiality**: Other (Information Leakage)

## Execution flow
Execution Flow Explore Observe communication and inputs: The fuzzing adversary observes the target system looking for inputs and communications between modules, subsystems, or systems. Techniques Network sniffing. Using a network sniffer such as wireshark, the adversary observes communications into and out of the target system. Monitor API execution. Using a tool such as ktrace, strace, APISpy, or another debugging tool, the adversary observes the system calls and API calls that are made by the target system, and the nature of their parameters. Observe inputs using web inspection tools (OWASP's WebScarab, Paros, TamperData, TamperIE, etc.) Experiment Generate fuzzed inputs: Given a fuzzing tool, a target input or protocol, and limits on time, complexity, and input variety, generate a list of inputs to try. Although fuzzing is random, it is not exhaustive. Parameters like length, composition, and how many variations to try are important to get the most cost-effective impact from the fuzzer. Techniques Boundary cases. Generate fuzz inputs that attack boundary cases of protocol fields, inputs, or other communications limits. Examples include 0xff and 0x00 for single-byte inputs. In binary situations, approach each bit of an individual field with on and off (e.g., 0x80). Attempt arguments to system calls or APIs. The variations include payloads that, if they were successful, could lead to a compromise on the system. Observe the outcome: Observe the outputs to the inputs fed into the system by fuzzers and see if there are any log or error messages that might provide information to map the application Exploit Craft exploit payloads: An adversary usually needs to modify the fuzzing parameters according to the observed error messages to get the desired sensitive information for the application. To defeat correlation, the adversary may try changing the origin IP addresses or client browser identification strings or start a new session from where they left off in obfuscating the attack. Techniques Modify the parameters in the fuzzing tool according to the observed error messages. Repeat with enough parameters until the application has been sufficiently mapped. If the application rejects the large amount of fuzzing messages from the same host machine, the adversary needs to hide the attacks by changing the IP addresses or other credentials.

## Mitigations
- Design: Construct a 'code book' for error messages. When using a code book, application error messages aren't generated in string or stack trace form, but are catalogued and replaced with a unique (often integer-based) value 'coding' for the error. Such a technique will require helpdesk and hosting personnel to use a 'code book' or similar mapping to decode application errors/logs in order to respond to them normally.
- Design: wrap application functionality (preferably through the underlying framework) in an output encoding scheme that obscures or cleanses error messages to prevent such attacks. Such a technique is often used in conjunction with the above 'code book' suggestion.
- Implementation: Obfuscate server fields of HTTP response.
- Implementation: Hide inner ordering of HTTP response header.
- Implementation: Customizing HTTP error codes such as 404 or 500.
- Implementation: Hide HTTP response header software information filed.
- Implementation: Hide cookie's software information filed.
- Implementation: Obfuscate database type in Database API's error message.

## Related weaknesses (CWE)
- [CWE-209](https://cwe.mitre.org/data/definitions/209.html)
- [CWE-532](https://cwe.mitre.org/data/definitions/532.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/215.html
