---
cwe_id: CWE-116
name: Improper Encoding or Escaping of Output
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, AI/ML, Database Server, Web Server]
related_capec: [CAPEC-104, CAPEC-73, CAPEC-81, CAPEC-85]
url: https://cwe.mitre.org/data/definitions/116.html
tags: [mitre-cwe, weakness, CWE-116]
---

# CWE-116 - Improper Encoding or Escaping of Output

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-116](https://cwe.mitre.org/data/definitions/116.html)

## Description
The product prepares a structured message for communication with another component, but encoding or escaping of the data is either missing or done incorrectly. As a result, the intended structure of the message is not preserved.

## Extended description
Improper encoding or escaping can allow attackers to change the commands that are sent to another component, inserting malicious commands instead. Most products follow a certain protocol that uses structured messages for communication between components, such as queries or commands. These structured messages can contain raw data interspersed with metadata or control information. For example, "GET /index.html HTTP/1.1" is a structured message containing a command ("GET") with a single argument ("/index.html") and metadata about which protocol version is being used ("HTTP/1.1"). If an application uses attacker-supplied inputs to construct a structured message without properly encoding or escaping, then the attacker could insert special characters that will cause the data to be interpreted as control information or metadata. Consequently, the component that receives the output will perform the wrong operations, or otherwise interpret the data incorrectly.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, AI/ML, Database Server, Web Server

## Common consequences
- **Integrity**: Modify Application Data
- **Integrity, Confidentiality, Availability, Access Control**: Execute Unauthorized Code or Commands
- **Confidentiality**: Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, consider using the ESAPI Encoding control [REF-45] or a similar tool, library, or framework. These will help the programmer encode outputs in a manner less prone to error. Alternately, use built-in functions, but consider using wrappers in case those functions are discovered to have a vulnerability.
- **Architecture and Design**: If available, use structured mechanisms that automatically enforce the separation between data and code. These mechanisms may be able to provide the relevant quoting, encoding, and validation automatically, instead of relying on the developer to provide this capability at every point where output is generated. For example, stored procedures can enforce database query structure and reduce the likelihood of SQL injection.
- **Architecture and Design, Implementation**: Understand the context in which your data will be used and the encoding that will be expected. This is especially important when transmitting data between different components, or when generating outputs that can contain multiple encodings at the same time, such as web pages or multi-part mail messages. Study all expected communication protocols and data representations to determine the required encoding strategies.
- **Architecture and Design**: In some cases, input validation may be an important strategy when output encoding is not a complete solution. For example, you may be providing the same output that will be processed by multiple consumers that use different encodings or representations. In other cases, you may be required to allow user-supplied input to contain control information, such as limited HTML tags that support formatting in a wiki or bulletin board. When this type of requirement must be met, use an extremely strict allowlist to limit which control sequences can be used. Verify that the resulting syntactic structure is what you expect. Use your normal encoding methods for the remainder of the input.
- **Architecture and Design**: Use input validation as a defense-in-depth measure to reduce the likelihood of output encoding errors (see CWE-20).
- **Requirements**: Fully specify which encodings are required by components that will be communicating with each other.
- **Implementation**: When exchanging data between components, ensure that both components are using the same character encoding. Ensure that the proper encoding is applied at each interface. Explicitly set the encoding you are using whenever the protocol allows you to do so.

## Related attack patterns (CAPEC)
- [CAPEC-104](https://capec.mitre.org/data/definitions/104.html)
- [CAPEC-73](https://capec.mitre.org/data/definitions/73.html)
- [CAPEC-81](https://capec.mitre.org/data/definitions/81.html)
- [CAPEC-85](https://capec.mitre.org/data/definitions/85.html)

## Related weaknesses
- CWE-707 (ChildOf)
- CWE-74 (CanPrecede)

## Observed examples (CVE)
- **CVE-2021-41232**: Chain: authentication routine in Go-based agile development product does not escape user name (CWE-116), allowing LDAP injection (CWE-90)
- **CVE-2008-4636**: OS command injection in backup software using shell metacharacters in a filename; correct behavior would require that this filename could not be changed.
- **CVE-2008-0769**: Web application does not set the charset when sending a page to a browser, allowing for XSS exploitation when a browser chooses an unexpected encoding.
- **CVE-2008-0005**: Program does not set the charset when sending a page to a browser, allowing for XSS exploitation when a browser chooses an unexpected encoding.
- **CVE-2008-5573**: SQL injection via password parameter; a strong password might contain "&"
- **CVE-2008-3773**: Cross-site scripting in chat application via a message subject, which normally might contain "&" and other XSS-related characters.
- **CVE-2008-0757**: Cross-site scripting in chat application via a message, which normally might be allowed to contain arbitrary content.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/116.html
