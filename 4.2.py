import sys
import re

passports = [
	dict(x.split(':') for x in p.split())
	for p in sys.stdin.read().strip().split('\n\n')
]

required = {
	'byr': lambda v: 1920 <= int(v) <= 2002,
	'iyr': lambda v: 2010 <= int(v) <= 2020,
	'eyr': lambda v: 2020 <= int(v) <= 2030,
	'hgt': lambda v: (v.endswith('cm') and (150 <= int(v[:-2]) <= 193)) or
		(v.endswith('in') and (59 <= int(v[:-2]) <= 76)),
	'hcl': lambda v: re.match('^#[a-f0-9]{6}$', v),
	'ecl': lambda v: v in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
	'pid': lambda v: re.match('^[0-9]{9}$', v)
}

def valid(k, v):
	f = required[k]
	try:
		return f(v)
	except Exception:
		return False

print len([p for p in passports if all(
	(k in p) and valid(k, p[k])
	for k in required
)])
