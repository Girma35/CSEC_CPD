text = input().strip()
text_set = set(text)
length = len(text_set)
if length % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
