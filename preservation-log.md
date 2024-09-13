# Preservation Log

Hargrett and Russell A&D uses a preservation log to record every action taken on a group of files, organized by accession and by each piece of removable media/file transfer. The log includes the action taken, tool used (if applicable), results of the action, and who performed the action.

There should be one preservation log per accession. The document is saved as a plain text, tab-delimited file (.txt).

## Information Recorded

Each row should only have information about one action taken on the files associated with a single ([Digital Media Identifier](./digital-media-identifier.md)). Record preservation actions as they occur so that the documentation is accurate and up-to-date. Relevant events include virus scanning, copying, bag creation, and bag validation (or other fixity validation).

* **Collection number:** The collection number for the materials, including any library-specific prefixes (RBRL, HARG.MS).

* **Accession number:** The accession number for the materials, which must include "-ER" at the end.

* **Date:** format YYYY-MM-DD. For actions that span more than one day, record the date the process finished.

* **Media Identifier:** unique ID for the media the action was taken on ([Digital Media Identifier](./digital-media-identifier.md)).

* **Action:** include a description of the action, the software or hardware used to complete the action (if applicable), and the result. When applicable, use the standard language provided below to describe an action and its outcome.

* **Staff:** name of the staff person who performed the action.

    ### [View sample preservation log](./sample-preservation-log.txt)

## Examples of Standardized Language Used

### Virus Scanning

*   Virus scanned with Microsoft Defender Antivirus. No security threats were detected.

*   Virus scanned with Microsoft Defender Antivirus. The following files were identified as viruses: _[list file path and name]_.

*   This media contains a virus and does not have high research value. The media was not copied.

*   _[filename]_ was identified as containing a virus. After research, it was determined that this was a false positive. The file can be copied and the file extension will be changed to _[whatever used]_ so that the file will no longer be identified as a virus.

*   _[filename]_ was identified as containing a virus. After research, it was determined that this is likely a virus. Other files on this disk do have high research value. They were copied to removable media and re-scanned for viruses. _[filename]_ was excluded.

*   _[filename]_ was identified as containing a virus. After research, it was determined that this is likely a virus. The rest of the file has have high research value. It was copied to removable media, the copy cleaned with Microsoft Defender Antivirus, and re-scanned using the same software. No security threats were detected.


### Copying

*   Copied files from _[source]_ to _[location]_ using TeraCopy. No errors were detected.

    *   Common sources: transfer media, removable media

    *   Common storage locations: Hub, external media (if copying from several smaller media like floppy disks)

    *   Common software: TeraCopy, Microsoft Defender Antivirus. Include the version number as well.

*   Attempted to copy files from _[source]_ to _[location]_ using TeraCopy.  _[describe errors]_

### Bagging

*   Bagged with accession _[accession number]_ using bagit.py. No errors were detected.

*   Validated bag for _[accession number]_ using bagit.py. The bag was valid.

### Appraisal (of previously copied files)

*   No files were kept from this disk after appraisal. The files were deleted from _[preservation location]_.

## Revision History 

Originally created by Brandon Pieczko, Processing and Digital Archivist, in 2019 and added to current documentation suite with minor updates in 2023 by Emmeline Kaser, Digital Archivist.

The workflow was updated in September 2024 by Emmeline Kaser to more accurately reflect the current documentation process and remove references to a database, as we currently have no plans for this. 
