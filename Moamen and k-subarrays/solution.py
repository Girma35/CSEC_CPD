import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


def is_sorted(n,k,array):
    sorted_array = sorted(array)
    index_map = {}
    for i,val in enumerate(sorted_array):
        index_map[val] = i 
    res = 1
    for i in range(1,n):
     if index_map[array[i]] != index_map[array[i - 1]] + 1:  
            res += 1
   
   
    if res > k:
        return "NO"
    else:
         return "YES"
       
        

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    array = list(map(int,input().split()))
    print(is_sorted(n,k,array)) 
