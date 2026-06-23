---
cwe_id: CWE-781
name: Improper Address Validation in IOCTL with METHOD_NEITHER I/O Control Code
type: weakness
abstraction: Variant
status: Draft
languages: [C, C++, Windows NT]
related_capec: []
url: https://cwe.mitre.org/data/definitions/781.html
tags: [mitre-cwe, weakness, CWE-781]
---

# CWE-781 - Improper Address Validation in IOCTL with METHOD_NEITHER I/O Control Code

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-781](https://cwe.mitre.org/data/definitions/781.html)

## Description
The product defines an IOCTL that uses METHOD_NEITHER for I/O, but it does not validate or incorrectly validates the addresses that are provided.

## Extended description
When an IOCTL uses the METHOD_NEITHER option for I/O control, it is the responsibility of the IOCTL to validate the addresses that have been supplied to it. If validation is missing or incorrect, attackers can supply arbitrary memory addresses, leading to code execution or a denial of service.

## Applicable platforms / languages
C, C++, Windows NT

## Common consequences
- **Integrity, Availability, Confidentiality**: Modify Memory, Read Memory, Execute Unauthorized Code or Commands, DoS: Crash, Exit, or Restart

## Potential mitigations
- **Implementation**: If METHOD_NEITHER is required for the IOCTL, then ensure that all user-space addresses are properly validated before they are first accessed. The ProbeForRead and ProbeForWrite routines are available for this task. Also properly protect and manage the user-supplied buffers, since the I/O Manager does not do this when METHOD_NEITHER is being used. See References.
- **Architecture and Design**: If possible, avoid using METHOD_NEITHER in the IOCTL and select methods that effectively control the buffer size, such as METHOD_BUFFERED, METHOD_IN_DIRECT, or METHOD_OUT_DIRECT.
- **Architecture and Design, Implementation**: If the IOCTL is part of a driver that is only intended to be accessed by trusted users, then use proper access control for the associated device or device namespace. See References.

## Related weaknesses
- CWE-1285 (ChildOf)
- CWE-822 (CanPrecede)

## Observed examples (CVE)
- **CVE-2006-2373**: Driver for file-sharing and messaging protocol allows attackers to execute arbitrary code.
- **CVE-2009-0686**: Anti-virus product does not validate addresses, allowing attackers to gain SYSTEM privileges.
- **CVE-2009-0824**: DVD software allows attackers to cause a crash.
- **CVE-2008-5724**: Personal firewall allows attackers to gain SYSTEM privileges.
- **CVE-2007-5756**: chain: device driver for packet-capturing software allows access to an unintended IOCTL with resultant array index error.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/781.html
