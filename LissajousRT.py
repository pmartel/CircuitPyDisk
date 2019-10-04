# Lissajous Real Time
import  math
import board,analogio

lChan = analogio.AnalogOut(board.A0)
rChan = analogio.AnalogOut(board.A1)

length = 1000
while True:
    for idx in range(length):
        left = round(math.sin(math.pi * 2 * idx / length) * 10000 + 10000)
        right = round(math.sin(math.pi * 2 * 3 * idx / length + math.pi / 2) * 10000 + 10000)
        lChan.value = left
        rChan.value = right
    pass