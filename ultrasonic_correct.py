import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
import os
TRIG1 = 8
ECHO1 = 7
TRIG2 = 20
ECHO2 = 21
TRIG3 = 23
ECHO3 = 24
TRIG4 = 12
ECHO4 = 16

GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)

GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)

GPIO.setup(TRIG3, GPIO.OUT)
GPIO.setup(ECHO3, GPIO.IN)

GPIO.setup(TRIG4, GPIO.OUT)
GPIO.setup(ECHO4, GPIO.IN)

def distance(GPIO_TRIGGER,GPIO_ECHO):
    GPIO.output(GPIO_TRIGGER,True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER,False)
    StartTime = time.time()
    StopTime=time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime=time.time()
    while GPIO.input(GPIO_ECHO)== 1:
        StopTime=time.time()
    TimeElapsed=StopTime -StartTime
    distance = (TimeElapsed*34300)/2
    return distance
if __name__ == '__main__':
    try:
        while True:
            p1 = distance(TRIG1,ECHO1)
            p2 = distance(TRIG2,ECHO2)
            p3 = distance(TRIG3,ECHO3)
            p4 = distance(TRIG4,ECHO4)
            print("p1=",p1)
            print("p2=",p2)
            print("p3=",p3)
            print("p4=",p4)
            if(p1<1000):
                if (p1<200):
                    if os.path.isfile("temp/us1.rob"):
                        pass
                    else:
                        f = open("temp/us1.rob", "w")
                        f.write(" ")
                        f.close()
                    if os.path.isfile("temp/for.rob"):
                        os.remove("temp/for.rob")
                else:
                    if os.path.isfile("temp/us1.rob"):
                        os.remove("temp/us1.rob") 
            else:
                print("Error in p1")

            if (p2<1000):
                if (p2<200):
                    if os.path.isfile("temp/us2.rob"):
                        pass
                    else:
                        f = open("temp/us2.rob", "w")
                        f.write(" ")
                        f.close()
                    if os.path.isfile("temp/for.rob"):
                        os.remove("temp/for.rob")
                else:
                    if os.path.isfile("temp/us2.rob"):
                        os.remove("temp/us2.rob")
            else:
                print("Error in p2")
                    
            if(p3<1000):
                if (p3<200):
                    if os.path.isfile("temp/us3.rob"):
                        pass
                    else:
                        f = open("temp/us3.rob", "w")
                        f.write(" ")
                        f.close()
                    if os.path.isfile("temp/back.rob"):
                        os.remove("temp/back.rob")
                else:
                    if os.path.isfile("temp/us3.rob"):
                        os.remove("temp/us3.rob")
            else:
                print("Error in p3")
            
            if(p4<1000):
                if (p4<200):
                    if os.path.isfile("temp/us4.rob"):
                        pass
                    else:
                        f = open("temp/us4.rob", "w")
                        f.write(" ")
                        f.close()
                    if os.path.isfile("temp/back.rob"):
                        os.remove("temp/back.rob")
                else:
                    if os.path.isfile("temp/us4.rob"):
                        os.remove("temp/us4.rob")
            else:
                print("Error in p4")



                
    except KeyboardInterrupt:
        GPIO.cleanup()
    
    

