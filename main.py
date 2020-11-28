import RPi.GPIO as GPIO
import os
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
en1 = 17
in1=27
in2=22
en2=10
in3=9
in4=11
pwm1 = 13
pwm2 =19

kills=26
uv1 = 3
uv2 = 4
dclight = 2



GPIO.setup(uv1, GPIO.OUT)
GPIO.setup(uv2, GPIO.OUT)
GPIO.setup(kills, GPIO.OUT)
GPIO.setup(dclight, GPIO.OUT)
GPIO.output(dclight, GPIO.LOW)
GPIO.output(uv1, GPIO.LOW)
GPIO.output(uv2, GPIO.LOW)


GPIO.setup(en1, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
GPIO.setup(pwm1, GPIO.OUT)
GPIO.setup(pwm2, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
root=""


p = GPIO.PWM(19,100)          #GPIO19 as PWM output, with 100Hz frequency
p.start(0)                              #generate PWM signal with 0% duty cycle
q = GPIO.PWM(13,100)
q.start(0)
spd=0



def speed_inc():    ##if uv on hoi speed 10  korbo lagbo
    global spd
    spd = spd + 10
    if(spd >75):
        spd = 75
    p.ChangeDutyCycle(spd)
    
def speed_dec():
    global spd
    spd = spd - 10
    if(spd < 0):
        spd = 0
    p.ChangeDutyCycle(spd)
    

def move_forward():
    GPIO.output(en1,GPIO.HIGH)
    GPIO.output(en2,GPIO.HIGH)
    speed_inc()
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)                           #
    print('moving forward')

def stop():
    GPIO.output(en1,GPIO.HIGH)
    GPIO.output(en2,GPIO.HIGH)
    speed_dec()
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    print('motor stop')
    
def turn_left():
    GPIO.output(en1,GPIO.HIGH)
    GPIO.output(en2,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def turn_right():
    GPIO.output(en1,GPIO.HIGH)
    GPIO.output(en2,GPIO.HIGH)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)



def move_backward():
    GPIO.output(en1,GPIO.HIGH)
    GPIO.output(en2,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)


while True:


    path=root+"temp/for.rob"
    if os.path.isfile(path):
        for i in range(5):
            if (os.path.isfile(path)) and (not os.path.isfile("temp/us1.rob")) and (not os.path.isfile("temp/us2.rob")) and (not os.path.isfile("temp/us3.rob") and (not os.path.isfile("temp/us4.rob"))):
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
    if os.path.isfile(path) and (not os.path.isfile("temp/pir1.rob")) and (not os.path.isfile("temp/pir2.rob")) and (not os.path.isfile("temp/pir3.rob")) and (not os.path.isfile("temp/pir4.rob")):
        GPIO.output(uv1,GPIO.HIGH)
        GPIO.output(uv2,GPIO.HIGH)
    else:
        GPIO.output(uv1,GPIO.LOW)
        GPIO.output(uv2,GPIO.LOW)

                    
    '''print('fan on')
                    
    path=root+"temp/fan.rob"
    if os.path.isfile(path):
        GPIO.output(fan,GPIO.HIGH)
        print('fan if')
    else:
        GPIO.output(fan,GPIO.LOW)
        print('fan else')'''
                    



