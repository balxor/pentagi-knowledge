---
cwe_id: CWE-642
name: External Control of Critical State Data
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific, Web Server]
related_capec: [CAPEC-21, CAPEC-31]
url: https://cwe.mitre.org/data/definitions/642.html
tags: [mitre-cwe, weakness, CWE-642]
---

# CWE-642 - External Control of Critical State Data

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-642](https://cwe.mitre.org/data/definitions/642.html)

## Description
The product stores security-critical state information about its users, or the product itself, in a location that is accessible to unauthorized actors.

## Extended description
If an attacker can modify the state information without detection, then it could be used to perform unauthorized actions or access unexpected resources, since the application programmer does not expect that the state can be changed. State information can be stored in various locations such as a cookie, in a hidden web form field, input parameter or argument, an environment variable, a database record, within a settings file, etc. All of these locations have the potential to be modified by an attacker. When this state information is used to control security or determine resource usage, then it may create a vulnerability. For example, an application may perform authentication, then save the state in an "authenticated=true" cookie. An attacker may simply create this cookie in order to bypass the authentication.

## Applicable platforms / languages
Not Language-Specific, Web Server

## Common consequences
- **Access Control**: Bypass Protection Mechanism, Gain Privileges or Assume Identity
- **Confidentiality**: Read Application Data
- **Availability**: DoS: Crash, Exit, or Restart

## Potential mitigations
- **Architecture and Design**: Understand all the potential locations that are accessible to attackers. For example, some programmers assume that cookies and hidden form fields cannot be modified by an attacker, or they may not consider that environment variables can be modified before a privileged program is invoked.
- **Architecture and Design**: Store state information and sensitive data on the server side only. Ensure that the system definitively and unambiguously keeps track of its own state and user state and has rules defined for legitimate state transitions. Do not allow any application user to affect state directly in any way other than through legitimate actions leading to state transitions. If information must be stored on the client, do not do so without encryption and integrity checking, or otherwise having a mechanism on the server side to catch tampering. Use a message authentication code (MAC) algorithm, such as Hash Message Authentication Code (HMAC) [REF-529]. Apply this against the state or sensitive data that has to be exposed, which can guarantee the integrity of the data - i.e., that the data has not been modified. Ensure that a strong hash function is used (CWE-328).
- **Architecture and Design**: Store state information on the server side only. Ensure that the system definitively and unambiguously keeps track of its own state and user state and has rules defined for legitimate state transitions. Do not allow any application user to affect state directly in any way other than through legitimate actions leading to state transitions.
- **Architecture and Design**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid [REF-1482]. With a stateless protocol such as HTTP, use some frameworks can maintain the state for you. Examples include ASP.NET View State and the OWASP ESAPI Session Management feature. Be careful of language features that provide state support, since these might be provided as a convenience to the programmer and may not be considering security.
- **Architecture and Design**: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server.
- **Operation, Implementation**: When using PHP, configure the application so that it does not use register_globals. During implementation, develop the application so that it does not rely on this feature, but be wary of implementing a register_globals emulation that is subject to weaknesses such as CWE-95, CWE-621, and similar issues.

## Related attack patterns (CAPEC)
- [CAPEC-21](https://capec.mitre.org/data/definitions/21.html)
- [CAPEC-31](https://capec.mitre.org/data/definitions/31.html)

## Related weaknesses
- CWE-668 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-2428**: Mail client stores password hashes for unrelated accounts in a hidden form field.
- **CVE-2008-0306**: Privileged program trusts user-specified environment variable to modify critical configuration settings.
- **CVE-1999-0073**: Telnet daemon allows remote clients to specify critical environment variables for the server, leading to code execution.
- **CVE-2007-4432**: Untrusted search path vulnerability through modified LD_LIBRARY_PATH environment variable.
- **CVE-2006-7191**: Untrusted search path vulnerability through modified LD_LIBRARY_PATH environment variable.
- **CVE-2008-5738**: Calendar application allows bypass of authentication by setting a certain cookie value to 1.
- **CVE-2008-5642**: Setting of a language preference in a cookie enables path traversal attack.
- **CVE-2008-5125**: Application allows admin privileges by setting a cookie value to "admin."
- **CVE-2008-5065**: Application allows admin privileges by setting a cookie value to "admin."
- **CVE-2008-4752**: Application allows admin privileges by setting a cookie value to "admin."
- **CVE-2000-0102**: Shopping cart allows price modification via hidden form field.
- **CVE-2000-0253**: Shopping cart allows price modification via hidden form field.
- **CVE-2008-1319**: Server allows client to specify the search path, which can be modified to point to a program that the client has uploaded.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/642.html
