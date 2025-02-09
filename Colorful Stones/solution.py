import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = input().strip()
ins = input().strip()
pos = 0
for char in ins:
    if char == t[pos]:
        pos += 1
pos += 1
print(pos)
