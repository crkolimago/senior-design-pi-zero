import io
import picamera

TOTAL_TIME = 30
AFTER_EVENT = 10

camera = picamera.PiCamera()
stream = picamera.PiCameraCircularIO(camera, seconds=TOTAL_TIME) # e.g. at t=TOTAL_TIME+1 t=0 will be deleted
camera.start_recording(stream, format='h264')

seconds = 0

# stores TOTAL_TIME seconds in memory, when event is detected overwrites 
# the first AFTER_EVENT seconds so the result is [TOTAL_TIME-AFTER_EVENT, AFTER_EVENT]

try:
    while True:
        print('recording for %d' % seconds)
        camera.wait_recording(1)
        if seconds == 40:
            print('event detected at %d seconds' % seconds)
            camera.wait_recording(AFTER_EVENT)
            seconds += 10
            stream.copy_to('motion.h264')
            break
        seconds+=1
finally:
    camera.stop_recording()
    print('recording stopped at %d seconds' % seconds)
    camera.close()
