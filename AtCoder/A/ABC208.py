a, b = map(int, input().split())
l = [i for i in range(a, 6*a+1)]
if b in l:
    print("Yes")
else:
    print("No")