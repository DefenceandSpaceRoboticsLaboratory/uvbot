import picamera
from time import sleep
camera = picamera.PiCamera()
camera.start_preview()
camera.start_recording('/home/pi/video.h264')
sleep(30)
camera.stop_recording()
camera.stop_preview()
