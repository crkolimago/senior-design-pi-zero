#!/usr/bin/python

import spidev
import time
import board
import neopixel

import busio
import adafruit_lsm9ds1
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)


pixels = neopixel.NeoPixel(board.D12, 60)

#Define Variables
delay = 0.1
pad_channel = 0

#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz=1000000

spi2 = spidev.SpiDev()
spi2.open(1, 0)
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
def led_on():
    pixels.fill((255,0,0))

def led_off():
    pixels.fill((0,0,0))

try:
    while True:
        pad_value = readadc(pad_channel)

        pad_value2 = readadc2(pad_channel)

        accel_x, accel_y, accel_z = sensor.acceleration
        accel_x =  0.10197162129779 * accel_x
        accel_y =  0.10197162129779 * accel_y
        accel_z =  0.10197162129779 * accel_z
        accel_vect = (accel_x**2 + accel_y**2+ accel_z**2)**.5
        if accel_vect > 2 or pad_value > 800 or pad_value2 > 800: 
            print("_____________CRASH DETECTED_____________"+str(accel_vect))
            led_on()

        time.sleep(delay)
except KeyboardInterrupt:
    led_off()