# WiFi Password Cracking Using Hashcat (CTF Write-Up).md

This write-up documents my process of cracking the password of a WiFi network using the network's SSID and PSK to solve a CTF challenge. The goal was to crack the password for an example network using the information provided by the challenge.

1. First, I collected the three SSIDs provided in the CTF:</br>
    <img width="547" height="247" alt="image" src="https://github.com/user-attachments/assets/bccbb185-810b-40ca-8dc4-3c9f19e0a440"/></br>
2. I then opened PowerShell and, using the `cd` command, I entered my Hashcat folder.
    ```
    PS C:\WINDOWS\system32> cd ..
    PS C:\WINDOWS> cd ..
    PS C:\> cd users\thoma\OneDrive\Documents\hashcat-6.2.6
    ```
3. I then needed to convert the PMK and SSID values from hex strings into base64 format, since that's what hashcat's mode 12000 requires. This was achieved using PowerShell, which performed  this conversion with the code below and writes all three networks out to `hashes.txt` so Hashcat can read use them.
    ```
    PS C:\users\thoma\OneDrive\Documents\hashcat-6.2.6> $networks | ForEach-Object {
    >>     $pmkBytes  = [byte[]] ($_.pmk -split '(?<=\G.{2})' | Where-Object {$_} | ForEach-Object { [Convert]::ToByte($_, 16) })
    >>     $ssidBytes = [System.Text.Encoding]::UTF8.GetBytes($_.ssid)
    >>     $pmkB64    = [Convert]::ToBase64String($pmkBytes)
    >>     $ssidB64   = [Convert]::ToBase64String($ssidBytes)
    >>     "$pmkB64`:$ssidB64"
    >> } | Out-File -Encoding ascii hashes.txt
    ```
4. I also validated the contents of `hashes.txt` to make sure the information was written to this file and in the correct format. 
    ```
    PS C:\users\thoma\OneDrive\Documents\hashcat-6.2.6> Get-Content hashes.txt
    2s/8MaDbaDsEYkmhxSHXo/YADnyWM6ZLUKqMsoVaqxg=:aG90ZWwtd2lmaQ==
    l1L4vBmOVGaIAlvpy13ZXWHVLpBMjvLXursMyCN2rto=:dW5pdmVyc2l0eS1ndWVzdA==
    xQ1vdjVklEVsCHCVWaGpJmfJpA8hFCnaOFsU3UpC9cI=:Y29ycG9yYXRlLWlvdA=
    ```
5. Finally, I told hashcat to run using mode  `12000` (PBKDF2-HMAC-SHA1), take the hashes from `hashes.txt`, and run those against the `rockyou.txt` wordlist: </br>
    `PS C:\users\thoma\OneDrive\Documents\hashcat-6.2.6> .\hashcat.exe -m 12000 hashes.txt rockyou.txt`
6. This quickly cracked all three passwords. The full session output is below, but the cracked password is obfuscated per CTF rules (password characters are noted by `*` in the Hashcat output below):
    ```
    sha1:4096:aG90ZWwtd2lmaQ==:2s/8MaDbaDsEYkmhxSHXo/YADnyWM6ZLUKqMsoVaqxg=:********
    sha1:4096:dW5pdmVyc2l0eS1ndWVzdA==:l1L4vBmOVGaIAlvpy13ZXWHVLpBMjvLXursMyCN2rto=:*********
    sha1:4096:Y29ycG9yYXRlLWlvdA==:xQ1vdjVklEVsCHCVWaGpJmfJpA8hFCnaOFsU3UpC9cI=:*********
    
    Session..........: hashcat
    Status...........: Cracked
    Hash.Mode........: 12000 (PBKDF2-HMAC-SHA1)
    Hash.Target......: hashes.txt
    Time.Started.....: Fri Apr 03 19:09:02 2026 (1 min, 34 secs)
    Time.Estimated...: Fri Apr 03 19:10:36 2026 (0 secs)
    Kernel.Feature...: Pure Kernel
    Guess.Base.......: File (rockyou.txt)
    Guess.Queue......: 1/1 (100.00%)
    Speed.#1.........:   291.9 kH/s (9.01ms) @ Accel:64 Loops:128 Thr:256 Vec:1
    Recovered........: 3/3 (100.00%) Digests (total), 3/3 (100.00%) Digests (new), 3/3 (100.00%) Salts
    Progress.........: 32931840/43033152 (76.53%)
    Rejected.........: 0/32931840 (0.00%)
    Restore.Point....: 10911744/14344384 (76.07%)
    Restore.Sub.#1...: Salt:1 Amplifier:0-1 Iteration:3968-4095
    Candidate.Engine.: Device Generator
    Candidates.#1....: LilGuy-13 -> Joythedog
    Hardware.Mon.#1..: Temp:  0c Fan:  0% Util: 84% Core:2255MHz Mem: 841MHz Bus:16
    
    Started: Fri Apr 03 19:08:47 2026
    Stopped: Fri Apr 03 19:10:38 2026
    ```

## What I learned: 
My main takeaway from this challenge was understanding how WiFi authentication data is actually structured, especially the difference between a PSK and a PMK. Going into this, I didn’t fully understand the difference between a PSK (pre-shared key) and PMK (pairwise master key), which is what actually gets derived from that password using PBKDF2. Getting the information provided into something usable by Hashcat was an interesting process and helped me see how these things fit together.

Step 3 was easily the most challenging part for me. Writing the PowerShell script to convert the hex-encoded PMKs into byte arrays and then into base64 took a lot of trial and error. I don’t have much experience with PowerShell, so even small syntax or formatting issues would break things, and debugging it felt slow compared to languages I’m more comfortable with. Looking back, I realized this step could have been much more straightforward if I had used Python instead. Converting hex to base64 is something I’ve done before, and I likely would have been able to write and debug that script much faster. This was a good reminder to lean into tools and languages I already know well, especially in a time-sensitive CTF environment.

Once the formatting issue was solved, the rest of the process felt much more familiar. Running Hashcat with mode 12000 and a wordlist was similar to other challenges I’ve done, so at that point, it became more about execution than problem-solving. Overall, I feel a lot more confident now in how WiFi password cracking works, especially the relationship between SSIDs, PMKs, and passwords, as well as the importance of properly formatting data before passing it into cracking tools.
