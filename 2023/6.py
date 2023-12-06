import sys
import math

lines = sys.stdin.read().strip().split("\n")
times, distances = [map(int, line.split()[1:]) for line in lines]

p2time, p2distance = [int(line.split(" ", 1)[1].replace(" ", "")) for line in lines]

# v = how long you hold button, and also speed
# d = v(t-v) where t is total race time
# this is maximised at d/dv v(t-v) = 0, t - 2v = 0, v = t/2
# to beat a target distance d, you want:
#  d < v(t-v)
#  d/v < t - v
#  d/v + v - t < 0
#  d + v^2 - tv < 0
#  v^2 - tv + d < 0
#  applying quadratic formula:
#    t/2 - sqrt(t^2 - 4d)/2 < v < t/2 + sqrt(t^2 - 4d)
#  which is a range of 2 * sqrt(t^2 - 4d)
#  but we need to take integer rounding into account

def get_range(time, distance):
	disc = float(time**2 - 4 * distance)**.5 / 2
	min = math.floor(time/2. - disc)
	max = math.ceil(time/2. + disc)
	return int(max - min) - 1 # fencepost issue: [min, max] is end-inclusive
	product *= range

product = 1
for time, distance in zip(times, distances):
	product *= get_range(time, distance)
print product

print get_range(p2time, p2distance)
