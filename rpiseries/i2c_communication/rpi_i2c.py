#RPi Pinouts

#I2C Pins 
#GPIO2 -> SDA
#GPIO3 -> SCL

#Import the Library Requreid 
import smbus
import time

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
MX_address = 0x70
MPU_address_1 = 0x68
MPU_address_2 = 0x69

MX_port = 0x07
MPU_WHO_AM_I = 0x77

MILIGHT_address = 0x70


max_loops = 20
i = 0
keepGoing = True

def writeNumber(value):
    bus.write_byte(MX_address, MX_port)
    #bus.write_byte(MPU_address_1, MPU_WHO_AM_I)
    #bus.write_byte(MPU_address_2, MPU_WHO_AM_I)
    return -1

def readNumber():
    # number = bus.read_byte(address)
    number = bus.read_byte_data(MX_address, 1)
    return number
    
while keepGoing:
	#Receives the data from the User
    #data = raw_input("Enter the data to be sent : ")
    #data_list = list(data)
    #for i in data_list:
    #Sends to the Slaves
    data = [int(0x80), int(0x35), int(0x00), int(0x00), int(0x00)]
    bus.write_byte_data(MILIGHT_address,0,data)
    #bus.write_byte(MILIGHT_address, int(0x80))
    #bus.write_byte(MILIGHT_address, int(0x35))
    #bus.write_byte(MILIGHT_address, int(0x00))
    #bus.write_byte(MILIGHT_address, int(0x00))
    #bus.write_byte(MILIGHT_address, int(0x00))
    #writeNumber(1)#(int(ord(i)))
    #writeNumber(int(0x0A))
    time.sleep(0.25)
    
    bus.write_byte(MILIGHT_address, int(0x80))
    bus.write_byte(MILIGHT_address, int(0x35))
    bus.write_byte(MILIGHT_address, int(0x08))
    bus.write_byte(MILIGHT_address, int(0x00))
    bus.write_byte(MILIGHT_address, int(0x00))
    time.sleep(0.25)
    
    print("Looping: " + str(i))
    i = i + 1
    if i > max_loops:
        keepGoing = False
    
#End of the Script

