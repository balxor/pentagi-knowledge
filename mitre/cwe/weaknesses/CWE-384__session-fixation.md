---
cwe_id: CWE-384
name: Session Fixation
type: weakness
abstraction: Compound
status: Incomplete
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: [CAPEC-196, CAPEC-21, CAPEC-31, CAPEC-39, CAPEC-59, CAPEC-60, CAPEC-61]
url: https://cwe.mitre.org/data/definitions/384.html
tags: [mitre-cwe, weakness, CWE-384]
---

# CWE-384 - Session Fixation

**Abstraction:** Compound  -  **Status:** Incomplete  -  **CWE:** [CWE-384](https://cwe.mitre.org/data/definitions/384.html)

## Description
Authenticating a user, or otherwise establishing a new user session, without invalidating any existing session identifier gives an attacker the opportunity to steal authenticated sessions.

## Extended description
Such a scenario is commonly observed when: A web application authenticates a user without first invalidating the existing session, thereby continuing to use the session already associated with the user. An attacker is able to force a known session identifier on a user so that, once the user authenticates, the attacker has access to the authenticated session. The application or container uses predictable session identifiers. In the generic exploit of session fixation vulnerabilities, an attacker creates a new session on a web application and records the associated session identifier. The attacker then causes the victim to associate, and possibly authenticate, against the server using that session identifier, giving the attacker access to the user's account through the active session.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Invalidate any existing session identifiers prior to authorizing a new user session.
- **Architecture and Design**: For platforms such as ASP that do not generate new values for sessionid cookies, utilize a secondary cookie. In this approach, set a secondary cookie on the user's browser to a random value and set a session variable to the same value. If the session variable and the cookie value ever don't match, invalidate the session, and force the user to log on again.
- **Operation**: Use an application firewall that can detect attacks against this weakness. It can be beneficial in cases in which the code cannot be fixed (because it is controlled by a third party), as an emergency prevention measure while more comprehensive software assurance measures are applied, or to provide defense in depth [REF-1481].

## Related attack patterns (CAPEC)
- [CAPEC-196](https://capec.mitre.org/data/definitions/196.html)
- [CAPEC-21](https://capec.mitre.org/data/definitions/21.html)
- [CAPEC-31](https://capec.mitre.org/data/definitions/31.html)
- [CAPEC-39](https://capec.mitre.org/data/definitions/39.html)
- [CAPEC-59](https://capec.mitre.org/data/definitions/59.html)
- [CAPEC-60](https://capec.mitre.org/data/definitions/60.html)
- [CAPEC-61](https://capec.mitre.org/data/definitions/61.html)

## Related weaknesses
- CWE-610 (ChildOf)
- CWE-610 (ChildOf)
- CWE-346 (Requires)
- CWE-472 (Requires)
- CWE-441 (Requires)

## Observed examples (CVE)
- **CVE-2022-2820**: Website software for game servers does not proprerly terminate user sessions, allowing for possible session fixation

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/384.html
