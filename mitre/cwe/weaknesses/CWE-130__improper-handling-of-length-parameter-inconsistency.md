---
cwe_id: CWE-130
name: Improper Handling of Length Parameter Inconsistency
type: weakness
abstraction: Base
status: Incomplete
languages: [C, C++, Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-47]
url: https://cwe.mitre.org/data/definitions/130.html
tags: [mitre-cwe, weakness, CWE-130]
---

# CWE-130 - Improper Handling of Length Parameter Inconsistency

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-130](https://cwe.mitre.org/data/definitions/130.html)

## Description
The product parses a formatted message or structure, but it does not handle or incorrectly handles a length field that is inconsistent with the actual length of the associated data.

## Extended description
If an attacker can manipulate the length parameter associated with an input such that it is inconsistent with the actual length of the input, this can be leveraged to cause the target application to behave in unexpected, and possibly, malicious ways. One of the possible motives for doing so is to pass in arbitrarily large input to the application. Another possible motivation is the modification of application state by including invalid data for subsequent properties of the application. Such weaknesses commonly lead to attacks such as buffer overflows and execution of arbitrary code.

## Applicable platforms / languages
C, C++, Not Language-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Memory, Modify Memory, Varies by Context

## Potential mitigations
- **Implementation**: When processing structured incoming data containing a size field followed by raw data, ensure that you identify and resolve any inconsistencies between the size field and the actual size of the data.
- **Implementation**: Do not let the user control the size of the buffer.
- **Implementation**: Validate that the length of the user-supplied data is consistent with the buffer size.

## Related attack patterns (CAPEC)
- [CAPEC-47](https://capec.mitre.org/data/definitions/47.html)

## Related weaknesses
- CWE-240 (ChildOf)
- CWE-119 (ChildOf)
- CWE-119 (ChildOf)
- CWE-805 (CanPrecede)

## Observed examples (CVE)
- **CVE-2014-0160**: Chain: "Heartbleed" bug receives an inconsistent length parameter (CWE-130) enabling an out-of-bounds read (CWE-126), returning memory that could include private cryptographic keys and other sensitive data.
- **CVE-2009-2299**: Web application firewall consumes excessive memory when an HTTP request contains a large Content-Length value but no POST data.
- **CVE-2001-0825**: Buffer overflow in internal string handling routine allows remote attackers to execute arbitrary commands via a length argument of zero or less, which disables the length check.
- **CVE-2001-1186**: Web server allows remote attackers to cause a denial of service via an HTTP request with a content-length value that is larger than the size of the request, which prevents server from timing out the connection.
- **CVE-2001-0191**: Service does not properly check the specified length of a cookie, which allows remote attackers to execute arbitrary commands via a buffer overflow, or brute force authentication by using a short cookie length.
- **CVE-2003-0429**: Traffic analyzer allows remote attackers to cause a denial of service and possibly execute arbitrary code via invalid IPv4 or IPv6 prefix lengths, possibly triggering a buffer overflow.
- **CVE-2000-0655**: Chat client allows remote attackers to cause a denial of service or execute arbitrary commands via a JPEG image containing a comment with an illegal field length of 1.
- **CVE-2004-0492**: Server allows remote attackers to cause a denial of service and possibly execute arbitrary code via a negative Content-Length HTTP header field causing a heap-based buffer overflow.
- **CVE-2004-0201**: Help program allows remote attackers to execute arbitrary commands via a heap-based buffer overflow caused by a .CHM file with a large length field
- **CVE-2003-0825**: Name services does not properly validate the length of certain packets, which allows attackers to cause a denial of service and possibly execute arbitrary code. Can overlap zero-length issues
- **CVE-2004-0095**: Policy manager allows remote attackers to cause a denial of service (memory consumption and crash) and possibly execute arbitrary code via an HTTP POST request with an invalid Content-Length value.
- **CVE-2004-0826**: Heap-based buffer overflow in library allows remote attackers to execute arbitrary code via a modified record length field in an SSLv2 client hello message.
- **CVE-2004-0808**: When domain logons are enabled, server allows remote attackers to cause a denial of service via a SAM_UAS_CHANGE request with a length value that is larger than the number of structures that are provided.
- **CVE-2002-1357**: Multiple SSH2 servers and clients do not properly handle packets or data elements with incorrect length specifiers, which may allow remote attackers to cause a denial of service or possibly execute arbitrary code.
- **CVE-2004-0774**: Server allows remote attackers to cause a denial of service (CPU and memory exhaustion) via a POST request with a Content-Length header set to -1.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/130.html
