---
cwe_id: CWE-409
name: Improper Handling of Highly Compressed Data (Data Amplification)
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/409.html
tags: [mitre-cwe, weakness, CWE-409]
---

# CWE-409 - Improper Handling of Highly Compressed Data (Data Amplification)

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-409](https://cwe.mitre.org/data/definitions/409.html)

## Description
The product does not handle or incorrectly handles a compressed input with a very high compression ratio that produces a large output.

## Extended description
An example of data amplification is a "decompression bomb," a small ZIP file that can produce a large amount of data when it is decompressed.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Availability**: DoS: Amplification, DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory)

## Related weaknesses
- CWE-405 (ChildOf)

## Observed examples (CVE)
- **CVE-2009-1955**: XML bomb in web server module
- **CVE-2003-1564**: Parsing library allows XML bomb

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/409.html
