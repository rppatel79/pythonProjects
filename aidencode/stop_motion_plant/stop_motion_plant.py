from picamera import PiCamera
from time import sleep
import datetime

camera = PiCamera()
camera.rotation = 180

date = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
camera.capture('/home/pi/plant_images/image'+date+'.jpg')


