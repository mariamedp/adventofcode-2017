import sys

try:
	fname = sys.argv[1]
except:
	fname = 'day11.txt'

with open(fname, 'r') as f:
	directions = f.read().split(',')


x_units = 0 # * sqrt(3) / 2
y_units = 0
max_dist = 0
for dir in directions:
	if dir == 'n':
		y_units += 1
	elif dir == 'ne':
		x_units += 1
		y_units += 0.5
	elif dir == 'se':
		x_units += 1
		y_units += -0.5
	elif dir == 's':
		y_units += -1
	elif dir == 'sw':
		x_units += -1
		y_units += -0.5
	elif dir == 'nw':
		x_units += -1
		y_units += 0.5
	else:
		raise Exception('Unknown direction: {}'.format(dir))
	
	dist = abs(x_units) + max(abs(y_units) - 0.5 * abs(x_units), 0)
	max_dist = max(dist, max_dist)

print(max_dist)
