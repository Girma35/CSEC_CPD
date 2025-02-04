import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def numOfPro():
    num = list(map(int,input().split()))
    sumOfNum = sum(num)
    if sumOfNum  >= 2:
            return 1
    else:
          return 0
res = 0
n = int(input())
for _ in range(n):
      res += numOfPro()

print(res)