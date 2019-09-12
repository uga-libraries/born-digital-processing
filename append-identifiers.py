# Written for Python 3.7.1
# Appends collection number and sequential aip identifier to each folder in a target directory.
# Required arguments:
    # (1) script name
    # (2) target directory
    # (3) collection number (e.g., 456)

import os
from sys import argv

errors = []     # create a list to hold error messages
if len(argv) == 3:        # if we are passed three arguments
    if os.path.exists(argv[1]):     # check if target directory exists
        if os.path.isdir(argv[1]):  # check if target directory is a directory
            target = argv[1]
        else:
            errors.append(f"Target directory {argv[1]} is not a valid directory.")  # if not a directory, add to error messages
    else:
        errors.append(f"Target directory {argv[1]} does not exist.")  # if it does not exist, add to error messages

    if len(argv[2]) == 3 and argv[2].isdigit():   # check if collection number is a three digit number 3 digits
        collection_number = argv[2]
    else:
        errors.append(f"Collection number {argv[2]} is not valid. Collection number must be a three digit number.")     # if collection number is invalid, add to error messages.
else:
    print("Please specify a target directory and collection number")
    exit()

if len(errors) > 0:     # if there are errors, print each error message
  for error in errors:
    print(error)
    exit()

os.chdir(target)

# rename each directory in target directory by appending collection number and aip id to front
aip_id = 1
for directory in os.listdir(target):
    os.rename(directory,f"rbrl-{collection_number}-er-{aip_id:06d}_{directory}")
    aip_id += 1
