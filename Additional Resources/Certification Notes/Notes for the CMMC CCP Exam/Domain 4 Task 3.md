# Domain 4 Task 3
## FCI Asset Scope Scinarios
### FCI data in different Asset Forms:
* Things to consider:
  * How does the sensitive data enter the environment?
    * Email
    * FTP, SSH, or SCP for secure transmission
    * REST, SOAP, or RCP call to an external system
    * Cloud-based
    * USB, CD, etc.
    * Paper (printed, faxed, or handwritten)
  * Network Diagrams: shows all the devices attached to the network. Large systems may need more than one. Devices include:
    * subnets
    * Switches
    * Routers
    * Firewalls
    * security tools
    * Systems on that network
  * Determine the data flows showing where the data is being transmitted and the security controls in place
  * Boundaries and Separations: Include both physical and logical separation.
    * Physical Boundaries: one physical barrier, physical separation for enclaves, access to the facility, and encryption
    * Logical Boundaries: Firewalls employed
    * Data transfer restricted
    * Data in transit encrypted
  * Data destruction:
    * Physical copies are burnt, shredded
    * When copied done on a device are the files deleted, is the device reformatted, and is the reformatting good enough?
    * Is all data properly destroyed when the contract is concluded?
    * Proper destruction from other workspaces (e.g., home/remote workers)
  * Other work sites:
    * Are any of the devices not in the secure facility? Can out-of-scope people access these or cause a loss of integrity?
    * Are passwords, encryption, and NACs in place to ensure security?
    * Are staff there for physical protection? Have they been trained?
* Before an assessment begins all parties must agree about the scope of the project.
* The scope can expand if data/artifacts show data is/can be discovered outside of scope.
##### Process
* Involves using or manipulating FCI:
  * Database queering FCI
  * Laptops for viewing/editing FCI
  * Printing copies of FCI
  * Workstations that can write info to a portable device
  * Apps that can load FCI into memory
  * Antivirus programs comparing FCI to known threats. 
##### Store
* FCI on an asset when not actively processed:
  * FCI on hard drives
  * Documents with FCI on them
  * CDs or portable devices with FCI
  * Cloud systems
  * Backups
  * Email servers
  * Facilities containing devices with FCI
  * Multi-functional Machines
  * Cameras that can take pictures of data
##### Transmit
* FCI passes through devices while in transit.
  * Carrying a document in hand
  * switch passing FCI packets
  * Wireless signal for transmission
  * Email server sitting between sender and recipient
### Out-of-Scope Assets
* Assets are out-of-scope if they do not **process, store, or transmit** CUI
* Boundaries are not required for FCI level 1.
### Specialised Assets:
* A lot of items are not in the CMMC Level on assessment scope and are considered "Specialised Assets"
##### Government Property
* This is all property leased or owned by the gov.
* Coube be used for contract performance, or purchased/leased by the contractor.
* Includes: materials, equipment, tooling, test equipment, property (e.g., facilities, land)
* Software and IP are not gov property.
##### IoT/Industural IoT (IIoT)
* Each device is uniquely identified and must have access to the systems with FCI/have FCI:
  * E.g., a timeclock system on a LAN with FCI.
##### Operational Technology (OT)
* Networked systems that are used for manufacturing, material handling, monitoring, or control, including:
  * Computerized Numerical Control (CNC)
  * Supervisory Control and Advisory Systems (SCADA)
  * Programmable Locial Controllers (PLC)
##### Restricted Information Systems
* Systems that are built based on gov requirements for a contract
* Normally built for the OSC and delivered to the DoD per the contract.
##### Test Equipment
* Specialized equipment used to test IT hardware components, including:
  * X-ray machines
  * spectrum analyzers
  * laboratory equipment
  * Power meters
  * Oscilloscopes
### Scoping Activities:
* CMMC Level 1 includes people, technology, facilities, and service providers that process, store, or transmit FCI.
* CMMC Level 2 assessment includes this and adds assets that perform security functions for CUI and connect to in-scope functions, but don't have to process, store, or transmit CUI.
##### People
* People can store, process, and transmit CUI, plus they can remember this and use it for out-of-scope items.
* Categorizing people is tricky; can they see/hear FCI on-site or at home?
##### Technology
* This includes all devices that have access to the FCI (e.g., firewalls, laptops, routers, NAS devices, switches, etc.)
##### Facilities
* Locations that store/house the data or devices that control the data. (e.g., home offices, office, warehouse, etc.)
##### External Service Providers (ESP)
* People/items that are in scope include those who might have access to the data but don't work on it (e.g., janitors)
