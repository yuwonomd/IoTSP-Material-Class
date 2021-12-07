from pyfirmata import Arduino, util
import pyfirmata
import time

#add port Arduino yang terbaca
port = "/dev/cu.usbmodem1101"
#create board
board = Arduino(port)

#initilization untuk pin Analog
pin1 = board.get_pin('a:3:i')

it = pyfirmata.util.Iterator(board)
it.start()

#time sensor warming up
time.sleep(0.1)

while True: 
    #read value sensor
    analog_value = pin1.read()
    #print(analog_value)
    #time.sleep(0.5)
    
#if condition
    if analog_value < 0.5:
       print("Wow", analog_value)
       time.sleep(0.1)
    else:
        print(analog_value)
        time.sleep(0.1)