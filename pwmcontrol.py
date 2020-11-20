import RPi.GPIO as GPIO          #calling header file which helps us use GPIO’s of PI
import time                            #calling time to provide delays in program
GPIO.setwarnings(False)           #do not show any warnings
GPIO.setmode (GPIO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
in1 = 27
in2 = 22
in3 = 5
in4 = 6
en = 17
GPIO.setup(19,GPIO.OUT)           # initialize GPIO19 as an output.
GPIO.setup(13,GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
p = GPIO.PWM(19,100)          #GPIO19 as PWM output, with 100Hz frequency
p.start(0)                              #generate PWM signal with 0% duty cycle
q = GPIO.PWM(13,100)
q.start(0)
def move_forward():
    for x in range (30):
        GPIO.output(en,GPIO.HIGH)                         #execute loop for 50 times, x being incremented from 0 to 49.
        p.ChangeDutyCycle(x)               #change duty cycle for varying the brightness of LED.
        q.ChangeDutyCycle(x) 
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)                           #
        
    print('moving forward')

def stop():

    for x in range (50):
        GPIO.output(en,GPIO.HIGH)                       #execute loop for 50 times, x being incremented from 0 to 49.
        p.ChangeDutyCycle(50-x)        #change duty cycle for changing the brightness of LED.
        q.ChangeDutyCycle(50-x)
                                #sleep for 100m second
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
    print('motor stop')
while 1:                               #execute loop forever
    move_forward()
    time.sleep(100)
    stop()
    time.sleep(100)
    
    
