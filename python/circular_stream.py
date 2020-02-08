import picamera

with picamera.PiCamera() as camera:
    with picamera.PiCameraCircularIO(camera, seconds=10) as stream:
        camera.start_recording(stream, format='h264')
        try:
            while True:
                camera.wait_recording(1)
                # if detect_crash():
                    # print('Crash detected!')
                    # camera.split_recording('after.h264')
                    # Write the 10 seconds before motion to disk
                    # stream.copy_to('before.h264', seconds=10)
                    # stream.clear()
                    # camera.split_recording(stream)
        finally:
            camera.stop_recording()
