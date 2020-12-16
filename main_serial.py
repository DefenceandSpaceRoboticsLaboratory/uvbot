import RPi.GPIO as GPIO
import os
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 
import serial

ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)
ser.flush()

root=""

spd=0

dr=0

def send2motor():
    speeds=str(spd)[0]
    drs=str(dr)[0]
    datast=bytes(""+drs+speeds+"\n",'utf-8')
    ser.write(datast)
    print("sent command")
    print(""+drs+speeds+"\n")

def send2uv():
    drs=str(dr)[0]
    datast=bytes(""+drs+"\n",'utf-8')
    ser.write(datast)
    print("sent command")
    print(""+drs+"\n")

def speed_inc():    
    global spd
    spd = spd + 1
    if(spd >7):
        spd = 7 
    
def speed_dec():
    global spd
    spd = spd - 1
    if(spd < 0):
        spd = 0 
    

def move_forward():
    global dr
    dr='1'
    speed_inc()     
    send2motor()                 
    print('motor forward')

def stop(): 
    global dr
    dr='0'
    send2motor()
    print('motor stop')
    
def turn_left(): 
    global dr
    dr='3'
    send2motor()
    print('motor left')

def turn_right(): 
    global dr
    dr='4'
    send2motor()
    print('motor right')

def move_backward():
    global dr
    dr='2'
    send2motor()
    print('motor back')

def uv_on():
    global dr
    dr='5'
    send2uv()
    print('uv on')

def uv_off():
    global dr
    dr='6'
    send2uv()
    print('uv off')

while True:
    path=root+"temp/for.rob"
    if os.path.isfile(path):
        for i in range(10):
            if (os.path.isfile(path)) and (not os.path.isfile("temp/us1.rob")) and (not os.path.isfile("temp/us2.rob")) and (not os.path.isfile("temp/us3.rob") and (not os.path.isfile("temp/us4.rob"))):
                move_forward()
                time.sleep(5)
            else:
                stop()
                break                   
        if os.path.isfile(path):
            os.remove(path)
            print('file removed')
            


    path=root+"temp/back.rob"
    if os.path.isfile(path):
        for i in range(10):
            if os.path.isfile(path):
                move_backward()
                time.sleep(5)
            else:
                stop()
                break                   
        if os.path.isfile(path):
            os.remove(path)
            print('file removed')
            

    path=root+"temp/left.rob"
    if os.path.isfile(path):
        for i in range(10):
            if os.path.isfile(path):
                turn_left()
                time.sleep(5)
            else:
                stop()
                break                   
        if os.path.isfile(path):
            os.remove(path)
            print('file removed')
            

    path=root+"temp/right.rob"
    if os.path.isfile(path):
        for i in range(10):
            if os.path.isfile(path):
                turn_right()
                time.sleep(5)
            else:
                stop()
                break                   
        if os.path.isfile(path):
            os.remove(path)
            print('file removed')
                                
    path=root+"temp/uv.rob"
    if os.path.isfile(path) and (not os.path.isfile("temp/pir1.rob")) and (not os.path.isfile("temp/pir2.rob")) and (not os.path.isfile("temp/pir3.rob")) and (not os.path.isfile("temp/pir4.rob")):
        uv_on()
    else:
        uv_off()

                    
'''
                    
    path=root+"temp/fan.rob"
    if os.path.isfile(path):
        GPIO.output(fan,GPIO.HIGH)
        print('fan if')
    else:
        GPIO.output(fan,GPIO.LOW)
        print('fan else')'''
                    




