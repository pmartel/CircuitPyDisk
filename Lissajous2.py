# Lissajous version 2
import array, math
import board, analogio
import time

length = 1000
samples_x = array.array("H", [0] * length)
samples_y = array.array("H", [0] * length)
for idx in range(length):
    samples_x[idx] = round(math.sin(math.pi * 2 * idx / length) * 10000 + 10000)
    samples_y[idx] = round(math.sin(math.pi * 2 * 3 * idx / length + math.pi / 2) * 10000 + 10000)

dac_a0 = analogio.AnalogOut(board.A0)
dac_a1 = analogio.AnalogOut(board.A1)
while True:
    for x, y in zip(samples_x, samples_y):
        dac_a0.value = x
        dac_a1.value = y
        #time.sleep(.001)