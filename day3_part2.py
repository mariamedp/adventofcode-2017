import sys

try:
	input = int(sys.argv[1])
except:
	input = 312051


spiral = {(0,0): 1}
last_value = 1
dir = 'right'
x, y = 1, 0
while input > last_value:
	posadj = [(x+i, y+j) for i in (-1, 0, 1) for j in (-1, 0, 1)]
	last_value = 0
	for pos in posadj:
		last_value += spiral.get(pos, 0)
	spiral[(x, y)] = last_value
	
	if dir == 'right':
		try_dir, try_x, try_y = 'up', x, y + 1
		x += 1
	elif dir == 'up':
		try_dir, try_x, try_y = 'left', x - 1, y
		y += 1
	elif dir == 'left':
		try_dir, try_x, try_y = 'down', x, y - 1
		x -= 1
	elif dir == 'down':
		try_dir, try_x, try_y = 'right', x + 1, y
		y -= 1
	
	if (try_x, try_y) not in spiral.keys():
		dir, x, y = try_dir, try_x, try_y

print(last_value)
