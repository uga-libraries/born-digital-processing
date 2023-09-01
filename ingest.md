# Creating and Ingesting AIPs into ARCHive

Finalized preservation copies of digital files should be ingested into the digital preservation system as AIPs. **Only preservation versions (AIPs) should be ingested. Altered access copies are considered DIPs and should be stored on the Digital Production Hub.**


## Create AIPs from arranged material
Digital Stewardship uses a custom Python script to create AIPs that are packaged with the appropriate PREMIS metadata. 

The [README](https://github.com/uga-libraries/general-aip#readme) file in the [general-aip repository](https://github.com/uga-libraries/general-aip/tree/main) contains instructions for using the [general-aip.py](https://github.com/uga-libraries/general-aip/blob/main/scripts/general_aip.py) script, including guidance for creating the required [metadata CSV](https://github.com/uga-libraries/general-aip#metadata-file-required-for-script) file with relevant departmental and collection information. Follow the instructions in that repo to create your AIPs.
         
## Ingest, QC, and delete AIPs from temporary storage
1. Copy AIPs to the appropriate ingest server using [TeraCopy](https://github.com/uga-libraries/born-digital-accessioning/blob/main/teracopy.md). 
2. Ingest the files into ARCHive and check for completeness. _NOTE: Technical instructions for ingest and the ARCHive interface are not publicly available. Refer to Digital Stewardship's internal ARCHive documentation._
3. Add a TXT file to the collection folder titled ingested.txt documenting which AIPs have been ingested, when, and by whom.
4. If immediate reformatting is required, create and ingest a second version of the AIPs with reformatted files.
5. Once any necessary access copies have been created and saved to Hub storage, AIPs and collection material can be deleted from the collection folder.