# Test
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

# Solve
def solve(num):
	sum = 0;
	for i in range(1, num+1):
		sum += i*(i+1)/2
	print(int(sum % MOD))

MOD = 10**9 + 7
n = int(input())

for i in range(n):
	num = int(input())
	solve(num)