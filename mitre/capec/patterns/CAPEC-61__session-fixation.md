---
capec_id: CAPEC-61
name: Session Fixation
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-384, CWE-664, CWE-732]
related_attack: []
url: https://capec.mitre.org/data/definitions/61.html
tags: [mitre-capec, attack-pattern, CAPEC-61]
---

# CAPEC-61 - Session Fixation

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-61](https://capec.mitre.org/data/definitions/61.html)

## Description
The attacker induces a client to establish a session with the target software using a session identifier provided by the attacker. Once the user successfully authenticates to the target software, the attacker uses the (now privileged) session identifier in their own transactions. This attack leverages the fact that the target software either relies on client-generated session identifiers or maintains the same session identifiers after privilege elevation.

## Prerequisites
- Session identifiers that remain unchanged when the privilege levels change.
- Permissive session management mechanism that accepts random user-generated session identifiers
- Predictable session identifiers

## Skills required
- **Low**: Only basic skills are required to determine and fixate session identifiers in a user's browser. Subsequent attacks may require greater skill levels depending on the attackers' motives.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges

## Execution flow
Execution Flow Explore Setup the Attack: Setup a session: The attacker has to setup a trap session that provides a valid session identifier, or select an arbitrary identifier, depending on the mechanism employed by the application. A trap session is a dummy session established with the application by the attacker and is used solely for the purpose of obtaining valid session identifiers. The attacker may also be required to periodically refresh the trap session in order to obtain valid session identifiers. Techniques The attacker chooses a predefined identifier that they know. The attacker creates a trap session for the victim. Experiment Attract a Victim: Fixate the session: The attacker now needs to transfer the session identifier from the trap session to the victim by introducing the session identifier into the victim's browser. This is known as fixating the session. The session identifier can be introduced into the victim's browser by leveraging cross site scripting vulnerability, using META tags or setting HTTP response headers in a variety of ways. Techniques Attackers can put links on web sites (such as forums, blogs, or comment forms). Attackers can establish rogue proxy servers for network protocols that give out the session ID and then redirect the connection to the legitimate service. Attackers can email attack URLs to potential victims through spam and phishing techniques. Exploit Abuse the Victim's Session: Takeover the fixated session: Once the victim has achieved a higher level of privilege, possibly by logging into the application, the attacker can now take over the session using the fixated session identifier. Techniques The attacker loads the predefined session ID into their browser and browses to protected data or functionality. The attacker loads the predefined session ID into their software and utilizes functionality with the rights of the victim.

## Mitigations
- Use a strict session management mechanism that only accepts locally generated session identifiers: This prevents attackers from fixating session identifiers of their own choice.
- Regenerate and destroy session identifiers when there is a change in the level of privilege: This ensures that even though a potential victim may have followed a link with a fixated identifier, a new one is issued when the level of privilege changes.
- Use session identifiers that are difficult to guess or brute-force: One way for the attackers to obtain valid session identifiers is by brute-forcing or guessing them. By choosing session identifiers that are sufficiently random, brute-forcing or guessing becomes very difficult.

## Related weaknesses (CWE)
- [CWE-384](https://cwe.mitre.org/data/definitions/384.html)
- [CWE-664](https://cwe.mitre.org/data/definitions/664.html)
- [CWE-732](https://cwe.mitre.org/data/definitions/732.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/61.html
