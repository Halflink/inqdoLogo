import time


class PixelCharacters:

    class PixelCharacter:

        def __init__(self, pixels, character, pixelRange, colour):
            self.character = character
            self.startPixel = pixelRange[0]
            self.endPixel = pixelRange[1]
            self.colour = colour
            self.base_colour = colour
            self.pixels = pixels

        def set_colour(self, colour):
            self.colour = colour

        def switch_colour(self, colour):
            self.set_colour(colour)
            self.pixels.set_pixel_line(self.startPixel, self.endPixel, self.colour)

        def is_character(self, character):
            return self.character == character

        def circle_colour(self, colour, colourFill):
            self.set_colour(colour)
            for i in range(self.startPixel, self.endPixel):
                self.pixels.set_pixel_line(self.startPixel, i, colourFill)
                self.pixels.set_pixel(i, self.colour)
                self.pixels.show()
                time.sleep(0.1)
            self.pixels.set_pixel_line(self.startPixel, self.endPixel, self.colour)

    def __init__(self, pixels, characterSettings, colour):
        self.pixelCharacters = []
        for characterSetting in characterSettings:
            character = characterSetting[0]
            characterPixelRange = characterSetting[1]
            self.pixelCharacters.append(self.PixelCharacter(pixels, character, characterPixelRange, colour))

    def set_character_colour(self, character, colour):
        pixelCharacter = self.get_pixel_character(character)
        if pixelCharacter is not None:
            pixelCharacter.switch_colour(colour)

    def get_pixel_character(self, character):
        returnPixelCharacter = None
        for pixelCharacter in self.pixelCharacters:
            if pixelCharacter.is_character(character):
                returnPixelCharacter = pixelCharacter
        return returnPixelCharacter

    def circle_character(self, character, colour, colourFill):
        pixelCharacter = self.get_pixel_character(character)
        if pixelCharacter is not None:
            pixelCharacter.circle_colour(colour, colourFill)


