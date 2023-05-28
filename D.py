# Test
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

# Solve 
def is_inside(x, y, d):
	return x**2 + y**2 <= d**2

def solve(x, y, n, d, vectors):
	for vector in vectors:
		dx, dy = vector
		new_x, new_y = x + dx, y + dy
		if (is_inside(new_x, new_y, d)):
			x, y = new_x, new_y
		else:
			return "Ron"

	return "Harry"

x, y, n, d = map(int, input().split())
vectors = []

for i in range(n):
	xi, yi = map(int, input().split())
	vectors.append((xi, yi))

print(solve(x, y, n, d, vectors))