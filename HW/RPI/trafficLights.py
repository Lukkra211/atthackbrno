#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.


# edited by Matuska Lukas

import time
from neopixel import *
import argparse

# LED strip configuration:
LED_COUNT      = 3      # Number of LED pixels.
LED_PIN        = 12      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PINS       = [12, 18, 40, 52]      # GPIO pin connected to the pixels (18 uses PWM!).
LED_PINS       = [12, 13, 18, 19]      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    strips = []
    yellowDelay = 3
    for ledPin in LED_PINS:
        print(ledPin)
	if ledPin in [13, 19, 41, 45, 53]:
		ledChannel =1
	else:
		ledChannel = 0
        # Create NeoPixel object with appropriate configuration.
        strips.append(Adafruit_NeoPixel(LED_COUNT, ledPin, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, ledChannel))
        # Intialize the library (must be called once before other functions).
        strips[-1].begin()

#    print(strips)
    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        print ('  *-*  Simulation started!  *-*  ')
        while True:
 	    print('TL0+1: Yellow! Get ready!')
	    colorWipe(strips[0], Color(255,255,0))  # Yellow wipe
            colorWipe(strips[1], Color(255,255,0))  # Yellow wipe
	    time.sleep(yellowDelay)
     	    print('TL0:   Green! Go!')
            colorWipe(strips[0], Color(255, 0, 0))  # Green wipe
	    print('TL1:   Red! STOP!')
            colorWipe(strips[1], Color(0, 255, 0))  # Red wipe
            #setColor(strips[1], Color(0, 255, 0))  # Red wipe
	    time.sleep(10)
	    print('TL0+1: Yellow! Break!')
            colorWipe(strips[0], Color(255,255,0))  # Yellow wipe
            colorWipe(strips[1], Color(255,255,0))  # Yellow wipe
	    time.sleep(yellowDelay)
	    print('TL0:   Red! STOP!')
     	    print('TL1:   Green! Go!')
            colorWipe(strips[0], Color(0, 255, 0))  # Red wipe
            colorWipe(strips[1], Color(255, 0, 0))  # Green wipe
	    time.sleep(10)


    except KeyboardInterrupt:
        if args.clear:
		for strip in strips:
			colorWipe(strip, Color(0,0,0), 10)
