---
cwe_id: CWE-193
name: Off-by-one Error
type: weakness
abstraction: Base
status: Draft
languages: [C, Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/193.html
tags: [mitre-cwe, weakness, CWE-193]
---

# CWE-193 - Off-by-one Error

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-193](https://cwe.mitre.org/data/definitions/193.html)

## Description
A product calculates or uses an incorrect maximum or minimum value that is 1 more, or 1 less, than the correct value.

## Applicable platforms / languages
C, Not Language-Specific

## Common consequences
- **Availability**: DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Instability
- **Integrity**: Modify Memory
- **Confidentiality, Availability, Access Control**: Execute Unauthorized Code or Commands, Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: When copying character arrays or using character manipulation methods, the correct size parameter must be used to account for the null terminator that needs to be added at the end of the array. Some examples of functions susceptible to this weakness in C include strcpy(), strncpy(), strcat(), strncat(), printf(), sprintf(), scanf() and sscanf().

## Related weaknesses
- CWE-682 (ChildOf)
- CWE-682 (ChildOf)
- CWE-617 (CanPrecede)
- CWE-170 (CanPrecede)
- CWE-119 (CanPrecede)

## Observed examples (CVE)
- **CVE-2003-0252**: Off-by-one error allows remote attackers to cause a denial of service and possibly execute arbitrary code via requests that do not contain newlines.
- **CVE-2001-1391**: Off-by-one vulnerability in driver allows users to modify kernel memory.
- **CVE-2002-0083**: Off-by-one error allows local users or remote malicious servers to gain privileges.
- **CVE-2002-0653**: Off-by-one buffer overflow in function usd by server allows local users to execute arbitrary code as the server user via .htaccess files with long entries.
- **CVE-2002-0844**: Off-by-one buffer overflow in version control system allows local users to execute arbitrary code.
- **CVE-1999-1568**: Off-by-one error in FTP server allows a remote attacker to cause a denial of service (crash) via a long PORT command.
- **CVE-2004-0346**: Off-by-one buffer overflow in FTP server allows local users to gain privileges via a 1024 byte RETR command.
- **CVE-2004-0005**: Multiple buffer overflows in chat client allow remote attackers to cause a denial of service and possibly execute arbitrary code.
- **CVE-2003-0356**: Multiple off-by-one vulnerabilities in product allow remote attackers to cause a denial of service and possibly execute arbitrary code.
- **CVE-2001-1496**: Off-by-one buffer overflow in server allows remote attackers to cause a denial of service and possibly execute arbitrary code.
- **CVE-2004-0342**: This is an interesting example that might not be an off-by-one.
- **CVE-2001-0609**: An off-by-one enables a terminating null to be overwritten, which causes 2 strings to be merged and enable a format string.
- **CVE-2002-1745**: Off-by-one error allows source code disclosure of files with 4 letter extensions that match an accepted 3-letter extension.
- **CVE-2002-1816**: Off-by-one buffer overflow.
- **CVE-2002-1721**: Off-by-one error causes an snprintf call to overwrite a critical internal variable with a null value.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/193.html
