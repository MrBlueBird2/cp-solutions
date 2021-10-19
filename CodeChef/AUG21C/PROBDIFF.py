t = int(input())
for i in range(t):
    a1, a2, a3, a4 = map(int, input().split())
    l = [a1, a2, a3, a4]
    res = set(l)
    if len(res) >= 3:
        print(2)
    elif len(res) == 2 and l.count(a1) == 2:
        print(2)
    elif len(res) == 1:
        print(0)
    else:
        print(1)