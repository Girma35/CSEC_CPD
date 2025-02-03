import sys

# Redirect input and output files
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def whoWin(n,text):
    letterA = "A"
    letterD = "D"
    
    countA = text.count(letterA) 
    countD =text.count(letterD)
    if countD < countA:
            return "Anton"
    elif countD > countA:
        return "Danik"
    else:
        return "Friendship"

n = int(input())
text = input().strip()
print(whoWin(n,text))
