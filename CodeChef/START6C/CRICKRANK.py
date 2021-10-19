t = int(input())
for i in range(t):
    r1, w1, c1 = map(int, input().split())
    r2, w2, c2 = map(int, input().split())
    A = 0
    B = 0
    if r1 > r2:
        A += 1
    else:
        B += 1
    if w1 > w2:
        A += 1
    else:
        B += 1
    if c1 > c2:
        A += 1
    else:
        B += 1
    if A > B:
        print("A")
    else:
        print("B")