import math
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    mx = max(a, b)
    mn = min(a, b)
    if math.gcd(a, b) > 1:
        print(0)
    elif math.gcd(a, b+1) > 1 or math.gcd(a+1, b) > 1:
        print(1)
    else:
        print(2)