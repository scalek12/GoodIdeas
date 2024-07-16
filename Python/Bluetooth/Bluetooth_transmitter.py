# Remote TILT! detector and transmitter for microbit
# Trace the code to determine how the basic system works
# A paired reciever is required and has separate code

# import the microbit and radio libraries
from microbit import *
import radio
# configure radio settings
radio.config(channel=24)
radio.on()

# setup program parameters 
delay = 200        # ms to delay between loops

# loop forever
while True:
    # get the micro:bit accelerometer data
    y = accelerometer.get_y()
    x = accelerometer.get_x()
    z = accelerometer.get_z()
    # get the status of A and B buttons
    a = button_a.is_pressed()
    b = button_b.is_pressed()

    # check for buttons pressed
    if  a:    # A button display HEART
        radio.send("A")
        print("A")
    elif b:    # B button display DIAMOND
        radio.send("B")
        print("B")
    
    # Transmit "X,Y,Z" data
    data = "{},{},{}".format(x,y,z)
    print(data)
    radio.send(data)

    # delay before repeating loop
    sleep(delay)
