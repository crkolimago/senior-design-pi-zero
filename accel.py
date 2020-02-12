import board
import time
import busio
import adafruit_lsm9ds1
import math

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)


def get_accel(accel_x,accel_y,accel_z):
    return math.sqrt( accel_x**2 + accel_y**2 + accel_z**2)

while True:
    # Read acceleration, magnetometer, gyroscope, temperature.
    accel_x, accel_y, accel_z = sensor.acceleration
    #mag_x, mag_y, mag_z = sensor.magnetic
    #gyro_x, gyro_y, gyro_z = sensor.gyro
    #temp = sensor.temperature
    # Print values.
    accel = get_accel(accel_x,accel_y,accel_z)
    
    print('Acceleration (m/s^2): ({0:0.3f})'.format(accel))
    print('Force normalized (g): ({0:0.3f})'.format(accel/9.8))
    #print('Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(mag_x, mag_y, mag_z))
    #print('Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(gyro_x, gyro_y, gyro_z))
    #print('Temperature: {0:0.3f}C'.format(temp))
    # Delay for a second.
    time.sleep(1.0)