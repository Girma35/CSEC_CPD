n = int(input())
nums = list(map(int,input().split()))
of = 0
res = 0
for num in nums:
    if num > 0:
        of += num
    else:
        if of > 0:
            of -= 1
        else:
            res += 1
print(res)

    