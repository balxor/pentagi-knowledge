---
cwe_id: CWE-616
name: Incomplete Identification of Uploaded File Variables (PHP)
type: weakness
abstraction: Variant
status: Incomplete
languages: [PHP]
related_capec: []
url: https://cwe.mitre.org/data/definitions/616.html
tags: [mitre-cwe, weakness, CWE-616]
---

# CWE-616 - Incomplete Identification of Uploaded File Variables (PHP)

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-616](https://cwe.mitre.org/data/definitions/616.html)

## Description
The PHP application uses an old method for processing uploaded files by referencing the four global variables that are set for each file (e.g. $varname, $varname_size, $varname_name, $varname_type). These variables could be overwritten by attackers, causing the application to process unauthorized files.

## Extended description
These global variables could be overwritten by POST requests, cookies, or other methods of populating or overwriting these variables. This could be used to read or process arbitrary files by providing values such as "/etc/passwd".

## Applicable platforms / languages
PHP

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Potential mitigations
- **Architecture and Design**: Use PHP 4 or later.
- **Architecture and Design**: If you must support older PHP versions, write your own version of is_uploaded_file() and run it against $HTTP_POST_FILES['userfile']))
- **Implementation**: For later PHP versions, reference uploaded files using the $HTTP_POST_FILES or $_FILES variables, and use is_uploaded_file() or move_uploaded_file() to ensure that you are dealing with an uploaded file.

## Related weaknesses
- CWE-345 (ChildOf)
- CWE-473 (PeerOf)

## Observed examples (CVE)
- **CVE-2002-1460**: Forum does not properly verify whether a file was uploaded or if the associated variables were set by POST, allowing remote attackers to read arbitrary files.
- **CVE-2002-1759**: Product doesn't check if the variables for an upload were set by uploading the file, or other methods such as $_POST.
- **CVE-2002-1710**: Product does not distinguish uploaded file from other files.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/616.html
