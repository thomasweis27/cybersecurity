Notes on the Assessment
	• Exam uses "Version 2" of the assessment guide. 
		○ level 1 assessment items (FCI) are grouped together
		○ Revised version (version 2.13) has all the level 1 and 2 items mixed together to make sure people do all controls. 
			§ Entire document is level 2 to make it clear that it's inclusive of level 1
			§ Also include the FAR numbering (e.g., "-b.1.i")
			§ When doing an assessment always use the most up-to-date version. 
	• When studying, use this document:
		○ 

Domain 4 Task 1
	• Artifacts: Anything that's a file:
		○ e.g., Roster, inventory, user access listing, privileged user access listing
		○ Evidence can be reused for different control objectives
		○ If they start talking about another topic, then the assessor may then realize that contradict themselves later or don't cover the information needed to pass the objective.
		○ Artifacts must be able to be reproduced during the interview process 
			§ Policies
			§ Procedures
			§ System Security Plans (SSP)
			§ Security requirements
			§ Architecture diagrams
			§ Asset inventories
			§ System configurations
			§ System audit logs
	• Interviews: Taking to the people that perform or set up those individual requirements
		○ Don't talk to people like admins, bosses, or people that are overseeing, but not actually doing the work. 
		○ Ask questions to see if they follow the assessment discussion, if they haven't read it, they probably aren't ready. 
	• Test:  Must be performed on the actual production system or control that is used in the production system environment (a screen shot is an artifact)
		○ Ask for materials to be created in a few minutes - is something takes hours or days to make, then it's not something that's "dynamic" and not a "dynamic report"
		○ The OSC can appeal and then the C3PAO committees can decide if that's official or not. 
		○ Involves hands-on work to identify security vulnerabilities
		○ Can be executed across an entire enterprise or on selected systems
		○ Must be conducted on a production or exact replica system
		
Access Controls
	• AC.L1-3.1.1 Authorized Access Control
		○ When looking at these controls look for the specific key words and use these to make sure you are looking for the correct things in the controls
	• AC.L1-3.1.2 Transaction & Function Control
		○ Looking for authorized users being defined ad system access being limited
	• AC.L2-3.1.3 - Control CUI Flow
		○ Looking for policies telling people what they are supposed to do regarding CUI flow
		○ Looking for a diagram of where the CUI can flow. 
		○ Can also have policies for moving the data in and out
	• AC.L2-3.1.4 — Separation of Duties
		○ Looking for defined different duties and reasonable controls in place
	• AC.L2-3.1.5 — Least Privilege
		○ Looking for defined privileges with all privileges for all accounts 
		○ Looking for process of authorizing people access (e.g., HR, supervisors)
		○ Looking for defined security functions (e.g., create account, manage permissions, grant/remove access, etc.) and different people have different functions. 
	• AC.L2-3.1.6 — Non-Privileged Account Use
		○ Looking for all defined non-security functions for users 
			§ non-security functions are functions without privileges
			§ E.g., timesheets, log-ins, using the internet, software updates, etc.
	• AC.L2-3.1.7 — Privileged Functions
		○ Look for a policy/procedure/list of clearly defined privileged and non-privileged functions
		○ Look for (at minimum) an administrative policy for what to do/not do. 
			§ This can be an AUP.
		○ Can also look for a technical and configuration policy of what is in place to allow/deny access to specific things. 
			§ E.g., RBAC, supporting logs
	• AC.L2-3.1.8 — Unsuccessful Logon Attempts
		○ Look for the threshold of unsuccessful login attempts and the consequences (e.g., disabling/locking the account)
		○ Note: Revision 3 has 80 "ODPs" for what to be using when it's recommended in the future. 
			§ The amount for Rev. 3 is five login attempts (will be implemented in likely 2026 or 2027)
	• AC.L2-3.1.9 — Privacy & Security Notices
		○ Look for a privacy and security notices required by CUI-specified rules are identified, consistent, and associated with the specific CUI category and that these privacy and security notices are displayed.
			§ Anything used for privacy and security should have this. 
			§ E.g., servers, data centers, posters in hallway ("Authorized personal only, CUI contained")
	• AC.L2-3.1.10 — Session Lock
		○ Look for a defined period of inactivity and a lock that happens after that period of time has lapsed.
		○ Can also look for settings configured in AD (Active Directory) 
			§ CMMC 3.0 (future) recommends that this is implemented for after 15 minutes. 
	§ AC.L2-3.1.11 - Session Termination
		○ Look for a defined condition for terminating the session (e.g., after logout, after XX minutes, after XX events)
		○ Look for controls or test that the session is terminated after the defined condition occurs. 
	· AC.L2-3.1.12 - Control Remote Access
		○ Look for if remote sessions are allowed, what types are allowed (home sessions, connections to websites, connections to data centers, connections to other systems on the network), the length of time permitted, connection types (RDP/VPN), who has access (via RBAC), and how these are monitored (AD, logs, SIEMs, etc.)
		○ Note: this isn't exactly asking for encryption methods (TLS)
	· AC.L2-3.1.13 — Remote Access Confidentiality
		○ Look for controls for data traversing networks and mechanisms controlling this 
			§ e.g., connection white list, logs, etc.
			§ I.e., connections using TLS versions 1.2 or 1.3
	· AC.L2-3.1.14 — Remote Access Routing:
		○ Look for managed access control points being listed and methods for implementing
			§ E.g., border router directing to specific firewall ports within the DMZ
	· AC.L2-3.1.15 — Privileged Remote Access
		○ Look for what commands are authorized (e.g., list of commands are allowed) and who have access to these commands and abilities.
	· AC.L2-3.1.16 - Wireless Access Authorization
		○ Look for a network diagram
		○ Look for a floor plan that shows the locations of the wireless access points and devices accessing these. 
		○ Look for something allowing wireless access being authorized for users (e.g., policy, user list, etc.)
	· AC.L2-3.1.17 — Wireless Access Protection
		○ Look for the defined and implemented method (e.g., WEP, WEP enterprise, something controlled by Kerberos)
	· AC.L2-3.1.18 - Mobile Device Connection
		○ Look for a list of devices that process, store, or transmit, CUI, and that these are all authorized
		○ Look for logs about the connections/connection terminations for CUI. 
			§ Note: there's nothing about protection or encryption for this. 
	· AC.L2-3.1.19 - Encrypt CUI on Mobile
		○ Look for a list of mobile devices and what encryption is used on these devices
		○ Note: Not everything requires FIPS, but anything handling CUI does. 
		○ Note: If there's additional cryptography, this doesn't count. Must be FIPS. 
	· AC.L1-3.1.20 External Connections
		○ Look for a list of external systems and how they are allowed to be used. 
		○ Look for the verification of these systems, (e.g., RBAC and MFA)
	· AC.L2-3.1.21 - Portable Storage Use
		○ The use and applicable devices are documented (e.g., not allowed, CDs, 3 flash drives, etc.).
		○ Look for the controls blocking the use of the external devices. 
			§ Note: It's still applicable if they are blocking it. If the OSC has port blocking on, then this is considered applicable. If there are not administrative controls, then all locations that would allow external drives are in scopes. 
	· AC.L1-3.1.22 Control Public Information
		○ Look for listing of people or groups (e.g., marketing) that post or process information. 
		○ Look for procedures to make sure that CUI are NOT being posted (some sort of oversite)
		○ Look for a process to review and remove CUI in locations it should not be at

Awareness and Training (AT)
	· AT.L2-3.2.1 Role-Based Risk Awareness
		○ Look for policies, procedures, and training to educate people for security risks. 
		○ Ask people if they know where the policies, procedures, and training is located. 
			§ If they don't know, they are not "aware" and this is failed. 
	○ AT-L.2-3.2.2 - Role-Based Training
		○ Look for a defined list of roles for designated security personnel
		○ Look for a process used to determine who to assign specific duties. (e.g., certifications, qualifications, privileges; users must be defined as to if they are appropriate people and why)
	○ AT.L2-3.2.3. - Insider Threat Awareness
		○ People going through insider threat awareness training are identified
			§ The DoD offers a free training with a certificate but this isn't specifically required, just some training from some group. 

Audit Accountability
	· AU.L2-3.3.1 — System Auditing
		○ Look for specific computer-created audit logs to fufill the following requirements:
			§ System Auditing (system processes should be collected and logged)
			§ User Accountability (time, username, items being accessed, length of access)
			§ Event Review (Microsoft has 400+ types of logging - spreadsheet of the types of events that are being collected)
			§ Audit Failure Alerting (alerting for issues (e.g., someone shut off the logging would result in emails/texts to admins))
			§ Audit Correlation (monitoring for what had happened first to figure out the timeline of what happened. (e.g., first DMZ, then firewall, then device one, etc.) these should all have a synchronized timestamp)
			§ Reduction & Reporting (10,000s of logs are made daily, there should be an aggregation server)
			§ Authoritative Time Source (having logs from a designated time source)
			§ Audit Protection (restrict all but specific admins from having access to logs - not all admins need log access)
			§ Audit Management 
	· AU.L2-3.3.3 — Event Review
		○ Look for reviewing of policies, logs, etc.
	· AU.L2-3.3.4 — Audit Failure Alerting
		○ Review the event logs of which events require administrative response
			§ E.g., not one failed on login attempt
			§ e.g., maybe for late night attacks of the nextwork
			§ These things should be defined which should result in an admin response 
	· AU.L2-3.3.6 - Reduction & Reporting
		○ 10,000s of logs are made daily, there should be an aggregation server to be able to sift through all of the logs 
		○ This is almost impossible on-demand for more than a few devices
		○ On-demand is a few minutes - hours or days are not on-demand
	· AU.L2-3.3.7 - Authoritative Time Source 
		○ Access a local or outside web server to have all devices corollate
	· AU.L2-3.3.8 — Audit Protection
		○ Look for protection of logs from unauthorized access, deletion, etc..
			§ This is the process (having something in place) and the tool's configuration.  
	· AU.L2-3.3.9 — Audit Management
		○ Having a few people managing the logs (just a small subset - not everyone needs access)

Configuration Management (CM)
	· CM.L2-3.4.1 — System Baselining
		○ Look for system baselines for hardware, software, firmware, and documentation.
			§ There should be one for all hardware types (e.g., Windows 10, Windows 11, Linux, servers, switches, etc.)
			§ Almost impossible without automation (people like to use Windows Intune)
			§ Updating or prompting a person to update things should all be automated. 
	· CM.L2-3.4.2 — Security Configuration Enforcement
		○ Look for defined security configuration settings for ALL information technology products being used by the organization
		○ Look to see the policies and technical controls that enforce these policies.
	· CM.L2-3.4.3 — System Change Management
		○ Look for a system to track, review, approve/deny, and log all changes. 
			§ This should be done by a board, not a specific person
			§ There should be a documented minutes, and consideration for doing/not doing the specific action and it's impacts. 
			§ Tracking can be done well through a ticketing system. 
	· CM.L2-3.4.4 — Security Impact Analysis
		○ Look for review of confidentiality, integrity, and availability (CIA) for analyzation changes before implementing
	· CM.L2-3.4.5 — Access Restrictions for Change
		○ Look for physical and logical controls and the changes in policies for changes management. 
		○ Look for processes/procedures for enforcement for physical access 
			§ E.g., data centers, data closets, data centers, remote access, keycards, VPNs, RDP, etc.
	· CM.L2-3.4.6 — Least Functionality
		○ Look for port restrictions on everything but essential system capabilities which should be defined in a list based on the principle of least functionality.
	· CM.L2-3.4.7 — Nonessential Functionality
		○ Look for a list of essential and non-essential programs and the restrictions placed on these. 
		○ Look for a list of essential and non-essential functions and the restrictions placed on these. 
		○ Look for a list of essential and non-essential ports and the restrictions placed on these. 
		○ Look for a list of essential and non-essential protocol and the restrictions placed on these. 
		○ Look for a list of essential and non-essential services and the restrictions placed on these. 
	· CM.L2-3.4.8 — Application Execution Policy
		○ Look for allow/deny lists and the software allowed/denied on these listings
		○ Look for the processes for implementing the whitelist/blacklist
	· CM.L2-3 4 9 - User-Installed Software
		○ Look for the definition of  installation and definition of who has the ability to install the software. 
		○ Look for controls on this installation of devices and monitoring of these controls. 

Identification & Authentication (IA)
	· IA-L1-3.5.1 Identification
		○ Look for a list of system users, devices, and processes and a process for identifying who those users are. 
			§ Note: The discussion part of this talks about looking for the identification of the users. (not just merely a list)
			§ e.g., Artic wolf, WSUS, etc.
	· IA-L1-3.5.2  - Authentication:
		○ Look for the requirement and implementation of single factor authentication (knowledge of the user ID and password)
		○ Look for a process to verify the user/processes/phones/laptops/workstations that identify the people and device before access is required. 
	· IA.L2-3 5 3 - Multifactor Authentication
		○ Look for a list of privileged accounts, and that MFA is implemented for local and network access for these accounts. 
		○ Look if multifactor authentication is implemented for network access to non-privileged accounts.
	· IA.L2-3.5.4 — Replay-Resistant Authentication
		○ Look for replay-resistant authentication mechanisms are implemented for network account access to privileged and non-privileged accounts.
			§ Note: TLS 1.2 and 1.3 both have replay resistant mechanisms (TLS 1.3 is better)
			§ Kerberos also prevents this. 
	· IA.L2-3.5.5 - Identifier Reuse
		○ Look for a unique identifiers for all specific process or human and a defined period of time that the identifier is reused. 
			§ E.g., after someone retires, the user ID is not reused for a new person until XX amount of time passes. 
	· IA.L2-3.5.6 — Identifier Handling
		○ Look for the defined length of time before an account is disabled and processes to enforce this
	· IA.L2-3.5.7 — Password Complexity
		○ Look for defined and how it's enforced password complexity, character types defined, length, and changes reequipments. 
			§ CCP requires SHA2 and above (SHA1, MD5, and others are no longer secure)
			§ This can be enforced through Microsoft's authenticator or AD.
	· IA.L2-3.5.8 — Password Reuse
		○ Look for a defined number of password generations before old ones will be reused and evidence of implementation.
	· IA.L2-3.5.9 — Temporary Passwords
		○ Look for the requirement and enforcement process of enforcing a temporary password on first logon.
	· IA.L2-3.5.10 — Cryptographically-Protected Passwords
		○ Look for evidence that a hash is protected in storage and transit. 
			§ Probably using TLS Version 1.2 or 1.3
	· IA.L2-3.5.11 - Obscure Feedback
		○ Look for obscured login information 
			§ e.g., "****"
			§ Can be displayed temporarily (< 1 second)

Incident Response (IR)
	· IR.L2-3.6.1 — Incident Handling
		○ Look for an established prepared, detection, analysis, containment, and recovery operation incident-handling capability.
			§ This would be a policy for this, and a procedure saying how someone would do this. 
		○ Look for response processes and activities
			§ There should be a process to quickly pull all information regarding the incident handling or creation of processes for any of these steps. This can be done through a ticketing system. 
			§ An SSP saying "as of XXXX" we have not had an incident - shows that they are following the process. 
	· IR.L2-3.6.2 — Incident Reporting
		○ Look for a tracking and documentation system for incidents
			§ E.g., ticketing system or a spreadsheet. 
		○ Look for a listing of people and organizations who to report incidents or report incident to 
			§ E.g., FBI, people in the company, management, MSPs
	· IR.L2-3.6.3 — Incident Response Testing
		○ Look for if the organizational system that processes, stores, or transmits CUI, the incident response capability is tested.
			§ There will be people beyond the IT group: council, managers, VPs, etc.
			§ Should include Table Top Exercises (TTX), training days, various teams tested

Maintenance (MA)
	· MA.L2-3 71 - Perform Maintenance
		○ Look for (as mentioned in the further discussion):
			§ corrective maintenance (e.g., repairing problems with the technology);
			§ preventative maintenance (e.g., updates to prevent potential problems);
			§ adaptive maintenance (e.g., changes to the operative environment); and
			§ perfective maintenance (e.g., improve operations).
	· MA.L2-3.7.2 — System Maintenance Control
		○ Look for a list of tools, techniques, mechanisms, and personnel that were allowed to conduct system maintenance
			§ There should be policies about the control of these and procedures for implementing them. 
			§ Usually "techniques" and  "mechanisms" mean policies AND procedures.
	· MA.L2-3.7.3 — Equipment Sanitization
		○ Look for a process for sanitization. 
			§ Simply deleting this is not good enough - there needs to be an actual process in place and documented. 
			§ If a disk is full disk encrypted (FDE), can perform a disk erase.
			§ Additionally, degaussing can work, but destroys drive  (not for SSD)
			§ Can physically destroy the drive with a shredder (for SSD)
	· MA.L2-3.7.4 - Media Inspection
		○ Look for a process to test programs for malicious code
			§ Can simply say "refer to 3.14.2"
	· MA.L2-3.7.5 — Nonlocal Maintenance
		○ Look for MFA is used to establish nonlocal maintenance sessions via external network connections.
		○ Look for nonlocal maintenance sessions established via external network connections are terminated when nonlocal maintenance is complete.
	· MA.L2-3.7.6 - maintenance personnel
		○ Look for if maintenance personnel without access authorization are supervised 
			§ Looking for a policy to require this. 

Media Protection (MP)
	· MP.L2-3.8.1 — Media Protection
		○ Look for policies and physical/logical controls in place for controlling and storing paper media and digital media. 
	· MP.L2-3.8.2 - Media Access
		○ Look for processes for limiting CUI media (physical content) to authorized users only. 
			§ Not access to information systems, this is access to media (physical stuff)
	· MP-LI-3.8.3 Media Disposal
		○ Look for sanitization before disposal and reuse. 
			§ This should be a policy. 
			§ This is very similar to previous controls, make sure that controls are stating the same process. (e.g., don't change one and not the other)
			§ Need to define what "reuse" and "disposal" means
	· MP.L2-3.8.4 - Media Markings
		○ Look for the correct documentation on documents
			§ NARA and 5200.48 say two different things about the footer (NARA says optional, 5200.48 says required)
			§ NARA is law but there's some debate currently if 5200.48 is required
			§ Needs specific CUI markings e.g., "CUI" or "CUI//SP-[type]//[dispersal information]"
	· MP.L2-3.8.5 — Media Accountability
		○ Look for processes and mechanisms in place for CUI control
			§ Some places have a "library system" where they can check out media, use it, and then check it back in to maintain control and tracking of the CUI. 
			§ E.g., using machines, printers, air gapped Linux machines, etc.
			§ Having an AUP disallowing this, is creating the control (so it's not, not applicable)
	· MP.L2-3.8.6 Portable Storage Encryption
		○ Look for defined and implementation mechanisms for the cryptographic mechanisms for CUI
	· MP.L2-3.8.7 — Removable Media
		○ Look for policies and controls for the use of removable media.
			§ E.g., port blocking, allow list for specific flash drives, etc.
	· MP.L2-3 8 8 - Shared Media
		○ Look for the prohibiting/disabling devices without an identifiable owner. 
			§ This can be something like labelling all flash drives that are allowed to identify them from disallowed ones. 
	· MP.L2-3.8.9 — Protect Backups
		○ Look for the protection of backed up data (if backups are created)
			§ Backups are not required, however it highly recommended. 
			§ This doesn't specify that is needs to be encrypted.

Personnel Security (PS)
	· PS.L2-3.9.1 — Screen Individuals
		○ Look for a screening function for all employees accessing CUI. 
			§ The discussion wants Personnel security screening (vetting) activities involve the evaluation/assessment of individual's conduct, integrity, judgment, loyalty, reliability, and stability
			§ There should be a procedure for this. 
			§ Probably more cost effective to hire a 3rd party to do these background checks. 
	· PS.L2-3 9 2 - Personnel Actions
		○ Look for a policy and procedure for the termination and transfers of people's access after being terminated/transferred. 
			§ This can be implemented through AD. 
			§ This can involve a policy for a re-review of privileges after  termination/transfer

Physical Access
	· PE.L1-3.10.1 Limit Physical Access
		○ Look for systems limiting  physical access for people, equipment, and environments to be defined
			§ Active Directory would limit logical access, not physical access. 
			§ This can involve a list of people or a list of departments. 
			§ e.g, everyone in HR, the CEO, someone's name, etc.
	· PE.L2-3.10.2 — Monitor Facility
		○ Look for policies and solutions for monitoring the physical facility and supporting infrastructure.
			§ E.g, keycards, cameras with someone watching, etc.
	· PE.L1-3.10.3 - Escort Visitors
		○ Look for a procedure for escorting visitors.
	· PE.L1-3.10.4 Physical Access Logs
		○ Look for logs for physical access
	· PE.L1-3.10.5 Manage Physical Access
		○ Look for policies and procedures that devices are identified, controlled, and managed.
			§ Companies should define what a devices is. 
			§ The discussion says that physical access devices include keys, locks, combinations, and card readers.
			§ Should be a library for all keys, plus if a key goes missing then door that the key opens must be replaced. 
	· PE.L2-3 10 6 -  Alternative Work Sites
		○ There should be a policy for restricting access to CUI at various types of facilities. 
			§ The different types of facilities should be listed (e.g., office, homes, worksites, etc.)
				□ For each location, there controls should be specified. (e.g., homes have this security, the office has this other security, etc.) 
			§ The discussion says alternate work sites may include government facilities or the private residences
			§ Homes should include MFA, physical security, and FIPS connections. 

Risk Assessment (RA)
	· RA.L2-3.1 1.1 - Risk Assessments
		○ Working through an analysis and determining what the impact is. 
			§ This can be a quantitative or qualitative risk assessment - should be ranked low through high so the organization knows in what order to address these issues . 
	· RA.L2-3.11.2 - Vulnerability Scan
		○ the frequency scan for vulnerabilities in organizational systems and applications is defined.
		○ vulnerability scans are performed on organizational systems with the defined frequency.
		○ vulnerability scans are performed on applications with the defined frequency.
		○ vulnerability scans are performed on organizational systems when new vulnerabilities are identified.
		○ vulnerability scans are performed on applications when new vulnerabilities are identified.
	· RA.L2-3.11.3 - Vulnerability Remediation
		○ vulnerabilities are identified.
		○ vulnerabilities are remediated in accordance with risk assessments.
			§ This can be done through the CVE. (Ranked 1 - 10 (lowest to highest)).
			§ There need to be policies for addressing this, in addition to proof they are actually doing this. 

Security Assessment (CA)
	· CA.L2-3.12.1 — Security Control Assessment
		○ Look for a defined timeline for assessment and make sure they have been addressed in the past 12 months. 
			§ Should review all 320 controls. 
			§ Should look for historical data to make sure this has been active since the last review.
	· CA.L2-3.12.2 - Plan of Action
		○ Look for a process to identify the issues, processes to fix those issues, and documentation of addressing and implementing the remediations for these issues. 
	· CA.L2-3.12.3 — Security Control Monitoring
		○ Look for monitoring.
			§ This doesn't specify continuous monitoring. 
			§ The discussion says to re-do 3.12.1 control assessment within a 12 month period to get the results again. 
			§ Could do things like patch management monthly, this could be "the test" and the others just "monitoring"
			§ Look for documentation of the monitoring of these solutions. 
			§ e.g., 320 workflows, a calendar for reviews, and having specific people in charge of reviewing all 320 items. 
	· CA.L2-3.12.4 — System Security Plan
		○ Look for an SSP, system boundaries, environments, defined security requirements, the implementation, connections, updating frequency of the SSP, and evidence of the updating of the SSP. 
			§ System boundaries can be network diagrams, but also floor plan diagrams (for physical boundaries)
			§ environments can be cloud, remote work, buildings, offices, etc.
			§ security requirements and implementation are basically they 320 controls. 
				□ Can identify non-applicable controls but addressing them makes them applicable. 
				□ E.g., saying "no removable media" is a policy the fulfils (not exempt from) that specific requirement
			§ A timeline for the updating of the SSP, plus evidence that it's being updated. 

System and Communications Protection (SC)
	· SC-LI-3.13.1 Boundary Protection
		○ Look for internal and external defined, monitored, controlled, and protected system boundaries. 
			§ This can take 5ish minutes if this is documented well. 
	· SC.L2-3.13.2 — Security Engineering
			§ The DoD has covered several of these with full sections already  -this was covered earlier
	· SC.L2-3.13.3 — Role Separation
		○ Look for separations of rolls from basic rolls and system management (not just organizational management)
			§ I.e., not all actions should be done in admin accounts
	· SC.L2-3.13.4 — Shared Resource Control
		○ Look for processes to detect unauthorized and unintended information transfer
			§ I.e., memory, registers, cache memory, hypervisors, shared resource stacks for VMs
	· SC-LI-3.13.5 Public-Access System Separation
		○ Look for a list/diagram that separates specific connections to blocked/allowed sites. 
			§ E.g., Facebook, LinkedIn, websites, etc.
	· SC.L2-3.13.6 — Network Communication by Exception
		○ Look for ports/sites that have access granted again. 
			§ E.g., ports 443, port 80, specific sites, etc. 
			§ These can include lists, plus a domain controller, firewall, etc. 
	· SC.L2-3.13.7 - split Tunneling
		○ Look if remote devices are prevented from simultaneously establishing non-remote connections with the system and communicating via some other connection to resources in external networks (i.e., split tunneling).
	· SC.L2-3.13.8 — Data in Transit
		○ Look if there are cryptographic mechanisms and safeguards for data in transit. 
			§ E.g., encrypted data in network, data in a laptop, data physically moving in a backpack, etc.
			§ This is both physical and logical.
	· SC.L2-3.13.9 — Connections Termination
		○ Look for a list of conditions that terminate connections. 
			§ E.g., network timeout, logout, end of session, length of time, etc.
	· SC.L2-3.13.10 — Key Management
		○ Look for a listing/policy for the defined types of cryptography employed and how they are established and managed. 
			§ Can say that Microsoft manages the cryptography for XXX situations. 
			§ Cannot have clear text passwords ever, cannot use mechanisms that utilize them. 
			§ Make sure cryptography is not used if hashing is required. Should not be able to decrypt passwords. 
			§ Can use things like salting, which is good, but not required. 
	· SC.L2-3.13.11 — CUI Encryption
		○ Look for evidence of FIPS-validated cryptography use for CUI
	· SC.L2-3.13.12 - Collaborative Device Control
		○ Look for a list of identified devices, notification to users that these devices are being used, and the policy/requirement that remote activation is prohibited. 
			§ The discussion talks about network, whiteboards, cameras, microphones, 
			§ This discussion also excludes methods of sharing information via other communication technologies like teams, Zoom, DM, etc.
			§ This prevents admins from being able to remotely view sessions/desktops
	· SC.L2-3.13.12 - Mobile Code
		○ Look for the use of mobile codes are controlled and monitored
			§ This would include a policy for the use of these and event log of the codes used. 
	· SC.L2-3.13.14 — Voice over Internet Protocol
		○ Look for the use of VOIP and it's control and monitoring. 
			§ There should be a policy for this, and logs of usage.
			§ VIOP can be used for eavesdropping and should always be encrypted. (using TLS)
	· SC.L2-3.13.15 — Communications Authenticity
		○ Look for policies and protocols for the protection of authenticity of communications. 
	· SC.L2-3.13.16 - Data at Rest
		○ Look for a list of methods of how data is protected at rest
			§ This can be done with cryptography, but not required. 
			§ (laptops yes, because mobile in another policy, but not mandatory for servers or desktops)
			§ E.g., BitLocker, encrypted hard/flash drives, etc.

System and Information Integrity (SI)
	· SI.L1-3.14.1 Flaw Remediation 
		○ Look for the required amount of time used to identify system flaws (e.g., monthly, weekly, daily)
		○ Look for logs of people identifying, reporting, and remediating these issues within the time zone
	· Sl.L1-3.14.2 Malicious Code Protection
		○ Look for a list of locations for malicious code is identified and proof they are implementing this protection. 
	· Sl.L2-3.14.3 — Security Alerts & Advisories
		○ response actions to system security alerts and advisories are identified.
		○ system security alerts and advisories are monitored.
		○ actions in response to system security alerts and advisories are taken.
	· Sl.L1-3.14.4 Update Malicious Code Protection
		○ Determine if malicious code protection mechanisms are updated when new releases are available
	· Sl.L1-3.14.5 System & File Scanning
		○ the frequency for malicious code scans is defined.
		○ malicious code scans are performed with the defined frequency.
		○ real-time malicious code scans of files from external sources as files are downloaded, opened, or executed are performed.
	· Sl.L2-3.14.6 — Monitor Communications for Attacks
		○ the system is monitored to detect attacks and indicators of potential attacks.
		○ inbound communications traffic is monitored to detect attacks and indicators of potential attacks.
		○ outbound communications traffic is monitored to detect attacks and indicators of potential attacks.
	· Sl.L2-3.14.7 — Identify Unauthorized Use
		○ authorized use of the system is defined.
		○ unauthorized use of the system is identified.
	
