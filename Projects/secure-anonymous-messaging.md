---
layout: project
title: Secure Anonymous Messaging System | Open Source Contribution
description: Steganographic communication platform disguised as an e‑commerce site with time‑limited decryption and decoy content for operational security.
category: Security Tools
status: Deployed (select details redacted)
date: 2025-11-10
permalink: /projects/secure-anonymous-messaging/
tags: [Security, Steganography, Crypto, Privacy, Zero‑Footprint]
---

## Overview

The Secure Anonymous Messaging System is a steganographic communication platform designed specifically for individuals in life‑threatening situations, particularly women experiencing domestic violence. Disguised as an innocuous e‑commerce returns workflow, the system enables secure, undetectable communication while maintaining complete operational security.

This project was developed as an open‑source contribution and had a real‑world deployment that **prevented harm** in a domestic violence case. The system's design prioritizes zero digital footprint, time‑limited access, and plausible deniability — critical features for victims who may have their devices monitored or inspected by abusers.

## System Design

### E‑Commerce Returns Disguise

The system presents itself as a standard product returns portal:

- **Innocuous Appearance**: Looks like a typical returns tracking website
- **Plausible Cover Story**: Viewing "return details" is the expected behavior
- **Normal Browser History**: Leaves only benign e‑commerce‑related traces
- **No Special Apps**: Works through standard web browsers, requiring no suspicious downloads

### Per‑Message Unlock Window

Messages are only accessible for a strictly limited time:

- **10‑Second Window**: Once unlocked, messages display for exactly 10 seconds
- **No Screenshots**: Technical and social measures discourage capture
- **Automatic Deletion**: Message access is revoked after the window expires
- **Single Unlock**: Each message can only be unlocked once per time period

### Encrypted Storage with Decoy Text

Multiple layers of protection:

- **End‑to‑End Encryption**: Messages encrypted before storage
- **Steganographic Embedding**: Real messages hidden within innocuous text
- **Decoy Content**: Plausible fake messages if forced to reveal access
- **Key Derivation**: Access keys derived from innocuous‑looking identifiers

### Zero Digital Footprint

Designed to leave minimal traces:

- **No Account Required**: No registration, login, or personal information
- **Browser‑Only**: No apps, no installed software, no persistent storage
- **Minimal Metadata**: Stripped headers and timing information
- **Ephemeral Sessions**: Sessions expire rapidly with no persistent state

## Technical Architecture

### Steganographic Layer

Messages hidden using multiple techniques:

- **Text Steganography**: Messages embedded in innocuous carrier text
- **Linguistic Patterns**: Maintains natural language patterns in carrier text
- **Multi‑Level Encoding**: Multiple encoding layers for defense in depth
- **Adaptive Hiding**: Adjusts technique based on message length and sensitivity

### Cryptographic Protections

Strong encryption throughout:

- **AES‑256 Encryption**: Industry‑standard symmetric encryption
- **Perfect Forward Secrecy**: Compromise of one message doesn't affect others
- **Key Derivation**: PBKDF2 with high iteration counts
- **Authenticated Encryption**: AEAD schemes to prevent tampering

### Time‑Limited Access Control

Enforcing the 10‑second window:

- **Server‑Side Timing**: Authoritative server controls message availability
- **Token Expiration**: Access tokens expire precisely on schedule
- **Client Enforcement**: JavaScript ensures UI compliance
- **Anti‑Bypass**: Multiple layers prevent circumventing time limits

### Decoy System

Plausible alternative content:

- **Decoy Messages**: Realistic but fake messages if compromised
- **Decoy Keys**: Separate key reveals innocuous content
- **Consistent Context**: Decoys match the e‑commerce cover story
- **Indistinguishable**: Cannot determine which content is real without correct key

## Use Case: Domestic Violence Support

### Problem Context

Domestic violence victims face unique communication challenges:

- **Device Monitoring**: Abusers may check phones, browsers, and messages
- **Physical Access**: Abusers may demand to see device contents
- **Limited Privacy**: Victim may have little time alone with devices
- **Safety Risk**: Discovery of help‑seeking could escalate danger

### Solution Features

The system addresses these specific threats:

- **Undetectable Communication**: Appears as normal e‑commerce activity
- **Time Pressure Compatible**: 10‑second window works with limited privacy
- **Forced Disclosure Protection**: Decoy system provides cover story
- **No Evidence Trail**: Minimal browser history, no installed apps
- **Immediate Access**: No registration process that could be discovered

### Real‑World Deployment

In the documented case:

- Victim able to coordinate with support services
- Communication remained undetected by abuser
- Victim successfully exited dangerous situation
- System facilitated connection with shelter and legal resources

The deployment **prevented harm** by enabling communication that would have been impossible through conventional channels.

## Ethics & Safety

### Responsible Design

Ethical considerations guided every design decision:

- **Harm Prevention**: Primary goal is preventing physical harm
- **User Safety**: Features prioritize user physical safety over convenience
- **No False Promises**: Clear about capabilities and limitations
- **Documentation**: Training materials for safe usage
- **Rapid Response**: Quick deployment when safety is time‑critical

### Limitations & Risks

Users must understand the system's boundaries:

- **Not Perfect Security**: No system provides absolute protection
- **Physical Safety First**: Technology is only one component of safety planning
- **Professional Support**: Must be used in conjunction with professional DV resources
- **Context Dependent**: Effectiveness varies with specific threat model
- **Regular Updates**: Security requires ongoing maintenance and updates

### Coordinated Support

Technology works best with holistic support:

- **DV Professionals**: Coordination with domestic violence experts
- **Legal Resources**: Connection to legal aid and protection orders
- **Shelter Networks**: Integration with emergency housing resources
- **Safety Planning**: Used as part of comprehensive safety plan
- **Follow‑Up**: Continued support after initial crisis resolution

## Technical Highlights

### Implementation Considerations

Key technical challenges and solutions:

- **Timing Precision**: Reliable 10‑second enforcement across different devices
- **Steganographic Quality**: Carrier text must appear naturally written
- **Performance**: Fast encryption/decryption even on older devices
- **Browser Compatibility**: Work across all common browsers without plugins
- **Offline Resilience**: Some functionality available without connectivity

### Security Measures

Defense‑in‑depth approach:

- **Multiple Encryption Layers**: Redundant protections against different attack vectors
- **Anti‑Forensics**: Minimizes recoverable artifacts on device
- **Traffic Analysis Resistance**: HTTPS with traffic pattern obfuscation
- **Timing Attack Mitigation**: Constant‑time operations where critical
- **Memory Safety**: Careful buffer handling to prevent exploitation

## Image

<img src="/assets/secure-anon/return-details.png" alt="Returns Portal Interface" style="max-width: 100%; border-radius: 10px; margin: 1rem 0;">

*Note: The system interface is designed to look like a standard e‑commerce returns portal.*

## Important Notes

### Deployment Details

For safety and operational security reasons:

- **Selective Disclosure**: Full technical details available only to vetted parties
- **Responsible Use**: System intended exclusively for legitimate safety applications
- **No Public Instance**: No publicly accessible deployment to prevent misuse
- **Professional Deployment**: Requires coordination with DV service organizations

### Getting Involved

If you're a domestic violence services organization or security professional interested in this work:

- **Ethical Use Only**: Clear commitment to harm prevention
- **Professional Context**: Operating within established DV support frameworks
- **Security Vetting**: Appropriate security clearance and background
- **Responsible Disclosure**: Agreement to protect sensitive details

## Lessons Learned

### Technical Lessons

- **Simplicity Matters**: Complex systems are harder to use under stress
- **Time Constraints**: Real‑world usage has severe time limitations
- **Cover Story**: Technical excellence means nothing without believable cover
- **User Testing**: Must test with real users in realistic conditions

### Design Lessons

- **Threat Model First**: Every feature must address specific threat
- **User Safety Primary**: Usability serves safety, not vice versa
- **Failure Modes**: Design for graceful, safe failures
- **Operational Security**: Technical security is only part of the solution

### Impact Lessons

- **Technology Enables**: Tech can enable outcomes impossible otherwise
- **Not Sufficient**: Technology alone doesn't solve safety problems
- **Coordinated Approach**: Most effective as part of broader support
- **Measurable Impact**: Clear case of technology preventing harm

---

## A Note on Impact

This project demonstrates that thoughtful application of security and privacy technology can have direct, measurable impact on human safety. The successful deployment that prevented harm in a domestic violence case validates the design approach and motivates continued work in this space.

Technology built with clear ethical purpose and deep understanding of user threat models can be a force for genuine good. This project stands as an example of security engineering in service of human safety.

---

*Select technical details of this system are not publicly disclosed to protect operational security. Serious inquiries from domestic violence service organizations or security professionals may contact for additional information.*
