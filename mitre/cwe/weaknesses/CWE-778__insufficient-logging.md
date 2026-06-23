---
cwe_id: CWE-778
name: Insufficient Logging
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Cloud Computing, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/778.html
tags: [mitre-cwe, weakness, CWE-778]
---

# CWE-778 - Insufficient Logging

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-778](https://cwe.mitre.org/data/definitions/778.html)

## Description
When a security-critical event occurs, the product either does not record the event or omits important details about the event when logging it.

## Extended description
When security-critical events are not logged properly, such as a failed login attempt, this can make malicious behavior more difficult to detect and may hinder forensic analysis after an attack succeeds. As organizations adopt cloud storage resources, these technologies often require configuration changes to enable detailed logging information, since detailed logging can incur additional costs. This could lead to telemetry gaps in critical audit logs. For example, in Azure, the default value for logging is disabled.

## Applicable platforms / languages
Not Language-Specific, Cloud Computing, Not Technology-Specific

## Common consequences
- **Non-Repudiation**: Hide Activities

## Potential mitigations
- **Architecture and Design**: Use a centralized logging mechanism that supports multiple levels of detail.
- **Implementation**: Ensure that all security-related successes and failures can be logged. When storing data in the cloud (e.g., AWS S3 buckets, Azure blobs, Google Cloud Storage, etc.), use the provider's controls to enable and capture detailed logging information.
- **Operation**: Be sure to set the level of logging appropriately in a production environment. Sufficient data should be logged to enable system administrators to detect attacks, diagnose errors, and recover from attacks. At the same time, logging too much data (CWE-779) can cause the same problems, including unexpected costs when using a cloud environment.
- **Operation**: To enable storage logging using Azure's Portal, navigate to the name of the Storage Account, locate Monitoring (CLASSIC) section, and select Diagnostic settings (classic). For each of the various properties (blob, file, table, queue), ensure the status is properly set for the desired logging data. If using PowerShell, the Set-AzStorageServiceLoggingProperty command could be called using appropriate -ServiceType, -LoggingOperations, and -RetentionDays arguments.

## Related weaknesses
- CWE-223 (ChildOf)

## Observed examples (CVE)
- **CVE-2008-4315**: server does not log failed authentication attempts, making it easier for attackers to perform brute force password guessing without being detected
- **CVE-2008-1203**: admin interface does not log failed authentication attempts, making it easier for attackers to perform brute force password guessing without being detected
- **CVE-2007-3730**: default configuration for POP server does not log source IP or username for login attempts
- **CVE-2007-1225**: proxy does not log requests without "http://" in the URL, allowing web surfers to access restricted web content without detection
- **CVE-2003-1566**: web server does not log requests for a non-standard request type

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/778.html
