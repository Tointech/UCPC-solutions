# Test
import sys
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'w')

# Solve
def solve(num):
    sum = 0
    
    for i in range(1, num+1):
        if (num % i == 0):
            sum += i

    return sum % MOD

MOD = 10**9 + 7
n = int(input())
total = 0

for i in range(1, n+1):
    total += solve(i)

print(total)    
