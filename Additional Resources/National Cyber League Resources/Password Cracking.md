## Password Cracking

“Password cracking is the process of guessing passwords protecting a computer system.”

The best item for this section is a reverse hash lookup—this is the one I’ve used. https://hashes.com/en/decrypt/hash

**Note**: Other tools such as “John The Ripper” or “HashCat” may be needed for more advanced searches. However, this is significantly quicker for less advanced hashes. 

![Screenshot 2024-10-05 101408](https://github.com/user-attachments/assets/02e7cd32-eeda-4500-a966-1ab90cd2845e)

**Step 1**: Copy & paste the hashed into the site, if more than one, separate by newlines [enters].

**Step 2**: Fill in the captcha and press “SUBMIT & SEARCH”.

**Step 3**: Copy the results found. 
Warning: Hashes may have changed locations from the order pasted in step one. Double-check hash to the hash results before entering your answer into the site. 

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

