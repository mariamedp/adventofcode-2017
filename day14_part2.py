import sys

try:
	input = sys.argv[1]
except:
	input = 'ljoxqyyw'


def get_knothash(ascii_str):

	lengths = [ord(c) for c in ascii_str] + [17, 31, 73, 47, 23]
	numbers = list(range(256))
	
	curr_pos = 0
	skip_size = 0
	for round in range(64):
		for length in lengths:
			for i in range(int(length/2)):
				ind1 = (curr_pos + i) % len(numbers)
				ind2 = (curr_pos + length - 1 - i) % len(numbers)
				numbers[ind1], numbers[ind2] = numbers[ind2], numbers[ind1]
			
			curr_pos = (curr_pos + length + skip_size) % len(numbers)
			skip_size += 1


	sparse_hash = numbers
	dense_hash = []
	for i in range(len(sparse_hash)):
		if i % 16 == 0:
			dense_hash.append(sparse_hash[i])
		else:
			dense_hash[-1] ^= sparse_hash[i]
	
	return(dense_hash)
	

grid_side = 128

grid = []
for i in range(grid_side):
	hash = get_knothash('{}-{}'.format(input, i))
	bin_hash = [bin(int(hex(d), 16)).replace('0b', '').zfill(8) for d in hash]
	bits = [int(b) for h in bin_hash for b in h]
	grid.append(bits)

	
def mark_neighbours_visited(grid, posc):

	if grid[posc[0]][posc[1]] == 0:
		return
	else:
		grid[posc[0]][posc[1]] = 0
	
	neighbours = [(posc[0] + p[0], posc[1] + p[1]) for p in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
	neighbours_tovisit = [n for n in neighbours if 0 <= n[0] < len(grid) and 0 <= n[1] < grid_side]
	for n in neighbours_tovisit:
		mark_neighbours_visited(grid, n)


nregions = 0
while grid and any(any(row) for row in grid):
	
	while all([b == 0 for b in grid[0]]):
		del grid[0]
	
	posc_start = (0, grid[0].index(1))
	mark_neighbours_visited(grid, posc_start)
	nregions += 1
	
print(nregions)
	
	
	
	
	
	
	