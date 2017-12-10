import sys

try:
	fname = sys.argv[1]
except:
	fname = 'day10.txt'

with open(fname, 'r') as f:
	lengths = [ord(l) for l in f.read()] + [17, 31, 73, 47, 23]

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

hash = ''.join(hex(d).replace('0x', '').zfill(2) for d in dense_hash)
print(hash)
