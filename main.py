import time
from neopixel import Neopixel
 
numpix = 21
pixels = Neopixel(numpix, 0, 28, "GRB")
 
yellow = (255, 100, 0)
orange = (255, 50, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white= (255, 255, 255)
colour0 = white
colour1 = blue
colour2 = yellow
colour3 = orange
counter = 0
useColour = colour3

pixels.brightness(50)
pixels.fill(colour0)
 
while True:
    pixels.fill(colour0)
    pixels.show()
    time.sleep(1)
    
    if useColour == colour3:
        useColour = colour1
    elif useColour == colour2:
        useColour = colour3
    elif useColour == colour1:
        useColour = colour2
    
    for counter in range(0, numpix):
        pixels.set_pixel(counter, useColour)
        pixels.show()
        time.sleep(0.5)

