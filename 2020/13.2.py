
import sys
import itertools
from fractions import gcd

lines = sys.stdin.read().strip().split('\n')
start, busses = lines
start = int(start)
# we're pre-calcluating (-index) % bus, see below
busses = [((-i) % int(bus), int(bus)) for i, bus in enumerate(busses.split(',')) if bus != 'x']

"""
from example:
 t = 7n
 ie. t % 7 == 0

 t + 1 = 13n
 ie. t % 13 == 12

in general: bus B at index N => t % B == -N % B

This is a quick and easy way to check if a bus matches for a given time.
However, needing to check every possible time is still too slow (won't finish for years)

The major trick is to realise:
 The relation of bus 0 and bus 1 must repeat every LCM(bus[0], bus[1]).
Therefore as soon as we find a valid offset, we can skip by that amount instead.
"""

def lcm(x, y):
	# shamelessly stolen from stackoverflow
    return x * y // gcd(x, y)

_, step = busses.pop(0)
time = 0
while busses:
	time += step
	for delay, bus in busses[:]:
		if time % bus == delay:
			step = lcm(step, bus)
			busses.pop(0)
		else:
			break

print time
