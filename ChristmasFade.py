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
NUM_LEDS = 200

# Define a Brightness Level.  This will be used to limit the intensity of the LED Lights
BRIGHTNESS = 0.5

#Initalize the LED Strip
led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma2040.DAT)
led_strip.start()

# Define what our buttons are
button_a = Button(plasma2040.BUTTON_A)
button_b = Button(plasma2040.BUTTON_B)

# Create a blank RGB Array.  This will be repeated over the lenght of the LED Strip
rgbArray = []

# Define Function that creates a color gradient ad adds it to the rgbArray
# Acepts two seperate colors, and the number of LED's in the gradient
def RGBGradiant(sourceRGB, targetRGB, gradiant_size):
	current_r = sourceRGB.r
	current_g = sourceRGB.g
	current_b = sourceRGB.b

	next_color_r = targetRGB.r
	next_color_g = targetRGB.g
	next_color_b = targetRGB.b

	delta_r = current_r - next_color_r
	delta_g = current_g - next_color_g
	delta_b = current_b - next_color_b

	for i in range(gradiant_size):
        	rgbArray.append(RGBValue(current_r, current_g, current_b))

		current_r  = int((float(next_color_r - current_r) * (float(i) / float(gradiant_size)) + current_r))
		current_g  = int((float(next_color_g - current_g) * (float(i) / float(gradiant_size)) + current_g))
		current_b  = int((float(next_color_b - current_b) * (float(i) / float(gradiant_size)) + current_b))

# Setup some default colors
color_black  = RGBValue(0, 0, 0)
color_white  = RGBValue(255,255,255)
color_red    = RGBValue(215, 20, 20)
color_green  = RGBValue(0, 255, 0)
color_blue   = RGBValue(15, 15, 235)
color_purple = RGBValue(127, 0, 127)
color_cyan   = RGBValue(0, 255, 255)
color_pink   = RGBValue(255, 20, 203)
color_yellow = RGBValue(255, 255, 0)
color_violet = RGBValue(127,0,255)
color_darkgreen = RGBValue(40,140,70)
color_orange = RGBValue(255, 165, 0)
color_spanishorange = RGBValue(232,97,0)
color_gold = RGBValue(255,215,0)
color_silver = RGBValue(192,192,192)

# Add values to the RGB Array
range_value = 2

#for i in range(range_value):
#	rgbArray.append(color_green)
#for i in range(range_value):
#	rgbArray.append(color_red)
#for i in range(range_value): 
#	rgbArray.append(color_blue)
#for i in range(range_value):
#	rgbArray.append(color_gold)
#for i in range(range_value):
#	rgbArray.append(color_silver)
#for i in range(range_value):
#	rgbArray.append(color_spanishorange)
#for i in range(range_value):
#	rgbArray.append(color_yellow)

gradiant_size = 5

RGBGradiant(color_black, color_red, gradiant_size)
RGBGradiant(color_red, color_black, gradiant_size)

RGBGradiant(color_black, color_green, gradiant_size)
RGBGradiant(color_green, color_black, gradiant_size)

RGBGradiant(color_black, color_blue, gradiant_size)
RGBGradiant(color_blue, color_black, gradiant_size)

RGBGradiant(color_black, color_gold, gradiant_size)
RGBGradiant(color_gold, color_black, gradiant_size)

RGBGradiant(color_black, color_silver, gradiant_size)
RGBGradiant(color_silver, color_black, gradiant_size)

RGBGradiant(color_black, color_spanishorange, gradiant_size)
RGBGradiant(color_spanishorange, color_black, gradiant_size)

RGBGradiant(color_black, color_yellow, gradiant_size)
RGBGradiant(color_yellow, color_black, gradiant_size)

#rgbArray.append(color_red)
#rgbArray.append(color_green)
#rgbArray.append(color_blue)



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
        #led_strip.set_rgb(i,
        #    int(rgbArray[current_array_pos].r * BRIGHTNESS),
        #    int(rgbArray[current_array_pos].g * BRIGHTNESS),
        #    int(rgbArray[current_array_pos].b * BRIGHTNESS))


	# Modifying the above script because this LED strip uses BGR instead of GBR
	led_strip.set_rgb(i,
	    int(rgbArray[current_array_pos].g * BRIGHTNESS),
	    int(rgbArray[current_array_pos].b * BRIGHTNESS),
	    int(rgbArray[current_array_pos].r * BRIGHTNESS))

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
    time.sleep(0.15)
    #time.sleep(0.1)

