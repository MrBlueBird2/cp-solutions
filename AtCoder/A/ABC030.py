# 30
a, b, c, d = map(int, input().split())
x = b / a
y = d / c
if x == y:
    print("DRAW")
elif x > y:
    print("TAKAHASHI")
else:
    print("AOKI")