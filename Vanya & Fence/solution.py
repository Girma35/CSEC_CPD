import sys

# Redirect input and output files
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def minWidth(n,k,heights):
    res = 0 
    for i in range(n):
        if heights[i] > k:
            res += 2
        else:
            res += 1
    return res

n,k = map(int,input().split())
heights = list(map(int,input().split()))
print(minWidth(n,k,heights))