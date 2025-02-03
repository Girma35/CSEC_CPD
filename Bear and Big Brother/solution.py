def weigh(bear,bob):
    year = 0
    while bear <= bob :
        bear *= 3
        bob *= 2
        year += 1
    return year


bear,bob = map(int,input().split())
print(weigh(bear,bob))
    
    