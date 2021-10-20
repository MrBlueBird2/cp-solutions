t = int(input())
for i in range(t):
    a, b, x, y, c = map(int, input().split())
    a1 = a / x
    a2 = b / y
    ans = min(a1, a2)
    if ans >= c:
        print("YES")
    else:
        print("NO")