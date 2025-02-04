import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def beuty(array):
    for i in range(5):
        for j in range(5):
            if array[i][j] == 1:
                return abs(i-2) + abs(j-2)
            


array = [list(map(int,input().split())) for _ in range(5)]
print(beuty(array))

    