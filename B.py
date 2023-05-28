# Test
import sys
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'w')

# Solve
def solve(s):
    countE = s.count('e')
    countR = s.count('r')
    countA = s.count('a')
    
    if s[0] == 'm' and s[1] == 'e' and s[countE+1] == 'o' and s[countE+2] == 'w' and s[-1] == 'w':
        print('meow')
    elif s[0] == 'p' and s[1] == 'u' and s[2] == 'r' and countR >= 2:
        print('purr')
    elif s[0] == 'r' and s[1] == 'o' and s[-1] == 'r' and s[-2] == 'a' and countA == 1:
        print('roar')
    else:
        print('human noises')

n = int(input())

for i in range(n):
    s = str(input())
    solve(s)

 