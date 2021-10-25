a, b, c = map(int,input().split())
if a == c:
    print(b)
elif a == b:
    print(c)
elif b == c:
    print(a)
else:
    print(0)