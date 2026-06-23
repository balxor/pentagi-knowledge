---
capec_id: CAPEC-209
name: XSS Using MIME Type Mismatch
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-79, CWE-20, CWE-646]
related_attack: []
url: https://capec.mitre.org/data/definitions/209.html
tags: [mitre-capec, attack-pattern, CAPEC-209]
---

# CAPEC-209 - XSS Using MIME Type Mismatch

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-209](https://capec.mitre.org/data/definitions/209.html)

## Description
An adversary creates a file with scripting content but where the specified MIME type of the file is such that scripting is not expected. The adversary tricks the victim into accessing a URL that responds with the script file. Some browsers will detect that the specified MIME type of the file does not match the actual type of its content and will automatically switch to using an interpreter for the real content type. If the browser does not invoke script filters before doing this, the adversary's script may run on the target unsanitized, possibly revealing the victim's cookies or executing arbitrary script in their browser.

## Prerequisites
- The victim must follow a crafted link that references a scripting file that is mis-typed as a non-executable file.
- The victim's browser must detect the true type of a mis-labeled scripting file and invoke the appropriate script interpreter without first performing filtering on the content.

## Resources required
- The adversary must have the ability to source the file of the incorrect MIME type containing a script.

## Execution flow
Execution Flow Explore Survey the application for stored user-controllable inputs: Using a browser or an automated tool, an adversary follows all public links and actions on a web site. They record all areas that allow a user to upload content through an HTTP POST request. This is typically found in blogs or forums. Techniques Use a spidering tool to follow and record all links and analyze the web pages to file upload features Use a proxy tool to record all links visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Experiment Probe identified potential entry points for MIME type mismatch: The adversary uses the entry points gathered in the "Explore" phase as a target list and uploads files with scripting content, but whose MIME type is specified as a file type that cannot execute scripting content. If the application only checks the MIME type of the file, it may let the file through, causing the script to be executed by any user who accesses the file. Techniques Upload a script file with a MIME type of text/plain to a forum and then access the uploaded file to see if the script is executed. If possible, the script displays a unique identifier so the adversary knows for certain it was executed when testing. Store malicious XSS content: Once the adversary has determined which file upload locations are vulnerable to MIME type mismatch, they will upload a malicious script disguised as a non scripting file. The adversary can have many goals, from stealing session IDs, cookies, credentials, and page content from a victim. Techniques Use a tool such as BeEF to store a hook into the web application. This will alert the adversary when the victim has accessed the content and will give the adversary control over the victim's browser, allowing them access to cookies, user screenshot, user clipboard, and more complex XSS attacks. Exploit Get victim to view stored content: In order for the attack to be successful, the victim needs to view the stored malicious content on the webpage. Techniques Send a phishing email to the victim containing a URL that will direct them to the malicious stored content. Simply wait for a victim to view the content. This is viable in situations where content is posted to a popular public forum.

## Related weaknesses (CWE)
- [CWE-79](https://cwe.mitre.org/data/definitions/79.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-646](https://cwe.mitre.org/data/definitions/646.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/209.html
