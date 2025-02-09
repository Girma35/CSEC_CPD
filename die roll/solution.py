import math

def die(y,w):
    mr = max(y,w)
    fo = 6 - mr + 1
    cd = math.gcd(fo,6)
    d = 6 // cd
    n = fo // cd
    return f"{n}/{d}"
y,w = map(int,input().split())
print(die(y,w))


