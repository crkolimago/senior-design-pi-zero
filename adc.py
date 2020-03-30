#!/usr/bin/python

import spidev
import time

#Define Variables
delay = 0.5
pad_channel = 0

#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz=1000000

spi2 = spidev.SpiDev()
spi2.open(0, 1)
spi2.max_speed_hz=1000000

def readadc(adcnum):
    # read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

def readadc2(adcnum):
    # read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi2.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data
try:
    while True:
        pad_value = readadc(pad_channel)
        pad_value2 = readadc2(pad_channel)



        if pad_value > 700: 
            print("---------------------------------------")
            print("Pressure Pad  1 Value: %d" % pad_value)
        if pad_value2 > 700: 
            print("---------------------------------------")
            print("Pressure Pad 2 Value: %d" % pad_value2)
        time.sleep(delay)
except KeyboardInterrupt:
    pass