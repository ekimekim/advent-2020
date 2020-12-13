
import sys
import itertools

lines = sys.stdin.read().strip().split('\n')
start, busses = lines
start = int(start)
busses = [((-i) % int(bus), int(bus)) for i, bus in enumerate(busses.split(',')) if bus != 'x']

# from example:
# t = 7n
# ie. t % 7 == 0
#
# t + 1 = 13n
# ie. t % 13 == 1
#
# in general: bus B at index N => t % B == N % B

import signal
def p(*a):
	print time
signal.signal(signal.SIGUSR1, p)

# step by first bus since we know that's where we need to start
_, first = busses.pop(0)
for time in itertools.count(0, first):
#	print time
#	for delay, bus in busses:
#		print delay, bus, time % bus, ("good" if time % bus == delay else "")
#	print
	if any(
		time % bus != delay
		for delay, bus in busses
	):
		continue
	print time
	break
