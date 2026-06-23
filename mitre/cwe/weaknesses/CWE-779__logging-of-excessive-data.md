---
cwe_id: CWE-779
name: Logging of Excessive Data
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/779.html
tags: [mitre-cwe, weakness, CWE-779]
---

# CWE-779 - Logging of Excessive Data

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-779](https://cwe.mitre.org/data/definitions/779.html)

## Description
The product logs too much information, making log files hard to process and possibly hindering recovery efforts or forensic analysis after an attack.

## Extended description
While logging is a good practice in general, and very high levels of logging are appropriate for debugging stages of development, too much logging in a production environment might hinder a system administrator's ability to detect anomalous conditions. This can provide cover for an attacker while attempting to penetrate a system, clutter the audit trail for forensic analysis, or make it more difficult to debug problems in a production environment.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability**: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Other)
- **Non-Repudiation**: Hide Activities
- **Non-Repudiation**: Hide Activities

## Potential mitigations
- **Architecture and Design**: Suppress large numbers of duplicate log messages and replace them with periodic summaries. For example, syslog may include an entry that states "last message repeated X times" when recording repeated events.
- **Architecture and Design**: Support a maximum size for the log file that can be controlled by the administrator. If the maximum size is reached, the admin should be notified. Also, consider reducing functionality of the product. This may result in a denial-of-service to legitimate product users, but it will prevent the product from adversely impacting the entire system.
- **Implementation**: Adjust configurations appropriately when the product is transitioned from a debug state to production.

## Related weaknesses
- CWE-400 (ChildOf)

## Observed examples (CVE)
- **CVE-2007-0421**: server records a large amount of data to the server log when it receives malformed headers
- **CVE-2002-1154**: chain: application does not restrict access to front-end for updates, which allows attacker to fill the error log

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/779.html
