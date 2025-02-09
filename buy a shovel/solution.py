def mod(p, r):
    for k in range(1, 11):  
        res = p * k 
        if res % 10 == 0 or res % 10 == r:
            return k  

p, r = map(int, input().split())  
print(mod(p, r))  
