# 🎣 Phishing Email Investigation Lab
![Attack](https://img.shields.io/badge/Attack-Phishing-red)
![Language](https://img.shields.io/badge/Language-Python-yellow)
![Protocol](https://img.shields.io/badge/Protocol-SMTP-lightgrey)
![Status](https://img.shields.io/badge/Status-Completed-success)


<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=00FF00&size=24&center=true&vCenter=true&width=600&lines=Phishing+Email+Investigation;SMTP+Email+Simulation;SOC+Analysis+Project" />
</p>

<p align="center">
  <img src="https://threatcop.com/blog/wp-content/uploads/2022/05/phishing-phisher.gif" width="550"/>
</p>

## 📌 Objective

To simulate and analyze a phishing email attack using a controlled lab environment.

## 🛠 Lab Setup

* Attacker: Kali Linux
* Victim: Windows 11
* Email Service: Gmail SMTP

## ⚙️ Tools Used

* Python (smtplib)
* VirusTotal
* Web Browser

## 🪜 Steps Performed

1. Created attacker and victim Gmail accounts
2. Generated App Password for SMTP
3. Developed Python script to send phishing email
4. Sent email from Kali Linux
5. Received email on Windows 11
6. Analyzed email content and link
7. Extracted Indicators of Compromise (IOCs)

## 🚨 Indicators of Compromise

* Email: [it.adminsupport2@gmail.com](mailto:it.adminsupport2@gmail.com)
* URL: http://213.209.159.159/google-login
* IP: 213.209.159.159

## 🔍 Key Findings

* Spoofed email address
* Suspicious IP-based URL
* Urgent call-to-action
* Social engineering techniques

## ✅ Conclusion

The email was identified as a phishing attempt based on multiple indicators and analysis.

## 📸 Evidence

### 📧 Email Received

![Email Received](screenshot/email_received.png)

### 🔗 Email Content

![Email Content](screenshot/email_content.png)

### 🌐 VirusTotal Analysis

![VirusTotal](screenshot/virustotal.png)

### 📑 Header Analysis

![Header Analysis](screenshot/header_analysis.png)

