import time
from JsonHandler import JsonHandler
from neopixel import Neopixel
from machine import Pin

settings = JsonHandler()
settings.print_settings()

pixels = Neopixel(settings.numberOfPixels, settings.state, settings.pin, settings.mode)

colour0 = settings.white
colour1 = settings.blue
colour2 = settings.yellow
colour3 = settings.orange
counter = 0
useColour = colour3

pixels.brightness(50)
pixels.fill(colour0)

led = Pin(25, Pin.OUT)
led.toggle()

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

    for neoPixelCharacter in settings.neoPixelCharacters:
        character = neoPixelCharacter[0]
        characterPixelRange = neoPixelCharacter[1]
        pixels.set_pixel_line(characterPixelRange[0], characterPixelRange[1], useColour)
        pixels.show()
        time.sleep(0.5)


