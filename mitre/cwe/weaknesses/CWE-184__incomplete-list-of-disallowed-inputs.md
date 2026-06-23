---
cwe_id: CWE-184
name: Incomplete List of Disallowed Inputs
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-120, CAPEC-15, CAPEC-182, CAPEC-3, CAPEC-43, CAPEC-6, CAPEC-71, CAPEC-73, CAPEC-85]
url: https://cwe.mitre.org/data/definitions/184.html
tags: [mitre-cwe, weakness, CWE-184]
---

# CWE-184 - Incomplete List of Disallowed Inputs

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-184](https://cwe.mitre.org/data/definitions/184.html)

## Description
The product implements a protection mechanism that relies on a list of inputs (or properties of inputs) that are not allowed by policy or otherwise require other action to neutralize before additional processing takes place, but the list is incomplete.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: Do not rely exclusively on detecting disallowed inputs. There are too many variants to encode a character, especially when different environments are used, so there is a high likelihood of missing some variants. Only use detection of disallowed inputs as a mechanism for detecting suspicious activity. Ensure that you are using other protection mechanisms that only identify "good" input - such as lists of allowed inputs - and ensure that you are properly encoding your outputs.

## Related attack patterns (CAPEC)
- [CAPEC-120](https://capec.mitre.org/data/definitions/120.html)
- [CAPEC-15](https://capec.mitre.org/data/definitions/15.html)
- [CAPEC-182](https://capec.mitre.org/data/definitions/182.html)
- [CAPEC-3](https://capec.mitre.org/data/definitions/3.html)
- [CAPEC-43](https://capec.mitre.org/data/definitions/43.html)
- [CAPEC-6](https://capec.mitre.org/data/definitions/6.html)
- [CAPEC-71](https://capec.mitre.org/data/definitions/71.html)
- [CAPEC-73](https://capec.mitre.org/data/definitions/73.html)
- [CAPEC-85](https://capec.mitre.org/data/definitions/85.html)

## Related weaknesses
- CWE-693 (ChildOf)
- CWE-1023 (ChildOf)
- CWE-79 (CanPrecede)
- CWE-78 (CanPrecede)
- CWE-434 (CanPrecede)
- CWE-98 (CanPrecede)

## Observed examples (CVE)
- **CVE-2024-6091**: Chain: AI agent platform does not restrict pathnames containing internal "/./" sequences (CWE-55), leading to an incomplete denylist (CWE-184) that does not prevent OS command injection (CWE-78)
- **CVE-2024-4315**: Chain: API for text generation using Large Language Models (LLMs) does not include the "\" Windows folder separator in its denylist (CWE-184) when attempting to prevent Local File Inclusion via path traversal (CWE-22), allowing deletion of arbitrary files on Windows systems.
- **CVE-2024-44335**: Chain: filter only checks for some shell-injection characters (CWE-184), enabling OS command injection (CWE-78)
- **CVE-2008-2309**: product uses a denylist to identify potentially dangerous content, allowing attacker to bypass a warning
- **CVE-2005-2782**: PHP remote file inclusion in web application that filters "http" and "https" URLs, but not "ftp".
- **CVE-2004-0542**: Programming language does not filter certain shell metacharacters in Windows environment.
- **CVE-2004-0595**: XSS filter doesn't filter null characters before looking for dangerous tags, which are ignored by web browsers. MIE and validate-before-cleanse.
- **CVE-2005-3287**: Web-based mail product doesn't restrict dangerous extensions such as ASPX on a web server, even though others are prohibited.
- **CVE-2004-2351**: Resultant XSS when only <script> and <style> are checked.
- **CVE-2005-2959**: Privileged program does not clear sensitive environment variables that are used by bash. Overlaps multiple interpretation error.
- **CVE-2005-1824**: SQL injection protection scheme does not quote the "\" special character.
- **CVE-2005-2184**: Detection of risky filename extensions prevents users from automatically executing .EXE files, but .LNK is accepted, allowing resultant Windows symbolic link.
- **CVE-2007-1343**: Product uses list of protected variables, but accidentally omits one dangerous variable, allowing external modification
- **CVE-2007-5727**: Chain: product only removes SCRIPT tags (CWE-184), enabling XSS (CWE-79)
- **CVE-2006-4308**: Chain: product only checks for use of "javascript:" tag (CWE-184), allowing XSS (CWE-79) using other tags

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/184.html
