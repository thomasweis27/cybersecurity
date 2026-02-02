# CMMC Study Notes  
## Domain 1 – Task 1

---

# Logical vs Physical Locations

## Key Study Focus
- Always reference **learning objectives** when studying.
- Understand **how Controlled Unclassified Information (CUI) is accessed and stored**.

### Data Location Considerations
- Determine where data resides:
  - On-premises
  - Cloud-hosted
  - Hybrid environments
- Many **Organizations Seeking Certification (OSCs)** are migrating to cloud environments to reduce infrastructure responsibility.
- On-premises environments place **full responsibility for protection** on the organization.

### Location-Based Limitations
- Organizations can restrict where CUI is accessed or stored.
  - Example:
    - All local/on-prem CUI is restricted to:
      - One secured room
      - Dedicated systems

### Thin Clients vs Local Storage
- Assess whether:
  - A workstation is a **thin client** (only accessing data remotely)
  - CUI exists locally on the device

### Physical Security Requirements
- Physical protections must exist even for **encrypted devices**.
- Assessors do **NOT** require direct access to CUI.
  - They require **evidence that controls protecting CUI are implemented**.
- OSCs should be prepared to demonstrate:
  - Virtual Desktop Infrastructure (VDI) configurations
  - Access restrictions
  - Logging and monitoring controls

---

## Virtualization Basics
- Virtual Machines (VMs) always operate on top of a **hypervisor**.
- The hypervisor supports:
  - Guest Operating Systems
  - Applications running inside VMs

---

## Access Control Requirements
- Access controls must apply regardless of user location.
- Safeguards must include:
  - Logical security controls
  - Physical security controls
- Security requirements may vary based on:
  - Remote vs in-person access
  - Cloud vs on-prem systems

---

# System Architecture

## Security Engineering
Security engineering involves:

- Architectural design
- Secure software development techniques
- Systems engineering principles
- Promoting effective organizational information security

---

## Architecture Requirements
OSCs should implement architectures that combine:

- On-prem security controls
- External/Cloud security controls

### Required Documentation
- Logical network diagrams
- Physical facility diagrams
- Security design documentation

### Recommended Security Frameworks
- OWASP Secure Design Principles
- NIST SP 800-160 Volume 1 Appendix F
- CIS security and architectural design resources

---

## Backup Security Requirements
- Backups are **not mandatory**, but if they exist and contain CUI:
  - They must be protected.
- Encryption alone is insufficient.
- Off-prem backups must be protected within a **FedRAMP Moderate (or equivalent) environment**.

---

## Network Segmentation

### Purpose
Segmentation protects CUI by isolating sensitive systems from public or less secure networks.

### Common Methods
- VLANs
- DMZs
- Enclaves
- Micro-segmentation
  - Device-level firewall rules
- Zero Trust Architecture
  - Continuous verification between devices
  - No implicit trust

### Evidence Requirements
Assessors typically require:
- Firewall rule sets
- Network segmentation configurations
- Network architecture diagrams

---

# Change Restrictions

## Access Restrictions for System Changes
OSCs must:

- Define change procedures
- Document change processes
- Approve changes before implementation
- Enforce both physical and logical access restrictions

---

### Examples of Change Controls
- Locked server rooms
- Mantraps
- Role-Based Access Control (RBAC)
- Change Control Boards (CCB)

### Small Organization Exception Practices
Small organizations may:
- Document changes via email or ticketing systems
- Document:
  - Security testing performed
  - Change justification
  - Approval evidence

---

## Maintenance Controls
Maintenance activities must include:

- Physical security (escorts, locks)
- Monitoring maintenance personnel
- Validating maintenance tools/software
- Logging maintenance activity

---

# In-Scope CMMC Asset Categories

## 1. CUI Assets
Assets that:
- Process
- Store
- Transmit CUI

---

## 2. Security Protection Assets
Includes security tools and resources such as:

- Firewalls
- SIEM systems
- Security staff
- Security facilities

> Note: Assets may fall into multiple categories.

### Managed Service Providers (MSPs)
If using MSPs:
- MSP personnel must be trained to handle CUI.
- MSPs must provide:
  - Service Level Agreements (SLAs)
  - Compliance attestations
  - Personnel screening and training evidence

---

## 3. Contractor Risk Managed Assets (CRMAs)
Characteristics:

- Within assessment scope
- Managed via risk-based security policies
- Not directly assessed against CMMC practices
- Capable of processing CUI but **not intended to**

> Note: CMMC 2.0 provides less explicit separation guidance.

### CRMA Documentation
Typically documented in:
- System Security Plan (SSP)
- Approved asset and personnel lists

---

## 4. Specialized Assets

### Government Property
- Owned or leased by government entities

### IoT / IIoT
- Interconnected physical or virtual devices

### Operational Technology (OT)
Examples:
- PLCs
- CNC machines
- Fabrication and machining controllers

### Restricted Information Systems
- Systems configured based on government requirements

### Test Equipment
- Used to validate systems, deliverables, or components

---

## Out-of-Scope Assets
Assets are out of scope if they:

- Cannot process, store, or transmit CUI
- Provide no security protections for CUI assets
- Are physically or logically separated from CUI environments

---

# Professional vs Industrial Environments

## Professional Environments
- Office-based systems
- Standard enterprise IT

## Industrial Environments
- Manufacturing systems
- Operational technology environments

---

# System Inventory and Baseline Management

## Requirements
OSCs must:

- Establish baseline configurations
- Maintain inventories of:
  - Hardware
  - Software
  - Firmware
  - Documentation
- Maintain asset lifecycle tracking

---

## Network Placement and Monitoring
Organizations must:

- Identify who accesses systems
- Maintain audit logging
- Track user actions across systems

---

# System Elements

Includes:

- Technology components
- Human operators
- Physical and environmental infrastructure
- Third-party interconnections

---

## Enabling Systems
Examples:
- Servers
- Workstations
- Administrative staff
- Infrastructure components

---

## Environment of Operation
Organizations must understand:
- How systems interact
- Environmental dependencies
- External system integrations

---

# Architecture Definition Process

### Purpose
To:
- Develop architectural alternatives
- Address stakeholder requirements
- Produce consistent security viewpoints

### Security Architecture Steps
- AR-1: Prepare for architecture definition
- AR-2: Develop security viewpoints
- AR-3: Create security models
- AR-4: Align architecture with design
- AR-5: Select candidate architecture
- AR-6: Maintain architecture security views

---

# Single vs Multi-Site Constraints

## Assessment Considerations
Includes:
- External connections
- Alternative work sites
- Session termination controls

### Remote Work Impact
- If CUI is taken home:
  - The home environment becomes **in scope**

### CAP Updates
- CAP 5.6.1 (Legacy):
  - More on-site validation required
- CAP 2.0:
  - Allows flexibility
  - Focuses on what is "appropriate and necessary"

---

# Remote Access Requirements

Organizations must:

- Control remote access
- Monitor remote sessions
- Define allowed remote access methods

---

## Cloud Considerations
- Accessing cloud-hosted CUI is still considered remote access.

---

## Encryption Requirements
- VPN or encrypted communications are still remote access.
- Must use **FIPS 140-2 or FIPS 140-3 validated encryption**.

### Important Distinction
- FIPS **Validated** ≠ FIPS **Compliant**

### Validation Authorities
- NIST Cryptographic Module Validation Program (CMVP)
- Cryptographic and Security Testing Laboratories (CSTL)

---

## Monitoring Requirements
Organizations must provide:

- VPN logs
- RDP session logs
- Network monitoring logs

---

# External Connections

Organizations must:

- Identify and document all external connections
- Limit external system communications
- Enforce secure authentication:
  - Unique user IDs
  - Passwords
  - Multi-Factor Authentication (MFA)

---

## External System Monitoring
Assessors may review:

- Event logs
- Network architecture diagrams
- External connection configuration documentation

---

# Alternative Work Sites

Organizations must:

- Maintain a list of all alternative work locations
- Document safeguards per location
- Separate remote vs on-site security requirements
- Address both:
  - Physical safeguards
  - Logical safeguards

---

# Facility and Service Ownership Considerations

## Co-Located Data Centers
- Limited ability to implement controls if managed by an External Service Provider (ESP)

---

## Security Operations Centers (SOC)

### OSC Owned
- Requires:
  - 24x7x365 staffing
  - Significant capital investment

### ESP Owned
- Limited control over security implementations

---

## Contractor Office Buildings

### OSC Owned
- Full control but high operational cost

### Leased Facilities
- Potential limitations on:
  - Physical security
  - Network architecture design

---

# Policy Timeline Requirement

Organizations must demonstrate policies and controls dating back to:

> **November 10th (CMMC implementation date)**

Failure to demonstrate historical control implementation may result in:

- Failed assessment controls
- Potential government compliance violations

---
