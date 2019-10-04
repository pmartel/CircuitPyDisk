# Lissajous version 1
import array, math
import board, audioio
length = 1000
samples_xy = array.array("H", [0] * length * 2)
# Created interleaved x, y samples
for idx in range(length):
    samples_xy[2 * idx] = round(math.sin(math.pi * 2 * idx / length) * 10000 + 10000)
    samples_xy[2 * idx + 1] = round(math.sin(math.pi * 2 * 3 * idx / length + math.pi / 2) * 10000 + 10000)
    output_wave = audioio.RawSample(samples_xy,
        channel_count=2,sample_rate=100*1000)
dacs.play(output_wave, loop=True)
while True:
    pass