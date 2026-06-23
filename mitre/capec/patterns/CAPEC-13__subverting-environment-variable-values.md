---
capec_id: CAPEC-13
name: Subverting Environment Variable Values
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Very High
related_cwe: [CWE-353, CWE-285, CWE-302, CWE-74, CWE-15, CWE-73, CWE-20, CWE-200]
related_attack: [T1562.003, T1574.006, T1574.007]
url: https://capec.mitre.org/data/definitions/13.html
tags: [mitre-capec, attack-pattern, CAPEC-13]
---

# CAPEC-13 - Subverting Environment Variable Values

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-13](https://capec.mitre.org/data/definitions/13.html)

## Description
The adversary directly or indirectly modifies environment variables used by or controlling the target software. The adversary's goal is to cause the target software to deviate from its expected operation in a manner that benefits the adversary.

## Prerequisites
- An environment variable is accessible to the user.
- An environment variable used by the application can be tainted with user supplied data.
- Input data used in an environment variable is not validated properly.
- The variables encapsulation is not done properly. For instance setting a variable as public in a class makes it visible and an adversary may attempt to manipulate that variable.

## Skills required
- **High**: Some more advanced attacks may require knowledge about protocols and probing technique which help controlling a variable. The malicious user may try to understand the authentication mechanism in order to defeat it.
- **Low**: In a web based scenario, the client controls the data that it submitted to the server. So anybody can try to send malicious data and try to bypass the authentication mechanism.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Accountability**: Hide Activities
- **Authorization**: Bypass Protection Mechanism
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code), Unreliable Execution
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Bypass Protection Mechanism, Read Data
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Probe target application: The adversary first probes the target application to determine important information about the target. This information could include types software used, software versions, what user input the application consumes, and so on. Most importantly, the adversary tries to determine what environment variables might be used by the underlying software, or even the application itself. Experiment Find user-controlled environment variables: Using the information found by probing the application, the adversary attempts to manipulate any user-controlled environment variables they have found are being used by the application, or suspect are being used by the application, and observe the effects of these changes. If the adversary notices any significant changes to the application, they will know that a certain environment variable is important to the application behavior and indicates a possible attack vector. Techniques Alter known environment variables such as "$PATH", "$HOSTNAME", or "LD_LIBRARY_PATH" and see if application behavior changes. Exploit Manipulate user-controlled environment variables: The adversary manipulates the found environment variable(s) to abuse the normal flow of processes or to gain access to privileged resources.

## Mitigations
- Protect environment variables against unauthorized read and write access.
- Protect the configuration files which contain environment variables against illegitimate read and write access.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.
- Apply the least privilege principles. If a process has no legitimate reason to read an environment variable do not give that privilege.

## Related weaknesses (CWE)
- [CWE-353](https://cwe.mitre.org/data/definitions/353.html)
- [CWE-285](https://cwe.mitre.org/data/definitions/285.html)
- [CWE-302](https://cwe.mitre.org/data/definitions/302.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-15](https://cwe.mitre.org/data/definitions/15.html)
- [CWE-73](https://cwe.mitre.org/data/definitions/73.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

## Related ATT&CK techniques
- T1562.003
- T1574.006
- T1574.007

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/13.html
