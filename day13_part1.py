import sys

try:
	fname = sys.argv[1]
except:
	fname = 'day13.txt'

with open(fname, 'r') as f:
	firewall = { int(l.split(':')[0]) : int(l.split(' ')[1].strip()) for l in f.readlines() }


severity = 0
for picosec in range(max(firewall.keys()) + 1):
	try:
		layer_depth = firewall[picosec]
		scanner_path = list(range(layer_depth)) + list(range(layer_depth-2, 0, -1))
		layer_scanner_posc = scanner_path[picosec % len(scanner_path)]
		if layer_scanner_posc == 0:
			severity += (picosec * layer_depth)
	except KeyError:
		pass

print(severity)
