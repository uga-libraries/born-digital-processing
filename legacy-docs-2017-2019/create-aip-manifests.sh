#!/bin/bash

# Purpose: Create text file inventory (manifest) for each aip using the Linux Tree Command
# Required arguments:
    # (1) the path of the target directory containing the aips

# Check that required arguments have been entered in the terminal.
if [ "$#" -ne "1" ]
then echo "Error: Provide target directory to run script"
    exit 1
fi

# Check that provided target directory is a valid directory.
if [ ! -d "$1" ]
then echo "Error: Target directory is not a valid directory."
    exit 1
fi

cd "$1"  # change to target directory entered as argv[1]

mkdir ../inventories-to-link-to-finding-aid  # make a new directory to hold the inventories

for d in "$1" * ;
do
    if [ -d "$d" ] ;  # if item in target directory is a directory
    then
        cd "$d"     # change to that directory
        tree -D -h -I "*_manifest.txt" -o "$d"_manifest.txt    # create manifest for the contents of the aip directory that includes the date last modified and size in human readible format, ignoring the *_manifest.txt files created by the script
        cd "$1"    # return to the target and repeat
    fi
done

find . -type f -name "*_manifest.txt" | xargs -I {} mv {} ../inventories-to-link-to-finding-aid      # find all the manifests and move them to the "inventories-to-link-to-finding-aid" folder
