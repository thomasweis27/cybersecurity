import re

# Define the function that processes the log file
def process_log_file(input_filename, output_filename):
    total_bytes = 0
    extracted_numbers = []

    # Regular expression to match lines containing "UPLOAD" and extract the number before "bytes"
    bytes_pattern = re.compile(r'DOWNLOAD.*?,\s*(\d+)\s+bytes')

    # Open the vsftpd.log file and read line by line
    with open(input_filename, 'r') as file:
        for line in file:
            if "DOWNLOAD" in line and "bytes" in line and "ftpuser" in line:
                # Search for the pattern and extract the number before "bytes"
                match = bytes_pattern.search(line)
                if match:
                    number_before_bytes = int(match.group(1))
                    extracted_numbers.append(number_before_bytes)
                    total_bytes += number_before_bytes

    # Write the extracted numbers and total to the output file
    with open(output_filename, 'w') as output_file:
        output_file.write("Numbers before 'bytes':\n")
        for num in extracted_numbers:
            output_file.write(f"{num}\n")
        output_file.write(f"\nTotal bytes: {total_bytes}\n")

# Call the function with the input log file and the desired output file
process_log_file('vsftpd.log', 'output.txt')
