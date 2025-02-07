import sys
import string

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

name = input().strip()
step = 0 
cp = 0
tp = 0
for char in name:
    tp = ord(char) - ord("a")
    cd =abs(tp - cp)
    ccd = 26 - cd
    step += min(cd,ccd)
    cp = tp
print(step)