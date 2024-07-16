# Simple TILT! detector for microbit
# Trace the code to determine how the basic system works
# Don't forget to click the "Show Serial" option to see
#      the raw data values

# import the microbit and radio libraries
from microbit import *
import radio
radio.config(channel=24)
radio.on

# setup program parameters

delay = 100
limit = 200

# loop forever
while True:
    # check for received data
    data = radio.receive()

    if data is not None:
        # check for buttons pressed
        if  data == "A":    # A button display HEART
            display.show(Image.HEART)
            print("A button pressed")
        elif data == "B":    # B button display DIAMOND
            display.show(Image.DIAMOND)
            print("B button pressed")
        
        elif data != "A" and data != "B":  # check x/y for direction of TILT and display arrow
            display.clear()
            x, y, z = data.split(",")
            x, y, z = int(x), int(y), int(z)
            if x<-limit:
                if y<-limit:        # tilted forwards and left
                    display.show(Image.ARROW_NW)
                elif y>limit:        # tilted backwards and left
                    display.show(Image.ARROW_SW)
                else:                # tilted to the left
                    display.show(Image.ARROW_W)
            elif x>limit:
                if y<-limit:         # tilted forwards and right
                    display.show(Image.ARROW_NE)
                elif y>limit:        # tilted backwards and right 
                    display.show(Image.ARROW_SE)
                else:                # tilted to the right
                    display.show(Image.ARROW_E)
            
            elif y>limit:            # tilted backwards
                display.show(Image.ARROW_S)
            elif y<-limit:           # tilted forwards
                display.show(Image.ARROW_N)
                
            # display accelerometer data to screen
            print("X:",x,"Y:",y,"Z:",z)
    
    # delay before repeating loop
    sleep(delay)
    
