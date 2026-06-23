---
capec_id: CAPEC-69
name: Target Programs with Elevated Privileges
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Very High
related_cwe: [CWE-250, CWE-15]
related_attack: []
url: https://capec.mitre.org/data/definitions/69.html
tags: [mitre-capec, attack-pattern, CAPEC-69]
---

# CAPEC-69 - Target Programs with Elevated Privileges

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-69](https://capec.mitre.org/data/definitions/69.html)

## Description
This attack targets programs running with elevated privileges. The adversary tries to leverage a vulnerability in the running program and get arbitrary code to execute with elevated privileges.

## Prerequisites
- The targeted program runs with elevated OS privileges.
- The targeted program accepts input data from the user or from another program.
- The targeted program is giving away information about itself. Before performing such attack, an eventual attacker may need to gather information about the services running on the host target. The more the host target is verbose about the services that are running (version number of application, etc.) the more information can be gather by an attacker.
- This attack often requires communicating with the host target services directly. For instance Telnet may be enough to communicate with the host target.

## Skills required
- **Low**: An attacker can use a tool to scan and automatically launch an attack against known issues. A tool can also repeat a sequence of instructions and try to brute force the service on the host target, an example of that would be the flooding technique.
- **Medium**: More advanced attack may require knowledge of the protocol spoken by the host service.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code), Resource Consumption (Denial of Service)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Find programs with elevated priveleges: The adversary probes for programs running with elevated privileges. Techniques Look for programs that write to the system directories or registry keys (such as HKLM, which stores a number of critical Windows environment variables). These programs are typically running with elevated privileges and have usually not been designed with security in mind. Such programs are excellent exploit targets because they yield lots of power when they break. Find vulnerability in running program: The adversary looks for a vulnerability in the running program that would allow for arbitrary code execution with the privilege of the running program. Techniques Look for improper input validation Look for improper failure safety. For instance when a program fails it may authorize restricted access to anyone. Look for a buffer overflow which may be exploited if an adversary can inject unvalidated data. Exploit Execute arbitrary code: The adversary exploits the vulnerability that they have found. For instance, they can try to inject and execute arbitrary code or write to OS resources.

## Mitigations
- Apply the principle of least privilege.
- Validate all untrusted data.
- Apply the latest patches.
- Scan your services and disable the ones which are not needed and are exposed unnecessarily. Exposing programs increases the attack surface. Only expose the services which are needed and have security mechanisms such as authentication built around them.
- Avoid revealing information about your system (e.g., version of the program) to anonymous users.
- Make sure that your program or service fail safely. What happen if the communication protocol is interrupted suddenly? What happen if a parameter is missing? Does your system have resistance and resilience to attack? Fail safely when a resource exhaustion occurs.
- If possible use a sandbox model which limits the actions that programs can take. A sandbox restricts a program to a set of privileges and commands that make it difficult or impossible for the program to cause any damage.
- Check your program for buffer overflow and format String vulnerabilities which can lead to execution of malicious code.
- Monitor traffic and resource usage and pay attention if resource exhaustion occurs.
- Protect your log file from unauthorized modification and log forging.

## Related weaknesses (CWE)
- [CWE-250](https://cwe.mitre.org/data/definitions/250.html)
- [CWE-15](https://cwe.mitre.org/data/definitions/15.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/69.html
