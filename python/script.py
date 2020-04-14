import spidev
import time
import board
import neopixel

import io
import picamera
from subprocess import call

import requests

import busio
import adafruit_lsm9ds1
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

pixels = neopixel.NeoPixel(board.D12, 60)

#Define Variables
delay = 0.1
pad_channel = 0
max_seconds = 30
camera_delay = 10 # final seconds will be [(max_seconds - camera_delay) + camera_delay]

#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz=1000000

spi2 = spidev.SpiDev()
spi2.open(1, 0)
spi2.max_speed_hz=1000000

# initialize camera
camera = picamera.PiCamera(framerate=24)
stream = picamera.PiCameraCircularIO(camera, seconds=max_seconds)
camera.start_recording(stream, format='h264', intra_period=24)

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

def h264_to_mp4():
    command = "rm crash.mp4"
    call([command], shell=True)
    command = "MP4Box -add crash.h264 crash.mp4"
    call([command], shell=True)

def main():
    try:
        while True:
            camera.wait_recording(0.1)

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

                r = requests.get('http://13.59.245.151:3031/crashfrompi')
                print(r.text)

                # send signal to iphone here???

                false_alarm = False # signal from iphone, currently does nothing
                save_video = True
                for i in range(camera_delay*10): # continue recording for camera_delay seconds
                    camera.wait_recording(0.1)
                    # check for signal from iphone here???
                    if false_alarm:
                        save_video = False
                        led_off()
                        break # takes us back to main while True loop
                
                if save_video:
                    stream.copy_to('crash.h264')
                    h264_to_mp4()
                    break # takes us to finally block
    finally:
        led_off()
        camera.stop_recording()
        camera.close()

main()
