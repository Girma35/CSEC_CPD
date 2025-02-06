n = int(input())
text = input().strip()
res = 0
for i in range(1,n):
    if text[i] == text[i-1]:
        res += 1
print(res)
