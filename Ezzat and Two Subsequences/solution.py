import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def max_sub(n):
    temp = 0
    for i in range(n):
        for j in range(i,n):
            
        