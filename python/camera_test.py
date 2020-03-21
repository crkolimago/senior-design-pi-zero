import io
import picamera
import time

TOTAL_TIME = 40

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.framerate = 24
    time.sleep(2)

    ring_buffer = picamera.PiCameraCircularIO(
            camera, seconds=10, bitrate=1000000)

    camera.start_recording(
            ring_buffer, format='h264', bitrate=1000000,
            intra_period=24)
    seconds = 0
    try:
        print('recording')
        while seconds < TOTAL_TIME:
            camera.wait_recording(1)
    finally:
        camera.stop_recording()
