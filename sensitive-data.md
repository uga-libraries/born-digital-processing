# Identifying and Redacting Sensitive Information in Born-Digital Archives 

Version 1.0 created by Emmeline Kaser, October 2022, updated March 2023 

## Purpose 

This document outlines tools and procedures for identifying and securely redacting sensitive information in non-AV born-digital archives. 

## Terms and definitions  

**Altered access copies:** access copies that are different from the preservation copies stored in ARCHive, e.g. reformatted files or files with redactions

**Sensitive information:** information that should not be made available to the public for legal/confidentiality reasons, because it contains cultural knowledge considered private to a particular community, and/or because it poses a personal risk to an individual (SSNs, credit card numbers, login credentials, bank information, etc.)

**Sensitivity:** the amount of sensitive information or restricted content in a given collection, as specified by the donor agreement or as identified by the archivist according to organizational policy and/or archival best practice

## Tools 
* [Bulk Reviewer](https://github.com/bulk-reviewer/bulk-reviewer#readme) (installed on BitCurator machine) 
* Windows Explorer search
* Adobe Acrobat Pro 
* pdf-batch-redaction.py 

## Process overview 

1. Identify sensitive info with keyword searches and Bulk Reviewer 
2. Suggest actions for each element flagged as sensitive 
3. Receive archivist sign-off on suggestions 
4. Ingest original files in ARCHive as V1 
5. Reformat files as required (optional)
6. Ingest reformatted versions into ARCHive as V2 (optional)
7. Make appropriate redactions to a copy of the most recent version of the files 
8. Save redacted versions of AIPs as access copies (DIPs)
9. Create finding aid inventories from DIPs and include redaction dates
10. Add Special Access Policy rights statement to AIPs with access copies 

## Identifying information for redaction

Very small collections can be manually reviewed for sensitive information, but this becomes untenable if there are more than just a few files. Use a combination of keyword searches and automated file-level scanning to identify areas that may require redaction.

1. During accessioning and [format analysis](./format-assessment-and-migration.md), keep an eye out for any obvious areas that may contain private information, e.g. directories with names like "taxes" or "financial."
2. For large collections, perform a high-level keyword search in Windows Explorer if you suspect (or have been told by the donor) that there may be large chunks of sensitive data to remove.
3. Scan the collection with Bulk Reviewer on the BitCurator machine. Bulk Reviewer scans the content of most file formats to find patterns or terms indicating sensitive data. **All collections with anticipated sensitivity should be scanned using Bulk Reviewer.** 
   * Bulk Reviewer can search directories and disk images for [several common categories of sensitive data](https://github.com/bulk-reviewer/bulk-reviewer#readme). These categories can be toggled on and off in the application. **Generally speaking, a scan should always look for Social Security Numbers, credit card numbers, and GPS data.** Other categories can be toggled on if they are especially sensitive within the collection. 
   * Use a [regular expressions file](https://bulk-reviewer.readthedocs.io/en/latest/newscan.html#processing-options) to search for specific terms. Sensitive topics (e.g. restricted cultural knowledge, health data, etc.) will need to be identified with term-based searching. Consult with the collection's archivist to determine what this sensitive data may look like and which terms may be most helpful to search.
4. Review the log of flagged elements created by Bulk Reviewer. "Dismiss" any that are obvious false positives. Export a CSV of the remaining results. 
5. Add an "Action" and "Notes" column to the CSV log. 
   * Use the "Action" column to suggest whether a whole file should be deleted or just the element redacted.
   * Use the "Notes" column to explain the suggested action as needed.
6. At the end of the CSV log, add any additional files or areas within files that were found through the Windows Explorer search or manual review.
   * The Bulk Reviewer scan is not always definitive and can be used to point to areas that require additional human review. 
7. Suggest an action for each element or file in the log.
8. Link the log to the Trello card for the collection and alert the collecting archivist that it needs review. 
   * The archivist can make the final determination for which files should be fully appraised out or redacted.

## Redaction 

When a file is redacted, an access copy of that file must be created. That access copy then needs to be monitored for format obsolescence, migrated as needed, and all changes documented over time. Because of these ongoing labor requirements, the digital archivist and collecting archivist should consider appraisal as an alternative solution for sensitive information when possible.

PDFs and spreadsheets are the most straightforward file types to redact. At this time, we are creating normalized access copies of redacted files in these formats when possible. 

**Redacted files should only be saved as access copies in the Digital Production Hub. They should not be ingested into ARCHive.**

1. Original versions of the files should already be ingested into ARCHive as Version 1. 
2. If the files must be reformatted as part of the processing plan, reformat them before making any redactions. This **does not** apply to files that are normalized for the purpose of redaction.
   * Ingest AIPs with reformatted files into ARCHive as Version 2.
3. Make a copy of the most recent versions of the AIPs. These will become the redacted access copies. 
4. For PDFs: Redact any sensitive elements from the PDF using the "Redact" tool in Adobe Acrobat. PDFs are the most straightforward format to redact. If it is possible to convert the file to a PDF, this is recommended. 
5. For spreadsheets: Delete sensitive columns or cell contents and save as a new version of the file.
6. Save the redacted version of the file with "_redacted" appended to the file name.
7. If the format has been normalized for the purpose of redaction, make sure "_reformatted" is appended to the file name.
   * Redaction workflows for other formats are in development.
8. Save redacted versions of AIPs as access copies (DIPs).
9. Create finding aid inventories from DIPs and include redaction dates.
10. Add a Special Access Policy rights statement in the digital preservation system for AIPs with access copies.