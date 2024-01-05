import scapy.all as scapy
import argparse
import pyfiglet

def Get_Elements():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="IP address Range / Network Address  With Mask /8 , /16 ,/24 , /32 \n Example 192.168.1.0/24")
    options = parser.parse_args()
    if not options.target:
        parser.error("[!!] Please specify a target IP address range or Use --help for more information.")
    return options

def Scan(ip):
    arp_Request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_Request_broadcast = broadcast / arp_Request
    answered_List = scapy.srp(arp_Request_broadcast, timeout=1, verbose=0)[0]
    devices_List = []
    for element in answered_List:
        devices_Dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        devices_List.append(devices_Dict)
    return devices_List

def Display_Result(result_List):
    print("IP \t\t\t Mac Address \n ------------------------------------------- ")
    for device in result_List:
        print(device["ip"] + "\t\t" + device["mac"])


if __name__ == "__main__":
    banner = pyfiglet.figlet_format("QuestorNet")
    print(banner)
    options = Get_Elements()
    scanResult = Scan(options.ip)
    Display_Result(scanResult)
