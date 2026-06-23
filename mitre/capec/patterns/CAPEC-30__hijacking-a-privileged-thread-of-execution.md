---
capec_id: CAPEC-30
name: Hijacking a Privileged Thread of Execution
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: Very High
related_cwe: [CWE-270]
related_attack: [T1055.003]
url: https://capec.mitre.org/data/definitions/30.html
tags: [mitre-capec, attack-pattern, CAPEC-30]
---

# CAPEC-30 - Hijacking a Privileged Thread of Execution

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-30](https://capec.mitre.org/data/definitions/30.html)

## Description
An adversary hijacks a privileged thread of execution by injecting malicious code into a running process. By using a privleged thread to do their bidding, adversaries can evade process-based detection that would stop an attack that creates a new process. This can lead to an adversary gaining access to the process's memory and can also enable elevated privileges. The most common way to perform this attack is by suspending an existing thread and manipulating its memory.

## Prerequisites
- The application in question employs a threaded model of execution with the threads operating at, or having the ability to switch to, a higher privilege level than normal users
- In order to feasibly execute this class of attacks, the adversary must have the ability to hijack a privileged thread. This ability includes, but is not limited to, modifying environment variables that affect the process the thread belongs to, or calling native OS calls that can suspend and alter process memory. This does not preclude network-based attacks, but makes them conceptually more difficult to identify and execute.

## Skills required
- **High**: Hijacking a thread involves knowledge of how processes and threads function on the target platform, the design of the target application as well as the ability to identify the primitives to be used or manipulated to hijack the thread.

## Resources required
- None: No specialized resources are required to execute this type of attack. The adversary needs to be able to latch onto a privileged thread. The adversary does, however, need to be able to program, compile, and link to the victim binaries being executed so that it will turn control of a privileged thread over to the adversary's malicious code. This is the case even if the adversary conducts the attack remotely.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Gain Privileges, Execute Unauthorized Commands (Run Arbitrary Code)
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Determine target thread: The adversary determines the underlying system thread that is subject to user-control Experiment Gain handle to thread: The adversary then gains a handle to a process thread. Techniques Use the "OpenThread" API call in Windows on a known thread. Cause an exception in a java privileged block public function and catch it, or catch a normal signal. The thread is then hanging and the adversary can attempt to gain a handle to it. Alter process memory: Once the adversary has a handle to the target thread, they will suspend the thread and alter the memory using native OS calls. Techniques On Windows, use "SuspendThread" followed by "VirtualAllocEx", "WriteProcessMemory", and "SetThreadContext". Exploit Resume thread execution: Once the process memory has been altered to execute malicious code, the thread is then resumed. Techniques On Windows, use "ResumeThread".

## Mitigations
- Application Architects must be careful to design callback, signal, and similar asynchronous constructs such that they shed excess privilege prior to handing control to user-written (thus untrusted) code.
- Application Architects must be careful to design privileged code blocks such that upon return (successful, failed, or unpredicted) that privilege is shed prior to leaving the block/scope.

## Related weaknesses (CWE)
- [CWE-270](https://cwe.mitre.org/data/definitions/270.html)

## Related ATT&CK techniques
- T1055.003

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/30.html
