# CMMC Assessment & Control Study Notes

> Personal study notes and practical assessor mindset reminders.  
> Focus: Evidence identification, interview preparation, and control validation strategies.

---

# Notes on the Assessment

## Assessment Guide Versioning
- The exam uses **Version 2** of the assessment guide.
  - Level 1 assessment items (FCI) are grouped together.
  - Revised version (**Version 2.13**) mixes Level 1 and Level 2 items to ensure all controls are evaluated.
    - Entire document is labeled Level 2 to clarify inclusion of Level 1.
    - Includes FAR numbering references (example: `-b.1.i`).
- **Always use the most up-to-date assessment guide during an assessment.**

## Study Recommendation
- Use the most current assessment guide revision when studying and performing assessments.

---

# Domain 4 – Task 1

## Evidence Types

### Artifacts
Artifacts are any documented or stored files used as evidence.

Examples:
- Rosters
- Asset inventories
- User access listings
- Privileged user listings

Key Notes:
- Evidence **can be reused** across multiple control objectives.
- Contradictory evidence or incomplete coverage may cause assessment failure.
- Artifacts must be reproducible during interviews.

Common Artifact Types:
- Policies
- Procedures
- System Security Plans (SSP)
- Security requirements
- Architecture diagrams
- Asset inventories
- System configurations
- Audit logs

---

### Interviews
Interviews validate that personnel **actually perform the documented processes**.

Best Practices:
- Interview personnel who perform the work.
- Avoid interviewing leadership or oversight-only personnel unless required.
- Confirm interviewees understand the assessment discussion.
  - If they do not understand the process or controls, awareness may be insufficient.

---

### Testing
Testing validates controls using real system functionality.

Requirements:
- Must be conducted on production systems or exact production replicas.
- Screenshots may qualify as artifacts.

Testing Expectations:
- Demonstrations should occur within minutes.
- Processes requiring hours/days typically are not considered dynamic reporting.

Appeals:
- The OSC may appeal findings.
- C3PAO committees determine official outcomes.

---

# Access Controls (AC)

## AC.L1-3.1.1 – Authorized Access Control
- Verify authorized users are defined.
- Look for keyword alignment with control requirements.

---

## AC.L1-3.1.2 – Transaction & Function Control
- Confirm system access is restricted to authorized users.

---

## AC.L2-3.1.3 – Control CUI Flow
Look for:
- Policies describing handling and movement of CUI.
- Diagrams showing CUI flow paths.
- Procedures governing inbound and outbound data transfers.

---

## AC.L2-3.1.4 – Separation of Duties
- Identify defined roles with separated responsibilities.
- Verify reasonable control mechanisms exist.

---

## AC.L2-3.1.5 – Least Privilege
Look for:
- Defined privileges for all accounts.
- Authorization processes (HR, supervisor approval).
- Separation of administrative security functions.

---

## AC.L2-3.1.6 – Non-Privileged Account Use
- Confirm defined non-security user functions.

Examples:
- Timesheets
- Internet usage
- Software usage
- Standard logins

---

## AC.L2-3.1.7 – Privileged Functions
Look for:
- Documentation defining privileged vs non-privileged functions.
- Administrative policies or Acceptable Use Policies.
- Technical enforcement controls:
  - RBAC
  - Logging

---

## AC.L2-3.1.8 – Unsuccessful Logon Attempts
- Confirm defined thresholds and consequences (account lockout).

Future Note:
- Revision 3 recommends **5 failed attempts** (expected implementation ~2026–2027).

---

## AC.L2-3.1.9 – Privacy & Security Notices
- Verify required notices exist and align with CUI categories.

Examples:
- Login banners
- Facility signage
- Data center notices

---

## AC.L2-3.1.10 – Session Lock
- Verify inactivity timeout definitions.
- Confirm implementation (example: Active Directory settings).

Future Recommendation:
- 15-minute inactivity timeout (CMMC 3.0 draft guidance).

---

## AC.L2-3.1.11 – Session Termination
- Confirm conditions that terminate sessions:
  - Logout
  - Timeout
  - Triggered events

---

## AC.L2-3.1.12 – Control Remote Access
Review:
- Allowed remote access types
- Time limitations
- Connection types (VPN, RDP)
- RBAC enforcement
- Monitoring through logs or SIEM

---

## AC.L2-3.1.13 – Remote Access Confidentiality
- Confirm protection mechanisms for data in transit.
- Examples:
  - TLS 1.2 / 1.3
  - Connection whitelisting
  - Logging

---

## AC.L2-3.1.14 – Remote Access Routing
- Confirm managed access control points.

Example:
- Border router directing traffic through DMZ firewall ports.

---

## AC.L2-3.1.15 – Privileged Remote Access
- Verify:
  - Authorized command lists
  - Role-based command access

---

## AC.L2-3.1.16 – Wireless Access Authorization
- Network diagrams
- Floor plans showing WAP placement
- Policies authorizing wireless access

---

## AC.L2-3.1.17 – Wireless Access Protection
- Confirm defined wireless encryption and authentication mechanisms.

---

## AC.L2-3.1.18 – Mobile Device Connection
- Authorized device lists
- Connection logs

---

## AC.L2-3.1.19 – Encrypt CUI on Mobile Devices
- Confirm FIPS-validated cryptography for CUI.
- Additional encryption does not replace FIPS requirements.

---

## AC.L1-3.1.20 – External Connections
- List external systems and validation methods:
  - RBAC
  - MFA

---

## AC.L2-3.1.21 – Portable Storage Use
- Document allowed devices and usage.
- Confirm port blocking and administrative controls.

---

## AC.L1-3.1.22 – Control Public Information
Look for:
- Approved personnel for public posting
- Review procedures preventing CUI disclosure
- CUI removal processes

---

# Awareness and Training (AT)

## AT.L2-3.2.1 – Role-Based Risk Awareness
- Policies and training addressing security risks.
- Personnel must know where resources are located.

---

## AT.L2-3.2.2 – Role-Based Training
- Defined security roles.
- Assignment based on qualifications and responsibilities.

---

## AT.L2-3.2.3 – Insider Threat Awareness
- Training participation documented.
- DoD training acceptable but not required.

---

# Audit & Accountability (AU)

## AU.L2-3.3.1 – System Auditing
Look for logging supporting:

- System auditing
- User accountability
- Event review
- Audit failure alerting
- Correlation and timeline reconstruction
- Log aggregation and reporting
- Authoritative time synchronization
- Audit protection
- Audit management

---

## AU.L2-3.3.3 – Event Review
- Confirm policies and logs are regularly reviewed.

---

## AU.L2-3.3.4 – Audit Failure Alerting
- Verify defined alert triggers requiring administrative action.

---

## AU.L2-3.3.6 – Reduction & Reporting
- Aggregation server or SIEM must exist.
- On-demand reporting should take minutes, not days.

---

## AU.L2-3.3.7 – Authoritative Time Source
- Confirm centralized time synchronization.

---

## AU.L2-3.3.8 – Audit Protection
- Verify log access restrictions.
- Confirm protection against deletion or tampering.

---

## AU.L2-3.3.9 – Audit Management
- Confirm limited personnel manage audit logs.

---

# Configuration Management (CM)

## CM.L2-3.4.1 – System Baselining
- Baselines for hardware, software, firmware, and documentation.
- Often implemented through automation tools (e.g., Intune).

---

## CM.L2-3.4.2 – Security Configuration Enforcement
- Policies and technical enforcement for configuration standards.

---

## CM.L2-3.4.3 – System Change Management
- Change tracking and approval process.
- Prefer review board decisions.
- Ticketing systems recommended.

---

## CM.L2-3.4.4 – Security Impact Analysis
- CIA impact analysis prior to changes.

---

## CM.L2-3.4.5 – Access Restrictions for Change
- Physical and logical change access controls.

---

## CM.L2-3.4.6 – Least Functionality
- Restrict ports and services to essential operations.

---

## CM.L2-3.4.7 – Nonessential Functionality
- Maintain allow/deny lists for:
  - Programs
  - Services
  - Protocols
  - Ports

---

## CM.L2-3.4.8 – Application Execution Policy
- Whitelisting / blacklisting processes and enforcement.

---

## CM.L2-3.4.9 – User-Installed Software
- Defined installation authority and monitoring.

---

# Identification & Authentication (IA)

## IA.L1-3.5.1 – Identification
- Identify users, devices, and processes.
- Must include verification processes.

---

## IA.L1-3.5.2 – Authentication
- Implement and enforce authentication processes.

---

## IA.L2-3.5.3 – Multifactor Authentication
- Required for:
  - Privileged accounts
  - Network access to non-privileged accounts

---

## IA.L2-3.5.4 – Replay-Resistant Authentication
Examples:
- TLS 1.2 / 1.3
- Kerberos

---

## IA.L2-3.5.5 – Identifier Reuse
- Define reuse delay after account termination.

---

## IA.L2-3.5.6 – Identifier Handling
- Define and enforce account disable timelines.

---

## IA.L2-3.5.7 – Password Complexity
- Complexity requirements and enforcement.
- Must use SHA-2 or higher.

---

## IA.L2-3.5.8 – Password Reuse
- Define password history enforcement.

---

## IA.L2-3.5.9 – Temporary Passwords
- Force change upon first login.

---

## IA.L2-3.5.10 – Cryptographically Protected Passwords
- Protect passwords in storage and transit.

---

## IA.L2-3.5.11 – Obscured Feedback
- Masked login entries.

---

# Incident Response (IR)

## IR.L2-3.6.1 – Incident Handling
- Preparedness
- Detection
- Analysis
- Containment
- Recovery

---

## IR.L2-3.6.2 – Incident Reporting
- Documented tracking system.
- External and internal reporting contacts defined.

---

## IR.L2-3.6.3 – Incident Response Testing
- Includes tabletop exercises and cross-department testing.

---

# Maintenance (MA)

## MA.L2-3.7.1 – Perform Maintenance
Maintenance types:
- Corrective
- Preventative
- Adaptive
- Perfective

---

## MA.L2-3.7.2 – System Maintenance Control
- Authorized tools, personnel, and processes defined.

---

## MA.L2-3.7.3 – Equipment Sanitization
Valid methods:
- Secure erase
- Degaussing
- Physical destruction
- FDE erase

---

## MA.L2-3.7.4 – Media Inspection
- Malicious code testing processes.

---

## MA.L2-3.7.5 – Nonlocal Maintenance
- MFA required.
- Sessions terminated after completion.

---

## MA.L2-3.7.6 – Maintenance Personnel
- Supervision required for unauthorized personnel.

---

# Media Protection (MP)

## MP.L2-3.8.1 – Media Protection
- Physical and logical storage controls.

---

## MP.L2-3.8.2 – Media Access
- Restrict physical CUI media to authorized users.

---

## MP.L2-3.8.3 – Media Disposal
- Sanitization procedures must be documented.

---

## MP.L2-3.8.4 – Media Markings
- Correct CUI marking requirements.
- Note regulatory differences between NARA and DoD 5200.48.

---

## MP.L2-3.8.5 – Media Accountability
- Tracking and control mechanisms required.

---

## MP.L2-3.8.6 – Portable Storage Encryption
- FIPS cryptographic protection for CUI.

---

## MP.L2-3.8.7 – Removable Media
- Usage controls such as port blocking or allow lists.

---

## MP.L2-3.8.8 – Shared Media
- Prohibit unidentified removable devices.

---

## MP.L2-3.8.9 – Protect Backups
- Backup protection required if backups exist.

---

# Personnel Security (PS)

## PS.L2-3.9.1 – Screen Individuals
- Background checks evaluating:
  - Integrity
  - Reliability
  - Stability
  - Conduct

---

## PS.L2-3.9.2 – Personnel Actions
- Access revocation during termination or transfer.
- Privilege review process.

---

# Physical Access (PE)

## PE.L1-3.10.1 – Limit Physical Access
- Restrict access to facilities and equipment.

---

## PE.L2-3.10.2 – Monitor Facilities
- Cameras, badge systems, or monitoring personnel.

---

## PE.L1-3.10.3 – Escort Visitors
- Visitor escort procedures required.

---

## PE.L1-3.10.4 – Physical Access Logs
- Maintain visitor and employee access logs.

---

## PE.L1-3.10.5 – Manage Physical Access Devices
- Inventory and manage keys, badges, and locks.

---

## PE.L2-3.10.6 – Alternate Work Sites
- Security controls for:
  - Home offices
  - Remote work
  - Alternate facilities

---

# Risk Assessment (RA)

## RA.L2-3.11.1 – Risk Assessments
- Qualitative or quantitative risk ranking required.

---

## RA.L2-3.11.2 – Vulnerability Scanning
- Defined scanning frequency.
- Scanning triggered by new vulnerabilities.

---

## RA.L2-3.11.3 – Vulnerability Remediation
- Remediation aligned with CVE severity and risk analysis.

---

# Security Assessment (CA)

## CA.L2-3.12.1 – Security Control Assessment
- All controls assessed annually.

---

## CA.L2-3.12.2 – Plan of Action & Milestones (POA&M)
- Track remediation planning and implementation.

---

## CA.L2-3.12.3 – Security Control Monitoring
- Monitoring evidence required.
- Does not require continuous monitoring.

---

## CA.L2-3.12.4 – System Security Plan (SSP)
Must include:
- Boundaries
- Environment descriptions
- Security implementations
- Connection mapping
- Update timelines

---

# System & Communications Protection (SC)

## SC.L2-3.13.1 – Boundary Protection
- Define and monitor internal and external boundaries.

---

## SC.L2-3.13.3 – Role Separation
- Separate administrative and standard user roles.

---

## SC.L2-3.13.4 – Shared Resource Control
- Prevent unintended data transfer between shared resources.

---

## SC.L2-3.13.5 – Public Access System Separation
- Separate public-facing systems from internal systems.

---

## SC.L2-3.13.6 – Network Communication by Exception
- Maintain explicit allow lists for network communication.

---

## SC.L2-3.13.7 – Split Tunneling
- Prevent simultaneous remote and external connections.

---

## SC.L2-3.13.8 – Data in Transit
- Cryptographic protection required for data movement.

---

## SC.L2-3.13.9 – Connection Termination
- Defined termination triggers required.

---

## SC.L2-3.13.10 – Key Management
- Document cryptographic lifecycle and management.
- Never store plaintext passwords.

---

## SC.L2-3.13.11 – CUI Encryption
- FIPS-validated cryptography required.

---

## SC.L2-3.13.12 – Collaborative Device Control
- Notify users when collaborative devices are active.
- Prevent unauthorized remote activation.

---

## SC.L2-3.13.13 – Mobile Code
- Control and monitor mobile code usage.

---

## SC.L2-3.13.14 – VoIP Protection
- Encrypt and monitor VoIP communications.

---

## SC.L2-3.13.15 – Communications Authenticity
- Ensure authenticity and integrity protections exist.

---

## SC.L2-3.13.16 – Data at Rest
- Identify protection methods such as:
  - BitLocker
  - Encrypted drives

---

# System & Information Integrity (SI)

## SI.L1-3.14.1 – Flaw Remediation
- Define remediation timelines.
- Maintain remediation logs.

---

## SI.L1-3.14.2 – Malicious Code Protection
- Identify protected system locations.
- Provide implementation evidence.

---

## SI.L2-3.14.3 – Security Alerts & Advisories
- Monitor alerts.
- Respond appropriately.

---

## SI.L1-3.14.4 – Update Malicious Code Protection
- Ensure protection mechanisms remain updated.

---

## SI.L1-3.14.5 – System & File Scanning
- Define and implement scan frequency.
- Enable real-time scanning for external files.

---

## SI.L2-3.14.6 – Monitor Communications for Attacks
- Monitor inbound and outbound communications.

---

## SI.L2-3.14.7 – Identify Unauthorized Use
- Define authorized usage.
- Detect unauthorized activity.

---
