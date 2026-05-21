# Arrangement

## Reasons to arrange
We most commonly keep files organized the way they are received to retain the creator's context, provided they are usable in that way.

We reorganize to make them more usable:
- Unite content split across multiple pieces of transfer media
- Split up content arbitrarily together on the same transfer media
- Remove unnecessary levels of hierarchy
- Address file paths that are too long

## Current practices
Because we have the initial manifest which documents the original folder and file names and hierarchy,
it is acceptable to make changes to the organization and naming as needed without additional documentation.

Changes we make include:
- Rename a folder if it is abbreviated or cryptic and you are confident in what you're naming it.
- Add additional files to existing folders when they are clearly on the same subject.
- Add new folders to combine files and/or folders, and there is no naming convention to show we provided the title.## Splitting AIPs while retaining context

### When to split
The final arrangement determines the AIP boundaries.
We recommend (but do not require) an AIP be no more than 10,000 files and 100 GB.
A bigger AIP can be made if it is the most logical unit for access or it cannot be split into useful subdivisions in a reasonable amount of time.
Even if an AIP is small enough, consider splitting if:
- It would improve user experience (subfolders are ecclectic enough they are likely to just want part, better description)
- It makes for fewer formats per AIP, which means less duplication when we need to migrate a single format for preservation
- It improves ongoing management, like having shorter filelists to view in the ARCHive application and faster bag validation

### Procedure

INSERT INFO ON RUNNING SCRIPT TO TEST FOR SIZE ONCE HAVE IN THE BAGS REPO

To split a top-level folder into multiple AIPs while retaining the contextual information:
- Make folders with each AIP ID
- Make a folder within each AIP ID folder with the same name as the top-level folder to retain the relationship outside of the finding aid
- Copy the files for each subfolder into their own AIP ID folder

In the metadata.csv:
- Folder and AIP_ID columns are the AIP ID
- Title is Top Folder - Sub Folder | date-date

### Additional Considerations
Everything must be in a folder named with its AIP ID, instead of having the script do that, so they can all have the same top level folder.

It is not important to keep AIP IDs in sequential order.
So, if an AIP is split after AIP IDs have already been assigned, the first AIP keeps the original AIP ID and the remaining AIPs are assigned the next available in sequence.
