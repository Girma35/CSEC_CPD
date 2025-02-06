n = int(input())
nums = list(map(int,input().split()))
left ,right = 0 , n-1
sirag,dima = 0,0
t = 0
while left <= right:
    choosen_card = 0
    if nums[left] > nums[right]:
        choosen_card = nums[left]
        left += 1
    else:
        choosen_card = nums[right]
        right -= 1
    if t  % 2 == 0:
        sirag += choosen_card
    else:
        dima += choosen_card
    t += 1

  
print(sirag,dima)

