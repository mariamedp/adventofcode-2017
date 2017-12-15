import sys

try:
	value_A, value_B = int(sys.argv[1]), int(sys.argv[2])
except:
	value_A, value_B = 722, 354

factor_A, factor_B = 16807, 48271

divisor = 2147483647

npairs = 5000000


stack_A = []
while len(stack_A) < npairs:
	value_A = (value_A * factor_A) % divisor
	if value_A % 4 == 0:
		stack_A.append(value_A)

stack_B = []
while len(stack_B) < npairs:
	value_B = (value_B * factor_B) % divisor
	if value_B % 8 == 0:
		stack_B.append(value_B)

judge_count = 0		
for i in range(npairs):	
	if bin(stack_A[i])[-16:].zfill(16) == bin(stack_B[i])[-16:].zfill(16):
		judge_count += 1

print(judge_count)
	