#!/usr/bin/env python3.7

import os

# Get the current working directory
directory = os.getcwd()

# Create an empty list to store file information
files = []

# Iterate through files in the current directory
for filename in os.listdir(directory):
    
    # Get the size, modified time, creation time, and path for each file
    file_size = os.path.getsize(filename)
    modified_time = os.path.getmtime(filename)
    creation_time = os.path.getctime(filename)
    file_path = os.path.realpath(filename)
   
    # Add a dictionary containing file information to the 'files' list
    files.append({'name': filename, 'size': file_size, 'time': modified_time, 'path': file_path})

# Print the list of dictionaries, one per file, with each dictionary separated by a newline
print(*files, sep="\n")