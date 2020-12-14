import sys
import itertools

to_set = 0
to_keep = 0
to_float = []
mem = {}

for line in sys.stdin:
	line = line.strip()
	dest, value = line.split(' = ')
	if dest == 'mask':
		# force Xs to 0s (don't set)
		to_set = int(value.replace('X', '0'), 2)
		# keep all but Xs
		to_keep = int(value.replace('0', '1').replace('X', '0'), 2)
		to_float = [2**i for i, c in enumerate(value[::-1]) if c == 'X']
	else:
		addr = int(dest[4:-1]) # strip "mem[" and "]"
		addr = (addr | to_set) & to_keep
		value = int(value)
		for bits in itertools.product(*[(0, b) for b in to_float]):
			mem[addr | sum(bits)] = value

print sum(mem.values())
