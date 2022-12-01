import sys
import itertools

target = 88311122
nums = map(int, sys.stdin)

def main():
	for length in itertools.count(2):
		for i in range(0, len(nums) - length):
			numrange = nums[i:i+length]
			if sum(numrange) == target:
				print min(numrange) + max(numrange)
				return

main()
