## Log Analysis

“Log analysis is the process of reviewing and interpreting log files to understand the performance, behavior, and security of a system”

The best items for this section are opening the file in Notepad (or some other test file) or making Python programs to search for keywords or specific things (like IP addresses) inside the log file. 

**Note**: I had a job teaching Python/Machine Learning with Python so this is my choice language. Feel free to use whatever is most comfortable for you. 

<img src="https://github.com/user-attachments/assets/45202b18-fb50-42cf-a299-b23b73578535" width="300" height="100"></br>

**Step 1**: Download the file. 

**Step 2**: Open the file in Mousepad/Notepad or a similar text editor. 

**Step 3**: Look at the questions and Ctrl-F (Command for Mac) for specific keywords that are needed. This should be satisfactory for many questions in all of these challenges. 

![Screenshot 2024-10-05 095837](https://github.com/user-attachments/assets/5ce0ad9e-9362-4b3d-b67c-f9463b5a382d)

**Note**: Google is your friend: If you look for “the hostname of the SSH server” and you’re not quite sure what this would look like or which one of these items in the file is the SSH server look things up!

</br>

---

</br>

Some challenges require you to look at all the entries in a log and add specific data. For example: VSFTPD (Easy) Below is my strategy:

**Step 1**: Download the file and open it in Notepad. 

**Step 2**: Open your favorite IDE and make a new Python (or your choice) program. 

**Step 3**: Look at the following log. Determine what the question is asking you and make a program to extract the data. Going by hand would take wayyyyyy too long. 

**Example**: 
Question: “How many total bytes did ftpuser upload?” 
Log Key Words: “ftpuser”, “bytes”, “UPLOAD”
	Program searching for the words:

```
import re

# Define the function that processes the log file
def process_log_file(input_filename, output_filename):
    total_bytes = 0
    extracted_numbers = []

    # Regular expression to match lines containing "UPLOAD" and extract the number before "bytes"
    bytes_pattern = re.compile(r'UPLOAD.*?,\s*(\d+)\s+bytes')

    # Open the vsftpd.log file and read line by line
    with open(input_filename, 'r') as file:
        for line in file:
            if "UPLOAD" in line and "bytes" in line and "ftpuser" in line:
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
```

**Note**: This program gives you an answer to a question. See if you can use this program to find “[H]ow many total bytes did ftpuser download” (or others in other programs!)

</br>

---

</br>

You don’t have to make Python Files for all of these files. Some online options can help. My favorite is https://www.somacon.com/p568.php. Here’s an example of how it can help. 

How many unique usernames appear in this log/username with the most login attempts/number of attempts were made for the username with the most login attempts?

**Step 1**: Download the log file.

**Step 2**: Create a new Python (or other) file. It’s no good with all the data available so we will remove the access. 

```
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
```

**Step 3**: Open the log file and copy and paste the usernames into the site provided. https://www.somacon.com/p568.php

**Step 4**: Use the online tool to look for the number of unique usernames (bottom of the page), the user with the most logins (Enable “Show Counts Column”), most login user numbers,  or total attempts. 

**Note**: Sometimes it’s just easier to look for an online tool than create a python file for everything you are looking for. In this case, this site found the answer to four questions that I would otherwise need individual Python files for (or another strategy.)

</br>

---

</br>

Sometimes there isn’t a file type that doesn’t work easily by opening it as a Word document and nothing is automatically installed on your computer to read the file. Generally, this is more secure than just downloading one-use items on your device. 

**For Example**: an sqlite file. The best bet with something like this is to Google “[file type] online viewer”. Here’s a site that does that with sqlite. 

**Step 1**: Google “sqlite online viewer” and select something. I used https://sqliteviewer.app/

**Step 2**: Select the file from the file you would like to view. 

<p align="center">
<img src="https://github.com/user-attachments/assets/68a68a09-2b4f-45e6-892f-cfbc9403802a" width="750" height="350"></br>
</p>

**Step 3**: Use the hints/keywords from the challenges as search words in the “Search column...” sections. If you don’t see something, try selecting a different log file on the left-hand side. 

![Screenshot 2024-10-05 100851](https://github.com/user-attachments/assets/f30faaf0-16f6-47ec-a031-821104330a6f)

**Step 4**: Using keywords [and a bit of common sense] find answers and score points! 
