# Intro to NIST 800-171
## DFARS review
`NIST 800-171` - The framework that helps manufacturers comply with DFARS. 

`DFARS 7012` and `7020` - for all DoD solutions contracts, task orders, or deliver orders. 
* "Flow down" - subcontractors need to be in compliance with DFARS
* Covered Defense Information (CDI) - resides on or is transmitted on internal info on the network.
  * Mandatory to report cyber events
  * Submit malicious software discovered and isolated in connection with a reported Cyber incident to the DOD Cyber Crimes Center
  * Submit media and info to support the damage assessment

## Key terms
Covered Defence Information: 
* Controlled Unclassified Information (CUI) - [definition] requires safeguarding or dissemination controls with laws/regs/gov. policies and:
  * Marked or otherwise identified in the contract, task order, or delivery order and provided to the contractor by or on behalf of DoD in support of the performance of the contract; or
  * Collected, developed, received, transmitted, used, or stored by or on behalf of the contractor in support of the performance of the contract.
* Federal Contract Information (FCI): Info given/created by the government not for public release.
* `NIST 800-171` - A subset of `NIST 800-53` for CIA (confidentiality, availability, and integrity) of CUI in nonfederal systems
  * Federal systems are FISMA/RMF
* `Non-federal Organization` (NFO) - An entity that owns, operates or maintains nonfederal info systems. Need to be compliant with NIST `800-171`
  * Federal contractors
  * State/local/tribunal govs.
  * Colleges/Universities

## Understand Controlled Unclassified Information (CUI)
Controlled Unclassified Information (CUI):
* Requires safeguarding/dissemination controls but not under `EOCNSI` (`Executive Order Classified National Security Information`), any predecessor or successor order, or `The Atomic Energy Act of 1954`. (`Executive Order 13556`)
* not secret - but still not public information
* Can be found in basically any information
  * **CDI and FCI are both types of CUI.**

Types of CUI:
* Basic: Basic handling and dissemination controls in `Final Rile` by NARA.
  * FISMA requires that CUI Basic be protected at the FISMA Moderate level and can be marked as either CUI or Controlled.
* Specified: a subset of CUI where the authorizing law, policy, or regulation puts more restrictive controls on the handling and control of the CUI-specified content

CUI Examples: 
* Agriculture
* Critical infastructure
* port control
* Financial
* systems vulnerability info
* Legal
* nuclear
* Privacy
* Acquisition
* Business info
* tax
* Transit

## How we got to NIST 800-171
CUI History: Different agencies are having issues with nation-states and this is the government's attempt to protect CUI. 
* Started with `Executive Order 13556` for Executive branch CUI
  * 10/01/2010 - how the government handles unclassified info
  * `National Archives and Records Administration` (`NARA`) - in charge of implementing the CUI program
  * US archivist dedicated responsibilities to `ISOO` (`Information Security Oversite Office`)
* CUI Registry: Federal CUI rule - 23 CFR Part 2002 - gov. wide controls for CUI
  * Info, guidance, and policy for CUI
  * Issues categories and sub-categories
  * Procedures for protecting CUI
* `DFARRS 252.204.7008` requires compliance with `NIST 800-171`
  * Requires "adequate security" and defines minimum protections being `NIST 800-171`
  * `NIST 800-171` was a self-assessment - not good enough leading to CMMC
  * Says need to know compliance and provide notice of things not in compliance. 
* `Nist 800-171` requires protecting CUI

## NIST 800-171 Applicability, Scoping and Requirements:
Non-federal orgs. with non-federal connections that do have CUI
* NOT required for orgs. without CUI

Assumptions:
* Requirements for the protection of CUI are consistent (federal or nonfederal)
* Safeguards are implemented to protect CUI
* Confidentiality impact value for CUOI is not lower than 'moderate' in accordance with FIPS Publication 199

Assumptions for NFOs
* Have information technology infrastructures currently in place and are not developing or acquiring systems specifically for CUI
* Have safeguards in place which may be sufficient to satisfy the CUI requirements
* May not satisfy every CUI requirement, but can implement equally effective alternatives
* Can implement a variety of potential security solutions directly or through the use of managed services

Requirement: 
* 110 controls - 14 families
* `FIPS` and `NIST 800-53` to eliminate requirements that are:
  * Just for federal information systems
  * Not just for protecting CUI
  * Should be satisfied with NFOs without specification
* Some controls are technical, and some are administrative
* There is some flexibility with variance from the requirements - Process to deviate if N/A

## Body of evidence
Body of Evidence (BOE): deliverables proving compliance - three items:
* Organizational Policy or Procedure - enforceable P&P by laws and HR
* System Security Plan (SSP) - develop, document, and update security to ensure compliance
* Plan of Actions and Milestones (POAM) - process for being in control (when not in compliance with a specific control) and action plan to reduce vulnerabilities - timeline for accomplishing lacking controls.

Scoping: 
* Isolate CUI which can help with compliance of just some systems on the network.
* Best response: Having people to oversee control and P&P to identify the workflow and controls

Resources
* `FISMA`
* `DFARS`
* `NIST 800-53`
* `NIST 800-171`
* `NARA`
* `FIPS 200`
* `FIPS 199`
* `32 CFR` - `Federal CUI Rule`


# Understanding NIST 800-171 Controls
