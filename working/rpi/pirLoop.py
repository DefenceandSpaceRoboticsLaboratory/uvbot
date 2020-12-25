from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import os

pir1 = 14
pir2 = 15
pir3 = 18
pir4 = 25
pirs = 0


GPIO.setup(pir1, GPIO.IN)
GPIO.setup(pir2, GPIO.IN)
GPIO.setup(pir3, GPIO.IN)
GPIO.setup(pir4, GPIO.IN)



while True :
    if(GPIO.input(pir1) == True ):
        if os.path.isfile("temp/pir1.rob"):
            pass
        else:
            f = open("temp/pir1.rob", "w")
            f.write(" ")
            f.close()
            print(pir1)
        if os.path.isfile("temp/uv.rob"):
            os.remove("temp/uv.rob")
    else:
        if os.path.isfile("temp/pir1.rob"):
            os.remove("temp/pir1.rob")

    if(GPIO.input(pir2) == True ):
        if os.path.isfile("temp/pir2.rob"):
            pass
        else:
            f = open("temp/pir2.rob", "w")
            f.write(" ")
            f.close()
        if os.path.isfile("temp/uv.rob"):
            os.remove("temp/uv.rob")
    else:
        if os.path.isfile("temp/pir2.rob"):
            os.remove("temp/pir2.rob")

    if(GPIO.input(pir3) == True ):
        if os.path.isfile("temp/pir3.rob"):
            pass
        else:
            f = open("temp/pir3.rob", "w")
            f.write(" ")
            f.close()
        if os.path.isfile("temp/uv.rob"):
            os.remove("temp/uv.rob")
    else:
        if os.path.isfile("temp/pir3.rob"):
            os.remove("temp/pir3.rob")
            
    if(GPIO.input(pir4) == True ):
        if os.path.isfile("temp/pir4.rob"):
            pass
        else:
            f = open("temp/pir4.rob", "w")
            f.write(" ")
            f.close()
        if os.path.isfile("temp/uv.rob"):
            os.remove("temp/uv.rob")
    else:
        if os.path.isfile("temp/pir4.rob"):
            os.remove("temp/pir4.rob")
            



            




