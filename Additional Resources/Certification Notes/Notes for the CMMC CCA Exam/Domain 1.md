Domain 1: Task 1
	• Logical versus physical locations
		○ When studying look for the learning objectives
		○ How to access the data
			§ Is the data on site? Remove? Hybrid? 
			§ OSEs are moving a lot to the cloud to have less responsibilities. 
			§ When things are on prem - there is more challenging for users to protect as it's all their responsibilities.
		○ Can put limitations on location. 
			§ E.g., all local, on-prem CUI is restricted to one room with a specific dedicated system(s). 
			§ When checking for data is the desktop a thin client (just being used to access data) or is there CI on the specific device. 
			§ Physical protections need to be implemented for encrypted devices. 
			§ The assessor doesn't ever need access to the CUI - just evidence that the controls for the CUI are in place. 
			§ The OSE should show the configurations for their virtual desktop infrastructure (VDI)
		○ For the exam: all certifications need to go in person for certifications. (out of date)
		○ For virtualization: there's always a hypervisor in place for VMs. 
			§ The application and the VM's OS are installed on top of the hypervisor. 
		○ When people access the CUI from whatever location they then need to have access controls specifying how to access things. (no matter where people are if remote).
			§ There always need to be safeguards, including physical security in place.
				□ These can be different depending on location, in person/remote/etc.

	○ System Architecture:
		○ Security engineering - Employ architectural designs, software development techniques, and systems engineering principles that promote effective information security within organizational systems.
		○ OSCs should establish architecture that combines on-prem and external controls.
		○ OSCs should give network maps, and also physical maps
			§ OWASP and NIST have information on critical security controls and what secure designs consist of. 
			§ CISCO has information about floor plans and logical plans for security. 
		○ Backups need to be secured (if they include CUI)
			§ There is no requirement to have backups
			§ Just having the backups "encrypted" is not good enough
			§ It needs to be fed ramp protected (moderate environment) if off-prem 
		○ OWASP, NIST SP 800-160 v1 Appendix F, and other controls have 50+ different implementations for security controls
			§ Not all are needed. Pick ones that are already in place and use this for system engineering principles. 
		○ Subnets:
			§ Implementing VLANs and/or DMZs for "enclaves" are important to segment parts of the network containing the CUI information. 
			§ Using this segments this from public/"more open" networks. 
			§ Micro-segmentation - a firewall with per-device rules can segment specific devices. 
			§ Zero-trust: every device on the network doesn't trust other devices and re-validates them after every use. 
				□ For all of these, need to see evidence for the network segmentation via firewall configurations or similar implementations. 

	○ Change Restrictions:
		○ Access Restrictions for Changes: Define, document, approve and enforce physical and logical access restrictions associated with changes to organizational systems.
		○ OSCs need to defined, document, approve, and enforce physical access restrictions. 
		○ OSCs also need logical access controls
			§ E.g., locked doors, man traps, secure areas, RBAC, configuration change board, etc.
			§ For small companies they need to have documentation for changes (e.g., sending themselves and email) where they document the change and note that they test for security considerations. 
		○ There needs to be access controls for maintenance
			§ There needs to be controls and tools in place for system being maintained
			§ e.g., locks, escorts, monitoring, testing for software used by the people testing. 

	○ In-scope CMMC assets:
		○ Controlled Unclassified Information Assets
		○ Security Protection Assets
		○ Contractor Risk Managed Assets
		○ Specialized Assets
		○ Anything that controls, manages, or stores CUI.
			§ Something like a firewall can fit into multiple categories.
			§ Can manage some things without a barrier, however, this makes it a lot harder to define the scope of the items that are in/out of scope.
		○ CUI asset documentation includes:
			§ Documented in asset inventory
			§ Documented in the System Security Plan
			§ Documented in network diagrams
			§ Included in scoping discussions
		○ Security protection assets can include people, tech, or the facility. 
			§ If using a managed service provider, needs to know the people, tech, and facility of the items there. 
			§ MSPs (managed service providers) need an SLA for their people to make sure they are trained for handling CUI
				□ MSPs then give an attestation that they have fulfilled the specific requirements (e.g., training, background check, software, etc.)
		○ Contractor Risk Managed Assets:
			§ Are part of the CMMC Assessment Scope.
			§ Managed using the contractor's risk-based information security policy, procedures, and practices.
			§ Not assessed against CMMC practices.
			§ Capable of, but are not intended to process, store, or transmit CUI.
			§ Not required to be physically or logically separated from CUI Assets.
				□ For version 2.0, this is not directly specified. 
		○ Contractor Risk Managed Asset Documentation:
			§ This can include an SSP with a list of approved people/tech/assets/etc.
		○ Companies need to have policies dating back to November 10th (the implementation of CMMC)
			○ If not, the controls are not adequate and can be marked not complete. 
			○ If they don't have this, they are "defrauding the government" 
		○ Specialized Assets:
			§ Asset
				□ Government Property
				□ Property owned or leased by the government
			§ IoT or Industrial Internet of Things (IIOT)
				□ Interconnected devices, physical or virtual, in the digital world
			§ Operational Technology (OT)
				□ Programmable logic controllers (PLCs), computerized numerical control (CNC) devices, machine controllers, fabricators, assemblers, and machining
			§ Restricted Information Systems
				□ Systems that are configured based on government requirements
			§ Test Equipment
				□ Used in the testing of products, system components, and deliverables
		○ Out of Scope:
			§ Assets that cannot process, store, or transmit CUI
		○ Professional vs Industrial:
			§ Professional - office environments, 
			§ Industrial - manufacturing Environments
			
			§ System inventory
				□ Developing a system baseline - Establish and maintain baseline configurations and inventories of organizational systems [including hardware, software, firmware and documentation] throughout the respective system development life cycles.
				□ OSCs need configurations for hardware, software, firmware, and documentation. 
				□ OSCs need to establish an inventory
				□ OSCs need to maintain and document a hardware lifecycle. 
				□ There is no specific clarification between which this have to be Professional vs Industrial
				□ Documenting what's in the enclave or not (if possible)
			§ Placement within the network
				□ Need to know who exact is accessing specific devices and information
				□ People actions need to be trackable in audit logs. 
				□ Both need inventory, maintained, life cycle, configuration, etc.
			§ System and system elements
				□ Systems, tech, machines, human elements, and physical/environmental elements. 
				□ Interconnections between all elements including things not controlled (e.g., updates from a 3rd party).
				□ Need access to an "enabling system" (e.g., severs, people, workstations, things that "you" can control.)
				□ Making sure there is an "environment of operation" 
			§ Architecture Definition Process:
				□ The purpose of the Architecture Definition process is to generate system architecture alternatives, to select one or more alternative(s) that frame stakeholder concerns and meet system requirements, and to express this in a set of consistent views.
				□ This process is synchronized with the System Requirements Definition and Design Definition processes.
				□ This then uses these requirements (on the test):
					® AR-1 Prepare for architecture definition from the security viewpoint
					® AR-2 Develop security viewpoints of the architecture
					® AR-3 Develop security models and security views of candidate architectures
					® AR-4 Relate security views of the architecture to design
					® AR-5 Select candidate architecture
					® AR-6 Manage the security view of the selected architecture
					
		○ Single and Multi-site constraints and Evidence:
			§ Remove access requirements, external connections, alternative work sites, session termination.
			§ If someone takes things home, then the home is in scope. 
				□ CAP 5.6.1 (old) - means there will be a lot of traveling for this.
				□ CAP 2.0 (new) - allows the OSE and C3PAO to know what's "appropriate and necessary"
					® Still sort of expects these things to be tested in person.

	· Remote Access Requirements - need to control and monitor remote access
		○ If CUI is in the cloud, then accessing it is in the cloud.
		○ There a difference between FIPS "validated" and FIPS "compliant" 
		○ Encrypted access/VPN is still "remote access"
			§ No alternative info for data in motion across TCP/IP networks.
		○ Ensure confidentiality between sites (VPN/RDP logs)
		○ Policy identifies when remote access is permitted and acceptable methods (written policies)
		○ Remote access sessions are controlled
		○ Remote access sessions are monitored
		
		○  Need to show all external connections - then limit the external information systems. 
			§ E.g., are people able to access Facebook? LinkedIn? Etc.? 
		○ Need to provide network architecture diagrams and VPN connections.
	 
		○ Alternative work sites:
			§ Make a list of all the connections and worksites, then make a list of all the safeguards for these
				□ Should be different for in person vs remote work
				□ If remote work is allowed, then there need to be specific policies, diagrams, and information for this specifically. 
			§ Can be physical or logical connections.  
	
	· External connections - identify and document all external connections
		○ Establish secure connections - logons require Id, password, should also for CUI access MFA (at all times)
		○ Specific network requirements (e.g., VPNs)
		○ Biophysical controls. 
		○ Show the assessor event logs to show this is being tracked. 
		○ OSE can permit remote access - need policy and configurations
		○ Need to be FIPS 140-2 / FIPS 140-3 Validated Encryption, otherwise to be treated like unencrypted.
			§ NIST Cryptographic Module Validation Program (CMVP)
			§ Cryptographic and Security Testing Laboratories (CSTL)

		○ Co-located data centers - limited ability to implement security controls not managed by ESP
		○ Security Operations Centers (SOCs)
			§ OSC owned - Requires trained staff 24x7x365 and capital investment
			§ ESP owned - Limited ability to implement security controls
		○ Contractor office buildings
			§ OSC owned - Requires trained staff 24x7x365 and capital investment
			§ Leased - Limited ability to implement security controls and secure network architecture
		○ Out-of-Scope Assets
			§ Cannot process, store, or transmit CUI or are inherently unable to do so
			§ Do not provide security protections to CUI assets
			§ Are outside of the CMMC Assessment Scope
			§ Are not part of the CMMC assessment engagement
			§ Are physically or logically separated from CUI assets
			§ Are not evaluated per applicable CMMC practices
			§ Do not have documentation requirements
		○ 
