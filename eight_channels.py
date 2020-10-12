
import RPi.GPIO as GPIO
import time
import serial


BCM = [6,15,19,26,12,16,20,21]

GPIO.setmode(GPIO.BCM)

keepGoing = True
i = 0
start = 0
maxLoops = 40

for i in range(8):
    GPIO.setup(BCM[i], GPIO.OUT)

#now, let's get down to business: use all eight data channels, on GPIO 22 through 29.
while keepGoing:
    
    if (i % 2 == 0):
        GPIO.output(BCM[0],GPIO.HIGH)
        GPIO.output(BCM[1],GPIO.LOW)
    else:
        GPIO.output(BCM[0],GPIO.LOW)
        GPIO.output(BCM[1],GPIO.HIGH)
    
    if (i % 4 == 0):
        GPIO.output(BCM[2],GPIO.HIGH)
        GPIO.output(BCM[3],GPIO.LOW)
    else:
        GPIO.output(BCM[2],GPIO.LOW)
        GPIO.output(BCM[3],GPIO.HIGH)

    
    if (i % 8 == 0):
        GPIO.output(BCM[4],GPIO.HIGH)
        GPIO.output(BCM[5],GPIO.LOW)
    else:
        GPIO.output(BCM[4],GPIO.LOW)
        GPIO.output(BCM[5],GPIO.HIGH)

    
    if (i % 16 == 0):
        GPIO.output(BCM[6],GPIO.HIGH)
        GPIO.output(BCM[7],GPIO.LOW)
    else:
        GPIO.output(BCM[6],GPIO.LOW)
        GPIO.output(BCM[7],GPIO.HIGH)

    i = i + 1
    if (i > maxLoops):
        keepGoing = False


    print "looping: " + str(i)
    time.sleep(0.1)

        
#Exit gracefully?
port.close()
GPIO.cleanup()

print "Done!"
