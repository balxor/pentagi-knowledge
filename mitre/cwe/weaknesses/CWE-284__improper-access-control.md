---
cwe_id: CWE-284
name: Improper Access Control
type: weakness
abstraction: Pillar
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific, ICS/OT, Web Based]
related_capec: [CAPEC-19, CAPEC-441, CAPEC-478, CAPEC-479, CAPEC-502, CAPEC-503, CAPEC-536, CAPEC-546, CAPEC-550, CAPEC-551, CAPEC-552, CAPEC-556, CAPEC-558, CAPEC-562, CAPEC-563, CAPEC-564, CAPEC-578]
url: https://cwe.mitre.org/data/definitions/284.html
tags: [mitre-cwe, weakness, CWE-284]
---

# CWE-284 - Improper Access Control

**Abstraction:** Pillar  -  **Status:** Incomplete  -  **CWE:** [CWE-284](https://cwe.mitre.org/data/definitions/284.html)

## Description
The product does not restrict or incorrectly restricts access to a resource from an unauthorized actor.

## Extended description
Access control involves the use of several protection mechanisms such as: Authentication (proving the identity of an actor) Authorization (ensuring that a given actor can access a resource), and Accountability (tracking of activities that were performed) When any mechanism is not applied or otherwise fails, attackers can compromise the security of the product by gaining privileges, reading sensitive information, executing commands, evading detection, etc. There are two distinct behaviors that can introduce access control weaknesses: Specification: incorrect privileges, permissions, ownership, etc. are explicitly specified for either the user or the resource (for example, setting a password file to be world-writable, or giving administrator capabilities to a guest user). This action could be performed by the program or the administrator. Enforcement: the mechanism contains errors that prevent it from properly enforcing the specified access control requirements (e.g., allowing the user to specify their own privileges, or allowing a syntactically-incorrect ACL to produce insecure settings). This problem occurs within the program itself, in that it does not actually enforce the intended security policy that the administrator specifies.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, ICS/OT, Web Based

## Common consequences
- **Other**: Varies by Context

## Potential mitigations
- **Architecture and Design, Operation**: Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.
- **Architecture and Design**: Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.

## Related attack patterns (CAPEC)
- [CAPEC-19](https://capec.mitre.org/data/definitions/19.html)
- [CAPEC-441](https://capec.mitre.org/data/definitions/441.html)
- [CAPEC-478](https://capec.mitre.org/data/definitions/478.html)
- [CAPEC-479](https://capec.mitre.org/data/definitions/479.html)
- [CAPEC-502](https://capec.mitre.org/data/definitions/502.html)
- [CAPEC-503](https://capec.mitre.org/data/definitions/503.html)
- [CAPEC-536](https://capec.mitre.org/data/definitions/536.html)
- [CAPEC-546](https://capec.mitre.org/data/definitions/546.html)
- [CAPEC-550](https://capec.mitre.org/data/definitions/550.html)
- [CAPEC-551](https://capec.mitre.org/data/definitions/551.html)
- [CAPEC-552](https://capec.mitre.org/data/definitions/552.html)
- [CAPEC-556](https://capec.mitre.org/data/definitions/556.html)
- [CAPEC-558](https://capec.mitre.org/data/definitions/558.html)
- [CAPEC-562](https://capec.mitre.org/data/definitions/562.html)
- [CAPEC-563](https://capec.mitre.org/data/definitions/563.html)
- [CAPEC-564](https://capec.mitre.org/data/definitions/564.html)
- [CAPEC-578](https://capec.mitre.org/data/definitions/578.html)

## Observed examples (CVE)
- **CVE-2023-26463**: Chain: IPSec VPN product uses the same variable for multiple purposes in the same function (CWE-1109), leading to incorrect access control (CWE-284) and expired pointer dereference (CWE-825)
- **CVE-2022-24985**: A form hosting website only checks the session authentication status for a single form, making it possible to bypass authentication when there are multiple forms
- **CVE-2022-29238**: Access-control setting in web-based document collaboration tool is not properly implemented by the code, which prevents listing hidden directories but does not prevent direct requests to files in those directories.
- **CVE-2022-23607**: Python-based HTTP library did not scope cookies to a particular domain such that "supercookies" could be sent to any domain on redirect
- **CVE-2021-21972**: Chain: Cloud computing virtualization platform does not require authentication for upload of a tar format file (CWE-306), then uses .. path traversal sequences (CWE-23) in the file to access unexpected files, as exploited in the wild per CISA KEV.
- **CVE-2021-37415**: IT management product does not perform authentication for some REST API requests, as exploited in the wild per CISA KEV.
- **CVE-2021-35033**: Firmware for a WiFi router uses a hard-coded password for a BusyBox shell, allowing bypass of authentication through the UART port
- **CVE-2020-10263**: Bluetooth speaker does not require authentication for the debug functionality on the UART port, allowing root shell access
- **CVE-2020-13927**: Default setting in workflow management product allows all API requests without authentication, as exploited in the wild per CISA KEV.
- **CVE-2010-4624**: Bulletin board applies restrictions on number of images during post creation, but does not enforce this on editing.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/284.html
