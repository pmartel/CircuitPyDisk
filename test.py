# Lissajous version 1
import time
import array, math
import board, audioio

dacs = audioio.AudioOut(left_channel=board.A0, right_channel=board.A1)

length = 1000
baseFreq = 200
sleepTime = 2
print("length = " + str(length))
print("base freq = " + str(baseFreq))
vP= 15000
center = 15000
samples_xy = array.array("H", [0] * length * 2)
samples_xy2 = array.array("H", [0] * length * 2)
# Created interleaved x, y samples
for idx in range(length):
	samples_xy[2 * idx] = round(math.sin(math.pi * 2 * idx / length) * vP + center)
	samples_xy2[2 * idx] = samples_xy[2 * idx]
	samples_xy[2 * idx + 1] = round(math.sin(math.pi * 2 * 3 * idx / length + math.pi / 2) * vP + center)
	samples_xy2[2 * idx+1] = samples_xy[2 * idx+1]
	if samples_xy2[2 * idx+1] < center :
		samples_xy2[2 * idx+1] = 2*center - samples_xy2[2 * idx+1]
output_wave = audioio.RawSample(samples_xy, channel_count=2,sample_rate= baseFreq * length)
output_wave2 = audioio.RawSample(samples_xy2, channel_count=2,sample_rate= baseFreq * length)
while True:
	dacs.play(output_wave, loop=True)
	time.sleep(sleepTime)
	dacs.play(output_wave2, loop=True)
	time.sleep(sleepTime)