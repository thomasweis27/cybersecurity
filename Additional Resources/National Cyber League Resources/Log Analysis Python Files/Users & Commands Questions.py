"""
The code will get the following information:
* Q1 - Number of users who ran sudo commands: 5
* Q2 - Number of unique commands run: 6
* Q3 - Number of commands successfully run: 657
* Q4 - Number of commands unsuccessfully run: 343
* Q5 - User with the most opened sessions: alice
"""

import re
from collections import defaultdict, Counter

# Read the log file
with open("audit.log", "r") as file:
    logs = file.readlines()

# Q1 - Number of users who ran sudo commands
sudo_users = set()
for log in logs:
    match = re.search(r'sudo:\s+(\w+)\s+:', log)
    if match:
        sudo_users.add(match.group(1))

num_sudo_users = len(sudo_users)
print("Q1 - Number of users who ran sudo commands:", num_sudo_users)

# Q2 - Number of unique commands run
commands = set()
for log in logs:
    match = re.search(r'COMMAND=(.+)', log)
    if match:
        commands.add(match.group(1))

num_unique_commands = len(commands)
print("Q2 - Number of unique commands run:", num_unique_commands)

# Q3 - Number of successfully run commands (session opened/closed logs indicate success)
success_count = sum(1 for log in logs if "session closed" in log or "session opened" in log)
print("Q3 - Number of commands successfully run:", success_count)

# Q4 - Number of unsuccessfully run commands (authentication failure logs)
failure_count = sum(1 for log in logs if "authentication failure" in log)
print("Q4 - Number of commands unsuccessfully run:", failure_count)

# Q5 - User with the most opened sessions
sessions = defaultdict(int)
for log in logs:
    match = re.search(r'session opened for user root by (\w+)', log)
    if match:
        sessions[match.group(1)] += 1

most_sessions_user = max(sessions, key=sessions.get)
print("Q5 - User with the most opened sessions:", most_sessions_user)
