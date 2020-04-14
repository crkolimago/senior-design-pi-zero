import io
import picamera

# 30, 10, 40

TOTAL_TIME = 10
AFTER_EVENT = 5

def main():
    """
    FAQ 5.13 Why is playback too fast in VLC? VLC framerate is different from Pi's - no fix as of 1 hr of searching
    FAQ 5.11 Why is there more than x seconds in circular buffer? seconds is a lower bound, if the recorded scene 
    has low motion the stream can store more than the specified seconds - not necessarily an issue if we
    say this
    """

    camera = picamera.PiCamera(framerate=24)
    stream = picamera.PiCameraCircularIO(camera, seconds=TOTAL_TIME)
    camera.start_recording(stream, format='h264', intra_period=24)

    seconds = 0

    try:
        print('start')
        while True:
            camera.wait_recording(0.1)
            print('%f' % seconds)
            if int(seconds) == 20:
                print('%d' % seconds)
                camera.wait_recording(AFTER_EVENT)
                stream.copy_to('motion.h264')
                break
            seconds+=0.1
    finally:
        print('end')
        camera.stop_recording()
        camera.close()

main()
