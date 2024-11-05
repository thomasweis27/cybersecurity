"""
A program that will find the day with the most requests and the following number of requests.
"""

from collections import defaultdict
import re

# Define the input file
input_file = 'access.log'

# Dictionary to store the count of requests per day
request_count_per_day = defaultdict(int)

# Regular expression pattern to extract the date from log entries
# Assuming the log format has the date in the format [DD/Mon/YYYY:HH:MM:SS]
date_pattern = re.compile(r"\[(\d{2}/\w{3}/\d{4})")

# Open the input file
with open(input_file, 'r') as infile:
    # Iterate over each line in the input file
    for line in infile:
        # Search for the date in the line using the regex pattern
        match = date_pattern.search(line)
        if match:
            # Extract the date (only the day part) and increment the request count for that day
            request_date = match.group(1)
            request_count_per_day[request_date] += 1

# Find the day with the maximum number of requests
max_requests_day = max(request_count_per_day, key=request_count_per_day.get)
max_requests = request_count_per_day[max_requests_day]

# Output the result
print(f"The day with the most requests is {max_requests_day} with {max_requests} requests.")
