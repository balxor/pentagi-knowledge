---
cwe_id: CWE-88
name: Improper Neutralization of Argument Delimiters in a Command ('Argument Injection')
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, PHP, Not Technology-Specific]
related_capec: [CAPEC-137, CAPEC-174, CAPEC-41, CAPEC-460, CAPEC-88]
url: https://cwe.mitre.org/data/definitions/88.html
tags: [mitre-cwe, weakness, CWE-88]
---

# CWE-88 - Improper Neutralization of Argument Delimiters in a Command ('Argument Injection')

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-88](https://cwe.mitre.org/data/definitions/88.html)

## Description
The product constructs a string for a command to be executed by a separate component in another control sphere, but it does not properly delimit the intended arguments, options, or switches within that command string.

## Extended description
When creating commands using interpolation into a string, developers may assume that only the arguments/options that they specify will be processed. This assumption may be even stronger when the programmer has encoded the command in a way that prevents separate commands from being provided maliciously, e.g. in the case of shell metacharacters. When constructing the command, the developer may use whitespace or other delimiters that are required to separate arguments when the command. However, if an attacker can provide an untrusted input that contains argument-separating delimiters, then the resulting command will have more arguments than intended by the developer. The attacker may then be able to change the behavior of the command. Depending on the functionality supported by the extraneous arguments, this may have security-relevant consequences.

## Applicable platforms / languages
Not Language-Specific, PHP, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Availability, Other**: Execute Unauthorized Code or Commands, Alter Execution Logic, Read Application Data, Modify Application Data

## Potential mitigations
- **Implementation**: Where possible, avoid building a single string that contains the command and its arguments. Some languages or frameworks have functions that support specifying independent arguments, e.g. as an array, which is used to automatically perform the appropriate quoting or escaping while building the command. For example, in PHP, escapeshellarg() can be used to escape a single argument to system(), or exec() can be called with an array of arguments. In C, code can often be refactored from using system() - which accepts a single string - to using exec(), which requires separate function arguments for each parameter.
- **Architecture and Design**: Understand all the potential areas where untrusted inputs can enter your product: parameters or arguments, cookies, anything read from the network, environment variables, request headers as well as content, URL components, e-mail, files, databases, and any external systems that provide data to the application. Perform input validation at well-defined interfaces.
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- **Implementation**: Directly convert your input type into the expected data type, such as using a conversion function that translates a string into a number. After converting to the expected data type, ensure that the input's values fall within the expected range of allowable values and that multi-field consistencies are maintained.
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180, CWE-181). Make sure that your application does not inadvertently decode the same input twice (CWE-174). Such errors could be used to bypass allowlist schemes by introducing dangerous inputs after they have been checked. Use libraries such as the OWASP ESAPI Canonicalization control. Consider performing repeated canonicalization until your input does not change any more. This will avoid double-decoding and similar scenarios, but it might inadvertently modify inputs that are allowed to contain properly-encoded dangerous content.
- **Implementation**: When exchanging data between components, ensure that both components are using the same character encoding. Ensure that the proper encoding is applied at each interface. Explicitly set the encoding you are using whenever the protocol allows you to do so.
- **Implementation**: When your application combines data from multiple sources, perform the validation after the sources have been combined. The individual data elements may pass the validation step but violate the intended restrictions after they have been combined.
- **Testing**: Use dynamic tools and techniques that interact with the product using large test suites with many diverse inputs, such as fuzz testing (fuzzing), robustness testing, and fault injection. The product's operation may slow down, but it should not become unstable, crash, or generate incorrect results.

## Related attack patterns (CAPEC)
- [CAPEC-137](https://capec.mitre.org/data/definitions/137.html)
- [CAPEC-174](https://capec.mitre.org/data/definitions/174.html)
- [CAPEC-41](https://capec.mitre.org/data/definitions/41.html)
- [CAPEC-460](https://capec.mitre.org/data/definitions/460.html)
- [CAPEC-88](https://capec.mitre.org/data/definitions/88.html)

## Related weaknesses
- CWE-77 (ChildOf)
- CWE-74 (ChildOf)
- CWE-77 (ChildOf)
- CWE-77 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-36069**: Python-based dependency management tool avoids OS command injection when generating Git commands but allows injection of optional arguments with input beginning with a dash (CWE-88), potentially allowing for code execution.
- **CVE-1999-0113**: Canonical Example - "-froot" argument is passed on to another program, where the "-f" causes execution as user "root"
- **CVE-2001-0150**: Web browser executes Telnet sessions using command line arguments that are specified by the web site, which could allow remote attackers to execute arbitrary commands.
- **CVE-2001-0667**: Web browser allows remote attackers to execute commands by spawning Telnet with a log file option on the command line and writing arbitrary code into an executable file which is later executed.
- **CVE-2002-0985**: Argument injection vulnerability in the mail function for PHP may allow attackers to bypass safe mode restrictions and modify command line arguments to the MTA (e.g. sendmail) possibly executing commands.
- **CVE-2003-0907**: Help and Support center in windows does not properly validate HCP URLs, which allows remote attackers to execute arbitrary code via quotation marks in an "hcp://" URL.
- **CVE-2004-0121**: Mail client does not sufficiently filter parameters of mailto: URLs when using them as arguments to mail executable, which allows remote attackers to execute arbitrary programs.
- **CVE-2004-0473**: Web browser doesn't filter "-" when invoking various commands, allowing command-line switches to be specified.
- **CVE-2004-0480**: Mail client allows remote attackers to execute arbitrary code via a URI that uses a UNC network share pathname to provide an alternate configuration file.
- **CVE-2004-0489**: SSH URI handler for web browser allows remote attackers to execute arbitrary code or conduct port forwarding via the a command line option.
- **CVE-2004-0411**: Web browser doesn't filter "-" when invoking various commands, allowing command-line switches to be specified.
- **CVE-2005-4699**: Argument injection vulnerability in TellMe 1.2 and earlier allows remote attackers to modify command line arguments for the Whois program and obtain sensitive information via "--" style options in the q_Host parameter.
- **CVE-2006-1865**: Beagle before 0.2.5 can produce certain insecure command lines to launch external helper applications while indexing, which allows attackers to execute arbitrary commands. NOTE: it is not immediately clear whether this issue involves argument injection, shell metacharacters, or other issues.
- **CVE-2006-2056**: Argument injection vulnerability in Internet Explorer 6 for Windows XP SP2 allows user-assisted remote attackers to modify command line arguments to an invoked mail client via " (double quote) characters in a mailto: scheme handler, as demonstrated by launching Microsoft Outlook with an arbitrary filename as an attachment. NOTE: it is not clear whether this issue is implementation-specific or a problem in the Microsoft API.
- **CVE-2006-2057**: Argument injection vulnerability in Mozilla Firefox 1.0.6 allows user-assisted remote attackers to modify command line arguments to an invoked mail client via " (double quote) characters in a mailto: scheme handler, as demonstrated by launching Microsoft Outlook with an arbitrary filename as an attachment. NOTE: it is not clear whether this issue is implementation-specific or a problem in the Microsoft API.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/88.html
