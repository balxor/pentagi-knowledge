---
cwe_id: CWE-287
name: Improper Authentication
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Technology-Specific, Web Based, ICS/OT]
related_capec: [CAPEC-114, CAPEC-115, CAPEC-151, CAPEC-194, CAPEC-22, CAPEC-57, CAPEC-593, CAPEC-633, CAPEC-650, CAPEC-94]
url: https://cwe.mitre.org/data/definitions/287.html
tags: [mitre-cwe, weakness, CWE-287]
---

# CWE-287 - Improper Authentication

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-287](https://cwe.mitre.org/data/definitions/287.html)

## Description
When an actor claims to have a given identity, the product does not prove or insufficiently proves that the claim is correct.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Technology-Specific, Web Based, ICS/OT

## Common consequences
- **Integrity, Confidentiality, Availability, Access Control**: Read Application Data, Gain Privileges or Assume Identity, Execute Unauthorized Code or Commands

## Potential mitigations
- **Architecture and Design**: Use an authentication framework or library such as the OWASP ESAPI Authentication feature.

## Related attack patterns (CAPEC)
- [CAPEC-114](https://capec.mitre.org/data/definitions/114.html)
- [CAPEC-115](https://capec.mitre.org/data/definitions/115.html)
- [CAPEC-151](https://capec.mitre.org/data/definitions/151.html)
- [CAPEC-194](https://capec.mitre.org/data/definitions/194.html)
- [CAPEC-22](https://capec.mitre.org/data/definitions/22.html)
- [CAPEC-57](https://capec.mitre.org/data/definitions/57.html)
- [CAPEC-593](https://capec.mitre.org/data/definitions/593.html)
- [CAPEC-633](https://capec.mitre.org/data/definitions/633.html)
- [CAPEC-650](https://capec.mitre.org/data/definitions/650.html)
- [CAPEC-94](https://capec.mitre.org/data/definitions/94.html)

## Related weaknesses
- CWE-284 (ChildOf)
- CWE-284 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-11680**: File-sharing PHP product does not check if user is logged in during requests for PHP library files under an includes/ directory, allowing configuration changes, code execution, and other impacts.
- **CVE-2022-35248**: Chat application skips validation when Central Authentication Service (CAS) is enabled, effectively removing the second factor from two-factor authentication
- **CVE-2022-36436**: Python-based authentication proxy does not enforce password authentication during the initial handshake, allowing the client to bypass authentication by specifying a 'None' authentication type.
- **CVE-2022-30034**: Chain: Web UI for a Python RPC framework does not use regex anchors to validate user login emails (CWE-777), potentially allowing bypass of OAuth (CWE-1390).
- **CVE-2022-29951**: TCP-based protocol in Programmable Logic Controller (PLC) has no authentication.
- **CVE-2022-29952**: Condition Monitor uses a protocol that does not require authentication.
- **CVE-2022-30313**: Safety Instrumented System uses proprietary TCP protocols with no authentication.
- **CVE-2022-30317**: Distributed Control System (DCS) uses a protocol that has no authentication.
- **CVE-2022-33139**: SCADA system only uses client-side authentication, allowing adversaries to impersonate other users.
- **CVE-2021-3116**: Chain: Python-based HTTP Proxy server uses the wrong boolean operators (CWE-480) causing an incorrect comparison (CWE-697) that identifies an authN failure if all three conditions are met instead of only one, allowing bypass of the proxy authentication (CWE-1390)
- **CVE-2021-21972**: Chain: Cloud computing virtualization platform does not require authentication for upload of a tar format file (CWE-306), then uses .. path traversal sequences (CWE-23) in the file to access unexpected files, as exploited in the wild per CISA KEV.
- **CVE-2021-37415**: IT management product does not perform authentication for some REST API requests, as exploited in the wild per CISA KEV.
- **CVE-2021-35033**: Firmware for a WiFi router uses a hard-coded password for a BusyBox shell, allowing bypass of authentication through the UART port
- **CVE-2020-10263**: Bluetooth speaker does not require authentication for the debug functionality on the UART port, allowing root shell access
- **CVE-2020-13927**: Default setting in workflow management product allows all API requests without authentication, as exploited in the wild per CISA KEV.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/287.html
