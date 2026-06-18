import pywifi
import time
import os

os.system('')

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

def clear_terminal():
    print("\033[H\033[2J", end="", flush=True)

clear_terminal()

while True:
    iface.scan()

    time.sleep(4)
    resaults = iface.scan_results()

    for network in resaults:
        print(network.ssid, network.signal)

    time.sleep(4)

    clear_terminal()
