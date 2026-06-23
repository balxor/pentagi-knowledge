---
cwe_id: CWE-1333
name: Inefficient Regular Expression Complexity
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-492]
url: https://cwe.mitre.org/data/definitions/1333.html
tags: [mitre-cwe, weakness, CWE-1333]
---

# CWE-1333 - Inefficient Regular Expression Complexity

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1333](https://cwe.mitre.org/data/definitions/1333.html)

## Description
The product uses a regular expression with a worst-case computational complexity that is inefficient and possibly exponential.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability**: DoS: Resource Consumption (CPU)

## Potential mitigations
- **Architecture and Design**: Use regular expressions that do not support backtracking, e.g. by removing nested quantifiers.
- **System Configuration**: Set backtracking limits in the configuration of the regular expression implementation, such as PHP's pcre.backtrack_limit. Also consider limits on execution time for the process.
- **Implementation**: Do not use regular expressions with untrusted input. If regular expressions must be used, avoid using backtracking in the expression.
- **Implementation**: Limit the length of the input that the regular expression will process.

## Related attack patterns (CAPEC)
- [CAPEC-492](https://capec.mitre.org/data/definitions/492.html)

## Related weaknesses
- CWE-407 (ChildOf)
- CWE-407 (ChildOf)

## Observed examples (CVE)
- **CVE-2020-5243**: server allows ReDOS with crafted User-Agent strings, due to overlapping capture groups that cause excessive backtracking.
- **CVE-2021-21317**: npm package for user-agent parser prone to ReDoS due to overlapping capture groups
- **CVE-2019-16215**: Markdown parser uses inefficient regex when processing a message, allowing users to cause CPU consumption and delay preventing processing of other messages.
- **CVE-2019-6785**: Long string in a version control product allows DoS due to an inefficient regex.
- **CVE-2019-12041**: Javascript code allows ReDoS via a long string due to excessive backtracking.
- **CVE-2015-8315**: ReDoS when parsing time.
- **CVE-2015-8854**: ReDoS when parsing documents.
- **CVE-2017-16021**: ReDoS when validating URL.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1333.html
