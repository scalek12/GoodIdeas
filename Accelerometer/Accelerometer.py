# import the microbit library
from microbit import *

# loop forever
while True:
    # get the micro:bit accelerometer data
    y = accelerometer.get_y()
    x = accelerometer.get_x()
    
    # setup program parameters 
    delay = 500
    limit = 200
    
    # check x/y for direction of TILT and display arrow
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
        
    else:                    # no tilt detected
        display.clear()
    # delay before repeating loop
    sleep(delay)

#REMEMBER – any line with a # in front of it is a comment and not code that the computer will execute
