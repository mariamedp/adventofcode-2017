import sys

try:
	fname = sys.argv[1]
except:
	fname = 'day10.txt'

with open(fname, 'r') as f:
	lengths = [int(l) for l in f.read().split(',')]

numbers = list(range(256))
curr_pos = 0
skip_size = 0

for length in lengths:
	for i in range(int(length/2)):
		ind1 = (curr_pos + i) % len(numbers)
		ind2 = (curr_pos + length - 1 - i) % len(numbers)
		numbers[ind1], numbers[ind2] = numbers[ind2], numbers[ind1]
	
	curr_pos = (curr_pos + length + skip_size) % len(numbers)
	skip_size += 1

print(numbers[0] * numbers[1])
