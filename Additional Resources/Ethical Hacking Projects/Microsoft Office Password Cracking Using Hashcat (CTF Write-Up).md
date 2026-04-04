# Microsoft Office Password Cracking Using Hashcat (CTF Write-Up).md

This write-up documents my process of cracking the password on a password-protected PowerPoint file as part of a CTF challenge. The goal was to recover the password from a `.pptx` file provided by the challenge.


1. First, I've downloaded my PowerPoint presentation from the website where I got the CTF.</br>
    <img width="123" height="144" alt="image" src="https://github.com/user-attachments/assets/8980249b-7cda-4515-9293-c4e12cc2898c" /></br>
2. I used a repository called **office2john** where I could extract the following `office2john.py` Python file. This tool converts Office document encryption into a hash format that cracking tools like Hashcat or John the Ripper can work with.
    * The link for **office2john**: `https://github.com/openwall/john/blob/bleeding-jumbo/run/office2john.py`
3. I placed both `office2john.py` and the `.pptx` file in my Google Colaboratory environment and ran the following commands to extract the hash:
    * NOTE: The ! prefix runs shell commands within a Jupyter/Colab environment. 
    ```
    !sudo apt-get install python3-olefile
    !python office2john.py ProtectedPasswordPresentation.pptx
    ```
4. This gave me the following hash, which I could then copy into a text file for further use in Hashcat:
    * Information provided through the office2john code: `ProtectedPasswordPresentation.pptx:$office$*2013*100000*256*16*602abff02d5615e4d09a8efc591d0976*51ba302519c5f9977b98b1333d90a83d*0c7a8665c0b00f6bb82ec429b2a88c2515c2953b7fb86e84d12d29469c851fa0`
    * Contents saved to hashes.txt (hash only, no filename prefix): `$office$*2013*100000*256*16*602abff02d5615e4d09a8efc591d0976*51ba302519c5f9977b98b1333d90a83d*0c7a8665c0b00f6bb82ec429b2a88c2515c2953b7fb86e84d12d29469c851fa0`
5. Following this, I opened PowerShell and used the `cd` command to enter my Hashcat folder.
    ```
    PS C:\WINDOWS\system32> cd ..
    PS C:\WINDOWS> cd ..
    PS C:\> cd users\thoma\OneDrive\Documents\hashcat-6.2.6
    ```
6. I then ran Hashcat, telling it to use mode `9600` (MS Office 2013), take the hashes from `hashes.txt`, and run those against the `rockyou.txt` wordlist:
    ```
    PS C:\users\thoma\OneDrive\Documents\hashcat-6.2.6> .\hashcat.exe -m 9600 hashes.txt rockyou.txt
    ```
7. After approximately 47 minutes, Hashcat successfully cracked the password. The full session output is below, but the cracked password is obfuscated per CTF rules (password noted as `**********` in Hashcat output below):
    ```
    $office$*2013*100000*256*16*602abff02d5615e4d09a8efc591d0976*51ba302519c5f9977b98b1333d90a83d*0c7a8665c0b00f6bb82ec429b2a88c2515c2953b7fb86e84d12d29469c851fa0:**********
    
    Session..........: hashcat
    Status...........: Cracked
    Hash.Mode........: 9600 (MS Office 2013)
    Hash.Target......: $office$*2013*100000*256*16*602abff02d5615e4d09a8ef...851fa0
    Time.Started.....: Fri Apr 03 19:27:19 2026 (46 mins, 44 secs)
    Time.Estimated...: Fri Apr 03 20:14:03 2026 (0 secs)
    Kernel.Feature...: Pure Kernel
    Guess.Base.......: File (rockyou.txt)
    Guess.Queue......: 1/1 (100.00%)
    Speed.#1.........:     2502 H/s (7.31ms) @ Accel:32 Loops:512 Thr:128 Vec:1
    Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
    Progress.........: 7016448/14344384 (48.91%)
    Rejected.........: 0/7016448 (0.00%)
    Restore.Point....: 7012352/14344384 (48.89%)
    Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
    Candidate.Engine.: Device Generator
    Candidates.#1....: jhulios -> jhomarnarvaez
    Hardware.Mon.#1..: Temp:  0c Fan:  0% Util: 84% Core:2158MHz Mem: 810MHz Bus:16
    
    Started: Fri Apr 03 19:26:53 2026
    Stopped: Fri Apr 03 20:14:04 2026
    ```

## What I learned: 
My main takeaway from this was figuring out how to go from a locked PowerPoint file to actually getting something usable out of it. At first, I didn’t really know how to even start with an Office file, so getting `office2john` working and seeing it produce a hash felt new and exciting.

Once I got the hash into Hashcat and everything was running correctly, it was mostly just waiting for my computer to figure it out. I felt more confident at that point since I had cracked other hashes with Hashcat before for various other CTFs.

This also reaffirmed how common it is for passwords to still be guessable with basic wordlists, even on a not-so-powerful laptop. Overall, I feel a lot more comfortable with this process now, especially knowing I can take something like an encrypted file and work through it step by step until I get a result.
