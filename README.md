# Processing Workflow for Born-Digital Archives
### The Hargrett Rare Book and Manuscript Library and The Richard B. Russell Jr. Library for Political Research and Studies, University of Georgia Special Collections Libraries

The following processes were instituted in August 2022. Digital archives processing is the responsibility of the digital archivist in the Digital Stewardship unit. This is a unified workflow that receives born-digital archival material from both the Russell and Hargrett libraries. The digital archivist works in collaboration with each library's collecting archivists to properly address sensitive information and provide an appropriate level of description for each collection.

## Overview

Processing actions are defined here as processes that prepare born-digital archives for ingest into permanent digital preservation storage and subsequent researcher access. Processing begins after all digital components in a collection are [accessioned](https://github.com/uga-libraries/born-digital-accessioning#accessioning-workflow-for-born-digital-archives) and [appraised](https://github.com/uga-libraries/born-digital-accessioning/blob/main/appraisal.md).

This documentation references Python scripts in the [accessioning-scripts repository](https://github.com/uga-libraries/accessioning-scripts) in the UGA Libraries GitHub.

## Purpose 
Processed born-digital archives should be arranged as needed, any known sensitive information should be addressed (or there should be a plan to address it when materials are requested), imminent preservation risks should be remediated, and the materials should be discoverable via the collection's finding aid. Processed materials are ingested into the digital preservation system for permanent storage.

### The goals of this workflow:

1. Create a processing plan.

2. Arrange material into AIPs.

3. Address any imminently at-risk formats, if necessary.

4. Address any sensitive information.

5. Create, document, and properly store any altered access copies (DIPs).

6. Document all decisions and actions performed on a collection.

7. Generate file inventories for each DIP.

8. Turn arranged materials into AIPs and ingest into the digital preservation system.

9. Perform subject analysis for description purposes, if necessary.

10. Update and publish the finding aid.

## Procedure Overview

1. Assign a [processing tier](./processing-tiers.md) to the collection.
2. Run  [format_analysis.py](https://github.com/uga-libraries/accessioning-scripts#format-analysispy) and review the format report it creates. Decide if any immediate [file format migration](./format-assessment-and-migration.md) is needed. 
   * Add this to the [processing plan,](./processing-plans.md) documented in the appropriate accession record(s).
3. If there is a risk for sensitive data, scan the collection using Bulk Reviewer in the BitCurator environment. [Identify any sensitive information](./sensitive-data.md#identifying-information-for-redaction-) and decide if redaction or further appraisal is needed. 
   * Add this to the [processing plan,](./processing-plans.md) documented in the appropriate accession record(s).
4. Arrange material into AIP groupings as needed and document.
5. If reformatting is required, create a second version of the AIPs. Reformat as needed and document.
6. If [redaction](./sensitive-data.md#redaction-) is required, create access copies of the AIP groupings (DIPs). Redact as needed and document.
7. Generate file inventories for each DIP.
8. Turn the arranged materials into AIPs using the [general_aip.py](https://github.com/uga-libraries/general-aip) script. 
9. [Ingest the AIPs](./ingest.md) into the digital preservation system. The original files should always be ingested as Version 1. Any AIPs containing reformatted files should be ingested as Version 2.
10. Perform subject analysis for description purposes as needed (workflow TBD).
11. Update the collection's resource record with AIP-level description and links to each AIP's file inventory spreadsheet.

## Documentation Overview

The ArchivesSpace resource record provides an overview of the collection materials, including a complete list of AIPs with titles, size information, subject information, and a linked file inventory spreadsheet containing relevant information regarding any redaction and/or reformatting. The finding aid data is supplemented by additional preservation documentation saved in the collection folder. 

This documentation includes:

  * Processing plan in the accession record
  * File path change log, if applicable
  * Redaction log, if applicable
  * Reformatting log, if applicable
  * Arrangement log, if applicable
  * File inventories for each DIP
  * Ingest note


## Policy Revision History

The first born-digital processing workflow was documented in the Hargrett and Russell libraries' "Electronic Records Processing Manual" created in 2013 by Adriane Hanson (Head of Digital Stewardship). Additional documentation and scripts were created by Brandon Pieczko (Processing and Digital Archivist, Russell Library) in 2019. This documentation supersedes the prior suite of [born-digital processing documentation](https://github.com/uga-libraries/born-digital-processing/tree/main/legacy-docs-2017-2019) created at that time.

The initial version of this workflow was completed in August 2023 by Emmeline Kaser (Digital Archivist, Digital Stewardship) and represents the processes in place starting in August 2022. This workflow draws conceptually from older documentation but supersedes those processes due to changes in technological capabilities.

Documentation last reviewed: March 2024
