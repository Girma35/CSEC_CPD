text = input().strip()
lower_case = sum(1 for char in text if char.islower())
upper_case = sum(1 for char in text if char.isupper())
if upper_case > lower_case:
    print(text.upper())
else:
    print(text.lower())
