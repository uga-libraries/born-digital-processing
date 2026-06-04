# Collection Documentation Guidelines

Version 1.0 created by Brenna Edwards, February 2026, updated June 2026

## Purpose 

This document outlines which documentation created through the accessioning, appraisal, and processing workflows goes into the permanent Collection Documentation folder in the Digital Stewardship Teams document library. 

## Collection Folders
Top level folders will be named according to the collection ID number. Both Hargrett and Russell materials will live in the same top-level folder (Collection Documentation), differentiated by their collection ID number.  

Inside each collection folder, separated by accession number:  
* Technical-analysis script outputs 
    * Initialmanifest_[date] 
    * Filestoreview_[date] 
    * Deletionlog_[date] 
* Format-analysis script outputs
    * [accession-number]_fits 
    * [accession-number]_format-analysis 
    * [accession-number]_full_risk_data 
* [collection-number]_medialabels 
* Manifest-md5 
    * Presumably copied out to main folder, but could also be located in bag 
* Any deaccession or appraisal notes 

Inside each collection folder, outside of accession-specific folders:  
* Preservation_log.txt 
* ProcessingPlan.docx 
* From processing copy folder: 
    * Initialmanifest_date  
    * Filestoreview_date 
* From AIP workflow: 
    * Aip_log.csv 
    * Fits-xml folder 
    * Preservation-xml folder 
    * Any additional notes or documents from AIP creation (aip_qc_results.txt, fixity_comparison.xslx, etc) 
    * IF different versions of AIPs: 
        * Create AIP_Version# folders: 
            * Aip_log.csv  
            * Fits-xml folder  
            * Preservation-xml folder 
        * aip_qc_results.txt 
        * fixity_comparison.xslx 
* Risk_remediation 
    * Deletion logs created 
    * Aip_log.csv 
    * Fits-xml folder 
    * Preservation-xml folder 

## Deaccessioned Collections
If a collection has had born-digital material deaccessioned, the following files are retained as permanent documentation in Collection Documentation\Deaccessioned:  
* Technical-analysis script outputs 
    * Initialmanifest_date 
    * Filestoreview_date 
* Format-analysis script outputs 
    * [accession-number]_fits 
    * [accession-number]_format-analysis 
    * [accession-number]_full_risk_data 
* Preservation_log 
* Any deaccession or appraisal notes 
* From the bag: 
    * Bag-info.txt 
    * Manifest-md5.txt 

## Deletion
Once the files listed above are successfully uploaded to the Collection Documentation folder, the Digital Archivist can then delete the collection fodler from the Hub, and update the Hub inventory spreadsheet. 