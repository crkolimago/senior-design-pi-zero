import io
import picamera
from gpiozero import Button

TIME = 5

button = Button(14)

camera = picamera.PiCamera()
stream = picamera.PiCameraCircularIO(camera, seconds=TIME) # e.g. at t=TIME+1 t=0 will be deleted
camera.start_recording(stream, format='h264')

seconds = 0

try:
    while True:
        print('recording for %d' % seconds)
        seconds += 1
        camera.wait_recording(1)
        if button.is_pressed:
            print('button pressed recording for %d more seconds' % TIME)
            camera.wait_recording(TIME)
            stream.copy_to('motion.h264')
            camera.stop_recording()
            print('recording stopped')
            camera.close()
finally:
    camera.stop_recording()
    print('recording stopped')
    camera.close()
