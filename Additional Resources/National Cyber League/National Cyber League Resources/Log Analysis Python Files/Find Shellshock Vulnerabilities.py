"""
Find the usage of Shellshock vulnerabilities and attempts to send the related to 'shellshock_detected.log'.
"""

import re

# Define the input and output files
input_file = 'access.log'
output_file = 'shellshock_detected.log'

# Regular expression pattern to detect Shellshock attempts
shellshock_pattern = re.compile(r"\(\)\s*{\s*:\s*;\s*}\s*;")

# Open the input file and the output file
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    # Iterate over each line in the input file
    for line in infile:
        # Search for the Shellshock pattern in the line
        if shellshock_pattern.search(line):
            # Write the matching line to the output file
            outfile.write(line)

print(f"Shellshock attempts have been written to {output_file}")
