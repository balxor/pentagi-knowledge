---
cwe_id: CWE-362
name: Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')
type: weakness
abstraction: Class
status: Draft
languages: [C, C++, Java, Mobile, ICS/OT]
related_capec: [CAPEC-26, CAPEC-29]
url: https://cwe.mitre.org/data/definitions/362.html
tags: [mitre-cwe, weakness, CWE-362]
---

# CWE-362 - Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-362](https://cwe.mitre.org/data/definitions/362.html)

## Description
The product contains a concurrent code sequence that requires temporary, exclusive access to a shared resource, but a timing window exists in which the shared resource can be modified by another code sequence operating concurrently.

## Extended description
A race condition occurs within concurrent environments, and it is effectively a property of a code sequence. Depending on the context, a code sequence may be in the form of a function call, a small number of instructions, a series of program invocations, etc. A race condition violates these properties, which are closely related: Exclusivity - the code sequence is given exclusive access to the shared resource, i.e., no other code sequence can modify properties of the shared resource before the original sequence has completed execution. Atomicity - the code sequence is behaviorally atomic, i.e., no other thread or process can concurrently execute the same sequence of instructions (or a subset) against the same resource. A race condition exists when an "interfering code sequence" can still access the shared resource, violating exclusivity. The interfering code sequence could be "trusted" or "untrusted." A trusted interfering code sequence occurs within the product; it cannot be modified by the attacker, and it can only be invoked indirectly. An untrusted interfering code sequence can be authored directly by the attacker, and typically it is external to the vulnerable product.

## Applicable platforms / languages
C, C++, Java, Mobile, ICS/OT

## Common consequences
- **Availability**: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Resource Consumption (Other)
- **Availability**: DoS: Crash, Exit, or Restart, DoS: Instability
- **Confidentiality, Integrity**: Read Files or Directories, Read Application Data
- **Access Control**: Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity, Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: In languages that support it, use synchronization primitives. Only wrap these around critical code to minimize the impact on performance.
- **Architecture and Design**: Use thread-safe capabilities such as the data access abstraction in Spring.
- **Architecture and Design**: Minimize the usage of shared resources in order to remove as much complexity as possible from the control flow and to reduce the likelihood of unexpected conditions occurring. Additionally, this will minimize the amount of synchronization necessary and may even help to reduce the likelihood of a denial of service where an attacker may be able to repeatedly trigger a critical section (CWE-400).
- **Implementation**: When using multithreading and operating on shared variables, only use thread-safe functions.
- **Implementation**: Use atomic operations on shared variables. Be wary of innocent-looking constructs such as "x++". This may appear atomic at the code layer, but it is actually non-atomic at the instruction layer, since it involves a read, followed by a computation, followed by a write.
- **Implementation**: Use a mutex if available, but be sure to avoid related weaknesses such as CWE-412.
- **Implementation**: Avoid double-checked locking (CWE-609) and other implementation errors that arise when trying to avoid the overhead of synchronization.
- **Implementation**: Disable interrupts or signals over critical parts of the code, but also make sure that the code does not go into a large or infinite loop.
- **Implementation**: Use the volatile type modifier for critical variables to avoid unexpected compiler optimization or reordering. This does not necessarily solve the synchronization problem, but it can help.
- **Architecture and Design, Operation**: Run your code using the lowest privileges that are required to accomplish the necessary tasks [REF-76]. If possible, create isolated accounts with limited privileges that are only used for a single task. That way, a successful attack will not immediately give the attacker access to the rest of the software or its environment. For example, database applications rarely need to run as the database administrator, especially in day-to-day operations.

## Related attack patterns (CAPEC)
- [CAPEC-26](https://capec.mitre.org/data/definitions/26.html)
- [CAPEC-29](https://capec.mitre.org/data/definitions/29.html)

## Related weaknesses
- CWE-662 (ChildOf)
- CWE-416 (CanPrecede)
- CWE-476 (CanPrecede)

## Observed examples (CVE)
- **CVE-2024-38106**: OS kernel stores sensitive data in improperly locked memory, allowing local users to gain privileges by winning a race condition
- **CVE-2022-29527**: Go application for cloud management creates a world-writable sudoers file that allows local attackers to inject sudo rules and escalate privileges to root by winning a race condition.
- **CVE-2021-1782**: Chain: improper locking (CWE-667) leads to race condition (CWE-362), as exploited in the wild per CISA KEV.
- **CVE-2021-0920**: Chain: mobile platform race condition (CWE-362) leading to use-after-free (CWE-416), as exploited in the wild per CISA KEV.
- **CVE-2020-6819**: Chain: race condition (CWE-362) leads to use-after-free (CWE-416), as exploited in the wild per CISA KEV.
- **CVE-2019-18827**: chain: JTAG interface is not disabled (CWE-1191) during ROM code execution, introducing a race condition (CWE-362) to extract encryption keys
- **CVE-2019-1161**: Chain: race condition (CWE-362) in anti-malware product allows deletion of files by creating a junction (CWE-1386) and using hard links during the time window in which a temporary file is created and deleted.
- **CVE-2015-1743**: TOCTOU in sandbox process allows installation of untrusted browser add-ons by replacing a file after it has been verified, but before it is executed
- **CVE-2014-8273**: Chain: chipset has a race condition (CWE-362) between when an interrupt handler detects an attempt to write-enable the BIOS (in violation of the lock bit), and when the handler resets the write-enable bit back to 0, allowing attackers to issue BIOS writes during the timing window [REF-1237].
- **CVE-2008-5044**: Race condition leading to a crash by calling a hook removal procedure while other activities are occurring at the same time.
- **CVE-2008-2958**: chain: time-of-check time-of-use (TOCTOU) race condition in program allows bypass of protection mechanism that was designed to prevent symlink attacks.
- **CVE-2008-1570**: chain: time-of-check time-of-use (TOCTOU) race condition in program allows bypass of protection mechanism that was designed to prevent symlink attacks.
- **CVE-2008-0058**: Unsynchronized caching operation enables a race condition that causes messages to be sent to a deallocated object.
- **CVE-2008-0379**: Race condition during initialization triggers a buffer overflow.
- **CVE-2007-6599**: Daemon crash by quickly performing operations and undoing them, which eventually leads to an operation that does not acquire a lock.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/362.html
