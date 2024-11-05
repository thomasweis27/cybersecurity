## Password Cracking

“Password cracking is the process of guessing passwords protecting a computer system.”

The best item for this section is a reverse hash lookup—this is the one I’ve used. https://hashes.com/en/decrypt/hash

**Note**: Other tools such as “John The Ripper” or “HashCat” may be needed for more advanced searches. However, this is significantly quicker for less advanced hashes. 

![Screenshot 2024-10-05 101408](https://github.com/user-attachments/assets/02e7cd32-eeda-4500-a966-1ab90cd2845e)

**Step 1**: Copy & paste the hashed into the site, if more than one, separate by newlines [enters].

**Step 2**: Fill in the captcha and press “SUBMIT & SEARCH”.

**Step 3**: Copy the results found. 
Warning: Hashes may have changed locations from the order pasted in step one. Double-check hash to the hash results before entering your answer into the site. 

</br></br>

---

Kali Linux [Shadow File]

“The shadow file stores the hashed passphrase (or “hash”) format for Linux user account with additional properties related to the user password.”

For more information on shadow files see: https://www.cyberciti.biz/faq/understanding-etcshadow-file/

Shadow file password entry layout:
```user:$pass_type&salt&hash:last[date]changed:Min[length]:Max[lenght]:Warn:Inactive:Expire```

Password Types:
```
$1$ — MD5
$2a$ — Blowfish
$2y$ — Blowfish
$5$  — SHA-256
$6$ — SHA-512
$y$ — yescrypt
```
</br></br>

---

## HashCat:
### Cracking from a wordlist:

Sometimes the hashes could represent passwords with a known common prefix or word, so we attempted a wordlist attack using rockyou.txt. The following code is good for running this information. 
</br>```hashcat.exe -m 500 -a 0 -o cracked_passwords.txt password_hashes.txt rockyou.txt``` </br>
* hashcat.exe: The executable file for Hashcat, the password-cracking tool.
* -m 500: Specifies the hash type to use. 500 is the mode for MD5-Crypt hashes (denoted by $1$ prefix in the hash).
* -a 0: Sets the attack mode to dictionary (wordlist) attack. This mode tries each word in a specified wordlist against the hash.
* -o cracked_passwords.txt: Tells Hashcat to output the cracked passwords to a file named cracked_passwords.txt.
* password_hashes.txt: The input file containing the hashes to be cracked.
* rockyou.txt: The wordlist (dictionary) file used for the dictionary attack. In this case, it’s a popular wordlist file containing millions of common passwords.


Sometimes there are some challenges where some of the password is known but not the full thing. In this case it's **```SKY-MASK-``` + 4 digits**. The following code is good for running this information. 
</br>```hashcat.exe -m 500 -a 3 -o cracked_passwords.txt password_hashes.txt SKY-MASK-?d?d?d?d``` </br>
* hashcat.exe: The executable file for Hashcat, the password-cracking tool.
* -m 500: Specifies the hash type to use. 500 is the mode for MD5-Crypt hashes (denoted by $1$ prefix in the hash).
* -a 3: Sets the attack mode to brute-force (mask) attack. This mode allows you to specify a pattern to brute-force each possible character combination.
* -o cracked_passwords.txt: Tells Hashcat to output the cracked passwords to a file named cracked_passwords.txt.
* password_hashes.txt: The input file containing the hashes to be cracked.
* SKY-MASK-?d?d?d?d: The mask pattern used for brute-forcing. This pattern specifies: The prefix SKY-MASK- as known characters. ?d?d?d?d, which represents four unknown digits (0-9) for Hashcat to brute-force.
  * ?d - Digit: Matches any digit (0-9).
  * ?l - Lowercase Letter: Matches any lowercase letter (a-z).
  * ?u - Uppercase Letter: Matches any uppercase letter (A-Z).
  * ?s - Special Character: Matches any special symbol (e.g., !, @, #, $, etc.).
  * ?a - All Printable Characters: Matches any printable ASCII character (a combination of ?d, ?l, ?u, and ?s).
  * ?b - Binary: Matches all binary characters, including non-printable ones (useful for custom hash formats).

</br></br>

---

## Wordlist Creation:

Sometimes a challenge requires you to make a wordlist to run HashCat against. Making this wordlist can be challenging, however, there's usually a starting point. Here's an example of a Python file I've made to create a celebrity wordlist. We will start by installing the Wikipedia API with the following code: </br>
```!pip install wikipedia-api```</br></br>

I used Google Colab as my coding medium. The ```!`` at the beginning of the line shows that this is to be run as a terminal line of code instead of as a Python file. </br></br>The code below is used to create a basic wordlist of names and so fourth. This won't be enough but this is a good starting point.

```
import wikipediaapi
import random

# Set up the Wikipedia API with a user-agent and language
wiki = wikipediaapi.Wikipedia(language='en', user_agent="MyCelebrityWordlistBot/1.0 (https://example.com)")

# Categories to look for famous people
categories = [
    "List of actors", "List of musicians", "List of painters",
    "List of writers", "List of scientists", "List of politicians",
    "List of athletes", "List of comedians", "List of directors",
    "List of inventors"
]

# Function to fetch names from a Wikipedia category page
def fetch_names_from_category(category_title):
    page = wiki.page(category_title)
    names = []
    if page.exists():
        for link in page.links:
            names.append(link)
    return names

# Generate the list of names
celebrity_names = []
for category in categories:
    names = fetch_names_from_category(category)
    celebrity_names.extend(names)

# Remove duplicates and shuffle the list
celebrity_names = list(set(celebrity_names))
random.shuffle(celebrity_names)

# Limit to 10,000 names or fewer if not enough names are found
celebrity_names = celebrity_names[:10000]

# Save the names to a file
with open("celebrity_wordlist.txt", "w") as f:
    for name in celebrity_names:
        f.write(name.replace(" ", "").lower() + "\n")  # Format without spaces
        f.write(name.replace(" ", "") + "\n")          # Format with spaces removed
        f.write(name + "\n")                           # Original format

print(f"Generated a wordlist of {len(celebrity_names)} celebrity names.")
```

</br></br></br>
The remainder of this code is to create more of a word list. Names of people might not be enough to run through HashCat so creating a wordlist from the names of celebrities. This includes the following:
*  Original lowercase
*  Replace 'o' with zero
*  Replace 'i' with '1' and 'a' with '@'
*  Append '123'
*  Append '2023'
*  Replace 'e' with '3' and add '*'
*  Replace 's' with '$'
*  Append '#1'
*  Create combinations of character substitutions
*  Append numbers and symbols at various positions
*  Add variations with symbols
*  All uppercase
*  All lowercase
*  First letter uppercase
*  Adding common number substitutions and variations
*  Without Spaces

</br>
I made this into two different files as the first one wasn't useful enough. 
</br>

#### Python Name Variations File 



```
# Function to create name variations
def create_variations(name):
    variations = []
    name_lower = name.lower()

    # Basic variations
    variations.append(name_lower)                                    # Original lowercase
    variations.append(name_lower.replace('o', '0'))                # Replace 'o' with zero
    variations.append(name_lower.replace('i', '1').replace('a', '@'))  # Replace 'i' with '1' and 'a' with '@'
    variations.append(name_lower + "123")                          # Append '123'
    variations.append(name_lower + "2023")                         # Append '2023'

    # Variations with symbols
    variations.append(name_lower.replace(' ', '').replace('e', '3') + "*")  # Replace 'e' with '3' and add '*'
    variations.append(name_lower.replace(' ', '').replace('s', '$'))        # Replace 's' with '$'
    variations.append(name_lower + "#1")                                   # Append '#1'

    return variations

# Read the existing celebrity names from the file
with open("celebrity_wordlist.txt", "r") as f:
    celebrity_names = [line.strip() for line in f.readlines()]

# Append variations to the same file
with open("celebrity_wordlist.txt", "a") as f:
    for name in celebrity_names:
        for variation in create_variations(name):
            f.write(variation + "\n")

print("Added variations to 'celebrity_wordlist.txt'.")
```

#### Python Extended Name Variations File

```
import itertools

# Function to create exhaustive variations of a name
def create_exhaustive_variations(name):
    variations = []
    base_name = name.lower().replace(" ", "")  # Remove spaces and convert to lowercase

    # Adding common number substitutions and variations
    substitutions = {
        'a': ['a', '@', '4'],
        'e': ['e', '3'],
        'i': ['i', '1'],
        'o': ['o', '0'],
        's': ['s', '5', '$'],
        't': ['t', '7'],
    }

    # Create combinations of character substitutions
    for chars in itertools.product(*substitutions.values()):
        substituted_name = base_name
        for original, new_char in zip(substitutions.keys(), chars):
            substituted_name = substituted_name.replace(original, new_char)
        variations.append(substituted_name)

    # Append numbers and symbols at various positions
    for i in range(100):  # Append numbers from 0 to 99
        variations.append(f"{base_name}{i}")
        variations.append(f"{i}{base_name}")

    # Add variations with symbols
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', '?', '/', '\\']

    for symbol in symbols:
        variations.append(base_name + symbol)
        variations.append(symbol + base_name)
        variations.append(base_name + symbol + str(random.randint(1, 99)))  # Symbol followed by numbers

    # Case variations (uppercase and lowercase)
    variations.append(name)  # Original name
    variations.append(name.upper())  # All uppercase
    variations.append(name.lower())  # All lowercase
    variations.append(name.capitalize())  # First letter uppercase

    return list(set(variations))  # Remove duplicates

# Read the existing celebrity names from the file
with open("celebrity_wordlist.txt", "r") as f:
    celebrity_names = [line.strip() for line in f.readlines()]

# Append exhaustive variations to the same file
with open("celebrity_wordlist.txt", "a") as f:
    for name in celebrity_names:
        variations = create_exhaustive_variations(name)
        for variation in variations:
            f.write(variation + "\n")

print("Added exhaustive variations to 'celebrity_wordlist.txt'.")
```
