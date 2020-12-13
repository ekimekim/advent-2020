
import sys
import itertools

lines = sys.stdin.read().strip().split('\n')
start, busses = lines
start = int(start)
busses = [int(bus) for bus in busses.split(',') if bus != 'x']

def main():
	for time in itertools.count(start):
		for bus in busses:
			if time % bus == 0:
				delay = time - start
				print bus * delay
				return

main()
