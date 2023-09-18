import plasma
from plasma import plasma2040
from pimoroni import Button
import time

#Define what an RGB Value is to add to our array later
class RGBValue():
    def __init__(self, r_val, g_val, b_val):
        self.r=r_val
        self.g=g_val
        self.b=b_val

# Define the number of LED's to work with
NUM_LEDS = 192

BRIGHTNESS = 0.5
#Initalize the LED Strip

led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma2040.DAT)
led_strip.start()

# Define what our buttons are
button_a = Button(plasma2040.BUTTON_A)
button_b = Button(plasma2040.BUTTON_B)

# Create a blank RGB Array.  This will be repeated over the lenght of the LED Strip
rgbArray = []

# Setup some default colors
color_black  = RGBValue(0, 0, 0)
color_white  = RGBValue(255,255,255)
color_red    = RGBValue(255, 0, 0)
color_green  = RGBValue(0, 230, 0)
color_blue   = RGBValue(0, 0, 255)
color_purple = RGBValue(221, 160, 221)
color_cyan   = RGBValue(0, 255, 255)
color_pink   = RGBValue(255, 20, 203)
color_yellow = RGBValue(255, 175, 0)
color_violet = RGBValue(127,0,255)
color_darkgreen = RGBValue(40,140,70)
color_orange = RGBValue(255, 165, 0)
color_spanishorange = RGBValue(232,97,0)

# Add values to the RGB Array
for i in range(10):
        rgbArray.append(color_yellow)
for i in range(10):
        rgbArray.append(color_orange)
for i in range(10): 
        rgbArray.append(color_spanishorange)
for i in range(10):
        rgbArray.append(color_red)
for i in range(10):
        rgbArray.append(color_spanishorange)
for i in range(10):
        rgbArray.append(color_orange)

# Clean up the LED Strip to start with
for i in range(NUM_LEDS):
    led_strip.set_rgb(i, 0, 0, 0)

# Set some inital values
current_array_pos = 0
start_array_pos = 0
pos_modifier = 1

# Loop forever
while True:
    current_array_pos = start_array_pos
    for i in range(NUM_LEDS):
        # Write values to the LED Strip.  Loops through the Array of LED Values entered Above
        led_strip.set_rgb(i,
            int(rgbArray[current_array_pos].r * BRIGHTNESS),
            int(rgbArray[current_array_pos].g * BRIGHTNESS),
            int(rgbArray[current_array_pos].b * BRIGHTNESS))
        current_array_pos = current_array_pos + 1
        
        # time.sleep(0.1)
        # Keep our values in a valid range
        if(current_array_pos >= len(rgbArray)):
            current_array_pos = 0
        if(current_array_pos < 0):
            current_array_pos = len(rgbArray) - 1
    
    # Let user change the direction of the scrolling LED's with buttons
    if(button_a.read()):
        pos_modifier = 1
        # print("Pressed A!")
    if(button_b.read()):
       pos_modifier = -1
       # print("Pressed B!")
    
    start_array_pos = start_array_pos + pos_modifier
    # Keep our values in a valid range
    if(start_array_pos >= len(rgbArray)):
        start_array_pos = 0
    if(start_array_pos < 0):
        start_array_pos = len(rgbArray) - 1

    # Delay to determine the speed of the scrolling LED's
    time.sleep(0.12)
