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

used_sq = 0
for i in range(grid_side):
	hash = get_knothash('{}-{}'.format(input, i))
	bin_hash = [bin(int(hex(d), 16)) for d in hash]
	used_sq += sum([h.count('1') for h in bin_hash])

print(used_sq)