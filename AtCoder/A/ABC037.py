# 37
a, b, c = map(int,input().split())
ans = 0
if(a <= b):
    print(c // a)
else:
    print(c // b)