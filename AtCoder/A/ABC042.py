# 42
a, b, c = map(int, input().split())
l = [a, b, c]
l = sorted(l)
if(l[0] == 5 and l[1] == 5 and l[2] == 7):
    print("YES")
else:
    print("NO")