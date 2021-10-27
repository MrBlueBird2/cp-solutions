a, b, c = map(int,input().split())
ans = a**2 + b**2
if(c**2 > ans):
    print("Yes")
else:
    print("No")