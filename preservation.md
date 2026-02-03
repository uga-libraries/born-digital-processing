# Preservation: AIP Creation and Ingest into ARCHive

## Roles

As of January 2026, the Digital Archivist organizes the contents into AIP folders and makes the metadata.csv
and the Head of Digital Stewardship makes AIPs and ingests them into ARCHive.
This is a workflow that the Head of Digital Stewardship is already doing for other departments,
so it frees up more time for the Digital Archivist to process 
and spares them another set of scripts and tools to be responsible for learning.

Communication is managed through the Born-Digital Collections Tracking in Planner.

## AIP Creation
Create AIPs within one month of being assigned a collection in Planner.

### Preparation
1. Move PreservationCopy from Hub to local machine with TeraCopy. (until address permission issues)
2. Move each AIP folder into a temporary folder, which can be renamed with the AIP ID. (until update script)
3. Update the folder column in metadata.csv to match the temporary folders.

TBD: check that AIPs do not exceed maximum size of 100 GB and 10,000 files.
See [aip_prep.py](https://github.com/uga-libraries/congressional-mail/blob/main/aip_prep.py) 
for automatically splitting AIPs that are too large and have no logical subdivisions.
Consult with the Digital Archivist to update IDs in the description if splitting AIPs
or establish a naming convention to keep AIP ID and DIP ID related but different,
like AIP ID = DIP ID + additional sequential number.

### Script
1. Make a copy of aips_directory, for an easier restart in case of script errors.
2. Verify the configuration.py paths are correct
3. Run [general_aip.py](https://github.com/uga-libraries/general-aip)

### Quality Control
Results are documented in [aip_qc_results.txt](linked-documents/aip_qc_results.txt)

1. Review AIP log for errors.
2. Zip all preservation.xml and validate in ARCHive, adding collection if needed.
3. Compare MD5 checksums of the accession(s) to the AIP(s) using the bag manifests. [excel-md5-compare.md](linked-documents/excel-md5-compare.md)
4. Check 1-5 AIPs (depending on number of AIPs and level of difference) in more detail.
    * Bag has MD5 and SHA manifests.
    * Bag has objects and metadata folders.
    * The number of files in objects matches the number of FITS in metadata.
    * The contents of preservation.xml matches the metadata.csv and combined FITS XML.
    * Look for anything that doesn't look right.
5. Note PASS/FAIL for the AIP Creation portion of aip_qc_results.txt

## ARCHive Ingest
Add the AIPs to UGA's digital preservation system. See DCWG Teams for documentation.

### Job Scheduling
1. Copy the zipped AIPs to the ARCHive ingest folder.
2. Schedule the job for ingest via the ARCHive application

### Quality Control
1. Review the Job Summary in the ARCHive application for errors.
2. Compare the preservation.xml and manifest.csv to the metadata in the ARCHive application for the AIP sample.
3. Check the version and audit logs in the ARCHive application for the AIP sample.
4. Request one file back from ARCHive.
    * Only do this once per day if creating AIPs for multiple collections, as the ARCHive automatic ingest verification is sound.
    * Validate the zip MD5 or unzip and validate the bag.
    * Check the copy request log for the AIP in the ARCHive application.
5. Note PASS/FAIL for the ARCHIVE INGEST portion of aip_qc_results.txt.

## Documentation and Hand Off

### Hub
Move PreservationCopy back into the Hub collection folder,
which now contains all the script outputs and logs.

At the end of processing, the Digital Archivist will move permanent documentation to the collections folder in Digital Stewardship Teams
and delete all other files from Hub.

### Preservation Log
Add an event for AIP creation and ingest.

Standard text for both on the same day:
* Created # AIPs with general_aip.py and ingested into ARCHive with no errors.

Standard text for different days (need to wait for ARCHive ingest to complete for final QC)
* Created # AIPs with general_aip.py with no errors.
* Ingested into ARCHive with no errors.

### Planner
This is how the Digital Archivist will be notified that preservation is complete.

1. In the checklist, mark Preservation: AIP creation and ingest as complete.
2. Add a comment if anything unusual happened.
3. Change the person assigned to the Digital Archivist, which generates an email notification.
4. Move the collection to the Finding Aid column