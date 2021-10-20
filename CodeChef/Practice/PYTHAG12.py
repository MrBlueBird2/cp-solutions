t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    l = [a, b, c]
    l.sort()
    x = (l[0] ** 2) + (l[1] ** 2)
    if x == l[2] ** 2:
        print("YES")
    else:
        print("NO")