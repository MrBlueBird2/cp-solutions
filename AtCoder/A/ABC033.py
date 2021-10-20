# 33
s = input()
x = 0
for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        x += 1
    else:
        x -= 1
if x == (len(s) - 1):
    print("SAME")
else:
    print("DIFFERENT")