import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

c = list(map(int,input().split()))
res = 0
for i in range(3):
    if c[i] == c[i+ 1]:
        res += 1
print(res)