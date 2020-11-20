import RPi.GPIO as GPIO
import os
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
in1 = 27
in2 = 22
in3 = 5
in4 = 6
light = 17
fan = 26

GPIO.setup(fan, GPIO.OUT)

GPIO.output(fan, GPIO.LOW)

GPIO.setup(light, GPIO.OUT)

GPIO.output(light, GPIO.LOW)

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
root=""

def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    print('motor stop')

myfile="/home/pi/UvRobot/forward.text"

def move_forward():
    print('moving forward')
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
   
    
def turn_left():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def turn_right():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)



def move_backward():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)


while True:


    path=root+"temp/for.rob"
    if os.path.isfile(path):
        for i in range(5):
            if (os.path.isfile(path)) and (not os.path.isfile("temp/us1.rob")) and (not os.path.isfile("temp/us2.rob")) and (not os.path.isfile("temp/us3.rob")):
                move_forward()
                time.sleep(.5)
            else:
                stop()
                break                   
        if os.path.isfile(path):
            os.remove(path)
            print('file removed')
            


                    



    path=root+"temp/back.rob"
    if os.path.isfile(path):
        for i in range(5):
            if os.path.isfile(path):
                move_backward()
                time.sleep(.5)
            else:
                stop()
                break                   
        if os.path.isfile(path):
            os.remove(path)
            print('file removed')
            



    path=root+"temp/left.rob"
    if os.path.isfile(path):
        for i in range(5):
            if os.path.isfile(path):
                turn_left()
                time.sleep(.5)
            else:
                stop()
                break                   
        if os.path.isfile(path):
            os.remove(path)
            print('file removed')
            



    path=root+"temp/right.rob"
    if os.path.isfile(path):
        for i in range(5):
            if os.path.isfile(path):
                turn_right()
                time.sleep(.5)
            else:
                stop()
                break                   
        if os.path.isfile(path):
            os.remove(path)
            print('file removed')
            


                    
    path=root+"temp/uv.rob"
    if os.path.isfile(path) and (not os.path.isfile("temp/pir1.rob")) and (not os.path.isfile("temp/pir2.rob")) and (not os.path.isfile("temp/pir3.rob")):
        GPIO.output(light,GPIO.HIGH)
    else:
        GPIO.output(light,GPIO.LOW)

                    
    print('fan on')
                    
    path=root+"temp/fan.rob"
    if os.path.isfile(path):
        GPIO.output(fan,GPIO.HIGH)
        print('fan if')
    else:
        GPIO.output(fan,GPIO.LOW)
        print('fan else')
                    


