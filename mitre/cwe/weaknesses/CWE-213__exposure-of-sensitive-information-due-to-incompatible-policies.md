---
cwe_id: CWE-213
name: Exposure of Sensitive Information Due to Incompatible Policies
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/213.html
tags: [mitre-cwe, weakness, CWE-213]
---

# CWE-213 - Exposure of Sensitive Information Due to Incompatible Policies

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-213](https://cwe.mitre.org/data/definitions/213.html)

## Description
The product's intended functionality exposes information to certain actors in accordance with the developer's security policy, but this information is regarded as sensitive according to the intended security policies of other stakeholders such as the product's administrator, users, or others whose information is being processed.

## Extended description
When handling information, the developer must consider whether the information is regarded as sensitive by different stakeholders, such as users or administrators. Each stakeholder effectively has its own intended security policy that the product is expected to uphold. When a developer does not treat that information as sensitive, this can introduce a vulnerability that violates the expectations of the product's users.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Related weaknesses
- CWE-200 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-1725**: Script calls phpinfo()
- **CVE-2004-0033**: Script calls phpinfo()
- **CVE-2003-1181**: Script calls phpinfo()
- **CVE-2004-1422**: Script calls phpinfo()
- **CVE-2004-1590**: Script calls phpinfo()
- **CVE-2003-1038**: Product lists DLLs and full pathnames.
- **CVE-2005-1205**: Telnet protocol allows servers to obtain sensitive environment information from clients.
- **CVE-2005-0488**: Telnet protocol allows servers to obtain sensitive environment information from clients.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/213.html
