import sys
import re

try:
	fname = sys.argv[1]
except:
	fname = 'day9.txt'

with open(fname, 'r') as f:
	input = f.read()

input = re.sub(r'!.', '', input)

garbage = re.findall(r'<[^>]*>', input)

print(sum([len(g) - 2 for g in garbage]))
