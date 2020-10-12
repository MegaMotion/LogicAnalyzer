
import RPi.GPIO as GPIO
import time
import serial


BCM = [21]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BCM[0], GPIO.OUT)

keepGoing = True
i = 0
start = 0
maxLoops = 100

#now: use all eight data channels, on GPIO 22 through 29.
while keepGoing:
    
    if (i % 2 == 0):
        GPIO.output(BCM[0],GPIO.HIGH)
    else:
        GPIO.output(BCM[0],GPIO.LOW)

    i = i + 1
    if (i > maxLoops):
        keepGoing = False


    print "looping: " + str(i)
    time.sleep(0.05)

        
#Exit gracefully?
GPIO.cleanup()

print "Done!"
