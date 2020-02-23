import board
import time
import busio
import adafruit_lsm9ds1
import matplotlib.pyplot as plt 
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

try:
    data_x = []
    data_y = []
    data_z = []


    start_time = time.time()
    while True:
        # Read acceleration, magnetometer, gyroscope, temperature.
        #f = open("results.txt", "a")
        accel_x, accel_y, accel_z = sensor.acceleration
        accel_x =  0.10197162129779 * accel_x
        accel_y =  0.10197162129779 * accel_y
        accel_z =  0.10197162129779 * accel_z

        data_x[time.time()-start_time] = accel_x
        data_y[time.time()-start_time] = accel_y
        data_z[time.time()-start_time] = accel_z
        
        #mag_x, mag_y, mag_z = sensor.magnetic
        #gyro_x, gyro_y, gyro_z = sensor.gyro
    #temp = sensor.temperature
        # Print values.
       # print('Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(accel_x, accel_y, accel_z))
        #print('Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(mag_x, mag_y, mag_z))
        #print('Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(gyro_x, gyro_y, gyro_z))
        #print('Temperature: {0:0.3f}C'.format(temp))
        # Delay for a second.
        time.sleep(.1)
except:
    plt.plot("time","accel(g's)",data = data_x)
    plt.show()
    plt.plot("time","accel(g's)",data = data_y)
    plt.show()
    plt.plot("time","accel(g's)",data = data_z)
    plt.show()
    #f.close()
