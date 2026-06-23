---
capec_id: CAPEC-74
name: Manipulating State
type: attack-pattern
abstraction: Meta
likelihood: Medium
severity: High
related_cwe: [CWE-372, CWE-315, CWE-353, CWE-693, CWE-1245, CWE-1253, CWE-1265, CWE-1271]
related_attack: []
url: https://capec.mitre.org/data/definitions/74.html
tags: [mitre-capec, attack-pattern, CAPEC-74]
---

# CAPEC-74 - Manipulating State

**Abstraction:** Meta  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-74](https://capec.mitre.org/data/definitions/74.html)

## Description
<xhtml:p>The adversary modifies state information maintained by the target software or causes a state transition in hardware. If successful, the target will use this tainted state and execute in an unintended manner.</xhtml:p>
            <xhtml:p>State management is an important function within a software application. User state maintained by the application can include usernames, payment information, browsing history as well as application-specific contents such as items in a shopping cart. Manipulating user state can be employed by an adversary to elevate privilege, conduct fraudulent transactions or otherwise modify the flow of the application to derive certain benefits.</xhtml:p>
            <xhtml:p>If there is a hardware logic error in a finite state machine, the adversary can use this to put the system in an undefined state which could cause a denial of service or exposure of secure data.</xhtml:p>

## Prerequisites
- User state is maintained at least in some way in user-controllable locations, such as cookies or URL parameters.
- There is a faulty finite state machine in the hardware logic that can be exploited.

## Skills required
- **Medium**: The adversary needs to have knowledge of state management as employed by the target application, and also the ability to manipulate the state in a meaningful way.

## Resources required
- The adversary needs a data tampering tool capable of generating and creating custom inputs to aid in the attack, like Fiddler, Wireshark, or a similar in-browser plugin (e.g., Tamper Data for Firefox).

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Unreliable Execution
- **Confidentiality**: Gain Privileges
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Adversary determines the nature of state management employed by the target. This includes determining the location (client-side, server-side or both applications) and possibly the items stored as part of user state. Experiment The adversary now tries to modify the user state contents (possibly indiscriminately if the contents are encrypted or otherwise obfuscated) or cause a state transition and observe the effects of this change on the target. Exploit Having determined how to manipulate the state, the adversary can perform illegitimate actions.

## Mitigations
- Do not rely solely on user-controllable locations, such as cookies or URL parameters, to maintain user state.
- Avoid sensitive information, such as usernames or authentication and authorization information, in user-controllable locations.
- Sensitive information that is part of the user state must be appropriately protected to ensure confidentiality and integrity at each request.
- All possible states must be handled by hardware finite state machines.

## Related weaknesses (CWE)
- [CWE-372](https://cwe.mitre.org/data/definitions/372.html)
- [CWE-315](https://cwe.mitre.org/data/definitions/315.html)
- [CWE-353](https://cwe.mitre.org/data/definitions/353.html)
- [CWE-693](https://cwe.mitre.org/data/definitions/693.html)
- [CWE-1245](https://cwe.mitre.org/data/definitions/1245.html)
- [CWE-1253](https://cwe.mitre.org/data/definitions/1253.html)
- [CWE-1265](https://cwe.mitre.org/data/definitions/1265.html)
- [CWE-1271](https://cwe.mitre.org/data/definitions/1271.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/74.html
