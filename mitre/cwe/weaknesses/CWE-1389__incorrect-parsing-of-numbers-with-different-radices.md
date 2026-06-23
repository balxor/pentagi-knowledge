---
cwe_id: CWE-1389
name: Incorrect Parsing of Numbers with Different Radices
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1389.html
tags: [mitre-cwe, weakness, CWE-1389]
---

# CWE-1389 - Incorrect Parsing of Numbers with Different Radices

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1389](https://cwe.mitre.org/data/definitions/1389.html)

## Description
The product parses numeric input assuming base 10 (decimal) values, but it does not account for inputs that use a different base number (radix).

## Extended description
Frequently, a numeric input that begins with "0" is treated as octal, or "0x" causes it to be treated as hexadecimal, e.g. by the inet_addr() function. For example, "023" (octal) is 35 decimal, or "0x31" is 49 decimal. Other bases may be used as well. If the developer assumes decimal-only inputs, the code could produce incorrect numbers when the inputs are parsed using a different base. This can result in unexpected and/or dangerous behavior. For example, a "0127.0.0.1" IP address is parsed as octal due to the leading "0", whose numeric value would be the same as 87.0.0.1 (decimal), where the developer likely expected to use 127.0.0.1. The consequences vary depending on the surrounding code in which this weakness occurs, but they can include bypassing network-based access control using unexpected IP addresses or netmasks, or causing apparently-symbolic identifiers to be processed as if they are numbers. In web applications, this can enable bypassing of SSRF restrictions.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality**: Read Application Data
- **Integrity**: Bypass Protection Mechanism, Alter Execution Logic

## Potential mitigations
- **Implementation**: If only decimal-based values are expected in the application, conditional checks should be created in a way that prevent octal or hexadecimal strings from being checked. This can be achieved by converting any numerical string to an explicit base-10 integer prior to the conditional check, to prevent octal or hex values from ever being checked against the condition.
- **Implementation**: If various numerical bases do need to be supported, check for leading values indicating the non-decimal base you wish to support (such as 0x for hex) and convert the numeric strings to integers of the respective base. Reject any other alternative-base string that is not intentionally supported by the application.
- **Implementation**: If regular expressions are used to validate IP addresses, ensure that they are bounded using ^ and $ to prevent base-prepended IP addresses from being matched.

## Related weaknesses
- CWE-704 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-29662**: Chain: Use of zero-prepended IP addresses in Perl-based IP validation module can lead to an access control bypass.
- **CVE-2021-28918**: Chain: Use of zero-prepended IP addresses in a product that manages IP blocks can lead to an SSRF.
- **CVE-2021-29921**: Chain: Use of zero-prepended IP addresses in a Python standard library package can lead to an SSRF.
- **CVE-2021-29923**: Chain: Use of zero-prepended IP addresses in the net Golang library can lead to an access control bypass.
- **CVE-2021-29424**: Chain: Use of zero-prepended IP addresses in Perl netmask module allows bypass of IP-based access control.
- **CVE-2016-4029**: Chain: incorrect validation of intended decimal-based IP address format (CWE-1286) enables parsing of octal or hexadecimal formats (CWE-1389), allowing bypass of an SSRF protection mechanism (CWE-918).
- **CVE-2020-13776**: Mishandling of hex-valued usernames leads to unexpected decimal conversion and privilege escalation in the systemd Linux suite.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1389.html
