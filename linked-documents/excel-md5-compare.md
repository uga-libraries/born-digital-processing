# Using Excel to Compare MD5

## Purpose
Compare the bag MD5 manifests for all accessions and all AIPs 
To verify that no files were accidentally deleted or altered during processing or AIP creation.

## Workflow Summary
Verify that every file's path and fixity (MD5) match between the accession(s) and AIP(s). 
Paths are compared and not just fixity to account for duplicates and to have enough information about missing or altered content to evaluate.

Paths for the accessions must be updated to match arrangement and folder renaming (e.g., removing media numbers)
and paths for AIPs must be updated to remove AIP-specific folders and metadata files.
The comparison must also take into account files purposefully deleted or restricted during processing.

## Workflow
1. Make an Excel file named fixity_comparison.xlsx in the parent folder of PreservationCopy.
2. Name the columns Accession MD5, Accession Path (modified), MD5 Match, Path Match, AIP MD5, AIP Path
3. Copy the contents of every MD5 manifest from the accession bags to the Accession MD5 column.
4. Copy the contents of every MD5 manifest from the AIP bags to the AIP MD5 column.
5. Replace "  data" (2 spaces) with "|data" to have a delimiter for splitting MD5s from paths.
6. Use text-to-columns to split each MD5 column on "|" and get paths to the correct column.
7. Sort AIP Path and delete the AIP columns for that row if the path starts data/metadata.
8. Replace data/objects with data.
9. Remove media IDs from the Accession Path column.
10. Sort the two path columns independently.
11. Use the if function to populate MD5 Match and Path Match.
    * If the path is only in the Accession, check the file deletion log and processing plan for restrictions.
    * If the paths aren't aligning, sort the two MD5 columns independently and look for changes from the arrangement.

## Future Plans
This will be automated with a script when time allows, to support efficient scaling.
The first collections being processed with this requirement are very small and can be done manually,
so it is not currently the top priority for development time.