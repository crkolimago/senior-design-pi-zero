import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 30)

for i in range(len(pixels)*2):
    if i%2 == 0: 
        pixels[i]= (255,0,0)
    else: 
        pixels[i] = (0,255,0)


    