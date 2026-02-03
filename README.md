# Processing Workflow for Born-Digital Archives
The Hargrett Rare Book and Manuscript Library and The Richard B. Russell Jr. Library for Political Research and Studies, 
University of Georgia Special Collections Libraries

The following processes were instituted in August 2022. 
Digital archives processing is the responsibility of the Digital Archivist in the Digital Stewardship unit. 
This is a unified workflow that receives born-digital archival material from both the Russell and Hargrett libraries. 
The Digital Archivist works in collaboration with each library's processing archivists to properly address sensitive information 
and provide an appropriate level of description for each collection.

Starting in 2026, preservation steps were transferred to the Head of Digital Stewardship.

## Overview

Processing actions are defined here as processes that prepare born-digital archives for ingest 
into permanent digital preservation storage and subsequent researcher access. 
Processing begins after all digital components in a collection are [accessioned](https://github.com/uga-libraries/born-digital-accessioning#accessioning-workflow-for-born-digital-archives) and [appraised](https://github.com/uga-libraries/born-digital-accessioning/blob/main/appraisal.md).

This documentation references Python scripts in the [accessioning-scripts repository](https://github.com/uga-libraries/accessioning-scripts) in the UGA Libraries GitHub.

## Purpose 
Processed born-digital archives should be arranged as needed, any known sensitive information should be addressed 
(or there should be a plan to address it when materials are requested), imminent preservation risks should be remediated, 
and the materials should be discoverable via the collection's finding aid. 
Processed materials are ingested into the digital preservation system (ARCHive) for permanent storage.

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
   * TBD - may fit better with Head of Digital Stewardship's preservation role now.
   
3. If there is a risk for sensitive data, scan the collection using Bulk Reviewer in the BitCurator environment. 
   [Identify any sensitive information](./sensitive-data.md#identifying-information-for-redaction-) and decide if redaction or further appraisal is needed. 
   * Add this to the [processing plan,](./processing-plans.md) documented in the appropriate accession record(s).
   
4. Arrange material into AIP groupings as needed and document.
   * Maximum size of 100 GB and 10,000 files required for preservation system.
   * Preference for fewer formats in an AIP if possible, to aid in format migration.
   
5. If reformatting is required, create a second version of the AIPs. Reformat as needed and document.
    * May also reformat to improve access, in which case only alter what is in the DIP.

6. If [redaction](./sensitive-data.md#redaction-) is required, create access copies of the AIP groupings (DIPs). Redact as needed and document.

7. Make a copy of the AIP folders and create a metadata.csv, in preparation for making AIPs.
   * Put in a folder named PreservationCopy (sibling of ProcessingCopy), and within that, in a folder named aips_directory
   * Within aips_directory, also make metadata.csv using [template](https://github.com/uga-libraries/general-aip/blob/main/documentation/metadata.csv)
     * AIP ID is dept-coll-er-######
     * Collection ID should not include letters from legacy Russell ids, 
       but does include Hargrett repository letters like ms and ua
   * Move to Preservation column in Planner and assign responsibility to the Head of Digital Stewardship to notify
   
8. Head of Digital Stewardship makes and ingests AIPs [preservation.md](preservation.md)
   * Digital Archivist will simultaneously continue with description and access copies.
   
9. Generate file inventories for each DIP.

10. Perform subject analysis for description purposes as needed (workflow TBD).

11. Update the collection's resource record with AIP-level description and links to each AIP's file inventory spreadsheet.

12. Wrap up
    * Move permanent documentation from Hub to the collection folder in Digital Stewardship Teams.
    * Delete the collection folder from Hub and the Hub inventory.
    * Close card in Planner.

## Documentation Overview

The ArchivesSpace resource record provides an overview of the collection materials, 
including a complete list of AIPs with titles, size information, subject information, 
and a linked file inventory spreadsheet containing relevant information regarding any redaction and/or reformatting. 
The finding aid data is supplemented by the processing plan in the accession record 
and additional preservation documentation saved in the collection folder. 

This documentation includes:

  * File path change log, if applicable
  * Redaction log, if applicable
  * Reformatting log, if applicable
  * Arrangement log, if applicable
  * File inventories for each DIP
  * Ingest note
  * Preservation log
  * AIP creation log

## Policy Revision History

The first born-digital processing workflow was documented in the Hargrett and Russell libraries' 
"Electronic Records Processing Manual" created in 2013 by Adriane Hanson (then Processing and Digital Archivist, Russell Library). 
Additional documentation and scripts were created by Brandon Pieczko (Processing and Digital Archivist, Russell Library) in 2019. 
This documentation supersedes the prior suite of [born-digital processing documentation](https://github.com/uga-libraries/born-digital-processing/tree/main/legacy-docs-2017-2019) created at that time.

The initial version of this workflow was completed in August 2023 by Emmeline Kaser (Digital Archivist, Digital Stewardship) 
and represents the processes in place starting in August 2022. 
This workflow draws conceptually from older documentation but supersedes those processes due to changes in technological capabilities.

The portion of the workflow related to AIP creation was updated in February 2026 
by Adriane Hanson (Head of Digital Stewardship) and Brenna Edwards (Digital Archivist) 
to define a new collaboration between our two positions.

Documentation last reviewed: September 2024
