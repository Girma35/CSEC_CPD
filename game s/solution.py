n = int(input())
nums = [list(map(int,input().split())) for _ in range(n)]
res = 0
for i  in range(n):
    for j in range(n):
        if i != j and nums[i][0] == nums[j][1]:
            res += 1

print(res)

