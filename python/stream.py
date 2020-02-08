import picamera
from gpiozero import Button

RECORD_TIME = 10
STREAM_TIME = 2

seconds = 0

button = Button(14)

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    with picamera.PiCameraCircularIO(camera, seconds=STREAM_TIME) as stream:
        camera.start_recording(stream, format='h264')

        print('INFO: Recording for %d seconds' % RECORD_TIME)

        while seconds < RECORD_TIME:
            print('t=%d' % seconds)
            camera.wait_recording(1)

            if button.is_pressed:
                print('EVENT: button press')
                print('INFO: saving t=[%d-%d]' % (seconds-STREAM_TIME, seconds))
                camera.split_recording('after.h264')
                stream.copy_to('before.h264', seconds=2)
                stream.clear()
                print('INFO: saving t=[%d-%d]' % (seconds, seconds+STREAM_TIME))
                seconds += STREAM_TIME
                camera.wait_recording(STREAM_TIME)
                camera.split_recording(stream)
                print('INFO: returning to stream')

            seconds += 1
        
        camera.stop_recording()

