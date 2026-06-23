---
cwe_id: CWE-625
name: Permissive Regular Expression
type: weakness
abstraction: Base
status: Draft
languages: [Perl, PHP]
related_capec: []
url: https://cwe.mitre.org/data/definitions/625.html
tags: [mitre-cwe, weakness, CWE-625]
---

# CWE-625 - Permissive Regular Expression

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-625](https://cwe.mitre.org/data/definitions/625.html)

## Description
The product uses a regular expression that does not sufficiently restrict the set of allowed values.

## Extended description
This effectively causes the regexp to accept substrings that match the pattern, which produces a partial comparison to the target. In some cases, this can lead to other weaknesses. Common errors include: not identifying the beginning and end of the target string using wildcards instead of acceptable character ranges others

## Applicable platforms / languages
Perl, PHP

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: When applicable, ensure that the regular expression marks beginning and ending string patterns, such as "/^string$/" for Perl.

## Related weaknesses
- CWE-185 (ChildOf)
- CWE-187 (PeerOf)
- CWE-184 (PeerOf)
- CWE-183 (PeerOf)

## Observed examples (CVE)
- **CVE-2021-22204**: Chain: regex in EXIF processor code does not correctly determine where a string ends (CWE-625), enabling eval injection (CWE-95), as exploited in the wild per CISA KEV.
- **CVE-2006-1895**: ".*" regexp leads to static code injection
- **CVE-2002-2175**: insertion of username into regexp results in partial comparison, causing wrong database entry to be updated when one username is a substring of another.
- **CVE-2006-4527**: regexp intended to verify that all characters are legal, only checks that at least one is legal, enabling file inclusion.
- **CVE-2005-1949**: Regexp for IP address isn't anchored at the end, allowing appending of shell metacharacters.
- **CVE-2002-2109**: Regexp isn't "anchored" to the beginning or end, which allows spoofed values that have trusted values as substrings.
- **CVE-2006-6511**: regexp in .htaccess file allows access of files whose names contain certain substrings
- **CVE-2006-6629**: allow load of macro files whose names contain certain substrings.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/625.html
