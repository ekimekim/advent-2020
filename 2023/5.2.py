import sys
import time
START = time.time()

sections = sys.stdin.read().strip().split("\n\n")

seeds = sections.pop(0)
seeds = map(int, seeds.split()[1:])
i = iter(seeds)
seeds = zip(i, i) # (start, len)

maps = {} # src type: (dst type, [(src base, dst base, len)])

for section in sections:
	lines = section.split("\n")
	types = lines.pop(0).split()[0]
	src_type, _, dst_type = types.split("-")
	ranges = []
	for line in lines:
		dst_base, src_base, length = map(int, line.split())
		ranges.append((src_base, dst_base, length))
	ranges.sort()
	maps[src_type] = dst_type, ranges

locations = []
for start, len in seeds:
	type = "seed"
	values = [(start, len)]
	while type != "location":
		type, ranges = maps[type]

		ranges = list(ranges) # copy, as we're going to mutate
		new_values = []
		while values and ranges:
			start, vlen = values[0]
			src_base, dst_base, rlen = ranges[0]
			end = start + vlen
			src_end = src_base + rlen
			if end <= src_base:
				# case 1: we're entirely before the next range. pass through with identity mapping
				new_values.append((start, vlen))
				values.pop(0)
				continue
			if start < src_base:
				# case 2: we start before the range, but overlap it. split the value range.
				new_len = src_base - start
				new_values.append((start, new_len))
				values[0] = src_base, vlen - new_len
				continue
			if end <= src_end:
				# case 3: we fall entirely within the range. translate.
				offset = start - src_base
				new_values.append((dst_base + offset, vlen))
				values.pop(0)
				continue
			if start < src_end:
				# case 4: we overlap the range, but run off the end. split the value range
				# and translate the first part.
				offset = start - src_base
				new_len = src_end - start
				new_values.append((dst_base + offset, new_len))
				values[0] = src_end, vlen - new_len
				continue
			# case 5: we are after the current range, try the next one.
			ranges.pop(0)

		# When we get here, we either ran out of values or out of ranges.
		# If we ran out of values, we're done. But if we ran out of ranges, the remaining values
		# are copied over with identity mapping.
		new_values += values

		new_values.sort()
		values = new_values

	locations += values

print min(start for start, length in locations)
print time.time() - START
