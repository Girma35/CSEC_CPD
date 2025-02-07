import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

nums1 = list(map(int,input().split()))
temp = input().strip()
nums2 = list(map(int,str(temp)))
res = 0
for num in nums2:
    res += nums1[num-1]
print(res)