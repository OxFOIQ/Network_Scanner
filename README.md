# QuestorNet


QuestorNet is a Python-based utility designed for discovering devices within a specified IP range on a local network. This tool utilizes the Scapy library to send ARP requests and collects responses, providing information about active devices including their IP addresses and MAC addresses.

## Features
IP Range Scanning: Scan a specified IP range to discover active devices on the network.

ARP Requests: Use ARP (Address Resolution Protocol) requests to obtain IP-MAC address mappings.

Simple and Fast: The tool is lightweight and offers quick network discovery with minimal setup.

Output Formatting: Display results in a clear and organized format, making it easy to identify devices on the network.

Customizable: Easily integrate the tool into other projects or scripts, adapting it to specific use cases.


## Usage
Install the required dependencies:
* pip install pyfiglet
* pip install scapy
* Run the tool with the desired IP range : 
- python network_discovery.py 192.168.1.0/24
- Replace 192.168.1.0/24 with the target IP range.


## Example Output

IP               MAC Address
-----------------------------------
192.168.1.1      00:1a:2b:3c:4d:5e
192.168.1.10     08:76:5a:4b:3c:2d
192.168.1.20     2c:5e:1d:3a:4b:6f



## Contributions

Contributions are welcome! If you have ideas for improvements, feature requests, or bug reports, please open an issue or submit a pull request.
