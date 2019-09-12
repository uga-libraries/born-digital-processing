# Born-Digital-Processing

## Purpose
Scripts used by Russell Library to arrange and describe born-digital archival AIPs prior to ingesting them into the UGA Libraries digital repository.

## Description

### append-identifiers.py
Python script that appends collection number and sequential AIP identifier to each AIP in a target directory so that they are in compliance with the naming procedures outlined in the AIP creation workflow documentation.

Run the script with the command: 
`python append-identifiers.py path/to/target/directory/containing/aips collection-number`


### create-aip-manifests.sh
Bash shell script that creates a text file manifest (inventory) for each AIP in a target directory using the Linux `tree` command. Manifests include the date last modified and size in human readible format for each file. These text file inventories can be linked in the online finding aid to provide AIP-level description for the collection.

Run the script with the command: 
`create-aip-manifests.sh path/to/target/directory/containing/aips`
   
## Initial Author
Brandon Pieczko, Processing and Digital Archivist, 2019
