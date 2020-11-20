
import RPi.GPIO as GPIO          #calling header file which helps us use GPIOâ€™s of PI
import time                            #calling time to provide delays in program
GPIO.setwarnings(False)           #do not show any warnings
GPIO.setmode (GPIO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as â€˜GPIO19â€™)
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
spd=0
def speed_inc():
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
    GPIO.output(en,GPIO.HIGH)
    speed_inc()
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)                           #
    print('moving forward')

def stop():
    GPIO.output(en,GPIO.HIGH)
    speed_dec()
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    print('motor stop')
    
while 1:                               #execute loop forever
    move_forward()
    time.sleep(100)
    stop()
    time.sleep(5)
