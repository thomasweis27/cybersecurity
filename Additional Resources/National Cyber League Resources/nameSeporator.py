import re

# Function to process the log file
def extract_names(input_filename, output_filename):
    extracted_names = []

    # Regular expression to match the IP address and extract the name following it
    name_pattern = re.compile(r'\d+\.\d+\.\d+\.\d+\s+(\S+)')

    # Open the log file and read line by line
    with open(input_filename, 'r') as file:
        for line in file:
            # Search for the pattern and extract the name after the IP address
            match = name_pattern.search(line)
            if match:
                name = match.group(1)
                extracted_names.append(name)

    # Write the extracted names to the output file
    with open(output_filename, 'w') as output_file:
        output_file.write("Extracted names:\n")
        for name in extracted_names:
            output_file.write(f"{name}\n")

# Call the function with the input log file and the desired output file
extract_names('login.log', 'names_output.txt')
