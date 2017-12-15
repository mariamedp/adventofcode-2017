import sys

try:
	value_A, value_B = int(sys.argv[1]), int(sys.argv[2])
except:
	value_A, value_B = 722, 354

factor_A, factor_B = 16807, 48271

divisor = 2147483647

npairs = 40000000


judge_count = 0
for i in range(npairs):
	value_A = (value_A * factor_A) % divisor
	value_B = (value_B * factor_B) % divisor
	
	if bin(value_A)[-16:].zfill(16) == bin(value_B)[-16:].zfill(16):
		judge_count += 1

print(judge_count)
	