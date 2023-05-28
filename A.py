# Test 
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

# Solve
def solve(board1, board2):
    moves = 0
    for i in range(4):
        for j in range(4):
            if chessboard1[i][j] != chessboard2[i][j]:
                moves += 1
    print(int(moves/2))  

chessboard1 = [list(map(int, input().split())) for i in range(4)]
chessboard2 = [list(map(int, input().split())) for i in range(4)]

solve(chessboard1, chessboard2)