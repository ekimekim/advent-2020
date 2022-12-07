
import sys

commands = sys.stdin.read().lstrip("$ ").rstrip("\n").split("\n$ ")

files = {}
cwd = ()
for command in commands:
	if command.startswith("cd "):
		assert "\n" not in command, "cd with newline: {!r}".format(command)
		path = command.split(" ", 1)[1]
		if path == "/":
			cwd = ()
		elif path == "..":
			cwd = cwd[:-1]
		else:
			cwd = cwd + (path,)
	elif command.startswith("ls\n"):
		entries = command.split("\n")[1:]
		for entry in entries:
			arg, path = entry.split()
			if arg == "dir":
				pass # this info isn't actually useful to us
			else:
				arg = int(arg)
				files[cwd + (path,)] = arg
	else:
		assert False, "bad command: {!r}".format(command)

dirs = {}
for path, size in files.items():
	while path:
		path = path[:-1]
		dirs[path] = dirs.get(path, 0) + size

print sum(size for size in dirs.values() if size <= 100000)

disk_size = 70000000
target = 30000000
free = disk_size - dirs[()]
to_delete = target - free
print min(size for size in dirs.values() if size > to_delete)
