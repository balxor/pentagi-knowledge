---
cwe_id: CWE-187
name: Partial String Comparison
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/187.html
tags: [mitre-cwe, weakness, CWE-187]
---

# CWE-187 - Partial String Comparison

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-187](https://cwe.mitre.org/data/definitions/187.html)

## Description
The product performs a comparison that only examines a portion of a factor before determining whether there is a match, such as a substring, leading to resultant weaknesses.

## Extended description
For example, an attacker might succeed in authentication by providing a small password that matches the associated portion of the larger, correct password.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Integrity, Access Control**: Alter Execution Logic, Bypass Protection Mechanism

## Potential mitigations
- **Testing**: Thoroughly test the comparison scheme before deploying code into production. Perform positive testing as well as negative testing.

## Related weaknesses
- CWE-1023 (ChildOf)

## Observed examples (CVE)
- **CVE-2014-6394**: Product does not prevent access to restricted directories due to partial string comparison with a public directory
- **CVE-2004-1012**: Argument parser of an IMAP server treats a partial command "body[p" as if it is "body.peek", leading to index error and out-of-bounds corruption.
- **CVE-2004-0765**: Web browser only checks the hostname portion of a certificate when the hostname portion of the URI is not a fully qualified domain name (FQDN), which allows remote attackers to spoof trusted certificates.
- **CVE-2002-1374**: One-character password by attacker checks only against first character of real password.
- **CVE-2000-0979**: One-character password by attacker checks only against first character of real password.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/187.html
