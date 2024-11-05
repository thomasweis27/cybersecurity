"""
This file is made to sort out the lines in the file 'access.log' that contain 'GET /'. Change this to sort out different lines. 
"""

# Define the input and output files
input_file = 'access.log'
output_file = 'filtered_access.log'

# Open the input file and the output file
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    # Iterate over each line in the input file
    for line in infile:
        # Check if the line contains "GET /"
        if 'google' in line:
            # Write the matching line to the output file
            outfile.write(line)

print(f"Filtered lines have been written to {output_file}")
