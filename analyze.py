
import RPi.GPIO as GPIO
import time
import serial


BCM = [14,15,19,26,12,16,20,21]

GPIO.setmode(GPIO.BCM)

#GPIO.setup(BCM[0], GPIO.OUT)
#GPIO.setup(BCM[1], GPIO.OUT)
#GPIO.setup(BCM[2], GPIO.OUT)
#GPIO.setup(BCM[3], GPIO.OUT)
#GPIO.setup(BCM[4], GPIO.OUT)
#GPIO.setup(BCM[5], GPIO.OUT)
#GPIO.setup(BCM[6], GPIO.OUT)
#GPIO.setup(BCM[7], GPIO.OUT)



keepGoing = False
i = 0
start = 0
maxLoops = 40

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

#NOW: can we get a bit more advanced? Like sending UART or I2C signals?

keepGoing = True
port = serial.Serial("/dev/ttyS0", 9600)
#port.open()
while keepGoing:
    port.write('SOS'.encode('utf-8'))
    print("writing!  " + str(i))
    i = i + 1
    if (i > maxLoops):
        keepGoing = False

        
#Exit gracefully?
port.close()
GPIO.cleanup()

print "Done!"
