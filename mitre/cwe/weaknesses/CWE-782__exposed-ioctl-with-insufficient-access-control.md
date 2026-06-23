---
cwe_id: CWE-782
name: Exposed IOCTL with Insufficient Access Control
type: weakness
abstraction: Variant
status: Draft
languages: [C, C++, Unix, Windows]
related_capec: []
url: https://cwe.mitre.org/data/definitions/782.html
tags: [mitre-cwe, weakness, CWE-782]
---

# CWE-782 - Exposed IOCTL with Insufficient Access Control

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-782](https://cwe.mitre.org/data/definitions/782.html)

## Description
The product implements an IOCTL with functionality that should be restricted, but it does not properly enforce access control for the IOCTL.

## Extended description
When an IOCTL contains privileged functionality and is exposed unnecessarily, attackers may be able to access this functionality by invoking the IOCTL. Even if the functionality is benign, if the programmer has assumed that the IOCTL would only be accessed by a trusted process, there may be little or no validation of the incoming data, exposing weaknesses that would never be reachable if the attacker cannot call the IOCTL directly. The implementations of IOCTLs will differ between operating system types and versions, so the methods of attack and prevention may vary widely.

## Applicable platforms / languages
C, C++, Unix, Windows

## Common consequences
- **Integrity, Availability, Confidentiality**: Varies by Context

## Potential mitigations
- **Architecture and Design**: In Windows environments, use proper access control for the associated device or device namespace. See References.

## Related weaknesses
- CWE-749 (ChildOf)
- CWE-781 (CanPrecede)

## Observed examples (CVE)
- **CVE-2009-2208**: Operating system does not enforce permissions on an IOCTL that can be used to modify network settings.
- **CVE-2008-3831**: Device driver does not restrict ioctl calls to its direct rendering manager.
- **CVE-2008-3525**: ioctl does not check for a required capability before processing certain requests.
- **CVE-2008-0322**: Chain: insecure device permissions allows access to an IOCTL, allowing arbitrary memory to be overwritten.
- **CVE-2007-4277**: Chain: anti-virus product uses weak permissions for a device, leading to resultant buffer overflow in an exposed IOCTL.
- **CVE-2007-1400**: Chain: sandbox allows opening of a TTY device, enabling shell commands through an exposed ioctl.
- **CVE-2006-4926**: Anti-virus product uses insecure security descriptor for a device driver, allowing access to a privileged IOCTL.
- **CVE-1999-0728**: Unauthorized user can disable keyboard or mouse by directly invoking a privileged IOCTL.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/782.html
