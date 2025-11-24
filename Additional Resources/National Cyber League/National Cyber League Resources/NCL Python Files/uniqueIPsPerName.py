import re
from collections import defaultdict

# Function to find the username with logins from the most unique IP addresses
def find_username_with_most_unique_ips(input_filename, output_filename):
    # Dictionary to store usernames and a set of their associated IPs
    user_ips = defaultdict(set)

    # Regular expression to match the IP address and username
    log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)\s+(\S+)')

    # Open the log file and read it line by line
    with open(input_filename, 'r') as file:
        for line in file:
            # Search for the pattern in the log lines
            match = log_pattern.search(line)
            if match:
                ip_address = match.group(1)
                username = match.group(2)

                # Add the IP address to the set of IPs for this username
                user_ips[username].add(ip_address)

    # Find the username with the most unique IP addresses
    max_unique_ips = 0
    top_user = None
    for username, ips in user_ips.items():
        if len(ips) > max_unique_ips:
            max_unique_ips = len(ips)
            top_user = username

    # Write the result to the output file
    with open(output_filename, 'w') as output_file:
        output_file.write(f"Username with the most unique IP addresses:\n")
        output_file.write(f"Username: {top_user}\n")
        output_file.write(f"Number of unique IP addresses: {max_unique_ips}\n")

# Call the function with the input log file and the desired output file
find_username_with_most_unique_ips('login.log', 'top_user_output.txt')
