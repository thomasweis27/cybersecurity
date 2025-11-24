# Domain 3 Task 1
## CMMC Governance and Source Documents
### Current DoD DIB (Defence Industrial Base) Cyber efforts, regulations executive orders
##### Part 32 of the Code of Federal Regulations (CFR)
* DIB (Defence Industrial Base): Thousands of companies that partner with the DoD, typically chosen for price, performance, schedule, and security.
* 11/15/2021 strategy for cybersecurity:
  * Cyber intel sharing
  * DIB requirements and assessments
  * Reporting
  * assistance and collaboration
![image](https://github.com/user-attachments/assets/28dc4c90-8ac5-4d33-ad29-7c57e56c3a44)
##### Defence Federal Acquisition Regulation Supplement (DFARS) - Part 48 for CFR
* The federal regs code was created in 2016 and updated in 2022. This was supposed to apply to the entire government starting with Executive Order 13556.
* Title 32 - The Code of Federal Regulations (32 CFR Part 2002) was the "implementing directive" for CUI control.
* Previously ad-hoc policies, dependent on the agency.
* 32 CFR Part 2002 Sections:
  * Subpart 1: General Information - includes: Purpose and scope, incorporation by reference, Definitions, CUI EA (Executive Agent), and Roles & Responsibilities
  * Subpart 2: Key elements of the CUI Program - includes: CUI registry, CUI categories & subcategories, safeguarding, accessing and disseminating, decontroling, marking, Limitations on applicability, and self-inspection policies.
  * Subpart 3: CUI Program Management - includes: education & training, CUI cover sheets, transferring records, legacy material, waving requirements, CUI & disclosure statutes, CUI Privacy act, CUI Administrative Procedure Act (APA), challenges to designating info as CUI, dispurt resolition agencies, misuse of CUI, sanctions for CUI misuse. 
##### DFARS Clause 252.204-7012
* The first version, made in 2017, overstepped the DoD's abilities and was walked back by the Office of the Undersecretary of Defence.
* This did require the implementation of NIST SP 800-171 </br></br></br>
* NIST SP 800-171:
  * EO 13556 was meant to establish control over CUI
  * NIST SP 800-171 r2 was derived from NIST SP 800-53 removing requirements that were for the federal government, not related to protecting CUI, expected to be done by non-federal orgs.
  * NIST SP 800-171 r2 is used by CMMC 2.0 and contains 14 families containing 110 security requirements.
  * Basic info was from the Federal Information Processing Standards (FIPS) 200, then supplemented by NIST SP 800-53. 
* Technical Data DFARS 252.227-7013
  * Noncommercial technical information, may not be marked as CUI but needs safeguarding with the support of a gov. program. 
* FedRAMP (Federal Risk and Authorization Management Program):
  * If a contractor uses an external cloud service provider for storing, transmitting, or processing data they need to meet FedRAMP requirements.
  * Established in 2011 by the Office of Management and Budget (OMB), and is basically the Federal Information Security Moniterization Act (FISMA) for the Cloud.
  * Cloud service providers (CSPs) and Agencies submit a Control Implementation Summary (CIS) including:
    * Identified required security controls
    * Customer Responsibility Matrix (CRM) - items required for the customer to maintain.
  * Uses C3PAOs for external assessments
  * Houses the Program Management Office (PMO) - a searchable database for cloud service offerings (CSOs) with FedRAMP certs.
  * CSPs prepping for moderate status use a Redy Assessment Report (RAR) on the FedRamp Site. 

</br></br>
### CMMC Framework Tenets:
* Using the current framework, CMMC cannot push any requirements - only the DoD
* DoD contracts require each contract to determine the CMMC level required.
  * All must have at least level 1 as they have Federal Contract information (FCI).
  * All programs with/generating CUi will be at least Level 2.
  * Programs with very sensitive CUI concerns will be Level 3. 
* If subcontracting, the subcontractor needs certification with a level appropriate to the data handled.
* CMMC-AB was created for independent oversight of the C3PAOs and OSCs with the strict Code of Personal Conduct (CoPE). </br></br></br>
##### CMMC v2.0 requirements:
* New 2.0 goals: safeguard info, enhance DIB for cyber threats, ensure accountability, contribute to a collaborative culture, and maintain public trust.
* New Features: Tiered model, assessment requirement, and implementation through contracts. </br></br></br>
* Streamlined model:
  * There are 3 tiers instead of the original 5 and simplified instead of having 2 & 3 and 4 & 5 being similar and 2 & 4 being a stepping stone to 3 & 5.
  * Additional documentation requirements removed (although 2.0 requires a lot of documentation still)
* Reliable Assessments:
  * Level 1 and 2 based on NIST SP 800-171 r2.
  * Level 3 will be based on NIST SP 800-172 - more info coming from DoD about level 3 assessments.
  * Allows for reduced cost implementation and some of the original self-attestation benefits for FCI and some CUI.
    * There is more ability for the DoJ (Department of Justice) to pursue fraud (noncompliance).
* Flexible implementation:
  * CMMC 2.0 lets for "near completion" status through the POA&M (Plan of Action & Milestones) process 100% perfection was unrealistic.
  *  POA&Ms must be completed in 180 days and are not allowed on the most high-weighted requirements.
  *  Allows for some CMMC wavers in VERY specific cases. 
* Rulemaking and timeline for CMMC v2.0
  * Requirements to be passed 2022/2023
  * DIB to enhance Cyber posture before the release
  * Before release, requirements are recommended, but not required.
  * Two sections:
    * 32 CFR - Established CMMC Program
    * 48 CFR - Updates DFARS requirements and implements CMMC 2.0. 
* CMMC Levels of Assessments and Requirements
  * Foundation/Level 1 (FAR Clause 52.204-21)
  * Advanced/Level 2 (NIST 800-171)
* Self Assessments vs. Third Party Assessments


|Level|Practices|Basis|CUI Type|Assessments|
|:--:|:---|:---|:---|:---|
|3|110+|NIST SP 800-172|Highest priority CUI|Triennial gov. lead|
|2|110|NIST SP 800-171|CUI Prioritized acquisitions or Non-Prioritized CUI|Triennial 3rd party or Self assessment (respectively)|
|1|17|NIST SP 800-171 & FAR Clause 52.204-21|Non critical FCI|Annual self assessment|

</br>

The 17 Basic Level 1 Security Requirements 
1. Limit access to authorized users, processes, or devices
2. Limit access to the type of actions that authorized users are permitted to execute
3. Verify and control (or limit) connections to external information systems
4. Control information posted or processed on publicly accessible systems
5. Identify information system users, processes, or devices
6. Authenticate identities of users, processes, or devices prior to allowing access
7. Sanitize or destroy media containing Federal Contract Information
8. Limit physical access to information systems, equipment, and operating environment to authorized individuals
9. Escort visitors, monitor visitor activity, maintain audit logs of visitor activity, and control and manage physical devices
  * This is the one that was turned into three (escort visitors, physical access logs, and manage physical access) 
10. Monitor, control, and protect organizational communications
11. Implement subnetworks for publicly accessible system components that are separated from internal networks
12. Identify, report, and correct information and system flaws in a timely manner
13. Provide protection from malicious code
14. Update malicious code protection mechanisms when new releases are available
15. Perform periodic scans of the system and real-time scans of files from external sources as files are downloaded, opened, or executed


##### The 110 Level 2 Security Requirements
* Mirror NIST SP 800-171 r2
  * NIST SP 800-171 r2 has an ```Appendix E: NFO Controls``` that should be considered when addressing these.
  * Users should utilize CMMC Assessment Guide Level 2


##### Self vs Third-Party Assessments:
* All Level 1 and some Level 2 data does "not include data critical to national security" - this means the self-assessment is acceptable.
  * Requires annual assessments
  * Requires affirmation from a senior company official
  * Requires both annual assessment and affirmation to be uploaded to be uploaded to the Supplier Performance Risk System (SPRS).
* Most Level 2 Companies require Third-Party Assessments
  * Assessments are done by C3PAOs and they deliver the report to the DoD.
  * C3PAOs can be found on the CMMC-AB site marketplace.
* More guidance to come for level 3 assessments. </br></br>
* Benefits to taking the Level 2 assessment if not required:
  * Prepared for more advanced contracts
  * Higher level of confidence/maturity
  * Improved overall risk profile

</br></br>
##### Non-Compliance Consequences:
* Failure to receive the awarded contract:
  * Non-compliance would mean losing out on the contract. They cannot accept the contract without the proper certifications (they can bid on one though). (Level 1 or Level 2)
  * Compliance must be checked by the SPRS system by an officer.
  * Non-compliance means losing the contract. 
* Contractual liability:
  * There must be a yearly < 1-year-old self assessment and, if applicable, < 3-year-old Level 2 formal assessment.
  * If a sub-contractor fails to comply this can overtly affect the primary contract holder. 
* False Claims Act (DoD Civil Cyber-Fraud Initiative)
  * False Claims Act (FCA), 31 U.S.C Sections 3729-3733 was created in 1863 in response to defense contractor fraud in the Civil War.
  * Now can cause payouts triple to the damages caused and penalties linked to inflation.
  * Suits called and brought forth by "qui tam" aka whistleblowers, can receive a part of the settlement with an average of 30% of the settlement
  * Civil Fraud Iniciative:
    * 2021 DoJ Iniciative to use FAC to do cyber reviews and ensure compliance.
    * "Hold accountable entities or individuals that put U.S systems or information at risk [...]"
    * Benefits of the initiative include:
      * Broad resiliency
      * Holding contractors to signed requirements
      * Help find, identify, and publish vulnerabilities to alert others to ongoing and developing threats.
      * Incentivize rule-following and proper security/security investments.
      * Reimburse taxpayers for lost money not directed to cyber funds and security and intended
      * Improve overall practices.

</br></br></br></br></br></br></br></br></br>

---

## Additional Notes from the In-Person Class
CMMC Governance and Source Documents are based on:
* Federal Acquisition Regulations
* Defense Federal Acquisition Regulation Supplement
* National Institute of Standards and Technology (NIST)
* Department of Defense (DoD) Instructions
* Department of Defense (DoD) Memorandum
* National Archives and Records Administration (NARA)
* CERT Resilience Management Model (CERT-RMM)

FCI vs CUI:
* FCI: The US Department of Defense (DoD) has a vested interest in ensuring the confidentiality of Federal Contract Information (FCI) and Controlled Unclassified Information (CUI)
* CUI: The Cybersecurity Maturity Model Certification (CMMC) Framework is designed to improve the security posture of Defense Industrial Base (DIB) participants and hold DIB participants accountable for the protection of FCI and CUI and process, store, or transmit CUI.
  * CUI extends the requirements of FCI
 
Defense Industrial Base (DIB): Cybersecurity Efforts, Regulations, and Executive Orders. 
* Created the following infographic showing all of the ways they help people. 
![image](https://github.com/user-attachments/assets/28dc4c90-8ac5-4d33-ad29-7c57e56c3a44)
* These include:
  * CYBER THREAT INFORMATION/INTELLIGENCE SHARING WITH DIB
    * DoD CISO/DIB CS Program - voluntary public-private contract between DoD and DIP to share info/intel
    * DC3/DCISE - an operational arm of DIB CS Program, sharing threat info, itell, products and tools
    * NSA - "left of boom" products and tools with DIB
      * "boom"=canon ball, on Cyber KillChain - exploiting a human - MFA **(this was a bit unclear)**
  * INCIDENT REPORTING
    * DoD CISO/DIB CS Program - The loss of DoD data.
    * DC3/DCISE - clearinghouse for unclassified Mandatory incident reports (MIR)
    * DCSA - clearinghouse of classified reports
      * Reporting 72 hours of discovery at https://dibnetdod.mil (DIBNet)
  * DIB CYBERSECURITY REQUIREMENTS & ASSESSMENT MECHANISMS
    * DoD CISO/DIB CS Program - assistance to DIB in understanding regulatory requirements
    * DCMA - Oversight of DFARS 252.204-7019/7020, DIBCAC
    * USD (A&S)- Oversight of DFARS 252204-7021, CMMC
      * *DFARS 252.204-70197020 stipulates a contractor's requirement to implement NIST SP 800-171, have an assessment (basic, medium, or high), and prove the ability to protect CUI.
      * *DFARS 252.2047021 stipulates a contractor have a current CMMC certificate at the CMMC level required by the contract, and maintain the certificate at the required level for the duration of the contract
  * CYBERSECURITY TECHNICAL ASSISTANCE AND COLLABORATION
      * Support DIB as it's part of critical infrastructure


32 CFR (Code of Federal Regulations)
* Includes PART 2002 - CONTROLLED UNCLASSIFIED INFORMATION (CUI)
* Includes DFARS --> continuing contract requirements for DoD supplement info
* CMMC rule established to memorialize the verification requirements for 252.202-7012
48 CFR (Code of Federal Regulations)
* Includes 7021 - Clause for cert requirements on a contract-by-contract basis. [Not on the exam]
* FAR (not DFAR) --> Contains requirements for **all federal agencies** - including DoD
* 52.202 --> Extend the compliance requirement for CUI to require 800-171 (800-171a)
* **252.202-7012 --> will be expanded to all federal suppliers not just DoD**

32 CFR PART 2002—Controlled Unclassified Information (CUI) establishes
* The CUI program effective November 14, 2016
* National Archives and Records Administration (NARA) as the CUI Executive Agent (EA)
* Information Security Oversight Office (ISOO) to oversee the Federal Government-wide CUI Program

ISOO- Information Security Oversight Office
* Establishes policy for agencies on designating, safeguarding, disseminating, marking, decontrolling, and disposing of CUI, self-inspection, and oversight requirements

The CUI Program affects
* Federal executive branch agencies that handle CUI
* All organizations (sources) that handle, possess, use, share, or receive CUI
CMMC relevance
* Establishes the organizations charged with managing the CUI program



More about CUI:
* www.archives.gov/cui/registry/category-list
* ALL ITAR is not CUI
* No CUI type called ITAR

2002 Section:
* 5 2002.10 The CUI Registry
* 5 2002.12 CUI categories and subcategories
* 5 2002.14 Safeguarding
* 5 2002.16 Accessing and disseminating
* 5 2002.18 Decontrolling
* 5 2002.20 Marking
* 5 2002.22 Limitations on the applicability of agency CUI policies
* 5 2002.24 Agency self-inspection program

---

FARS System - Established for the codification and publication of uniform policies and procedures for acquisition by all executive agencies
* DFARS - D stands for DoD - cannot contradict, only supplement
* DFARS - starts with '25' instead of just '5'
* DFARS Clause 252.204-7012: Safeguarding Covered Defense Information and Cyber Incident Reporting
  * Requirements: Adequate security per NIST Special Publication (SP) 800-171 & Rapidly report cyber incidents within 72 hours to DoD at https://dibnet.dod.mil
  * CMMC assessments are conducted per NIST 800-171 and NIST 800-171 A
  * Subcontracts - Include this clause without alteration


DFARS Clause 252.204-7012 -
* 252.204-7012 includes
*  Controlled Technical Information (CTI)
* Covered Contractor Information systems
* Covered Defense Information (CDI)
* Controlled Unclassified Information (CUI)
* Safeguarding CDI

DFARS Provision 252.204-7019
* Notice of NIST SP 800-171 DoD Assessment Requirements
* Requirement
  * If the Offeror is required to implement NIST SP 800-171, the Offeror shall have a current assessment (i.e., not more than 3 years old) per the NIST SP 800-171 DoD Assessment Methodology
  * Post the results in the Supplier Performance Risk System (SPRS)
* CMMC self-assessment scores per the DoD Assessment Methodology are posted in SPRS

DFARS Clause 252.204-7021
* Cybersecurity Maturity Model Certification Requirements
* Requirement - The Contractor shall have a current (i.e. not older than 3 years) CMMC certificate at the CMMC level required by this contract and maintain the CMMC certificate at the required level for the duration of the contract
* Subcontracts. The Contractor shall—
  * Insert the substance of this clause, including this paragraph (c), in all subcontracts
  * Prior to awarding to a subcontractor, ensure that the subcontractor has a current (i.e., not older than 3 years) CMMC certificate at the CMMC level that is appropriate for the information that is being flowed down to the subcontractor
 
NIST SP 800-171
* National Institute of Standards and Technology (NIST)
* NIST sp 800-171, February 2020
  * Protecting CUI in Nonfederal Systems and Organizations
  * Establishes 110 security practices
* CMMC relevance
  * Establishes initial source for security practices
 
NIST SP 800-171 Document structure
* Fundamentals: Basic assumptions and how security requirements were developed
* Requirements: 14 Security domains representing 110 security practices and Dedicated discussion for each security practice
* Appendix A- References; list of vetted references applied during document development
* Appendix B - Glossary; approved and vetted terminology for consistently applying the framework
* Appendix C - Acronyms; approved and vetted terminology for consistently applying the framework
* Appendix D - Mapping Tables; cross reference to NIST 800-53 and ISO/IEC 27001
* Appendix E - Tailoring Criteria; the methodology used to extract relevant practices from federal standard

DFARS Clause 252.227-7013 Technical Data
* Rights In Technical Data—noncommercial items (FEB 2014)
  * Contractors grant the government royalty-free, worldwide, nonexclusive, irrevocable license rights in technical data other than computer software documentation
* The Government shall have
  * Unlimited rights to technical data that are
  * Government purpose rights for a five-year period
* All rights not granted to the Government are retained by the Contractor
* CMMC relevance: Technical data rights include assessment authority


DFARS Clause 252.204-7012 - FedRAMP
* CMMC assessments with in-scope external cloud service providers
  * Must provide a body of evidence (BOE), including but not limited to, documentation demonstrating FedRAMP status (if any) regarding the CSP
  * FedRAMP BOE may include items such as an SSP and a Customer Implementation Summary/Customer Responsibility Matrix that summarizes how each control is met and which party is responsible for maintaining that control
* Requirement per DFARS 252.204-7012 (b) Adequate security (2) (ii) (D)
  * If the [CMMC] Contractor intends to use an external cloud service provider to store, process, or transmit any covered defense information in performance Of this contract, the Contractor shall require and ensure that the cloud service provider meets security requirements equivalent to those established by the Government for the Federal Risk and Authorization Management Program (FedRAMP) Moderate baseline https://www.fedramp.gov/assets/resources/documents/FedRAMP Security Controls Baseline.xlsx

 ---

 CMMC v2.O Program Requirements
 * Streamlines Model:
   * Three levels
   * Removed Delta controls [removed because of DoD overeach]
   * Alligned with NIST SP 800-171, 800-171A, 800-172, and 800-172A standards
* Reliable Assessments:
  * Reduced Assessment Cost: Allows all companies at Level 1 (Foundational), and a subset of companies at Level 2 (Advanced) to demonstrate compliance through self-assessments
  * Higher Accountability: Increases oversight of professional and ethical standards of third-party assessors
* Flexible Implementation
  * Spirit of collaboration - DoD collaboration with Defense Industrial Base (DIB) to improve cybersecurity
  * Added flexibility and speed - CMMC 2.0 allows
  * Level 1 (FCI only) organizations "self-attest"
    * Assessment (all I IO practices) per the NIST DoD Assessment Methodology
    * Enter the score into the Supplier Performance Risk System (SPRS)
  * Level 2 (CUI and FCI) organizations may
    * Configure network to logically or physically separate scope for FCI only and for FCI and CUI
    * C3PAO confirms that OSC conducted a self-assessment for FCI scope
    * C3PAO verifies all 110 practices (FCI and CUI) within the scope for the Level 2 assessment

Rulemaking and Timeline for CMMC v2.O
* When will CMMC 2.0 be required for DoD contracts?
  * CMMC 2.0 will not be a contractual requirement until the DoD completes rulemaking to implement the program
  * The rulemaking process and timelines typically take 9-24 months
  * The Proposed Rule was published on 12/26/2023
    * The public comment period lasts for 60 days
  * The Final Rule typically takes 280 days to complete once the proposed rule is published (i.e., first half of 2025)
  * CMMC 2.0 will become a contract requirement when DoD completes rulemaking and updates related assessment guides
    * Contact certification requirements will be in clause 252-202.7021
   
CMMC Assessment Levels and Requirements
* Level I - Foundational (same as previous CMMC vl .O level I)
* Level 2 - Advanced (same as previous CMMC VI .0 levels 2 and 3)
* Level 3- Expert (same as previous CMMC vl .0 levels 4 and 5)

Access Control (AC) Practices
AC.LI -3.1.1 Authorized Access Control
AC.LI -3.1.2 Transaction & Function


Access Control (AC)
* AC.L2-3.1.3 control CUI Flow
* AC.L2-3.1.4 Separation of Duties
* AC.L2-3.1.5 Least Privilege
* AC.L2-3.1.6 Non-Privileged Account Use
* AC.L2-3.1.7 Privileged Functions
* AC.L2-3.1.8 Unsuccessful Logon Attempts
* AC.L2-3.1.9 Privacy & Security Notices
* AC.L2-3.1.10 Session Lock
* AC.L2-3.1.11 Session Termination
* AC.L2-3.1.12 Control Remote Access
* AC.L2-3.1.13 Remote Access Confidentiality
* AC.L2-3.1.14 Remote Access Routing
* AC.L2-3.1.15 Privileged Remote Access
* AC.L2-3.1.16 Wireless Access Authorization
* AC.L2-3.1.17 Wireless Access Protection
* AC.L2-3.1.18 Mobile Device Connection
* AC.L2-3.1.19 Encrypt CUI on Mobile
* AC.L1-3.1.20 External Connections
* AC.L2-3.1.21 Portable storage Use
* AC.L1-3.1.22 Control Public Information

Audit and Accountability (AU) Practices
* AU.L2-3.3.1 System Auditing
* AU.L2-3.3.2 User Accountability
* AU.L2-3.3.3 Event Review
* AU.L2-3.3.4 Audit Failure Alerting
* AU.L2-3.3.5 Audit Correlation
* AU.L2-3.3.6 Reduction & Reporting
* AU.L2-3.3.7 Authoritative Time Source
* AU.L2-3.3.8 Audit Protection
* AU.L2-3.3.9 Audit Management

---

Documentation:
* Understand the context - go to the discussion to understand
* Read the discussion
* Discover the trigger word
* Draft the implementation - don't wordsmith - use the exact words in the request
  * Make sure to address the specific things in the NIST "Discussion"
    * e.g., Mobile device = phones, ereaders, SOMETIMES laptops, things that work disconnected with a power source - not just a phone.
    * Make sure to look at the specific word in the assessment objective. 
</br>

* Bob's Machine Shop defines information flow control policies [a] via layer managed switch access control lists (ACLs).
* Bob's Machine Shop defines methods and enforcement mechanisms for controlling the flow of CUI [b] via procedures and L3 Switch configurations.
* Per the implementation statements; Determine and provide the adequate and sufficient evidence.

* Disputes: SPRS - supplier performance risk system
  * Sam.gov --> DLA --> Cage Code --> used by OSE for cert
  * For aceess SPRS: PIEE --> Accounts --> RBAC



 
NIST DoD Assessment Methodology
* Determine Basic score (self-assessment)
* DIBAC - Moderate, High in Person, High Remote
* USG SSO
* SAM - System for Award Management
  * CAGE - Commercial and Government Entity Program
  * IJEI • Unique Entity Identifier
  * D&B- Dun & Bradstreet
* PIEE - Procurement Integrated Enterprise Environment
  * OSC must identify the OSC's contract administrator
* SPRS - Supplier Performance Requirements System
  * this score ends up (for independent assessments only) in eMASS
* eMASS - Enterprise Mission Assurance support Service
  * eMASS is DoD database for storing security results
  * eMASS has multiple instances e.g. Army, AF, Navy, Marines, CMMC
  * C3PAO's will have an person on staff to enter L2 results
  * That person must have an eMASS acceptable identity certificate
* ECA - External Certification Authority

---

## When auditing:

Three approved methods:
* **Review** the documentation - see it exists,
* **Interview** to verify that the documents are used and people know about it
* **Testing** to ensure that what they say they do, they can actually do. (If we don't believe them.)

People being audited should be able to hit all the points and know how to hit all the requirements. 

OSEs need to train the staff how to respond:
* In one or two full sentences (this is like playing poker - focus on typing not the interviewee)
* The interviewee should not say something that would hurt the audit (easy if they keep talking)
* Two person process, one person asks questions, one takes notes. (switching back and fourth)

---

Self-Assessment vs. Third Party:
* Self-assessments
  * (Foundational) does not involve sensitive national security information
  * allows companies to assess their cybersecurity and begin adopting practices that will thwart cyber-attacks
  * Contractors conduct self-assessments per NIST DoD Assessment Methodology
    * Annually (per DoD CIO FAQ)
    * Triennially (per DFARS 252.204-7019)
  * Organizations register self-assessments and affirmations in the Supplier Performance Risk System (SPRS)
  * Self-assessments require annual affirmation from a senior company official (inherent in SPRS)
* Third-party assessments
  * CMMC 2.0
    * Contractors obtain a third-party CMMC assessment for a subset of acquisitions requiring Level 2 ("Advanced") cybersecurity standards that involve information critical to national security.
  * The Cyber-AB will accredit
    * CMMC Third Party Assessment Organizations (C3PAOs)
    * CMMC Assessors and Instructors Certification Organization (CAICO)
  * Accredited C3PAOs are listed on the Cyber-AB Marketplace
  * DIB companies are responsible for obtaining the needed assessment and certification
  * Begin by ensuring there's no conflict of interest.
  * The Cyber-AB must achieve compliance with the ISO/IEC 17011 standard prior to accrediting C3PAOs and the CAICO
  * C3PAOs will be required to comply with ISO/IEC 17020
  * CAICO will be required to comply with ISO/IEC 17024 requirements
* Government Assessments
  * Level 3 cybersecurity requirements to be assessed by government officials i.e., DIBCAC
  * Level 3 assessment requires prerequsite of Level 2 C3PAO assessment
  * Scoping is different between level 2 and 3; not the controls.


Consequences of Non-Compliance
* Failure to receive an award of contract — Vendors that do not meet contract certification requirements will be excluded from those contracts
* Contractual liability — Failure to meet contract terms and conditions subjects the vendor to legal action by DoD and impacted supply chain participants


False Claims Act
* US Department of Justice Civil Cyber-Fraud Initiative
* Deputy Attorney General Lisa O. Monaco 10/26/2021
  * Announces New Civil Cyber-Fraud Initiative
  * Combines the department's expertise in civil fraud enforcement, government procurement and cybersecurity to combat new and emerging cyber threats to the security of sensitive information and critical systems




