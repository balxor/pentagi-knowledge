---
cwe_id: CWE-943
name: Improper Neutralization of Special Elements in Data Query Logic
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-676]
url: https://cwe.mitre.org/data/definitions/943.html
tags: [mitre-cwe, weakness, CWE-943]
---

# CWE-943 - Improper Neutralization of Special Elements in Data Query Logic

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

## Description
The product generates a query intended to access or manipulate data in a data store such as a database, but it does not neutralize or incorrectly neutralizes special elements that can modify the intended logic of the query.

## Extended description
Depending on the capabilities of the query language, an attacker could inject additional logic into the query to: Modify the intended selection criteria, thus changing which data entities (e.g., records) are returned, modified, or otherwise manipulated Append additional commands to the query Return more entities than intended Return fewer entities than intended Cause entities to be sorted in an unexpected way The ability to execute additional commands or change which entities are returned has obvious risks. But when the product logic depends on the order or number of entities, this can also lead to vulnerabilities. For example, if the query expects to return only one entity that specifies an administrative user, but an attacker can change which entities are returned, this could cause the logic to return information for a regular user and incorrectly assume that the user has administrative privileges. While this weakness is most commonly associated with SQL injection, there are many other query languages that are also subject to injection attacks, including HTSQL, LDAP, DQL, XQuery, Xpath, and "NoSQL" languages.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity, Availability, Access Control**: Bypass Protection Mechanism, Read Application Data, Modify Application Data, Varies by Context

## Related attack patterns (CAPEC)
- [CAPEC-676](https://capec.mitre.org/data/definitions/676.html)

## Related weaknesses
- CWE-74 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-50672**: NoSQL injection in product for building eLearning courses allows password resets using a query processed by the Mongoose find function
- **CVE-2021-20736**: NoSQL injection in team collaboration product
- **CVE-2020-35666**: NoSQL injection in a PaaS platform using a MongoDB operator
- **CVE-2014-2503**: Injection using Documentum Query Language (DQL)
- **CVE-2014-2508**: Injection using Documentum Query Language (DQL)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/943.html
