---
cwe_id: CWE-827
name: Improper Control of Document Type Definition
type: weakness
abstraction: Variant
status: Incomplete
languages: [XML]
related_capec: []
url: https://cwe.mitre.org/data/definitions/827.html
tags: [mitre-cwe, weakness, CWE-827]
---

# CWE-827 - Improper Control of Document Type Definition

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-827](https://cwe.mitre.org/data/definitions/827.html)

## Description
The product does not restrict a reference to a Document Type Definition (DTD) to the intended control sphere. This might allow attackers to reference arbitrary DTDs, possibly causing the product to expose files, consume excessive system resources, or execute arbitrary http requests on behalf of the attacker.

## Extended description
As DTDs are processed, they might try to read or include files on the machine performing the parsing. If an attacker is able to control the DTD, then the attacker might be able to specify sensitive resources or requests or provide malicious content. For example, the SOAP specification prohibits SOAP messages from containing DTDs.

## Applicable platforms / languages
XML

## Common consequences
- **Confidentiality**: Read Files or Directories
- **Availability**: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory)
- **Integrity, Confidentiality, Availability, Access Control**: Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity

## Related weaknesses
- CWE-706 (ChildOf)
- CWE-829 (ChildOf)
- CWE-776 (CanPrecede)

## Observed examples (CVE)
- **CVE-2010-2076**: Product does not properly reject DTDs in SOAP messages, which allows remote attackers to read arbitrary files, send HTTP requests to intranet servers, or cause a denial of service.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/827.html
