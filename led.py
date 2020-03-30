import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 60)

for i in range(len(pixels)):
    if i%2 == 0: 
        pixels[i]= (255,0,0)
    else: 
        pixels[i] = (0,255,0)


    