from picamera import PiCamera
from os import system
from time import sleep

IMAGE_COUNT = 10
IMG_INTERVAL = 1

camera = PiCamera()
camera.resolution = (1024, 768)

for i in range(IMAGE_COUNT):
    camera.capture('image{0:04d}.jpg'.format(i))
    sleep(IMG_INTERVAL)
    
system('convert -delay 10 -loop 0 image*.jpg animation.gif')
print('gif has been created')
