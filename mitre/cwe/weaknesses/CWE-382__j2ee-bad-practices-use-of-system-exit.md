---
cwe_id: CWE-382
name: J2EE Bad Practices: Use of System.exit()
type: weakness
abstraction: Variant
status: Draft
languages: [Java, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/382.html
tags: [mitre-cwe, weakness, CWE-382]
---

# CWE-382 - J2EE Bad Practices: Use of System.exit()

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-382](https://cwe.mitre.org/data/definitions/382.html)

## Description
A J2EE application uses System.exit(), which also shuts down its container.

## Extended description
It is never a good idea for a web application to attempt to shut down the application container. Access to a function that can shut down the application is an avenue for Denial of Service (DoS) attacks.

## Applicable platforms / languages
Java, Web Based, Web Server

## Common consequences
- **Availability**: DoS: Crash, Exit, or Restart

## Potential mitigations
- **Architecture and Design**: The shutdown function should be a privileged function available only to a properly authorized administrative user
- **Implementation**: Web applications should not call methods that cause the virtual machine to exit, such as System.exit()
- **Implementation**: Web applications should also not throw any Throwables to the application server as this may adversely affect the container.
- **Implementation**: Non-web applications may have a main() method that contains a System.exit(), but generally should not call System.exit() from other locations in the code

## Related weaknesses
- CWE-705 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/382.html
