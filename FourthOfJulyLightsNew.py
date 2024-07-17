import plasma
from plasma import plasma2040
from pimoroni import Button
import time
import random

#Define what an RGB Value is to add to our array later
class RGBValue():
    def __init__(self, r_val, g_val, b_val):
        self.r=r_val
        self.g=g_val
        self.b=b_val

# Define the number of LED's to work with
NUM_LEDS = 192

# Define a Brightness Level.  This will be used to limit the intensity of the LED Lights
BRIGHTNESS = 0.2

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


def RGBGradiantReturn(sourceRGB, targetRGB, gradiant_size, inBufferArray):
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
                inBufferArray.append(RGBValue(current_r, current_g, current_b))
                current_r  = int((float(next_color_r - current_r) * (float(i) / float(gradiant_size)) + current_r))
                current_g  = int((float(next_color_g - current_g) * (float(i) / float(gradiant_size)) + current_g))
                current_b  = int((float(next_color_b - current_b) * (float(i) / float(gradiant_size)) + current_b))



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
color_lightblue = RGBValue(135,206,235)
color_amber = RGBValue(236,134,0)
color_passionatepink = RGBValue(255,192,203)
color_irishgreen = RGBValue(0,154,73)
color_shamrockgreen = RGBValue(0,158,96)
color_forestgreen = RGBValue(34,139,34)
color_softlilac = RGBValue(200,162,200)
color_springgreen = RGBValue(127,255,0)
color_daffodilyellow = RGBValue(255,255,0)
color_skyblue = RGBValue(135,206,235)
color_blushpink = RGBValue(255,192,203)
color_robineggblue = RGBValue(0,206,209)
color_sunfloweryellow = RGBValue(255,215,0)
color_oceanblue = RGBValue(0,128,255)
color_watermellonpink = RGBValue(255,105,180)
color_coralreeforange = RGBValue(255,127,80)


# Add values to the RGB Array
#for i in range(10):
#	rgbArray.append(color_yellow)
#for i in range(10):
#	rgbArray.append(color_orange)
#for i in range(10): 
#	rgbArray.append(color_spanishorange)
#for i in range(10):
#	rgbArray.append(color_red)
#for i in range(10):
#	rgbArray.append(color_spanishorange)
#for i in range(10):
#	rgbArray.append(color_orange)

gradiant_size = 50

# Clean up the LED Strip to start with
for i in range(NUM_LEDS):
    led_strip.set_rgb(i, 0, 0, 0)
    rgbArray.append(color_black)

# Set some inital values
current_array_pos = 0
start_array_pos = 0
pos_modifier = 1

mid_position = round(NUM_LEDS / 2)

bufferArray=[]
colorPallet=[]
colorPallet.append(color_red)
colorPallet.append(color_white)
colorPallet.append(color_blue)
colorPallet.append(color_robineggblue)
colorPallet.append(color_violet)
colorPallet.append(color_yellow)
colorPallet.append(color_spanishorange)


# Loop forever
while True:
    current_array_pos = start_array_pos
    
    if(len(bufferArray) == 0):
       currentColor = random.choice(colorPallet) 
       RGBGradiantReturn(rgbArray[mid_position], currentColor, gradiant_size, bufferArray)

    rgbArray[mid_position] = bufferArray.pop(0)

    for i in range(0, mid_position):
        rgbArray[i] = rgbArray[i+1]
    for i in range(NUM_LEDS - 1, mid_position, -1):
        rgbArray[i] = rgbArray[i-1]

    for i in range(NUM_LEDS):
        # Write values to the LED Strip.  Loops through the Array of LED Values entered Above
        led_strip.set_rgb(i,
            int(rgbArray[i].r * BRIGHTNESS),
            int(rgbArray[i].g * BRIGHTNESS),
            int(rgbArray[i].b * BRIGHTNESS))
        #current_array_pos = current_array_pos + 1
        
        # time.sleep(0.1)
        # Keep our values in a valid range
       # if(current_array_pos >= len(rgbArray)):
       #     current_array_pos = 0
       # if(current_array_pos < 0):
       #     current_array_pos = len(rgbArray) - 1
    
    # Let user change the direction of the scrolling LED's with buttons
    #if(button_a.read()):
    #    pos_modifier = 1
        # print("Pressed A!")
    # if(button_b.read()):
    #   pos_modifier = -1
       # print("Pressed B!")
    
    # start_array_pos = start_array_pos + pos_modifier
    # Keep our values in a valid range
    # if(start_array_pos >= len(rgbArray)):
    #     start_array_pos = 0
    # if(start_array_pos < 0):
    #     start_array_pos = len(rgbArray) - 1

    # Delay to determine the speed of the scrolling LED's
    time.sleep(0.12)



