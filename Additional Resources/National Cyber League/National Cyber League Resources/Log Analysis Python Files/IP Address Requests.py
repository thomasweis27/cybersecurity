"""
A program that finds the IP address that made the most requests and also the number of requests made.
"""

from collections import defaultdict
import re

# Define the input file
input_file = 'access.log'

# Dictionaries to store request counts per IP and total bytes transferred
request_count_per_ip = defaultdict(int)
total_bytes_transferred = 0

# Regular expression patterns
ip_pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+)')  # Extracts the IP address
bytes_pattern = re.compile(r'(\d+|-)\s*"[^"]*"$')   # Captures bytes before the last field in the line

# Open the input file and process each line
with open(input_file, 'r') as infile:
    for line in infile:
        # Extract the IP address from the line
        ip_match = ip_pattern.match(line)
        if ip_match:
            ip_address = ip_match.group(1)
            # Increment the request count for the IP
            request_count_per_ip[ip_address] += 1

        # Extract the bytes transferred
        bytes_match = bytes_pattern.search(line)
        if bytes_match:
            bytes_transferred = bytes_match.group(1)
            # Only add if the bytes transferred is not a dash '-'
            if bytes_transferred != '-':
                total_bytes_transferred += int(bytes_transferred)

# Q3: Find the IP address that made the most requests
most_requests_ip = max(request_count_per_ip, key=request_count_per_ip.get)
most_requests_count = request_count_per_ip[most_requests_ip]

# Output the result for Q3
print(f"The IP address that made the most requests is {most_requests_ip} with {most_requests_count} requests.")

# Q4: Output the result for total bytes transferred
print(f"The total number of bytes transferred is {total_bytes_transferred} bytes.")
