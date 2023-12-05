import sys

sections = sys.stdin.read().strip().split("\n\n")

seeds = sections.pop(0)
seeds = map(int, seeds.split()[1:])

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
for seed in seeds:
	type = "seed"
	value = seed
	while type != "location":
		type, ranges = maps[type]
		for src_base, dst_base, length in ranges:
			offset = value - src_base
			if 0 <= offset < length:
				value = dst_base + offset
				break
			if offset < 0:
				# ranges are sorted by src_base, so if we haven't found it yet we never will
				break
	locations.append(value)

print min(locations)
