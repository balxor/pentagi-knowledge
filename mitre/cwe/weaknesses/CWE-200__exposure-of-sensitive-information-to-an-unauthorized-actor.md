---
cwe_id: CWE-200
name: Exposure of Sensitive Information to an Unauthorized Actor
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, Web Based, Mobile]
related_capec: [CAPEC-116, CAPEC-13, CAPEC-169, CAPEC-22, CAPEC-224, CAPEC-285, CAPEC-287, CAPEC-290, CAPEC-291, CAPEC-292, CAPEC-293, CAPEC-294, CAPEC-295, CAPEC-296, CAPEC-297, CAPEC-298, CAPEC-299, CAPEC-300, CAPEC-301, CAPEC-302, CAPEC-303, CAPEC-304, CAPEC-305, CAPEC-306, CAPEC-307, CAPEC-308, CAPEC-309, CAPEC-310, CAPEC-312, CAPEC-313, CAPEC-317, CAPEC-318, CAPEC-319, CAPEC-320, CAPEC-321, CAPEC-322, CAPEC-323, CAPEC-324, CAPEC-325, CAPEC-326, CAPEC-327, CAPEC-328, CAPEC-329, CAPEC-330, CAPEC-472, CAPEC-497, CAPEC-508, CAPEC-573, CAPEC-574, CAPEC-575, CAPEC-576, CAPEC-577, CAPEC-59, CAPEC-60, CAPEC-616, CAPEC-643, CAPEC-646, CAPEC-651, CAPEC-79]
url: https://cwe.mitre.org/data/definitions/200.html
tags: [mitre-cwe, weakness, CWE-200]
---

# CWE-200 - Exposure of Sensitive Information to an Unauthorized Actor

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

## Description
The product exposes sensitive information to an actor that is not explicitly authorized to have access to that information.

## Extended description
There are many different kinds of mistakes that introduce information exposures. The severity of the error can range widely, depending on the context in which the product operates, the type of sensitive information that is revealed, and the benefits it may provide to an attacker. Some kinds of sensitive information include: private, personal information, such as personal messages, financial data, health records, geographic location, or contact details system status and environment, such as the operating system and installed packages business secrets and intellectual property network status and configuration the product's own code or internal state metadata, e.g. logging of connections or message headers indirect information, such as a discrepancy between two internal operations that can be observed by an outsider Information might be sensitive to different parties, each of which may have their own expectations for whether the information should be protected. These parties include: the product's own users people or organizations whose information is created or used by the product, even if they are not direct product users the product's administrators, including the admins of the system(s) and/or networks on which the product operates the developer Information exposures can occur in different ways: the code explicitly inserts sensitive information into resources or messages that are intentionally made accessible to unauthorized actors, but should not contain the information - i.e., the information should have been "scrubbed" or "sanitized" a different weakness or mistake indirectly inserts the sensitive information into resources, such as a web script error revealing the full system path of the program. the code manages resources that intentionally contain sensitive information, but the resources are unintentionally made accessible to unauthorized actors. In this case, the information exposure is resultant - i.e., a different weakness enabled the access to the information in the first place. It is common practice to describe any loss of confidentiality as an "information exposure," but this can lead to overuse of CWE-200 in CWE mapping. From the CWE perspective, loss of confidentiality is a technical impact that can arise from dozens of different weaknesses, such as insecure file permissions or out-of-bounds read. CWE-200 and its lower-level descendants are intended to cover the mistakes that occur in behaviors that explicitly manage, store, transfer, or cleanse sensitive information.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based, Mobile

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design**: Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.

## Related attack patterns (CAPEC)
- [CAPEC-116](https://capec.mitre.org/data/definitions/116.html)
- [CAPEC-13](https://capec.mitre.org/data/definitions/13.html)
- [CAPEC-169](https://capec.mitre.org/data/definitions/169.html)
- [CAPEC-22](https://capec.mitre.org/data/definitions/22.html)
- [CAPEC-224](https://capec.mitre.org/data/definitions/224.html)
- [CAPEC-285](https://capec.mitre.org/data/definitions/285.html)
- [CAPEC-287](https://capec.mitre.org/data/definitions/287.html)
- [CAPEC-290](https://capec.mitre.org/data/definitions/290.html)
- [CAPEC-291](https://capec.mitre.org/data/definitions/291.html)
- [CAPEC-292](https://capec.mitre.org/data/definitions/292.html)
- [CAPEC-293](https://capec.mitre.org/data/definitions/293.html)
- [CAPEC-294](https://capec.mitre.org/data/definitions/294.html)
- [CAPEC-295](https://capec.mitre.org/data/definitions/295.html)
- [CAPEC-296](https://capec.mitre.org/data/definitions/296.html)
- [CAPEC-297](https://capec.mitre.org/data/definitions/297.html)
- [CAPEC-298](https://capec.mitre.org/data/definitions/298.html)
- [CAPEC-299](https://capec.mitre.org/data/definitions/299.html)
- [CAPEC-300](https://capec.mitre.org/data/definitions/300.html)
- [CAPEC-301](https://capec.mitre.org/data/definitions/301.html)
- [CAPEC-302](https://capec.mitre.org/data/definitions/302.html)
- [CAPEC-303](https://capec.mitre.org/data/definitions/303.html)
- [CAPEC-304](https://capec.mitre.org/data/definitions/304.html)
- [CAPEC-305](https://capec.mitre.org/data/definitions/305.html)
- [CAPEC-306](https://capec.mitre.org/data/definitions/306.html)
- [CAPEC-307](https://capec.mitre.org/data/definitions/307.html)
- [CAPEC-308](https://capec.mitre.org/data/definitions/308.html)
- [CAPEC-309](https://capec.mitre.org/data/definitions/309.html)
- [CAPEC-310](https://capec.mitre.org/data/definitions/310.html)
- [CAPEC-312](https://capec.mitre.org/data/definitions/312.html)
- [CAPEC-313](https://capec.mitre.org/data/definitions/313.html)
- [CAPEC-317](https://capec.mitre.org/data/definitions/317.html)
- [CAPEC-318](https://capec.mitre.org/data/definitions/318.html)
- [CAPEC-319](https://capec.mitre.org/data/definitions/319.html)
- [CAPEC-320](https://capec.mitre.org/data/definitions/320.html)
- [CAPEC-321](https://capec.mitre.org/data/definitions/321.html)
- [CAPEC-322](https://capec.mitre.org/data/definitions/322.html)
- [CAPEC-323](https://capec.mitre.org/data/definitions/323.html)
- [CAPEC-324](https://capec.mitre.org/data/definitions/324.html)
- [CAPEC-325](https://capec.mitre.org/data/definitions/325.html)
- [CAPEC-326](https://capec.mitre.org/data/definitions/326.html)
- [CAPEC-327](https://capec.mitre.org/data/definitions/327.html)
- [CAPEC-328](https://capec.mitre.org/data/definitions/328.html)
- [CAPEC-329](https://capec.mitre.org/data/definitions/329.html)
- [CAPEC-330](https://capec.mitre.org/data/definitions/330.html)
- [CAPEC-472](https://capec.mitre.org/data/definitions/472.html)
- [CAPEC-497](https://capec.mitre.org/data/definitions/497.html)
- [CAPEC-508](https://capec.mitre.org/data/definitions/508.html)
- [CAPEC-573](https://capec.mitre.org/data/definitions/573.html)
- [CAPEC-574](https://capec.mitre.org/data/definitions/574.html)
- [CAPEC-575](https://capec.mitre.org/data/definitions/575.html)
- [CAPEC-576](https://capec.mitre.org/data/definitions/576.html)
- [CAPEC-577](https://capec.mitre.org/data/definitions/577.html)
- [CAPEC-59](https://capec.mitre.org/data/definitions/59.html)
- [CAPEC-60](https://capec.mitre.org/data/definitions/60.html)
- [CAPEC-616](https://capec.mitre.org/data/definitions/616.html)
- [CAPEC-643](https://capec.mitre.org/data/definitions/643.html)
- [CAPEC-646](https://capec.mitre.org/data/definitions/646.html)
- [CAPEC-651](https://capec.mitre.org/data/definitions/651.html)
- [CAPEC-79](https://capec.mitre.org/data/definitions/79.html)

## Related weaknesses
- CWE-668 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-31162**: Rust library leaks Oauth client details in application debug logs
- **CVE-2021-25476**: Digital Rights Management (DRM) capability for mobile platform leaks pointer information, simplifying ASLR bypass
- **CVE-2001-1483**: Enumeration of valid usernames based on inconsistent responses
- **CVE-2001-1528**: Account number enumeration via inconsistent responses.
- **CVE-2004-2150**: User enumeration via discrepancies in error messages.
- **CVE-2005-1205**: Telnet protocol allows servers to obtain sensitive environment information from clients.
- **CVE-2002-1725**: Script calls phpinfo(), revealing system configuration to web user
- **CVE-2002-0515**: Product sets a different TTL when a port is being filtered than when it is not being filtered, which allows remote attackers to identify filtered ports by comparing TTLs.
- **CVE-2004-0778**: Version control system allows remote attackers to determine the existence of arbitrary files and directories via the -X command for an alternate history file, which causes different error messages to be returned.
- **CVE-2000-1117**: Virtual machine allows malicious web site operators to determine the existence of files on the client by measuring delays in the execution of the getSystemResource method.
- **CVE-2003-0190**: Product immediately sends an error message when a user does not exist, which allows remote attackers to determine valid usernames via a timing attack.
- **CVE-2008-2049**: POP3 server reveals a password in an error message after multiple APOP commands are sent. Might be resultant from another weakness.
- **CVE-2007-5172**: Program reveals password in error message if attacker can trigger certain database errors.
- **CVE-2008-4638**: Composite: application running with high privileges (CWE-250) allows user to specify a restricted file to process, which generates a parsing error that leaks the contents of the file (CWE-209).
- **CVE-2007-1409**: Direct request to library file in web application triggers pathname leak in error message.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/200.html
