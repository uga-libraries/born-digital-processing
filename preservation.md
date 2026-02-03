# Preservation: AIP Creation and Ingest into ARCHive

## Roles

As of January 2026, the Digital Archivist organizes the contents into AIP folders and makes the metadata.csv
and the Head of Digital Stewardship makes AIPs and ingests them into ARCHive.


Communication is managed through the Born-Digital Collections Tracking in Planner.

## AIP Creation

### Preparation
1. Copy PreservationCopy from Hub to local machine with TeraCopy. (until address permission issues)
2. Move each AIP folder into a temporary folder, which can be renamed with the AIP ID. (until update script)
3. Update the folder column in metadata.csv to match the temporary folders.

### Script
1. Make a copy of aips_directory, for an easier restart in case of script errors.
2. Verify the configuration.py paths are correct
3. Run [general_aip.py](https://github.com/uga-libraries/general-aip)

### Quality Control
Results are documented in aip_qc_results.txt. Template in Digital Stewardship Teams.

1. Review AIP log for errors.
2. Zip all preservation.xml and validate in ARCHive, adding collection if needed.
3. Compare MD5 checksums of the accession(s) to the AIP(s) using the bag manifests.
4. Check 1-5 AIPs (depending on number of AIPs and level of difference) in more detail.
    * Bag has MD5 and SHA manifests.
    * Bag has objects and metadata folders.
    * The number of files in objects matches the number of FITS in metadata.
    * The contents of preservation.xml matches the metadata.csv and combined FITS XML.

## ARCHive Ingest

## Documentation and Hand Off