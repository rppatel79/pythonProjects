from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180

camera.start_preview()
frame = 1
while True:
    try:
        input('Press Enter to take a picture')
        sleep(1)
        camera.capture('/home/pi/stop_motion/images/frame%03d.jpg' % frame)
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break
