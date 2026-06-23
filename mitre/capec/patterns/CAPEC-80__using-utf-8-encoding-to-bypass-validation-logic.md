---
capec_id: CAPEC-80
name: Using UTF-8 Encoding to Bypass Validation Logic
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-173, CWE-172, CWE-180, CWE-181, CWE-73, CWE-74, CWE-20, CWE-697, CWE-692]
related_attack: []
url: https://capec.mitre.org/data/definitions/80.html
tags: [mitre-capec, attack-pattern, CAPEC-80]
---

# CAPEC-80 - Using UTF-8 Encoding to Bypass Validation Logic

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-80](https://capec.mitre.org/data/definitions/80.html)

## Description
This attack is a specific variation on leveraging alternate encodings to bypass validation logic. This attack leverages the possibility to encode potentially harmful input in UTF-8 and submit it to applications not expecting or effective at validating this encoding standard making input filtering difficult. UTF-8 (8-bit UCS/Unicode Transformation Format) is a variable-length character encoding for Unicode. Legal UTF-8 characters are one to four bytes long. However, early version of the UTF-8 specification got some entries wrong (in some cases it permitted overlong characters). UTF-8 encoders are supposed to use the "shortest possible" encoding, but naive decoders may accept encodings that are longer than necessary. According to the RFC 3629, a particularly subtle form of this attack can be carried out against a parser which performs security-critical validity checks against the UTF-8 encoded form of its input, but interprets certain illegal octet sequences as characters.

## Prerequisites
- The application's UTF-8 decoder accepts and interprets illegal UTF-8 characters or non-shortest format of UTF-8 encoding.
- Input filtering and validating is not done properly leaving the door open to harmful characters for the target host.

## Skills required
- **Low**: An attacker can inject different representation of a filtered character in UTF-8 format.
- **Medium**: An attacker may craft subtle encoding of input data by using the knowledge that they have gathered about the target host.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Authorization**: Bypass Protection Mechanism
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code), Unreliable Execution
- **Confidentiality**: Bypass Protection Mechanism, Execute Unauthorized Commands (Run Arbitrary Code)
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code), Modify Data

## Execution flow
Execution Flow Explore Survey the application for user-controllable inputs: Using a browser or an automated tool, an attacker follows all public links and actions on a web site. They record all the links, the forms, the resources accessed and all other potential entry-points for the web application. Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Make special note of any links that include parameters in the URL. Use a proxy tool to record all user input entry points visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Experiment Probe entry points to locate vulnerabilities: The attacker uses the entry points gathered in the "Explore" phase as a target list and injects various UTF-8 encoded payloads to determine if an entry point actually represents a vulnerability with insufficient validation logic and to characterize the extent to which the vulnerability can be exploited. Techniques Try to use UTF-8 encoding of content in Scripts in order to bypass validation routines. Try to use UTF-8 encoding of content in HTML in order to bypass validation routines. Try to use UTF-8 encoding of content in CSS in order to bypass validation routines.

## Mitigations
- The Unicode Consortium recognized multiple representations to be a problem and has revised the Unicode Standard to make multiple representations of the same code point with UTF-8 illegal. The UTF-8 Corrigendum lists the newly restricted UTF-8 range (See references). Many current applications may not have been revised to follow this rule. Verify that your application conform to the latest UTF-8 encoding specification. Pay extra attention to the filtering of illegal characters.
- The exact response required from an UTF-8 decoder on invalid input is not uniformly defined by the standards. In general, there are several ways a UTF-8 decoder might behave in the event of an invalid byte sequence: 1. Insert a replacement character (e.g. '?', ''). 2. Ignore the bytes. 3. Interpret the bytes according to a different character encoding (often the ISO-8859-1 character map). 4. Not notice and decode as if the bytes were some similar bit of UTF-8. 5. Stop decoding and report an error (possibly giving the caller the option to continue). It is possible for a decoder to behave in different ways for different types of invalid input. RFC 3629 only requires that UTF-8 decoders must not decode "overlong sequences" (where a character is encoded in more bytes than needed but still adheres to the forms above). The Unicode Standard requires a Unicode-compliant decoder to "...treat any ill-formed code unit sequence as an error condition. This guarantees that it will neither interpret nor emit an ill-formed code unit sequence." Overlong forms are one of the most troublesome types of UTF-8 data. The current RFC says they must not be decoded but older specifications for UTF-8 only gave a warning and many simpler decoders will happily decode them. Overlong forms have been used to bypass security validations in high profile products including Microsoft's IIS web server. Therefore, great care must be taken to avoid security issues if validation is performed before conversion from UTF-8, and it is generally much simpler to handle overlong forms before any input validation is done. To maintain security in the case of invalid input, there are two options. The first is to decode the UTF-8 before doing any input validation checks. The second is to use a decoder that, in the event of invalid input, returns either an error or text that the application considers to be harmless. Another possibility is to avoid conversion out of UTF-8 altogether but this relies on any other software that the data is passed to safely handling the invalid data. Another consideration is error recovery. To guarantee correct recovery after corrupt or lost bytes, decoders must be able to recognize the difference between lead and trail bytes, rather than just assuming that bytes will be of the type allowed in their position.
- For security reasons, a UTF-8 decoder must not accept UTF-8 sequences that are longer than necessary to encode a character. If you use a parser to decode the UTF-8 encoding, make sure that parser filter the invalid UTF-8 characters (invalid forms or overlong forms).
- Look for overlong UTF-8 sequences starting with malicious pattern. You can also use a UTF-8 decoder stress test to test your UTF-8 parser (See Markus Kuhn's UTF-8 and Unicode FAQ in reference section)
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system. Test your decoding process against malicious input.

## Related weaknesses (CWE)
- [CWE-173](https://cwe.mitre.org/data/definitions/173.html)
- [CWE-172](https://cwe.mitre.org/data/definitions/172.html)
- [CWE-180](https://cwe.mitre.org/data/definitions/180.html)
- [CWE-181](https://cwe.mitre.org/data/definitions/181.html)
- [CWE-73](https://cwe.mitre.org/data/definitions/73.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)
- [CWE-692](https://cwe.mitre.org/data/definitions/692.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/80.html
