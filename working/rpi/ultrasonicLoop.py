

################################################
# AUTHOR:   Fayjie
# EMAIL:    fayjie92@gmail.com
# DATE:     22-10-2016

# DATE MODIFIED:    13-10-2020
###############################################


### Get the sensor data


import time
import threading
import pigpio
import os

# Connection PIN settings 
TRIG1 = 8
ECHO1 = 7
TRIG2 = 20
ECHO2 = 21
TRIG3 = 23
ECHO3 = 24


# Initialize pi gpio module
pi = pigpio.pi()

# Threading 
done1 = threading.Event()
done2 = threading.Event()
done3 = threading.Event()


# High, Low, and Distance Function

def high1(gpio, level, T):
    global H1 
    H1 = T

def low1(gpio, level, T):
    global L1 
    L1 = T - H1 
    done1.set()

def dist1():
    global L1 
    done1.clear()
    pi.gpio_trigger(TRIG1, 50, 1)
    
    if done1.wait(timeout=5):
        return L1*0.034/2
    else:
        return 99999



def high2(gpio, level, T):
    global H2 
    H2 = T

def low2(gpio, level, T):
    global L2 
    L2 = T - H2 
    done2.set()

def dist2():
    global L2 
    done2.clear()
    pi.gpio_trigger(TRIG2, 50, 1)
    
    if done2.wait(timeout=5):
        return L2*0.034/2
    else:
        return 99999




def high3(gpio, level, T):
    global H3 
    H3 = T

def low3(gpio, level, T):
    global L3 
    L3 = T - H3 
    done3.set()

def dist3():
    global L3 
    done3.clear()
    pi.gpio_trigger(TRIG3, 50, 1)
    
    if done3.wait(timeout=5):
        return L3*0.034/2
    else:
        return 99999



'''/ 58.0 / 100.0'''




pi.set_mode(TRIG1, pigpio.OUTPUT)
pi.set_mode(ECHO1, pigpio.INPUT)

pi.set_mode(TRIG2, pigpio.OUTPUT)
pi.set_mode(ECHO2, pigpio.INPUT)

pi.set_mode(TRIG3, pigpio.OUTPUT)
pi.set_mode(ECHO3, pigpio.INPUT)

pi.callback(ECHO1, pigpio.RISING_EDGE, high1)
pi.callback(ECHO1, pigpio.FALLING_EDGE, low1)

pi.callback(ECHO2, pigpio.RISING_EDGE, high2)
pi.callback(ECHO2, pigpio.FALLING_EDGE, low2)

pi.callback(ECHO3, pigpio.RISING_EDGE, high3)
pi.callback(ECHO3, pigpio.FALLING_EDGE, low3)


 	

### If filter is needed

import collections
import numpy as np



history1 = collections.deque(maxlen=10)

history2 = collections.deque(maxlen=10)

history3 = collections.deque(maxlen=10)

def filtered_dist1():
    #history1.append(dist1())
    #return np.median(history1)
    return (dist1())

def filtered_dist2():
    #history2.append(dist2())
    #return np.median(history2)
    return (dist2())

def filtered_dist3():
    #history3.append(dist3())
    #return np.median(history3)
    return (dist3())




while True: 
    p1 = filtered_dist1()
    if(p1<1000):
        print(p1)
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
            

    p2 = filtered_dist2()
    if (p2<1000):
        print(p2)
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
            

    p3 = filtered_dist3()
    if(p3<1000):
        print(p3)
        if (p3<200):
            if os.path.isfile("temp/us3.rob"):
                pass
            else:
                f = open("temp/us3.rob", "w")
                f.write(" ")
                f.close()
            if os.path.isfile("temp/for.rob"):
                os.remove("temp/for.rob")
        else:
            if os.path.isfile("temp/us3.rob"):
                os.remove("temp/us3.rob")
            






