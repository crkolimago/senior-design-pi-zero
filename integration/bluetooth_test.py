import os
import subprocess
from bluetooth import *


def main():
    print("Hello there")

    print("performing inquiry...")

    nearby_devices = discover_devices(lookup_names = True)

    print("found " + str(len(nearby_devices)) + " devices")

    my_name='B0:19:C6:64:EC:91' # matts iphone
    my_name='A4:83:E7:A6:7D:0B' # 3MC02ZC4RULVDR

    for name, addr in nearby_devices:
        print(addr + ", " + name) 
        if addr == "3MC02ZC4RULVDR":
            my_name = name
            print("Found computer!")

    shellpath = os.path.abspath("transfer.sh")
    subprocess.call([shellpath + " " + my_name + ' test2.txt'], shell=True)

if __name__ == "__main__":
    main()
