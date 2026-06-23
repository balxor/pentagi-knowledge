---
capec_id: CAPEC-107
name: Cross Site Tracing
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Very High
related_cwe: [CWE-693, CWE-648]
related_attack: []
url: https://capec.mitre.org/data/definitions/107.html
tags: [mitre-capec, attack-pattern, CAPEC-107]
---

# CAPEC-107 - Cross Site Tracing

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-107](https://capec.mitre.org/data/definitions/107.html)

## Description
Cross Site Tracing (XST) enables an adversary to steal the victim's session cookie and possibly other authentication credentials transmitted in the header of the HTTP request when the victim's browser communicates to a destination system's web server.

## Extended description
The adversary uses an XSS attack to have victim's browser sent an HTTP TRACE request to a destination web server, which will proceed to return a response to the victim's web browser that contains the original HTTP request in its body. Since the HTTP header of the original HTTP TRACE request had the victim's session cookie in it, that session cookie can now be picked off the HTTP TRACE response and sent to the adversary's malicious site. XST becomes relevant when direct access to the session cookie via the "document.cookie" object is disabled with the use of httpOnly attribute which ensures that the cookie can be transmitted in HTTP requests but cannot be accessed in other ways. Using SSL does not protect against XST. If the system with which the victim is interacting is susceptible to XSS, an adversary can exploit that weakness directly to get their malicious script to issue an HTTP TRACE request to the destination system's web server.

## Prerequisites
- HTTP TRACE is enabled on the web server
- The destination system is susceptible to XSS or an adversary can leverage some other weakness to bypass the same origin policy
- Scripting is enabled in the client's browser
- HTTP is used as the communication protocol between the server and the client

## Skills required
- **Medium**: Understanding of the HTTP protocol and an ability to craft a malicious script

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Read Data, Gain Privileges
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Determine if HTTP Trace is enabled: Determine if HTTP Trace is enabled at the web server with which the victim has an active session Techniques An adversary may issue an HTTP Trace request to the target web server and observe if the response arrives with the original request in the body of the response. Experiment Identify mechanism to launch HTTP Trace request: The adversary attempts to force the victim to issue an HTTP Trace request to the targeted application. Techniques The adversary probes for cross-site scripting vulnerabilities to force the victim into issuing an HTTP Trace request. Exploit Create a malicious script that pings the web server with HTTP TRACE request: The adversary creates a malicious script that will induce the victim's browser to issue an HTTP TRACE request to the destination system's web server. The script will further intercept the response from the web server, pick up sensitive information out of it, and forward to the site controlled by the adversary. Techniques The adversary's malicious script circumvents the httpOnly cookie attribute that prevents from hijacking the victim's session cookie directly using document.cookie and instead leverages the HTTP TRACE to catch this information from the header of the HTTP request once it is echoed back from the web server in the body of the HTTP TRACE response. Execute malicious HTTP Trace launching script: The adversary leverages an XSS vulnerability to force the victim to execute the malicious HTTP Trace launching script Intercept HTTP TRACE response: The adversary's script intercepts the HTTP TRACE response from teh web server, glance sensitive information from it, and forward that information to a server controlled by the adversary.

## Mitigations
- Administrators should disable support for HTTP TRACE at the destination's web server. Vendors should disable TRACE by default.
- Patch web browser against known security origin policy bypass exploits.

## Related weaknesses (CWE)
- [CWE-693](https://cwe.mitre.org/data/definitions/693.html)
- [CWE-648](https://cwe.mitre.org/data/definitions/648.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/107.html
