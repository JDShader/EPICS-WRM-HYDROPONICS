import RPi.GPIO as GPIO
import os
import sys
import time
from subprocess import Popen

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) #\
#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) # |- these are copy-paste. figure out which to use.
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #/



movie1 = ("/home/pi/Desktop/videoprog1/20190112_150342.mp4") #replace with actual video location

unmute = GPIO.input(17)
muteState = 0

os.system('killall omxplayer.bin')

while 1:
    videoTime = time.time() + 20
    
    if(muteState == 0):
        omxc = Popen(['omxplayer', '--vol', '-3000000', movie1])
        while (time.time() < videoTime):
            if (unmute == 0):
                print ('unmute %d', unmute)
                muteState += 1
                 
    elif(muteState > 0):
        muteState = 0
        omxc = Popen(['omxplayer', '--vol', '-0', movie1])
        while (time.time() < videoTime):
            if (unmute == 0):
                muteState += 1        
    
    os.system('killall omxplayer.bin')
    print (muteState)