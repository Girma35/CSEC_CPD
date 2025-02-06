import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

str1 = input().strip().lower()
str2 = input().strip().lower()
if str1 < str2:
    print('-1')
elif str1 > str2:
    print('1')
else:
    print('0')
