# Lissajous version 1
import array, math
import board, audioio

dacs = audioio.AudioOut(left_channel=board.A0, right_channel=board.A1)

length = 1000
baseFreq = 100
#print("length = " + length.tostring())
#print("base frea = " + baseFreq)
vP= 15000
center = 15000
samples_xy = array.array("H", [0] * length * 2)
# Created interleaved x, y samples
for idx in range(length):
    samples_xy[2 * idx] = round(math.sin(math.pi * 2 * idx / length) * vP + center)
    samples_xy[2 * idx + 1] = round(math.sin(math.pi * 2 * 3 * idx / length + math.pi / 2) * vP + center)
output_wave = audioio.RawSample(samples_xy, channel_count=2,sample_rate= baseFreq * length)
dacs.play(output_wave, loop=True)
while True:
    pass