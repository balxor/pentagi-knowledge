---
cwe_id: CWE-20
name: Improper Input Validation
type: weakness
abstraction: Class
status: Stable
languages: [Not Language-Specific, AI/ML]
related_capec: [CAPEC-10, CAPEC-101, CAPEC-104, CAPEC-108, CAPEC-109, CAPEC-110, CAPEC-120, CAPEC-13, CAPEC-135, CAPEC-136, CAPEC-14, CAPEC-153, CAPEC-182, CAPEC-209, CAPEC-22, CAPEC-23, CAPEC-230, CAPEC-231, CAPEC-24, CAPEC-250, CAPEC-261, CAPEC-267, CAPEC-28, CAPEC-3, CAPEC-31, CAPEC-42, CAPEC-43, CAPEC-45, CAPEC-46, CAPEC-47, CAPEC-473, CAPEC-52, CAPEC-53, CAPEC-588, CAPEC-63, CAPEC-64, CAPEC-664, CAPEC-67, CAPEC-7, CAPEC-71, CAPEC-72, CAPEC-73, CAPEC-78, CAPEC-79, CAPEC-8, CAPEC-80, CAPEC-81, CAPEC-83, CAPEC-85, CAPEC-88, CAPEC-9]
url: https://cwe.mitre.org/data/definitions/20.html
tags: [mitre-cwe, weakness, CWE-20]
---

# CWE-20 - Improper Input Validation

**Abstraction:** Class  -  **Status:** Stable  -  **CWE:** [CWE-20](https://cwe.mitre.org/data/definitions/20.html)

## Description
The product receives input or data, but it does not validate or incorrectly validates that the input has the properties that are required to process the data safely and correctly.

## Extended description
Input validation is a frequently-used technique for checking potentially dangerous inputs in order to ensure that the inputs are safe for processing within the code, or when communicating with other components. Input can consist of: raw data - strings, numbers, parameters, file contents, etc. metadata - information about the raw data, such as headers or size Data can be simple or structured. Structured data can be composed of many nested layers, composed of combinations of metadata and raw data, with other simple or structured data. Many properties of raw data or metadata may need to be validated upon entry into the code, such as: specified quantities such as size, length, frequency, price, rate, number of operations, time, etc. implied or derived quantities, such as the actual size of a file instead of a specified size indexes, offsets, or positions into more complex data structures symbolic keys or other elements into hash tables, associative arrays, etc. well-formedness, i.e. syntactic correctness - compliance with expected syntax lexical token correctness - compliance with rules for what is treated as a token specified or derived type - the actual type of the input (or what the input appears to be) consistency - between individual data elements, between raw data and metadata, between references, etc. conformance to domain-specific rules, e.g. business logic equivalence - ensuring that equivalent inputs are treated the same authenticity, ownership, or other attestations about the input, e.g. a cryptographic signature to prove the source of the data Implied or derived properties of data must often be calculated or inferred by the code itself. Errors in deriving properties may be considered a contributing factor to improper input validation.

## Applicable platforms / languages
Not Language-Specific, AI/ML

## Common consequences
- **Availability**: DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory)
- **Confidentiality**: Read Memory, Read Files or Directories
- **Integrity, Confidentiality, Availability**: Modify Memory, Execute Unauthorized Code or Commands

## Potential mitigations
- **Architecture and Design**: Consider using language-theoretic security (LangSec) techniques that characterize inputs using a formal language and build "recognizers" for that language. This effectively requires parsing to be a distinct layer that effectively enforces a boundary between raw input and internal data representations, instead of allowing parser code to be scattered throughout the program, where it could be subject to errors or inconsistencies that create weaknesses. [REF-1109] [REF-1110] [REF-1111]
- **Architecture and Design**: Use an input validation framework such as Struts or the OWASP ESAPI Validation API. Note that using a framework does not automatically address all input validation problems; be mindful of weaknesses that could arise from misusing the framework itself (CWE-1173).
- **Architecture and Design, Implementation**: Understand all the potential areas where untrusted inputs can enter the product, including but not limited to: parameters or arguments, cookies, anything read from the network, environment variables, reverse DNS lookups, query results, request headers, URL components, e-mail, files, filenames, databases, and any external systems that provide data to the application. Remember that such inputs may be obtained indirectly through API calls.
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- **Architecture and Design**: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server. Even though client-side checks provide minimal benefits with respect to server-side security, they are still useful. First, they can support intrusion detection. If the server receives input that should have been rejected by the client, then it may be an indication of an attack. Second, client-side error-checking can provide helpful feedback to the user about the expectations for valid input. Third, there may be a reduction in server-side processing time for accidental input errors, although this is typically a small savings.
- **Implementation**: When your application combines data from multiple sources, perform the validation after the sources have been combined. The individual data elements may pass the validation step but violate the intended restrictions after they have been combined.
- **Implementation**: Be especially careful to validate all input when invoking code that crosses language boundaries, such as from an interpreted language to native code. This could create an unexpected interaction between the language boundaries. Ensure that you are not violating any of the expectations of the language with which you are interfacing. For example, even though Java may not be susceptible to buffer overflows, providing a large argument in a call to native code might trigger an overflow.
- **Implementation**: Directly convert your input type into the expected data type, such as using a conversion function that translates a string into a number. After converting to the expected data type, ensure that the input's values fall within the expected range of allowable values and that multi-field consistencies are maintained.
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180, CWE-181). Make sure that your application does not inadvertently decode the same input twice (CWE-174). Such errors could be used to bypass allowlist schemes by introducing dangerous inputs after they have been checked. Use libraries such as the OWASP ESAPI Canonicalization control. Consider performing repeated canonicalization until your input does not change any more. This will avoid double-decoding and similar scenarios, but it might inadvertently modify inputs that are allowed to contain properly-encoded dangerous content.
- **Implementation**: When exchanging data between components, ensure that both components are using the same character encoding. Ensure that the proper encoding is applied at each interface. Explicitly set the encoding you are using whenever the protocol allows you to do so.

## Related attack patterns (CAPEC)
- [CAPEC-10](https://capec.mitre.org/data/definitions/10.html)
- [CAPEC-101](https://capec.mitre.org/data/definitions/101.html)
- [CAPEC-104](https://capec.mitre.org/data/definitions/104.html)
- [CAPEC-108](https://capec.mitre.org/data/definitions/108.html)
- [CAPEC-109](https://capec.mitre.org/data/definitions/109.html)
- [CAPEC-110](https://capec.mitre.org/data/definitions/110.html)
- [CAPEC-120](https://capec.mitre.org/data/definitions/120.html)
- [CAPEC-13](https://capec.mitre.org/data/definitions/13.html)
- [CAPEC-135](https://capec.mitre.org/data/definitions/135.html)
- [CAPEC-136](https://capec.mitre.org/data/definitions/136.html)
- [CAPEC-14](https://capec.mitre.org/data/definitions/14.html)
- [CAPEC-153](https://capec.mitre.org/data/definitions/153.html)
- [CAPEC-182](https://capec.mitre.org/data/definitions/182.html)
- [CAPEC-209](https://capec.mitre.org/data/definitions/209.html)
- [CAPEC-22](https://capec.mitre.org/data/definitions/22.html)
- [CAPEC-23](https://capec.mitre.org/data/definitions/23.html)
- [CAPEC-230](https://capec.mitre.org/data/definitions/230.html)
- [CAPEC-231](https://capec.mitre.org/data/definitions/231.html)
- [CAPEC-24](https://capec.mitre.org/data/definitions/24.html)
- [CAPEC-250](https://capec.mitre.org/data/definitions/250.html)
- [CAPEC-261](https://capec.mitre.org/data/definitions/261.html)
- [CAPEC-267](https://capec.mitre.org/data/definitions/267.html)
- [CAPEC-28](https://capec.mitre.org/data/definitions/28.html)
- [CAPEC-3](https://capec.mitre.org/data/definitions/3.html)
- [CAPEC-31](https://capec.mitre.org/data/definitions/31.html)
- [CAPEC-42](https://capec.mitre.org/data/definitions/42.html)
- [CAPEC-43](https://capec.mitre.org/data/definitions/43.html)
- [CAPEC-45](https://capec.mitre.org/data/definitions/45.html)
- [CAPEC-46](https://capec.mitre.org/data/definitions/46.html)
- [CAPEC-47](https://capec.mitre.org/data/definitions/47.html)
- [CAPEC-473](https://capec.mitre.org/data/definitions/473.html)
- [CAPEC-52](https://capec.mitre.org/data/definitions/52.html)
- [CAPEC-53](https://capec.mitre.org/data/definitions/53.html)
- [CAPEC-588](https://capec.mitre.org/data/definitions/588.html)
- [CAPEC-63](https://capec.mitre.org/data/definitions/63.html)
- [CAPEC-64](https://capec.mitre.org/data/definitions/64.html)
- [CAPEC-664](https://capec.mitre.org/data/definitions/664.html)
- [CAPEC-67](https://capec.mitre.org/data/definitions/67.html)
- [CAPEC-7](https://capec.mitre.org/data/definitions/7.html)
- [CAPEC-71](https://capec.mitre.org/data/definitions/71.html)
- [CAPEC-72](https://capec.mitre.org/data/definitions/72.html)
- [CAPEC-73](https://capec.mitre.org/data/definitions/73.html)
- [CAPEC-78](https://capec.mitre.org/data/definitions/78.html)
- [CAPEC-79](https://capec.mitre.org/data/definitions/79.html)
- [CAPEC-8](https://capec.mitre.org/data/definitions/8.html)
- [CAPEC-80](https://capec.mitre.org/data/definitions/80.html)
- [CAPEC-81](https://capec.mitre.org/data/definitions/81.html)
- [CAPEC-83](https://capec.mitre.org/data/definitions/83.html)
- [CAPEC-85](https://capec.mitre.org/data/definitions/85.html)
- [CAPEC-88](https://capec.mitre.org/data/definitions/88.html)
- [CAPEC-9](https://capec.mitre.org/data/definitions/9.html)

## Related weaknesses
- CWE-707 (ChildOf)
- CWE-345 (PeerOf)
- CWE-22 (CanPrecede)
- CWE-41 (CanPrecede)
- CWE-74 (CanPrecede)
- CWE-119 (CanPrecede)
- CWE-770 (CanPrecede)

## Observed examples (CVE)
- **CVE-2024-37032**: Large language model (LLM) management tool does not validate the format of a digest value (CWE-1287) from a private, untrusted model registry, enabling relative path traversal (CWE-23), a.k.a. Probllama
- **CVE-2022-45918**: Chain: a learning management tool debugger uses external input to locate previous session logs (CWE-73) and does not properly validate the given path (CWE-20), allowing for filesystem path traversal using "../" sequences (CWE-24)
- **CVE-2021-30860**: Chain: improper input validation (CWE-20) leads to integer overflow (CWE-190) in mobile OS, as exploited in the wild per CISA KEV.
- **CVE-2021-30663**: Chain: improper input validation (CWE-20) leads to integer overflow (CWE-190) in mobile OS, as exploited in the wild per CISA KEV.
- **CVE-2021-22205**: Chain: backslash followed by a newline can bypass a validation step (CWE-20), leading to eval injection (CWE-95), as exploited in the wild per CISA KEV.
- **CVE-2021-21220**: Chain: insufficient input validation (CWE-20) in browser allows heap corruption (CWE-787), as exploited in the wild per CISA KEV.
- **CVE-2020-9054**: Chain: improper input validation (CWE-20) in username parameter, leading to OS command injection (CWE-78), as exploited in the wild per CISA KEV.
- **CVE-2020-3452**: Chain: security product has improper input validation (CWE-20) leading to directory traversal (CWE-22), as exploited in the wild per CISA KEV.
- **CVE-2020-3161**: Improper input validation of HTTP requests in IP phone, as exploited in the wild per CISA KEV.
- **CVE-2020-3580**: Chain: improper input validation (CWE-20) in firewall product leads to XSS (CWE-79), as exploited in the wild per CISA KEV.
- **CVE-2021-37147**: Chain: caching proxy server has improper input validation (CWE-20) of headers, allowing HTTP response smuggling (CWE-444) using an "LF line ending"
- **CVE-2008-5305**: Eval injection in Perl program using an ID that should only contain hyphens and numbers.
- **CVE-2008-2223**: SQL injection through an ID that was supposed to be numeric.
- **CVE-2008-3477**: lack of input validation in spreadsheet program leads to buffer overflows, integer overflows, array index errors, and memory corruption.
- **CVE-2008-3843**: insufficient validation enables XSS

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/20.html
