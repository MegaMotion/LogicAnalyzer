
import RPi.GPIO as GPIO
import time
import serial


i = 0
start = 0
maxLoops = 40

#NOW: sending UART signals
keepGoing = True
port = serial.Serial("/dev/ttyS0", 9600)
while keepGoing:
    port.write('THIS IS UART.'.encode('utf-8'))
    print("writing!  " + str(i))
    i = i + 1
    if (i > maxLoops):
        keepGoing = False

        
#Exit gracefully?
port.close()

print "Done!"
