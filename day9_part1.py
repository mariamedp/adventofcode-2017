import sys
import re

try:
	fname = sys.argv[1]
except:
	fname = 'day9.txt'

with open(fname, 'r') as f:
	input = f.read()

input = re.sub(r'!.', '', input)
input = re.sub(r'<[^>]*>', '', input)

total_score = 0
current_score = 0
for char in input:
	if char == '{':
		current_score += 1
	elif char == '}':
		total_score += current_score
		current_score -= 1
	elif char == ',':
		pass
	else:
		raise Exception('Unknown character found: "{}"'.format(char))

print(total_score)
