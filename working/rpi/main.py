import RPi.GPIO as GPIO
import os
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 
import serial

#ser=serial.Serial('/dev/ttyACM0',9600,parity=serial.PARITY_ODD,stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

#ser = serial.Serial('/dev/ttyACM0',9600)
#ser.flush()
path="temp/uv.rob"
if os.path.isfile(path):
    os.remove(path)



ser = serial.Serial('/dev/ttyACM0',9600, timeout=.5)
ser.flush()

root=""

spd=0
spds='0'

dr=0
uv=0

f = open( './temp/speed.rob', "w")
f.write("0")
f.close()

def send2motor():
    global spds
    getSpeed()

    speeds=str(spds)[0]
    drs=str(dr)[0]
    uvs=str(uv)[0]
    datast=drs+speeds+uvs+"\n"
    #bytes(datast,'utf-8')

    time.sleep(.05)

    ser.write(datast.encode('ascii') + b'13' + b'10')
    time.sleep(1)
    #ser.close()

    #ser.flush()
    print("sent command")
    print(datast)





def getSpeed():
    global spds
    fileHandle = open ( 'temp/speed.rob',"r" )
    lineList = fileHandle.readlines()
    fileHandle.close()
    spds= lineList[-1]

'''
def send2motor():
    global spds
    getSpeed()
    speeds=str(spds)[0]
    drs=str(dr)[0]
    uvs=str(uv)[0]
    datast=drs+speeds+uvs+"\n"
    #bytes(datast,'utf-8')
    ser.write(datast.encode())
    print("sent command")
    print(datast)

'''
def speed_inc():    
    global spd
    spd = spd + 1
    #if(spd >7):
    #    spd = 7 
    
def speed_dec():
    global spd
    spd = spd - 1
    if(spd < 0):
        spd = 0 
    

def move_forward():
    global dr
    dr='1'
    #speed_inc()     
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
    global uv
    uv='1'
    send2motor()
    print('uv on')

def uv_off():
    global uv
    uv='0'
    send2motor()
    print('uv off')

while True:
    path=root+"temp/for.rob"
    if os.path.isfile(path):
        for i in range(6):
            if (os.path.isfile(path)) and (not os.path.isfile("temp/us1.rob")) and (not os.path.isfile("temp/us2.rob")) and (not os.path.isfile("temp/us3.rob") and (not os.path.isfile("temp/us4.rob"))):
                move_forward()
            else:     
                stop()
                break                   
        if os.path.isfile(path):
            os.remove(path)
            print('file removed')
            dr=0

            


    path=root+"temp/back.rob"
    if os.path.isfile(path):
        for i in range(6):
            if os.path.isfile(path):
                move_backward()
            else:
                stop()
                break                   
        if os.path.isfile(path):
            os.remove(path)
            print('file removed')
            dr=0

            

    path=root+"temp/left.rob"
    if os.path.isfile(path):
        for i in range(6):
            if os.path.isfile(path):
                turn_left()
            else:
                stop()
                break                   
        if os.path.isfile(path):
            os.remove(path)
            print('file removed')
            dr=0

            

    path=root+"temp/right.rob"
    if os.path.isfile(path):
        for i in range(6):
            if os.path.isfile(path):
                turn_right()
            else:
                stop()
                break                   
        if os.path.isfile(path):
            os.remove(path)
            print('file removed')
            dr=0                                
    path=root+"temp/uv.rob"
    if os.path.isfile(path) and (not os.path.isfile("temp/pir1.rob")) and (not os.path.isfile("temp/pir2.rob")) and (not os.path.isfile("temp/pir3.rob")) and (not os.path.isfile("temp/pir4.rob")):
        uv_on()
    else:
        uv_off()






