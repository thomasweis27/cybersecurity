import re

# Function to extract dates from the log file
def extract_dates(input_filename, output_filename):
    extracted_dates = []

    # Regular expression to match the date in the format YYYY-MM-DD
    date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')

    # Open the log file and read it line by line
    with open(input_filename, 'r') as file:
        for line in file:
            # Search for the date pattern
            match = date_pattern.search(line)
            if match:
                date = match.group(0)
                extracted_dates.append(date)

    # Write the extracted dates to the output file
    with open(output_filename, 'w') as output_file:
        output_file.write("Extracted dates:\n")
        for date in extracted_dates:
            output_file.write(f"{date}\n")

# Call the function with the input log file and the desired output file
extract_dates('login.log', 'dates_output.txt')
