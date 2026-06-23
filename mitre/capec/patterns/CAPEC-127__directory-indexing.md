---
capec_id: CAPEC-127
name: Directory Indexing
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Medium
related_cwe: [CWE-424, CWE-425, CWE-288, CWE-285, CWE-732, CWE-276, CWE-693]
related_attack: [T1083]
url: https://capec.mitre.org/data/definitions/127.html
tags: [mitre-capec, attack-pattern, CAPEC-127]
---

# CAPEC-127 - Directory Indexing

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-127](https://capec.mitre.org/data/definitions/127.html)

## Description
An adversary crafts a request to a target that results in the target listing/indexing the content of a directory as output. One common method of triggering directory contents as output is to construct a request containing a path that terminates in a directory name rather than a file name since many applications are configured to provide a list of the directory's contents when such a request is received. An adversary can use this to explore the directory tree on a target as well as learn the names of files. This can often end up revealing test files, backup files, temporary files, hidden files, configuration files, user accounts, script contents, as well as naming conventions, all of which can be used by an attacker to mount additional attacks.

## Prerequisites
- The target must be misconfigured to return a list of a directory's content when it receives a request that ends in a directory name rather than a file name.
- The adversary must be able to control the path that is requested of the target.
- The administrator must have failed to properly configure an ACL or has associated an overly permissive ACL with a particular directory.
- The server version or patch level must not inherently prevent known directory listing attacks from working.

## Skills required
- **High**: To bypass the access control of the directory of listings
- **Low**: To issue the request to URL without given a specific file name

## Resources required
- Ability to send HTTP requests to a web application.

## Consequences
- **Confidentiality**: Read Data (Information Leakage)

## Execution flow
Execution Flow Explore Directory Discovery: Use a method, either manual, scripted, or automated to discover the directories on the server by making requests for directories that may possibly exist. During this phase the adversary is less concerned with whether a directory can be accessed or indexed and more focused on simply discovering what directories do exist on the target. Techniques Send requests to the web server for common directory names If directories are discovered that are native to a server type further refine the directory search to include directories usually present on those types of servers. Search for uncommon or potentially user created directories that may be present. Experiment Iteratively explore directory/file structures: The adversary attempts to access the discovered directories that allow access and may attempt to bypass server or application level ACLs by using manual or automated methods Techniques Use a scanner tool to dynamically add directories/files to include their scan based upon data obtained in initial probes. Use a browser to manually explore the website by issuing a request ending the URL in a slash '/'. Attempt to bypass ACLs on directories by using methods that known to work against some server types by appending data to the directory request. For instance, appending a Null byte to the end of the request which may cause an ACL to fail and allow access. Sequentially request a list of common base files to each directory discovered. Try multiple fuzzing techniques to list directory contents for directories that will not reveal their contents with a "/" request Exploit Read directories or files which are not intended for public viewing.: The adversary attempts to access the discovered directories that allow access and may attempt to bypass server or application level ACLs by using manual or automated methods Techniques Try multiple exploit techniques to list directory contents for directories that will not reveal their contents with a "/" request Try other known exploits to elevate privileges sufficient to bypass protected directories. List the files in the directory by issuing a request with the URL ending in a "/" slash. Access the files via direct URL and capture contents. Attempt to bypass ACLs on directories by using methods that are known to work against some server types by appending data to the directory request. For instance, appending a Null byte to the end of the request which may cause an ACL to fail and allow access. Sequentially request a list of common base files to each directory discovered.

## Mitigations
- 1. Using blank index.html: putting blank index.html simply prevent directory listings from displaying to site visitors.
- 2. Preventing with .htaccess in Apache web server: In .htaccess, write "Options-indexes".
- 3. Suppressing error messages: using error 403 "Forbidden" message exactly like error 404 "Not Found" message.

## Related weaknesses (CWE)
- [CWE-424](https://cwe.mitre.org/data/definitions/424.html)
- [CWE-425](https://cwe.mitre.org/data/definitions/425.html)
- [CWE-288](https://cwe.mitre.org/data/definitions/288.html)
- [CWE-285](https://cwe.mitre.org/data/definitions/285.html)
- [CWE-732](https://cwe.mitre.org/data/definitions/732.html)
- [CWE-276](https://cwe.mitre.org/data/definitions/276.html)
- [CWE-693](https://cwe.mitre.org/data/definitions/693.html)

## Related ATT&CK techniques
- T1083

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/127.html
