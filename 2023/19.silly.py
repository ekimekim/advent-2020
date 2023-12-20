
import sys
import socket
import errno
import struct
import subprocess

offsets = {
	"x": 0,
	"m": 4,
	"a": 8,
	"s": 12,
}

def make_test(field, op, threshold):
	offset = offsets[field]
	# This mini-program in the iptables u32 matcher location language
	# looks up the u32 starting at a given offset in the UDP payload.
	# "0 >> 22 & 0x3C @" calulates and moves to the start of the IP payload (the UDP header).
	# The final number specifies the offset into the IP packet. Since a UDP header is always 8 bytes,
	# the ip payload offset = 8 + the UDP payload offset.
	location = "0 >> 22 & 0x3C @ {}".format(8 + offset)
	if op == "<":
		value = "0:{}".format(threshold - 1)
	else:
		# match >= threshold by doing a range from threshold to u32-max.
		value = "{}:0xFFFFFFFF".format(threshold)
	return "{} = {}".format(location, value)

def make_rule(target, condition):
	if condition is None:
		return ["-j", target]
	field, op, threshold = condition
	return [
		"-m", "u32", "--u32", make_test(field, op, threshold),
		"-j", target
	]

def make_name(name):
	return "AOC-{}".format(name.upper())

def parse_chains(input):
	chains = {}
	for line in input.split("\n"):
		name, rest = line.split("{")
		name = make_name(name)
		rule_input = rest[:-1].split(",")
		rules = []
		for rule in rule_input:
			if ":" in rule:
				rule, target = rule.split(":")
				field = rule[0]
				op = rule[1]
				threshold = int(rule[2:])
				condition = field, op, threshold
			else:
				target = rule
				condition = None
			if target == 'A':
				target = 'ACCEPT'
			elif target == 'R':
				target = 'REJECT'
			else:
				target = make_name(target)
			rules.append(make_rule(target, condition))
		chains[name] = rules
	return chains

def make_begin_rule(dport):
	return [
		"--protocol", "udp", "--destination", "127.0.0.1", "--dport", str(dport),
		"-j", "AOC-IN",
	]

def create_chains(chains, dport):
	# Chains need to exist to be referenced, so we need to make them all first,
	# then make the rules.
	for name in chains:
		yield ["sudo", "iptables", "-N", name]
	for name, rules in chains.items():
		for rule in rules:
			yield ["sudo", "iptables", "-A", name] + rule
	yield ["sudo", "iptables", "-I", "INPUT"] + make_begin_rule(dport)

def delete_chains(chains, dport):
	yield ["sudo", "iptables", "-D", "INPUT"] + make_begin_rule(dport)
	# Because rules refer to other chains, we need to delete all rules THEN all chains
	for name in chains:
		yield ["sudo", "iptables", "-F", name]
	for name in chains:
		yield ["sudo", "iptables", "-X", name]

def run(commands, ignore_error=False):
	for command in commands:
		try:
			subprocess.check_call(command)
		except subprocess.CalledProcessError:
			if not ignore_error:
				raise

def parse_parts(input):
	for line in input.split("\n"):
		part = {}
		for kv in line[1:-1].split(","):
			k, v = kv.split("=")
			part[k] = int(v)
		yield struct.pack("!IIII", part["x"], part["m"], part["a"], part["s"])

port = 1234
def main():
	workflow_input, part_input = sys.stdin.read().strip().split("\n\n")
	chains = parse_chains(workflow_input)
	parts = parse_parts(part_input)

	reciever = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	reciever.bind(("127.0.0.1", port))
	reciever.setblocking(0)
	sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sender.connect(("127.0.0.1", port))

	try:
		run(create_chains(chains, port))

		for packet in parts:
			retried = False
			for retry in range(2):
				try:
					sender.send(packet)
					break
				except socket.error as e:
					# Rejected packets get a "connection refused" response,
					# but sometimes they cause the *next* message to be rejected.
					# So we retry once.
					if e.errno != errno.ECONNREFUSED:
						raise

		accepted = []
		try:
			while True:
				packet = reciever.recv(4096)
				accepted.append(packet)
		except socket.error as e:
			if e.errno != errno.EAGAIN:
				raise
	finally:
		run(delete_chains(chains, port))

	print sum(
		sum(struct.unpack("!IIII", packet))
		for packet in accepted
	)

if __name__ == '__main__':
	main()
