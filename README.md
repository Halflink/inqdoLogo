# INQDO LOGO
---
## PROJECT
| Project name:    | Halflink/inqdoLogo         |
|------------------|----------------------------|
| Author:          | Jeroen van Zwam            |
| Date:            | 2023-07-02                 |  
| Last update:     | 2023-10-10                 |
| Project type:    | Raspberry Pico             |     
---
## EXECUTABLES
* Start main.py

## PROJECT DESCRIPTION
I came up with the idea for this project when the company I work for asked the
employees if they had suggestions to put in an steampunk themed display cabinet.
I already had a strip of neopixels that I wanted to experiment with, all I
needed was an idea -> a frame with the company logo for in the display cabinet.
The frame is a 3D printed representation of copper piping. As the frame is too
big to print in one go I designed it in several parts using an peg/hole assembly.
At the connections I made flanges with a bolt detail to mimic more copper piping.
The canvas used is a piece of triplex in which I have laser-cutted the logo.
The charring of the triplex gives a more rusty, steampunky look, so I decided
not to varnish the triplex. Behind the triplex a semi-transparent white pane
covers the neopixels.
As the inQdo logo is quite intricate I needed a way to clamp and structure the
neopixel strip. To do that I measured up one single pixel and created a bracket
for it. this bracket is used as a template to create a bracket per letter, which
is basically a concatenation of multiple single pixel brackets.
The housing for the batteries and the pico are intended to be metallic (tin) so
they are part of the steampunk look.
---
## WORKINGS
### turning on off
To turn the logo on, flip the switch in the ON position.<br>
You could also power over the micro usb connector of the pico. 

### patterns
I created 3 different patterns, which run one after the other. 


---
## PARTS LIST
* [raspberry Pico](https://elektronicavoorjou.nl/product/raspberry-pi-pico/)
* [Tumble switch](https://www.benselectronics.nl/mini-tuimel-schakelaar.html)
* [Battery holder](https://www.kiwi-electronics.com/nl/3x-aaa-batterijhouder-met-jst-connector-3734?country=NL&utm_term=3734&gclid=EAIaIQobChMIt-Dz-ubwgQMVtJODBx2EGQ7QEAQYASABEgJ9JvD_BwE)
* [NeoPixel strip](https://www.bitsandparts.nl/LED-Strip-RGB-WS2812-5V-IP67-60-LEDs-m-5-meter-zwart-p1892774)

---
## PROJECT PROGRESS
