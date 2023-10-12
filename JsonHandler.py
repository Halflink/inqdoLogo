import json as json


class JsonHandler:

    def __init__(self):
        with open("init.json") as jsonFile:
            init_info = json.load(jsonFile)
            jsonFile.close()

            # set colours
            colours = init_info['colours']
            self.white = self.get_rgb(colours['white'])
            self.yellow = self.get_rgb(colours['yellow'])
            self.orange = self.get_rgb(colours['orange'])
            self.blue = self.get_rgb(colours['blue'])
            self.green = self.get_rgb(colours['green'])
            self.red = self.get_rgb(colours['red'])

            # set character pixels
            self.characterSettings = []
            self.add_character_settings(init_info['characters'])

            # set neopixel
            neoPixelSettings = init_info['neoPixelSettings']
            self.numberOfPixels = neoPixelSettings['numberOfPixels']
            self.state = neoPixelSettings['state']
            self.neoPixelPin = neoPixelSettings['pin']
            self.mode = neoPixelSettings['mode']
            self.brightness = neoPixelSettings['pixelBrightness']

            # set LED pin
            self.ledPin = init_info['ledPin']

    @staticmethod
    def get_rgb(colour):
        rgb = (colour[0], colour[1], colour[2])
        return rgb

    def add_character_settings(self, characters):
        for character in characters:
            characterSetting = [character, characters[character]]
            self.characterSettings.append(characterSetting)

    def print_settings(self):
        print("white: {}, yellow: {}, blue: {}, orange: {}, green: {}".format(self.white, self.yellow, self.blue,
                                                                              self.orange, self.green))
        print(self.characterSettings)


if __name__ == '__main__':
    jsonHandler = JsonHandler()
    jsonHandler.print_settings()
