# Describing Born-Digital Archives in ArchivesSpace
Draft created December 2022 by Emmeline Kaser, updated February 2026 by Brenna Edwards

## Purpose
This document contains the workflow for updating the collection resource record in ArchivesSpace to include born-digital materials so they are requestable through the reading room.  

## Workflow
1. For hybrid collections, discuss with the processing archivist how born-digital materials should be arranged and/or integrated with paper materials in the finding aid 
    * Files are described at the AIP level, so this should factor into arrangement decisions 
2. From the collection's resource record, create an archival object record for each "file" (AIP) of digital records 
    * Make sure you are in *Edit* mode 
    * If placing in-situ: 
        * Navigate to Archival Object above where the new Archival Object will be inserted 
        * Click *Add Sibling*
    * If placing anywhere, or rearranging later, in the Resource: 
        * Make sure to be on the top-most level (the Collection Resource record) 
        * Click *Add Child*
    * Required data fields for Archival Object records:  
        * Title: AIP title 
            * Be sure to add *[electronic files]* to the end of the title 
        * Level of Description: *File*
            * Should match the other Archival Objects 
        * Publish? Yes
        * Date: creation date 
            * Begin and end dates not needed here 
        * Extent in GB 
        * Instances 
    * Instances field: 
        * Type: electronic_records 
        * Top Container: create a new record (arrow to right -> *Create*)  
            * Top Container record: 
                * Container Type: electronic_records 
                * Indicator: *ER [AIP #]* 
                * Barcode: AIP ID 
                * Click *Create and Link to Top Container*
        * Save the Archival Onject 
            * If creating a list next to each other, click *+1* next to the *Save* button 
3. Update the collection (resource) record with date, scope note, extent, and note information to reflect the digital materials 
    * Note: Conditions Governing Access 
        * Local Access Restriction Type: 2 - Repository imposed access restriction 
        * This collection contains digital files. To access these files, please request the folders you would like through the finding aid using your research account. An archivist will be in contact with you to explain how to access the files. Please note that not all file formats are currently supported by the library for research use. 
4. Save Resource record  
5. For hybrid collections, notify processing archivist that the finding aid is ready for review if needed

## Publishing the finding aid
1. Log into the ArchviesSpace exporter tool
2. Choose proper repository for the collections to update - Russell or Hargrett 
    * Only one repository can be chosen at a time
3. Type in the resource identifier(s) for the collection(s) you want to update
    * Russell - enter RBRL# 
    * Hargrett - enter ms#  
4. Click *Export*
5. Wait for "Job execution: success" message
6. Close out of the ASpace Batch Exporter tool
7. Verify the intended changes have occurred by checking the finding aids staging server

## For files with redacted or otherwise altered access copies: 
* Include a *General Note* in the Notes field of each AIP's archival object record: "These files contain redactions. All redacted files include "_redacted" in the file name." 
* Can be made more specific as appropriate, e.g. "These files contain redacted contact information," etc. 

## For files that have been migrated or reformatted:  
* Include *Processing Information* in the Notes field of each AIP's archival object record: "These files have been [migrated/reformatted] to [new format] from [old format] [date] for [preservation/access]. These files will have [date] file creation dates instead of the original file creation date noted in the description."
* Can be made more specific as appropriate. 

## For larger, complex collections: 
1. Generate a file-level CSV inventory of each AIP (this can be automated with technical-appraisal-logs.py) 
    * Inventories must include file path, size, date created, and date modified for each file 
        * Redacted or reformatted files must have the original date information in the CSV (created and modified dates, as the file was received at the libraries) and a note describing what was changed, e.g. "Reformatted from .wdb to .csv on 1-6-2023" 
    * Save the inventories in a folder with the collection number on the SCLDigital OneDrive account 
    * Make sure the CSV cannot be edited and that viewing permissions are set to "public"  
2. Link the publicly-viewable inventory to the AIP's archival object in a Notes > Scope and Contents field: 
    * [free text scope note of AIP contents] 
    * `<emph render="bold"><extref actuate="onload" show="new" href="[inventory link]">View an inventory of this folder online.</extref></emph>`