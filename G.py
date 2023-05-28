# Test 
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


# Solve
def solve(s, queries):
	database = [s]

	for query in queries:
		query_type = int(query[0])
		p = int(query[1])
		n = int(query[2])

		if query_type == 1:
			c = query[3]
			x = database[n - 1]
			z = x[:p - 1] + c
			database.append(z)
		elif query_type == 2:
			x = database[n - 1]
			z = x[:p]
			database.append(z)
		elif query_type == 3:
			l = int(query[1])
			r = int(query[2])
			s = query[3]
			exist = False

			for i in range(l - 1, r):
				u = database[i]
				if u.startswith(s):
					exist = True
					break

			if exist:
				print("yes")
			else:
				print("no")


s = input().strip()
q = int(input())
queries = []

for i in range(q):
	queries.append(input().split())

solve(s, queries)
