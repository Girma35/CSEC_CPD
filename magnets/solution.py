n = int(input())
magnets = [input().strip()for _ in range(n)]
res = 1
for i in range(1,n):
    if magnets[i] != magnets[i-1]:
        res += 1
print(res)
