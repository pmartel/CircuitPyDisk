import time
import adafruit_trellism4

trellis = adafruit_trellism4.TrellisM4Express()
i = 0
n = 128
while True:
    trellis.pixels[0, 0] = (i, 0, 0)
    trellis.pixels[1, 1] = (0, i, 0)
    trellis.pixels[2, 2] = (0, 0, i)
    trellis.pixels[7, 0] = (i, 0, 0)
    trellis.pixels[6, 1] = (0, i, 0)
    trellis.pixels[5, 2] = (0, 0, i)
    time.sleep(0.005)
    i = (i+1) % n