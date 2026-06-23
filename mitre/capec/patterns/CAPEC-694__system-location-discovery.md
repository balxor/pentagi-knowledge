---
capec_id: CAPEC-694
name: System Location Discovery
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Very Low
related_cwe: [CWE-497]
related_attack: [T1614]
url: https://capec.mitre.org/data/definitions/694.html
tags: [mitre-capec, attack-pattern, CAPEC-694]
---

# CAPEC-694 - System Location Discovery

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Very Low  -  **CAPEC:** [CAPEC-694](https://capec.mitre.org/data/definitions/694.html)

## Description
<xhtml:p>An adversary collects information about the target system in an attempt to identify the system's geographical location.</xhtml:p>
            <xhtml:p>Information gathered could include keyboard layout, system language, and timezone. This information may benefit an adversary in confirming the desired target and/or tailoring further attacks.</xhtml:p>

## Prerequisites
- The adversary must have some level of access to the system and have a basic understanding of the operating system in order to query the appropriate sources for relevant information.

## Skills required
- **Low**: The adversary must know how to query various system sources of information respective of the system's operating system to obtain the relevant information.

## Resources required
- The adversary requires access to the target's operating system tools to query relevant system information. On windows, registry queries can be conducted with powershell, wmi, or regedit. On Linux or macOS, queries can be performed with through a shell.

## Consequences
- **Confidentiality**: Read Data

## Execution flow
Execution Flow Explore System Locale Information Discovery: The adversary examines system information from various sources such as registry and native API functions and correlates the gathered information to infer the geographical location of the target system Techniques Registry Query: Query the registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ContentIndex\Language\Language_Dialect on Windows to obtain system language, Computer\HKEY_CURRENT_USER\Keyboard Layout\Preload to obtain the hexadecimal language IDs of the current user's preloaded keyboard layouts, and Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation to obtain the system timezone configuration Native API Requests: Parse the outputs of Windows API functions GetTimeZoneInformation, GetUserDefaultUILanguage, GetSystemDefaultUILanguage, GetKeyboardLayoutList and GetUserDefaultLangID to obtain information about languages, keyboard layouts, and timezones installed on the system or on macOS or Linux systems, query locale to obtain the $LANG environment variable and view keyboard layout information or use timeanddatectl status to show the system clock settings. Read Configuration Files: For macOS and Linux-based systems, view the /etc/vconsole.conf file to get information about the keyboard mapping and console font.

## Mitigations
- To reduce the amount of information gathered, one could disable various geolocation features of the operating system not required for system operation.

## Related weaknesses (CWE)
- [CWE-497](https://cwe.mitre.org/data/definitions/497.html)

## Related ATT&CK techniques
- T1614

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/694.html
