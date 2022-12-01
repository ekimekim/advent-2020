import sys

passports = [
	dict(x.split(':') for x in p.split())
	for p in sys.stdin.read().strip().split('\n\n')
]

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

print len([p for p in passports if not (required - set(p.keys()))])
