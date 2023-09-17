import time
from neopixel import Neopixel

numpix = 63
pixels = Neopixel(numpix, 0, 28, "GRB")
neoPixelCharacters = [
    ['I', [0, 8]],
    ['N', [9, 20]],
    ['Q', [21, 39]],
    ['D', [40, 51]],
    ['O', [52, 62]]
]

yellow = (255, 100, 0)
orange = (255, 50, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
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

    for neoPixelCharacter in neoPixelCharacters:
        character = neoPixelCharacter[0]
        characterPixelRange = neoPixelCharacter[1]
        pixels.set_pixel_line(characterPixelRange[0], characterPixelRange[1], useColour)
        pixels.show()
        time.sleep(0.5)


