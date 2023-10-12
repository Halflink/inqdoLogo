import time
from JsonHandler import JsonHandler
from neopixel import Neopixel
from machine import Pin
from pixelCharacters import PixelCharacters


class Main:

    def __init__(self):
        self.settings = JsonHandler()
        self.pixels = Neopixel(self.settings.numberOfPixels, self.settings.state, self.settings.neoPixelPin,
                               self.settings.mode)
        self.pixels.brightness(self.settings.brightness)
        self.pixels.fill(self.settings.white)
        self.led = Pin(self.settings.ledPin, Pin.OUT)
        self.led.toggle()
        self.pixelCharacters = PixelCharacters(self.pixels, self.settings.characterSettings, self.settings.white)

    def show(self, sleep):
        self.pixels.show()
        time.sleep(sleep)

    def pattern_1(self):
        for i in range(3):
            for colour in [self.settings.yellow, self.settings.orange, self.settings.blue]:
                self.pixels.fill(self.settings.white)
                self.show(1)
                self.pixelCharacters.set_character_colour('I', colour)
                self.pixelCharacters.set_character_colour('O', colour)
                self.show(0.5)
                self.pixels.fill(self.settings.white)
                self.pixelCharacters.set_character_colour('N', colour)
                self.pixelCharacters.set_character_colour('D', colour)
                self.show(0.5)
                self.pixels.fill(self.settings.white)
                self.pixelCharacters.set_character_colour('Q', colour)
                self.show(3)

    def pattern_2(self):
        for colour in [self.settings.blue, self.settings.orange, self.settings.yellow]:
            self.pixels.fill(self.settings.white)
            self.show(1)
            self.pixelCharacters.circle_character('Q', colour, colour)
            self.show(3)

    def pattern_3(self):
        for colour in [self.settings.blue, self.settings.orange, self.settings.yellow]:
            self.pixels.fill(self.settings.white)
            self.show(1)
            self.pixelCharacters.circle_character('I', colour, self.settings.white)
            self.show(0.5)
            self.pixelCharacters.circle_character('N', colour, self.settings.white)
            self.show(0.5)
            self.pixelCharacters.circle_character('Q', colour, self.settings.white)
            self.show(0.5)
            self.pixelCharacters.circle_character('D', colour, self.settings.white)
            self.show(0.5)
            self.pixelCharacters.circle_character('O', colour, self.settings.white)
            self.show(3)


if __name__ == '__main__':
    print('start')
    main = Main()

    while True:
        main.pattern_3()
        main.pattern_2()
        main.pattern_1()
