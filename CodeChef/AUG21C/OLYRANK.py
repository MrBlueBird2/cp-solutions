t = int(input())
for i in range(t):
    g1, s1, b1, g2, s2, b2 = map(int, input().split())
    co1 = g1 + s1 + b1
    co2 = g2 + s2 + b2
    if co1 > co2:
        print(1)
    else:
        print(2)