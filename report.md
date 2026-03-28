# Phishing Email Investigation Report

## 1. Overview

This project simulates a phishing attack and analyzes its characteristics.

## 2. Environment

* Attacker: Kali Linux
* Victim: Windows 11

## 3. Email Details

* Sender: [it.adminsupport2@gmail.com](mailto:it.adminsupport2@gmail.com)
* Receiver: [mitnick.user@gmail.com](mailto:mitnick.user@gmail.com)
* Subject: Critical Security Update Required

## 4. Analysis

### 4.1 Sender Analysis

The sender email mimics a legitimate service but contains subtle differences.

### 4.2 URL Analysis

The email contains an IP-based URL (213.209.159.159), which is uncommon for legitimate services.

### 4.3 VirusTotal Analysis

The URL was analyzed and appeared clean, indicating lack of reputation data.

### 4.4 Header Analysis

Email headers were reviewed to trace the origin and authentication path.

## 5. Phishing Indicators

* Spoofed sender email
* Use of IP address instead of domain
* Urgent language
* Call-to-action button

## 6. Conclusion

The email demonstrates typical phishing characteristics and was successfully identified.

## 7. Recommendations

* Verify sender identity
* Avoid clicking suspicious links
* Use email filtering tools
* Educate users on phishing awareness
