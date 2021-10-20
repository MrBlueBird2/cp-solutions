# 28
n = int(input())
if n <= 59:
    print("Bad")
elif n >= 60 and n <= 89:
    print("Good")
elif n >= 90 and n <= 99:
    print("Great")
else:
    print("Perfect")