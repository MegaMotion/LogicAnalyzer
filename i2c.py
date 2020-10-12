
import RPi.GPIO as GPIO
import time
from smbus2 import SMBus
import ic_msg

i = 0
start = 0
maxLoops = 40
bus = SMBus(1)

keepGoing = True
while keepGoing:
    msg = i2c_msg.write(80, [65,66,67,68])
    bus.i2c_rdwr(msg)
        
    print("writing!  " + str(i))
    i = i + 1
    if (i > maxLoops):
        keepGoing = False
    time.sleep(0.05)

        
#Exit gracefully?

print "Done!"
