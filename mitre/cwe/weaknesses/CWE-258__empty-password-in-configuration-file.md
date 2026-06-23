---
cwe_id: CWE-258
name: Empty Password in Configuration File
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/258.html
tags: [mitre-cwe, weakness, CWE-258]
---

# CWE-258 - Empty Password in Configuration File

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-258](https://cwe.mitre.org/data/definitions/258.html)

## Description
Using an empty string as a password is insecure.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **System Configuration**: Passwords should be at least eight characters long -- the longer the better. Avoid passwords that are in any way similar to other passwords you have. Avoid using words that may be found in a dictionary, names book, on a map, etc. Consider incorporating numbers and/or punctuation into your password. If you do use common words, consider replacing letters in that word with numbers and punctuation. However, do not use "similar-looking" punctuation. For example, it is not a good idea to change cat to c@t, ca+, (@+, or anything similar. Finally, it is never appropriate to use an empty string as a password.

## Related weaknesses
- CWE-260 (ChildOf)
- CWE-521 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-26117**: Network access control (NAC) product has a configuration file with an empty password

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/258.html
