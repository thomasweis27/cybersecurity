"""
A program that will find the total number of bytes transferred.
"""

import re

# Define the input file
input_file = 'access.log'

# Initialize total bytes transferred counter
total_bytes_transferred = 0

# Regular expression to match the log format and capture the bytes transferred
log_pattern = re.compile(r'\s(\d{3})\s(\d+)\s')

# Open the input file and process each line
with open(input_file, 'r') as infile:
    for line in infile:
        # Search for the bytes transferred in the line
        match = log_pattern.search(line)
        if match:
            # Extract the bytes transferred (second captured group)
            bytes_transferred = match.group(2)
            total_bytes_transferred += int(bytes_transferred)

# Output the result for total bytes transferred
print(f"The total number of bytes transferred is {total_bytes_transferred} bytes.")
